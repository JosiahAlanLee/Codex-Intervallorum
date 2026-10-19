"""Opaque, fixed-page PDF for readers that mishandle layered illustrations.

Each page is one lossless RGB image at 144 dpi, with explicit matching page
boxes. The vector master remains the source for printing, text selection and
deep zoom. This copy preserves page order, bookmarks and links; it does not
reflow text or remove a reader application's external letterboxing.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import fitz

VERSION = 'phone-1'
DEFAULT_DPI = 144


def links(page):
    return [{k: v for k, v in link.items() if k not in ('xref', 'id')}
            for link in page.get_links()]


def copy_link(target, page_number, link):
    page = target[page_number]
    # MuPDF exposes a native /Fit destination as a named-style link with a
    # one-based page string. insert_link expects a different named-link shape.
    if (link['kind'] == fitz.LINK_NAMED and link.get('view') == 'Fit'
            and isinstance(link.get('page'), str) and link['page'].isdecimal()):
        destination = int(link['page']) - 1
        if not 0 <= destination < len(target):
            raise ValueError('Internal /Fit destination is outside the book')
        existing = {x['xref'] for x in page.get_links()}
        page.insert_link(dict(kind=fitz.LINK_GOTO, **{'from': link['from']},
                              page=destination, to=fitz.Point(0, 0)))
        page = target.reload_page(page)
        added = [x['xref'] for x in page.get_links() if x['xref'] not in existing]
        if len(added) != 1:
            raise ValueError('Cannot identify the copied internal link')
        target.xref_set_key(added[0], 'A', 'null')
        target.xref_set_key(added[0], 'Dest', f'[{target.page_xref(destination)} 0 R /Fit]')
    else:
        page.insert_link(link)


def outline(doc):
    return [[*entry[:3], {k: v for k, v in entry[3].items() if k != 'xref'}]
            for entry in doc.get_toc(simple=False)]


def copy_outline(original, target):
    source = original.get_toc(simple=False)
    prepared = []
    for level, title, page, destination in source:
        dest = {k: v for k, v in destination.items() if k != 'xref'}
        if dest.get('view') == 'Fit':
            dest = dict(kind=fitz.LINK_GOTO, page=page - 1, to=fitz.Point(0, 0), zoom=0)
        prepared.append([level, title, page, dest])
    target.set_toc(prepared)
    for before, after in zip(source, target.get_toc(simple=False)):
        if before[3].get('view') == 'Fit':
            xref = after[3]['xref']
            target.xref_set_key(xref, 'A', 'null')
            target.xref_set_key(xref, 'Dest', f'[{target.page_xref(before[2] - 1)} 0 R /Fit]')
        # Keep expansion state and optional formatting of the existing outline.
        for key in ('Count', 'F', 'C'):
            kind, value = original.xref_get_key(before[3]['xref'], key)
            if kind != 'null':
                target.xref_set_key(after[3]['xref'], key, value)


def build(source, output, *, dpi=DEFAULT_DPI):
    source, output = Path(source), Path(output)
    if source.resolve() == output.resolve():
        raise ValueError('Keep the vector master; choose a separate output file')
    if not isinstance(dpi, int) or not 72 <= dpi <= 300:
        raise ValueError('dpi must be an integer between 72 and 300')
    output.parent.mkdir(parents=True, exist_ok=True)
    temporary = output.with_name(output.name + '.tmp')
    raster_hashes = []
    with fitz.open(source) as original, fitz.open() as target:
        if any(p.rotation or p.rect.x0 or p.rect.y0 for p in original):
            raise ValueError('Phone export requires unrotated, zero-origin pages')
        try:
            for page in original:
                out = target.new_page(width=page.rect.width, height=page.rect.height)
                for setter in ('set_cropbox', 'set_trimbox', 'set_bleedbox', 'set_artbox'):
                    getattr(out, setter)(out.rect)
            # Create forward destinations and check navigation before rendering.
            for i, page in enumerate(original):
                for link in links(page):
                    copy_link(target, i, link)
            for i, page in enumerate(original):
                pix = page.get_pixmap(dpi=dpi, colorspace=fitz.csRGB, alpha=False)
                # Hash the actual source capture so export fidelity does not
                # depend on repeating a complex vector render during validation.
                raster_hashes.append((pix.width, pix.height,
                                      hashlib.sha256(pix.samples).hexdigest()))
                out = target[i]
                # Full-page image placement uses the source page's exact shape.
                # At the books' 7 x 10 inch trim, 144 dpi is exactly 1008 x 1440.
                image = out.insert_image(out.rect, pixmap=pix, keep_proportion=False)
                target.xref_set_key(image, 'ColorSpace', '/DeviceRGB')
                if (i + 1) % 50 == 0:
                    print(f'Phone: rendered {i + 1}/{len(original)} pages', flush=True)
            copy_outline(original, target)
            target.set_page_labels(original.get_page_labels())
            metadata = dict(original.metadata)
            metadata['title'] = (metadata.get('title') or source.stem) + ' (phone copy)'
            metadata['keywords'] = (metadata.get('keywords') or '') + '; ' + VERSION
            target.set_metadata(metadata)
            target.xref_set_key(target.pdf_catalog(), 'PageLayout', '/SinglePage')
            target.save(temporary, garbage=4, deflate=True, no_new_id=True)
            with fitz.open(temporary) as saved:
                if len(saved) != len(original) or outline(saved) != outline(original):
                    raise ValueError('Page order or bookmarks changed')
                if saved.get_page_labels() != original.get_page_labels():
                    raise ValueError('Page labels changed')
                for i, (before, after) in enumerate(zip(original, saved)):
                    if (after.rect != before.rect or after.rotation
                            or any(getattr(after, box) != after.rect for box in
                                   ('mediabox', 'cropbox', 'trimbox', 'bleedbox', 'artbox'))):
                        raise ValueError(f'Page {i + 1}: page geometry changed')
                    images = after.get_images()
                    if len(images) != 1 or images[0][1] or images[0][5] != 'DeviceRGB':
                        raise ValueError(f'Page {i + 1}: expected one opaque RGB image')
                    if links(before) != links(after):
                        raise ValueError(f'Page {i + 1}: links changed')
                    actual = after.get_pixmap(dpi=dpi, colorspace=fitz.csRGB, alpha=False)
                    expected = raster_hashes[i]
                    if ((actual.width, actual.height) != expected[:2]
                            or hashlib.sha256(actual.samples).hexdigest() != expected[2]):
                        raise ValueError(f'Page {i + 1}: rendered pixels changed')
                    if (i + 1) % 50 == 0:
                        print(f'Phone: verified {i + 1}/{len(original)} pages', flush=True)
            temporary.replace(output)
        except Exception:
            temporary.unlink(missing_ok=True)
            raise
        with source.open('rb') as stream:
            digest = hashlib.file_digest(stream, 'sha256').hexdigest()
        report = dict(version=VERSION, pages=len(original), dpi=dpi,
                      source_file=source.name, source_sha256=digest,
                      encoding='lossless RGB', selectable_text=False,
                      captured_raster_sha256=[x[2] for x in raster_hashes],
                      verification=dict(rendered_pixels_exact=True, page_geometry_exact=True,
                                        bookmarks_exact=True, links_exact=True,
                                        page_labels_exact=True, image_soft_masks=0),
                      device_tested=False)
    output.with_suffix('.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({k: v for k, v in report.items() if k != 'captured_raster_sha256'}), flush=True)
    return report


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source', type=Path)
    parser.add_argument('output', type=Path)
    parser.add_argument('--dpi', type=int, default=DEFAULT_DPI)
    args = parser.parse_args()
    build(args.source, args.output, dpi=args.dpi)
