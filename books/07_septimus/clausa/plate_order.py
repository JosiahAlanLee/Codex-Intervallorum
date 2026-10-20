"""Read and spatially serialize the Nota Clausa's public plot marks.

Cell coordinates and colours carry the reading. SVG document order must not carry
the agent numbers used to recover it. Only the mark paths are reordered; all other
SVG bytes, including the lettering and contour paths, are retained.
"""
from __future__ import annotations

import argparse
import hashlib
from pathlib import Path
import re

INK, RED = '#161918', '#a32b24'
G, D, N = 260, 236, 7920
X0, Y0, PITCH = 14.35, 61.35, 0.7
ALPHABET = " ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,;:'-/[]\n()?!\"&+=*#%<>@_|~"
MARK_PATH = re.compile(r'<path fill="none" stroke="(#[0-9a-f]{6})" stroke-width="0\.17" d="M([^"L]+L[^"L]+)"/>')


def inside(x, y):
    return 0 <= x < G and 0 <= y < G and (2 * x + 1 - G) ** 2 + (2 * y + 1 - G) ** 2 <= D * D


def _records(svg):
    art = svg.split('inkscape:label="Text Outlines"', 1)[0]
    records = []
    cells = set()
    for match in MARK_PATH.finditer(art):
        colour, d = match.groups()
        a, b = d.split('L')
        (x1, y1), (x2, y2) = [tuple(map(float, p.split(','))) for p in (a, b)]
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        cx, cy = round((mx - X0) / PITCH), round((my - Y0) / PITCH)
        if abs(cx * PITCH + X0 - mx) > 0.05 or abs(cy * PITCH + Y0 - my) > 0.05:
            raise ValueError(f'mark off the lattice at {mx:.2f},{my:.2f}')
        if (cx, cy) in cells:
            raise ValueError(f'two marks on cell {(cx, cy)}')
        if colour not in (INK, RED):
            raise ValueError(f'third ink {colour}')
        cells.add((cx, cy))
        records.append(((cx, cy), int(colour == RED), match))
    return records


def marks_from_text(svg):
    """Return {(x, y): bit}, retaining document order for the leakage check."""
    return {cell: bit for cell, bit, _ in _records(svg)}


def spatially_ordered(svg):
    cells = list(marks_from_text(svg))
    return cells == sorted(cells, key=lambda cell: (cell[1], cell[0]))


def ordered_svg(svg):
    """Sort mark paths by (y, x), preserving every cell, colour and other byte."""
    records = _records(svg)
    ordered = iter(sorted(records, key=lambda row: (row[0][1], row[0][0])))
    parts = []
    start = 0
    for _, _, match in records:
        parts.extend((svg[start:match.start()], next(ordered)[2].group(0)))
        start = match.end()
    parts.append(svg[start:])
    return ''.join(parts)


def document_order_digest(svg):
    """Digest the known six-bit shortcut, without printing or saving a reading."""
    bits = list(marks_from_text(svg).values())
    if len(bits) % 6:
        raise ValueError('incomplete six-bit sign')
    reading = bytes(ord(ALPHABET[sum(bits[i + j] << (5 - j) for j in range(6))])
                    for i in range(0, len(bits), 6))
    return hashlib.sha256(reading).hexdigest()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('plates', nargs='+', type=Path)
    args = ap.parse_args()
    for path in args.plates:
        source = path.read_text()
        result = ordered_svg(source)
        if marks_from_text(source) != marks_from_text(result):
            raise ValueError(f'{path}: cell colours changed')
        if result != source:
            path.write_text(result)
            print(f'{path}: ordered {len(marks_from_text(result))} marks')


if __name__ == '__main__':
    main()
