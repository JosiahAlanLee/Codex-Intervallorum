import hashlib
import importlib.util
from pathlib import Path
import re
import sys
import tempfile
import unittest

import fitz

ROOT = Path(__file__).resolve().parents[1]
CLAUSA = ROOT / 'clausa'
sys.path.insert(0, str(CLAUSA))
import plate_order as po


class ClausaOrderingTests(unittest.TestCase):
    def test_shortcut_uses_the_complete_printed_sign_table(self):
        text = (CLAUSA / 'REGULA.md').read_text().split('19. ', 1)[1].split('20. ', 1)[0]
        signs = []
        for line in text.splitlines():
            if re.match(r'\s*\| \d+ \|', line):
                cells = [cell.strip() for cell in re.split(r'(?<!\\)\|', line.strip())[2:-1]]
                signs.extend({'space': ' ', '¶': '\n', r'\|': '|'}.get(cell, cell) for cell in cells)
        self.assertEqual(len(signs), 64)
        self.assertEqual(''.join(signs), po.ALPHABET)

    def test_document_order_shortcut_is_removed_without_changing_cell_bits(self):
        # In document order these six colours encode A. Spatial order differs.
        paths = []
        for i, x in enumerate([131, 130, 132, 133, 134, 129]):
            mx, my = po.X0 + x * po.PITCH, po.Y0 + 130 * po.PITCH
            colour = po.RED if i == 5 else po.INK
            paths.append(f'<path fill="none" stroke="{colour}" stroke-width="0.17" d="M{mx-.1:.2f},{my:.2f}L{mx+.1:.2f},{my:.2f}"/>')
        footer = '<path fill="none" stroke="#a32b24" stroke-width="0.17" d="M85.6,279.99L87.28,277.4"/>'
        source = '<svg><g inkscape:label="Art Paths">' + ''.join(paths) + '</g><g inkscape:label="Text Outlines">' + footer + '</g></svg>'
        expected = hashlib.sha256(b'A').hexdigest()
        self.assertEqual(po.document_order_digest(source), expected)
        ordered = po.ordered_svg(source)
        self.assertNotEqual(po.document_order_digest(ordered), expected)
        self.assertEqual(po.marks_from_text(ordered), po.marks_from_text(source))
        self.assertEqual(len(po.marks_from_text(ordered)), 6)
        self.assertIn(footer, ordered)
        self.assertTrue(po.spatially_ordered(ordered))
        self.assertEqual(po.ordered_svg(ordered), ordered)

    def test_public_plates_are_ordered_and_do_not_match_the_shortcut(self):
        table = (CLAUSA / 'TABULA.md').read_text()
        expected = dict(re.findall(r'^\| (I|II|III|IV|V|VI|VII) \| `([0-9a-f]{64})` \|$', table, re.M))
        for k, roman in enumerate(['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'], 1):
            with self.subTest(field=roman):
                source = (CLAUSA / 'plates' / f'nota-clausa-{k}.svg').read_text()
                self.assertEqual(len(po.marks_from_text(source)), po.N)
                self.assertTrue(po.spatially_ordered(source))
                self.assertNotEqual(po.document_order_digest(source), expected[roman])

    def test_pdf_builder_orders_even_an_unsorted_input(self):
        spec = importlib.util.spec_from_file_location('clausa_reading_build', CLAUSA / 'build.py')
        build = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(build)
        # Field II also contains a zero-length contour segment on a data cell.
        source = (CLAUSA / 'plates/nota-clausa-2.svg').read_text()
        art, boundary, lettering = source.partition('inkscape:label="Text Outlines"')
        paths = iter(reversed([m.group(0) for m in po.MARK_PATH.finditer(art)]))
        unsorted = po.MARK_PATH.sub(lambda _: next(paths), art) + boundary + lettering
        self.assertFalse(po.spatially_ordered(unsorted))
        original = po.marks_from_text(source)
        with tempfile.TemporaryDirectory() as folder:
            svg, pdf = Path(folder, 'unsorted.svg'), Path(folder, 'ordered.pdf')
            svg.write_text(unsorted)
            build.fonts()
            book = build.Book(pdf)
            book.plate(2, svg)
            book.c.save()
            # The builder fits an A4 sheet into a 432-point-wide frame. PDF
            # coordinates below are measured downwards, as in the Regula.
            scale = 432 / 210
            top = (build.PH - 297 * scale) / 2 + 8
            cells = []
            bits = {}
            with fitz.open(pdf) as doc:
                for drawing in doc[0].get_drawings():
                    items = drawing['items']
                    if len(items) != 1 or items[0][0] != 'l':
                        continue
                    _, a, b = items[0]
                    if abs(b - a) < .01 or abs(drawing['width'] - .17 * scale) > .001:
                        continue
                    mx, my = ((a.x + b.x) / 2 - 36) / scale, ((a.y + b.y) / 2 - top) / scale
                    x, y = round((mx - po.X0) / po.PITCH), round((my - po.Y0) / po.PITCH)
                    if not po.inside(x, y) or abs(mx - po.X0 - x * po.PITCH) > .05 or abs(my - po.Y0 - y * po.PITCH) > .05:
                        continue
                    cells.append((x, y))
                    bits[(x, y)] = int(drawing['color'][0] > .4)
            self.assertEqual(len(cells), po.N)
            self.assertEqual(cells, sorted(cells, key=lambda cell: (cell[1], cell[0])))
            self.assertEqual(bits, original)


class CommentariumStructureTests(unittest.TestCase):
    def test_claim_identifiers_are_unique_and_match_operation_tags(self):
        source = (ROOT / 'manuscript/de-vinculis.md').read_text()
        claims = re.findall(r'^\*\*(V\d+) — ', source, re.M)
        self.assertEqual(len(claims), len(set(claims)))
        for operation in re.split(r'<!-- operation: ', source)[1:]:
            header, body = operation.split('-->', 1)
            self.assertEqual(set(re.findall(r'\bV\d+\b', header)), set(re.findall(r'^\*\*(V\d+) — ', body, re.M)))

    def test_each_commentarium_has_a_revision(self):
        source = (ROOT / 'manuscript/de-vinculis.md').read_text()
        operations = re.split(r'<!-- operation: ', source)[1:]
        self.assertEqual(len(operations), 7)
        for operation in operations:
            self.assertIn('**Revision.**', operation)


if __name__ == '__main__':
    unittest.main()
