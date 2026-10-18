"""Validate retained body pages and the newly typeset back section."""
import hashlib
import json
from pathlib import Path
import re

import fitz
from pypdf import PdfReader
from vellum import source_images, source_image_info


def normalized(text):return ' '.join(text.split())


def validate(pdf,repo,log):
    pdf,repo=Path(pdf),Path(repo);doc=fitz.open(pdf);bib=log['bibliography'];used=set();next_page=5;spreads=0;relocated=0
    septimus_spreads=0;citation_links=0
    reader=PdfReader(pdf) if any(t in log for t in ('Clavis','De Vinculis')) else None
    page_ids={(p.indirect_reference.idnum,p.indirect_reference.generation):i+1 for i,p in enumerate(reader.pages)} if reader else {}
    destinations={key:e['start_page'] for e in bib['entries'] for key in e['keys']}
    def require(ok,message):
        if not ok:raise ValueError(message)
    require(len(doc)==log['total_pages'],'Page count differs from binding log')
    for title,e in log.items():
        if not isinstance(e,dict) or 'source' not in e:continue
        path=repo/e['source'];require(hashlib.sha256(path.read_bytes()).hexdigest()==e['source_sha256'],title+': source hash changed')
        source=fitz.open(path);body={int(k):v for k,v in e['body_page_map'].items()}
        bibl=set(e['bibliography_source_pages']);prod=set(e['production_source_pages'])
        alignment=set(e.get('omitted_alignment_source_pages',[]))
        require(not(set(body)&(bibl|prod)),title+': relocated leaf remains in the body')
        require(set(body)|bibl|prod|alignment==set(range(1,len(source)+1)),title+': unexplained missing source leaf')
        for n in alignment:require(not source[n-1].get_text().strip() and not source[n-1].get_images(),'Omitted alignment leaf contains content')
        require(e['start_page']%2==1,title+': component does not begin recto')
        require(e['start_page']==next_page+int(e['blank_before']),title+': unexplained component gap')
        require(set(body.values())|set(e['body_blank_pages'])==set(range(e['start_page'],e['end_page']+1)),title+': unexplained body leaf')
        for r in e['metadata_redactions']:
            p=source[r['source_page']-1];p.add_redact_annot(fitz.Rect(r['rect']),fill=None,cross_out=False)
        for p in source:
            if p.annots():p.apply_redactions(images=0,graphics=0,text=0)
        for local,physical in body.items():
            require(local%2==physical%2,title+': page side changed')
            require(physical not in used,title+': overlapping page');used.add(physical)
            require(normalized(source[local-1].get_text())==normalized(doc[physical-1].get_text()),title+f': body text changed on source page {local}')
        for n in e['body_blank_pages']:
            require(not doc[n-1].get_text().strip() and not source_images(doc[n-1]),'Alignment leaf is not blank')
        if title=='Tarot of Intervals':
            paging=json.loads(path.with_name(path.stem+'-log.json').read_text())
            for card in paging['cards']:
                v,r=body[card['verso']],body[card['recto']]
                require(v%2==0 and r==v+1,'Tarot facing pair changed')
                require(len(source_images(doc[r-1]))==1,'Tarot illustration missing');spreads+=1
        if title in ('Clavis','De Vinculis'):
            manifest=json.loads(path.with_name('build-manifest.json').read_text())
            kind='clavis' if title=='Clavis' else 'vinculis'
            edition=manifest['books'][kind]
            require(edition['sha256']==e['source_sha256'],title+': stale Septimus manifest')
            for pair in edition['tabula_pairs']:
                v,r=body[pair['tabula_page']],body[pair['commentarium_page']]
                require(v%2==0 and r==v+1,'Septimus Tabula and Commentarium do not face')
                septimus_spreads+=1
            for local,physical in body.items():
                original=source[local-1]
                require([i['digest'] for i in original.get_image_info(hashes=True)]==
                        [i['digest'] for i in source_image_info(doc[physical-1])],title+': illumination changed or missing')
                for link in original.get_links():
                    match=re.fullmatch(r'\s*\[(S\d+)\]\s*',original.get_textbox(link['from']))
                    if not match:continue
                    key='VII/'+match[1];rect=link['from']
                    expected=(rect.x0,720-rect.y1,rect.x1,720-rect.y0)
                    annotations=[a.get_object() for a in reader.pages[physical-1].get('/Annots',[])]
                    matching=[a for a in annotations if a.get('/Subtype')=='/Link' and len(a.get('/Rect',[]))==4
                              and all(abs(float(x)-y)<.1 for x,y in zip(a['/Rect'],expected))]
                    require(len(matching)==1,title+': missing or duplicated citation link '+key)
                    dest=matching[0].get('/Dest');target=dest[0] if isinstance(dest,list) and dest else None
                    require(hasattr(target,'idnum') and page_ids.get((target.idnum,target.generation))==destinations[key],
                            title+': citation points outside its consolidated entry: '+key)
                    citation_links+=1
        next_page=e['end_page']+1;relocated+=len(bibl)
    require(bib['start_page']%2==1 and bib['start_page'] in (next_page,next_page+1),'Back section does not follow the books')
    require(bib['end_page']==len(doc),'Bibliography is not at the end')
    if 'De Vinculis' in log:
        require('Tarot of Intervals' in log,'Book VII has no preceding Tarot')
        require(log['De Vinculis']['start_page'] in (log['Tarot of Intervals']['end_page']+1,log['Tarot of Intervals']['end_page']+2),
                'Book VII does not immediately follow Tarot')
        require(septimus_spreads==7,'Septimus facing pairs missing')
    require(citation_links==log.get('septimus_citation_links',0),'Septimus citation-link count differs')
    if bib['start_page']>next_page:require(not doc[next_page-1].get_text().strip(),'Back section alignment leaf is not blank')
    records=json.loads(pdf.with_name('bibliography-records.json').read_text())
    # Reflow can split an account across leaves; running heads and folios do
    # not interrupt the account's text for comparison.
    running={'CODEX INTERVALLORUM','BIBLIOGRAPHY','Bibliography','Bibliography, continued','Production and source notes',
             'PRODUCTION NOTES','Production and source notes, continued','Project records','Project records, continued'}
    tail=' '.join(normalized('\n'.join(line for line in p.get_text().splitlines() if line.strip() not in running and line.strip()!=str(p.number+1))) for p in doc[bib['start_page']-1:])
    for r in records['references']:
        require(normalized(r['citation']) in tail,'Bibliography citation missing: '+r['citation'][:80])
        for key in r['keys']:require(key in tail,'Bibliography key missing: '+key)
        for account in r['accounts']:
            for key in ['status','use']:
                if account.get(key):require(normalized(account[key]) in tail,'Source account missing')
    for n in records['production_notes']:
        for text in n['paragraphs']:
            require(normalized(text) in tail,'Production note missing: '+text[:70])
    for path,digest in bib['input_sha256'].items():require(hashlib.sha256((repo/path).read_bytes()).hexdigest()==digest,'Bibliographic input changed: '+path)
    for p in doc:
        require(p.rect.width==504 and p.rect.height==720,'Wrong trim')
        for block in p.get_text('dict')['blocks']:
            for line in block.get('lines',[]):require(p.rect.contains(fitz.Rect(line['bbox'])),'Text outside page bounds')
    contents=normalized(doc[1].get_text())
    for title,e in log.items():
        if isinstance(e,dict) and 'source' in e:
            require(f"pages {e['start_page']}–{e['end_page']}" in contents,title+': contents range missing')
    for p in doc[bib['start_page']-1:]:
        for block in p.get_text('dict')['blocks']:
            for line in block.get('lines',[]):
                for s in line['spans']:require(s['font'].startswith(('EBGaramond','IM_FELL','IMFELL','IM_Fell')),'Unexpected backmatter font: '+s['font'])
    result=dict(pages=len(doc),components=len([e for e in log.values() if isinstance(e,dict) and 'source' in e]),facing_tarot_spreads=spreads,
                facing_septimus_spreads=septimus_spreads,septimus_citation_links=citation_links,
                all_components_start_recto=True,source_hashes_match=True,bibliography_at_end=True,bibliography_source_pages=relocated,
                typeset_references=len(records['references']),source_leaves_accounted_for=True,uniform_backmatter_fonts=True)
    pdf.with_name('binding-validation.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2));return result


