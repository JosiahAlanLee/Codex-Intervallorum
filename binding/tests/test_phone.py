"""Exercise layered artwork, page shape and navigation in the phone export."""
import importlib.util
from pathlib import Path
import tempfile
import unittest

import fitz

SPEC = importlib.util.spec_from_file_location('phone', Path(__file__).resolve().parents[1] / 'phone.py')
phone = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(phone)


class PhoneTests(unittest.TestCase):
    def test_layered_pages_are_opaque_exact_and_keep_navigation(self):
        with tempfile.TemporaryDirectory() as tmp:
            source, output = Path(tmp) / 'source.pdf', Path(tmp) / 'phone.pdf'
            with fitz.open() as doc:
                for i in range(2):
                    p = doc.new_page(width=504, height=720)
                    p.draw_rect(p.rect, color=None, fill=(.93, .90, .83))
                    p.insert_text((60, 90), f'Page {i + 1}: intact letters', fontsize=18)
                    p.draw_circle((180, 280), 80, color=(.6, .1, .1), width=.5)
                    p.draw_rect((80, 300, 420, 450), fill=(.2, .1, .05),
                                color=None, fill_opacity=.12)
                doc[0].insert_link(dict(kind=fitz.LINK_GOTO, **{'from': fitz.Rect(40, 40, 200, 70)},
                                        page=1, to=fitz.Point(0, 0)))
                doc[1].insert_link(dict(kind=fitz.LINK_URI, **{'from': fitz.Rect(40, 40, 200, 70)},
                                        uri='https://example.com'))
                p = doc[0]
                p.insert_link(dict(kind=fitz.LINK_GOTO, **{'from': fitz.Rect(40, 90, 200, 110)},
                                   page=1, to=fitz.Point(0, 0)))
                p = doc.reload_page(p)
                xref = p.get_links()[-1]['xref']
                doc.xref_set_key(xref, 'A', 'null')
                doc.xref_set_key(xref, 'Dest', f'[{doc.page_xref(1)} 0 R /Fit]')
                doc.set_toc([[1, 'First', 1], [1, 'Second', 2]])
                xref = doc.get_toc(simple=False)[0][3]['xref']
                doc.xref_set_key(xref, 'A', 'null')
                doc.xref_set_key(xref, 'Dest', f'[{doc.page_xref(0)} 0 R /Fit]')
                doc.set_page_labels([dict(startpage=0, prefix='leaf-', style='D', firstpagenum=1)])
                doc.save(source)
            original = source.read_bytes()
            result = phone.build(source, output)
            self.assertEqual(source.read_bytes(), original)
            self.assertTrue(result['verification']['rendered_pixels_exact'])
            self.assertFalse(result['selectable_text'])
            with fitz.open(output) as doc:
                self.assertEqual(doc[0].rect, fitz.Rect(0, 0, 504, 720))
                self.assertEqual(doc[0].get_images()[0][2:4], (1008, 1440))
                self.assertFalse(doc[0].get_text().strip())
                self.assertEqual(doc[0].get_links()[1]['page'], '2')
                self.assertEqual(doc[0].get_links()[1]['view'], 'Fit')
                self.assertEqual(doc.get_toc(simple=False)[0][3]['view'], 'Fit')
                self.assertFalse(any('/SMask ' in doc.xref_object(i)
                                     for i in range(1, doc.xref_length())))

    def test_master_cannot_be_overwritten(self):
        with self.assertRaisesRegex(ValueError, 'separate output'):
            phone.build('master.pdf', 'master.pdf')

    def test_rotated_pages_require_explicit_normalization(self):
        with tempfile.TemporaryDirectory() as tmp:
            source, output = Path(tmp) / 'source.pdf', Path(tmp) / 'phone.pdf'
            with fitz.open() as doc:
                doc.new_page(width=504, height=720).set_rotation(90)
                doc.save(source)
            with self.assertRaisesRegex(ValueError, 'unrotated'):
                phone.build(source, output)
            self.assertFalse(output.exists())


if __name__ == '__main__':
    unittest.main()
