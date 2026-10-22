import importlib.util
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest

import fitz
from reportlab.pdfgen.canvas import Canvas

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'binding'))
import backmatter
import unified


class BackmatterTests(unittest.TestCase):
    def test_septimus_parts_share_the_register_without_repeating_accounts(self):
        books=[('Clavis','Clavis','','clavis.pdf',''),('VII','De Vinculis','','vinculis.pdf','')]
        records,_,inputs=backmatter.collect(books)
        # S21 is cited only by the Quaestio Clausa, printed open at the end of De Vinculis.
        self.assertEqual({k for r in records for k in r['keys']},{f'VII/S{i}' for i in range(1,22)})
        for record in records:
            self.assertEqual(len(record['accounts']),len({json.dumps(a,sort_keys=True) for a in record['accounts']}))
        self.assertIn('books/07_septimus/manuscript/clavis.md',inputs)
        self.assertIn('books/07_septimus/manuscript/de-vinculis.md',inputs)
        self.assertIn('books/07_septimus/manuscript/quaestio.md',inputs)

    def test_quaestio_keys_with_the_book_prefix_select_and_link_their_entries(self):
        import re
        records,_,_=backmatter.collect([('VII','De Vinculis','','vinculis.pdf','')])
        keys={k for r in records for k in r['keys']}
        quaestio=(ROOT/'books/07_septimus/manuscript/quaestio.md').read_text()
        for key in re.findall(r'\[VII/(S\d+)\]',quaestio):self.assertIn('VII/'+key,keys)
        pattern,prefix=unified.CITATIONS['De Vinculis']
        self.assertEqual(prefix+re.fullmatch(pattern,' [VII/S10] ')[1],'VII/S10')
        self.assertEqual(prefix+re.fullmatch(pattern,'[S10]')[1],'VII/S10')
        self.assertIsNone(re.fullmatch(pattern,'[V/S8]'))

    def test_relocated_septimus_citation_targets_the_new_entry_and_keeps_external_links(self):
        from pypdf import PdfReader,PdfWriter
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory);source=root/'septimus.pdf'
            c=Canvas(str(source),pagesize=(504,720),invariant=1)
            c.drawString(50,600,'[S1]');c.linkRect('', 'old-reference',(50,598,75,612),relative=0)
            c.linkURL('https://example.org',(50,500,100,512),relative=0)
            c.showPage();c.bookmarkPage('old-reference');c.drawString(50,600,'Old reference');c.showPage();c.save()
            writer=PdfWriter()
            writer.add_blank_page(504,720);writer.add_page(PdfReader(source).pages[0]);writer.add_blank_page(504,720)
            log={'De Vinculis':dict(source='septimus.pdf',body_page_map={'1':2})}
            entries=[dict(keys=['VII/S1'],start_page=3)]
            self.assertEqual(unified.relink_septimus(writer,log,entries,root),1)
            out=root/'bound.pdf'
            with out.open('wb') as f:writer.write(f)
            reader=PdfReader(out);annotations=[a.get_object() for a in reader.pages[1]['/Annots']]
            internal=[a for a in annotations if '/Dest' in a]
            self.assertEqual(len(internal),1)
            self.assertEqual(internal[0]['/Dest'][0].idnum,reader.pages[2].indirect_reference.idnum)
            self.assertTrue(any(a.get('/A',{}).get('/URI')=='https://example.org' for a in annotations))

    def test_book_vi_register_joins_the_end_bibliography_in_sequence(self):
        import bind
        register=json.loads((ROOT/backmatter.BOOK_VI_REGISTER).read_text())
        records,notes,inputs=backmatter.collect([bind.POTESTATE])
        self.assertEqual({k for r in records for k in r['keys']},{k for r in register for k in r['keys']})
        self.assertIn(backmatter.BOOK_VI_REGISTER,inputs)
        # The preparation leaf moves from the PDF (unified.MOVE_HEADINGS), not from collect().
        self.assertEqual(notes,[])
        # Surname-first citations sort among the other books' entries.
        literature=[r['citation'] for r in records if not backmatter.is_project_record(r)]
        self.assertEqual(literature,sorted(literature,key=backmatter.identity))
        self.assertTrue(any(c.startswith('Hoorens, V., and Renders, H. (2012)') for c in literature))
        # Freeman's composite version is one entry with I-II's, each wording kept.
        book=json.loads((ROOT/'books/01_matricis_intervallorum/manuscript/book.json').read_text())
        merged=backmatter.consolidate(backmatter.opening_records(book)+records)
        freeman=[r for r in merged if 'VI/F1' in r['keys']]
        self.assertEqual(len(freeman),1)
        self.assertEqual(set(freeman[0]['keys']),{'I-II/G3','VI/F1'})
        self.assertEqual(len(freeman[0]['accounts']),2)

    def test_nota_clausa_files_its_preparation_record_and_no_register(self):
        import bind
        records,notes,inputs=backmatter.collect([bind.CLAUSA])
        self.assertEqual(records,[])
        self.assertIn('books/07_septimus/clausa/README.md',inputs)
        self.assertEqual([n['title'] for n in notes],['Nota Clausa / preparation'])
        text=' '.join(notes[0]['paragraphs'])
        self.assertIn('Hand: Claude',text)
        self.assertIn('matched all eight digests',text)
        self.assertIn('The author holds them.',text)

    def test_consolidation_leaves_no_two_entries_with_one_citation(self):
        # A SAME_SOURCE group that omits a key citing the source splits the entry it joins.
        import bind
        records,_,_=backmatter.collect(bind.BOOKS)
        identities=[backmatter.identity(r['citation']) for r in records]
        self.assertEqual(len(identities),len(set(identities)))

    def _book_vi_source(self,root,text):
        from reportlab.platypus import Paragraph
        from reportlab.lib.styles import ParagraphStyle
        source=root/'vi.pdf';c=Canvas(str(source),pagesize=(504,720),invariant=1)
        p=Paragraph(text,ParagraphStyle('t',fontName='Helvetica',fontSize=11,leading=14))
        p.wrap(380,100);p.drawOn(c,66,600);c.showPage()
        c.bookmarkPage('ref-A1');c.drawString(52,600,'VI/A1');c.drawString(52,560,'VI/B2')
        c.bookmarkPage('ref-B2',top=560);c.showPage();c.save()
        return source

    def test_book_vi_key_links_read_through_brackets_and_target_the_new_entries(self):
        from pypdf import PdfReader,PdfWriter
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory)
            source=self._book_vi_source(root,'As the record shows [<a href="#ref-A1">A1</a>, <a href="#ref-B2">B2</a>].')
            writer=PdfWriter()
            writer.add_blank_page(504,720);writer.add_page(PdfReader(source).pages[0]);writer.add_blank_page(504,720);writer.add_blank_page(504,720)
            log={'De Potestate et Accusatione':dict(source='vi.pdf',body_page_map={'1':2})}
            entries=[dict(keys=['VI/A1'],start_page=3),dict(keys=['III/D05','VI/B2'],start_page=4)]
            self.assertEqual(unified.relink(writer,log,entries,root,unified.BOOK_VI),2)
            out=root/'bound.pdf'
            with out.open('wb') as f:writer.write(f)
            reader=PdfReader(out);ids=[p.indirect_reference.idnum for p in reader.pages]
            targets=sorted(ids.index(a.get_object()['/Dest'][0].idnum)+1 for a in reader.pages[1]['/Annots'])
            self.assertEqual(targets,[3,4])

    def test_an_unreadable_book_vi_link_stops_the_binding(self):
        from pypdf import PdfReader,PdfWriter
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory)
            source=self._book_vi_source(root,'See <a href="#ref-A1">the register</a>.')
            writer=PdfWriter();writer.add_blank_page(504,720);writer.add_page(PdfReader(source).pages[0])
            log={'De Potestate et Accusatione':dict(source='vi.pdf',body_page_map={'1':2})}
            with self.assertRaises(ValueError):
                unified.relink(writer,log,[dict(keys=['VI/A1'],start_page=1)],root,unified.BOOK_VI)

    def test_shared_citation_keeps_both_keys_and_inspection_accounts(self):
        citation='Ashby, W. R. (1956). An Introduction to Cybernetics.'
        records=[dict(citation=citation,keys=[key],accounts=[dict(book=key.split('/')[0],status=status,use='Available responses.')],urls=[])
                 for key,status in [('I-II/A1','Primary text inspected.'),('IV/A1','Not inspected in this pass.')]]
        merged=backmatter.consolidate(records)
        self.assertEqual(len(merged),1)
        self.assertEqual(merged[0]['keys'],['I-II/A1','IV/A1'])
        self.assertEqual(len(merged[0]['accounts']),2)

    def test_publication_details_do_not_get_labeled_as_an_inspection(self):
        books=[('V','Ars Notoria Stigmatum','', 'present.pdf','Claude and ChatGPT/Codex')]
        records,notes,inputs=backmatter.collect(books)
        waite=next(r for r in records if 'V/S2' in r['keys'])
        self.assertTrue(waite['citation'].startswith('Waite, A. E.'))
        self.assertIn('1910',waite['citation'])
        self.assertTrue(waite['accounts'][0]['status'].startswith('Online transcription inspected'))
        self.assertEqual({k for r in records for k in r['keys']},{f'V/S{i}' for i in range(1,13)}|{'V/R0'})
        jones=next(r for r in records if 'V/S9' in r['keys'])
        self.assertTrue(jones['citation'].startswith('Jones, J.'))
        self.assertIn('Artificial Life 16(2)',jones['citation'])
        self.assertTrue(jones['accounts'][0]['status'].startswith('Publication metadata checked'))
        # Book V's own source trail is the account; no generated use line is added.
        self.assertTrue(all(not a['use'] for r in records for a in r['accounts']))

    def test_book_v_ifa_sources_keep_their_editions_and_inspection_limits(self):
        records,_,_=backmatter.collect([('V','Ars Notoria Stigmatum','','present.pdf','Claude and ChatGPT/Codex')])
        cases=[
            ('V/S10','Ogunnaike, O. Sufism and Ifa: Ways of Knowing in Two West African Intellectual Traditions. Doctoral dissertation, Harvard University, 2015.',
             'Inspected passages: pp. 257–262; 280; 283–286; 316–321; 377–397.',
             'selected passage checks, not a claim to have reviewed all 542 PDF pages',
             'https://dash.harvard.edu/entities/publication/73120378-f5d2-6bd4-e053-0100007fdf3b'),
            ('V/S11','Barry Hallen, “Ethical Knowledge in an African Philosophy.” Florida Philosophical Review 3(1), Summer 2003, pp. 81–90.',
             'Article inspected, especially pp. 83–87',
             "not an inspection of their entire joint monograph or a substitute for Ogunnaike's Ifá fieldwork",
             'https://cah.ucf.edu/fpr/article/ethical-knowledge-in-an-african-philosophy/'),
            ('V/S12','William Bascom, Ifa Divination: Communication Between Gods and Men in West Africa. Bloomington: Indiana University Press, 1969.',
             'Chapter-opening excerpts inspected on JSTOR: I, p. 3; V, p. 51; VII, p. 68; XII, p. 120.',
             "not independent inspection of Bascom's pp. 76–80",
             'https://www.jstor.org/stable/j.ctt16gzhwk'),
        ]
        for key,citation,opening,limit,url in cases:
            with self.subTest(key=key):
                record=next(r for r in records if key in r['keys'])
                self.assertEqual(record['keys'],[key])
                self.assertEqual(record['citation'],citation)
                self.assertEqual(len(record['accounts']),1)
                account=record['accounts'][0]
                self.assertEqual(account['book'],'V')
                self.assertTrue(account['status'].startswith(opening))
                self.assertIn(limit,account['status'])
                self.assertEqual(account['use'],'')
                self.assertEqual(record['urls'],[url])
        # The dissertation cannot silently stand in for the uninspected book chapters.
        book=next(r for r in records if 'V/S7' in r['keys'])
        self.assertEqual(book['keys'],['V/S7'])
        self.assertIn('Deep Knowledge:',book['citation'])
        self.assertIn('Penn State University Press, 2020.',book['citation'])
        self.assertIn('Full Ifá chapters not inspected.',book['accounts'][0]['status'])
        self.assertIn('not substituted for this edition',book['accounts'][0]['status'])

    def test_escalationum_debts_split_at_their_bibliographic_heads(self):
        catalogue=json.loads((ROOT/'books/03_escalationum/manuscript/catalogue.json').read_text())
        debts=[p for s in catalogue['back'] if s['title'].startswith('A register of debts') for p in s['paragraphs']
               if not p.startswith(('The research check','Four parables','Robert Fludd'))]
        prefixes=[h[0] for h in backmatter.ESCALATIONUM_HEADS]
        for p in debts:self.assertTrue(p.startswith(tuple(prefixes)),'No register head for: '+p[:60])
        books=[('III','Pseudomonarchia Escalationum','','present.pdf','ChatGPT/Codex')]
        records,notes,inputs=backmatter.collect(books)
        braverman=next(r for r in records if r['citation'].startswith('Braverman'))
        self.assertTrue(braverman['citation'].endswith('especially chapter 4.'))
        self.assertTrue(braverman['accounts'][0]['use'].startswith('Separation of conception'))
        for r in records:
            for a in r['accounts']:
                self.assertEqual(a['status'],'')
                self.assertNotIn('inspection limits are recorded',a['use'])

    def test_same_source_in_different_words_merges_and_keeps_each_wording(self):
        records=[dict(citation='Toyota production system: andon and jidoka.',keys=['IV/T1'],
                      accounts=[dict(book='IV',status='General knowledge.',use='The stop-work cord.')],urls=[]),
                 dict(citation='Toyota. Public description of the Toyota Production System: jidoka and andon.',keys=['III/D10'],
                      accounts=[dict(book='III',status='',use='A deliberate inversion.')],urls=[])]
        merged=backmatter.consolidate(records)
        self.assertEqual(len(merged),1)
        self.assertEqual(set(merged[0]['keys']),{'III/D10','IV/T1'})
        self.assertTrue(merged[0]['citation'].startswith('Toyota. Public description'))
        iv=next(a for a in merged[0]['accounts'] if a['book']=='IV')
        self.assertEqual(iv['cited_as'],'Toyota production system: andon and jidoka.')
        self.assertEqual(backmatter.consolidate(merged),merged)

    def test_project_records_are_set_apart_and_opening_has_no_duplicate_reading(self):
        book=json.loads((ROOT/'books/01_matricis_intervallorum/manuscript/book.json').read_text())
        records=backmatter.consolidate(backmatter.opening_records(book))
        for author in ('Freeman, J.','Birch, J.','Nussbaum, M. C.'):
            self.assertEqual(sum(1 for r in records if author in r['citation']),1,author)
        project={k for r in records if backmatter.is_project_record(r) for k in r['keys']}
        self.assertIn('I-II/P0',project);self.assertIn('I-II/P1',project)
        self.assertFalse(any(k in project for k in ('I-II/A1','I-II/G3','I-II/V3')))
        b=io.BytesIO();c=Canvas(b,pagesize=(504,720),invariant=1)
        result=backmatter.write(c,records,[dict(title='I-II / preparation',paragraphs=['A note. '*400])]);c.save()
        self.assertEqual([s['title'] for s in result['sections']][:2],['Project records','Production and source notes'])
        d=fitz.open(stream=b.getvalue(),filetype='pdf')
        notes_pages=[p for p in d if 'PRODUCTION NOTES' in p.get_text()]
        self.assertTrue(notes_pages)
        for p in notes_pages:self.assertNotIn('Bibliography, continued',p.get_text())

    def test_preparation_labels_move_without_removing_historical_text(self):
        with tempfile.TemporaryDirectory() as directory:
            path=Path(directory)/'book.pdf';c=Canvas(str(path),pagesize=(504,720),invariant=1)
            c.drawString(50,650,'A text of 1577 remains evidence.')
            c.drawString(50,100,'Josiah Alan-Lee')
            c.drawString(50,80,'Prepared for Josiah Alan-Lee, 17 October 2026')
            c.showPage();c.save()
            raw,moved,notes,redactions=unified.clean_source('Pseudomonarchia Escalationum',path,ROOT)
            clean=fitz.open(stream=raw,filetype='pdf')[0].get_text()
            self.assertIn('A text of 1577 remains evidence.',clean)
            self.assertNotIn('Josiah',clean)
            self.assertTrue(redactions)
            self.assertIn('Josiah',fitz.open(path)[0].get_text())

    def test_long_reference_and_note_flow_in_one_font_system(self):
        record=dict(citation='Author (2026). '+('A long bibliographic title. '*80),keys=['IV/X1'],
                    accounts=[dict(book='IV',status='Not independently verified.',use='A stated illustration.')],urls=[])
        b=io.BytesIO();c=Canvas(b,pagesize=(504,720),invariant=1)
        result=backmatter.write(c,[record],[dict(title='Preparation',paragraphs=['Prepared for the author.'])]);c.save()
        d=fitz.open(stream=b.getvalue(),filetype='pdf');text=' '.join(p.get_text() for p in d)
        self.assertIn('Not independently verified.',text)
        self.assertIn('Prepared for the author.',text)
        self.assertGreater(len(d),1)
        for p in d:
            for block in p.get_text('dict')['blocks']:
                for line in block.get('lines',[]):self.assertTrue(p.rect.contains(fitz.Rect(line['bbox'])))


if __name__=='__main__':unittest.main()
