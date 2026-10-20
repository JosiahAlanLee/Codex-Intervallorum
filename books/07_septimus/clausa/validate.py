#!/usr/bin/env python3
"""Public checks for the Nota Clausa. Needs no key and reads nothing sealed.

1. Each plot sheet in fields/ carries 7920 marks, one per cell, every cell inside the arena
   of the Regula, in the two inks only.
2. Each sheet lists its marks in the order of the ground, by y and then x (Regula, clause 17).
   The first seal listed them in the order of the agents, and could be read without the key.
3. The Tabula prints eight digests.
4. The first seal's record: the readings filed in plates/readings/ match the digests its
   Tabula printed, kept in plates/README.md. That text is printed open in De Vinculis.
5. Optionally, a proposed reading of the fields is checked against the Tabula's digests:
       python validate.py --reading readings/
   where readings/ holds field-1.txt ... field-7.txt, each the 1320 signs of the
   Regula's clause 21 (line feeds as line feeds).
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent
INK, RED = '#161918', '#a32b24'
G, D, N = 260, 236, 7920
X0, Y0, PITCH = 14.35, 61.35, 0.7     # Regula, clause 17
ROMAN = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']


def inside(x, y):
    return 0 <= x < G and 0 <= y < G and (2 * x + 1 - G) ** 2 + (2 * y + 1 - G) ** 2 <= D * D


def marks(svg_path):
    """The marks of one plot sheet, in the order the sheet lists them: [((x, y), bit)]."""
    s = Path(svg_path).read_text().split('inkscape:label="Text Outlines"')[0]   # marks are in Art Paths
    out, seen = [], set()
    for colour, d in re.findall(r'<path fill="none" stroke="(#[0-9a-f]{6})" stroke-width="0\.17" d="M([^"L]+L[^"L]+)"/>', s):
        a, b = d.split('L')
        (x1, y1), (x2, y2) = [tuple(map(float, p.split(','))) for p in (a, b)]
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        cx, cy = round((mx - X0) / PITCH), round((my - Y0) / PITCH)
        if abs(cx * PITCH + X0 - mx) > 0.05 or abs(cy * PITCH + Y0 - my) > 0.05:
            raise ValueError(f'{svg_path}: mark off the lattice at {mx:.2f},{my:.2f}')
        if (cx, cy) in seen:
            raise ValueError(f'{svg_path}: two marks on cell {(cx, cy)}')
        if colour not in (INK, RED):
            raise ValueError(f'{svg_path}: third ink {colour}')
        seen.add((cx, cy))
        out.append(((cx, cy), 1 if colour == RED else 0))
    return out


def digests(path):
    rows = re.findall(r'^\| (I|II|III|IV|V|VI|VII|All seven) \| `([0-9a-f]{64})` \|$', Path(path).read_text(), re.M)
    return dict(rows)


def reading_digests(folder):
    texts = [Path(folder, f'field-{k}.txt').read_bytes() for k in range(1, 8)]
    got = {ROMAN[k]: hashlib.sha256(t).hexdigest() for k, t in enumerate(texts)}
    got['All seven'] = hashlib.sha256(b''.join(texts)).hexdigest()
    return got


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument('--reading', help='folder holding field-1.txt ... field-7.txt')
    args = ap.parse_args(argv)
    report = {'fields': {}}
    for k in range(1, 8):
        m = marks(ROOT / 'fields' / f'nota-clausa-{k}.svg')
        cells = [c for c, _ in m]
        outside = [c for c in cells if not inside(*c)]
        ground_order = cells == sorted(cells, key=lambda c: (c[1], c[0]))
        report['fields'][ROMAN[k - 1]] = {'marks': len(m), 'red': sum(b for _, b in m), 'outside_arena': len(outside),
                                          'in_ground_order': ground_order,
                                          'ok': len(m) == N and not outside and ground_order}
    dg = digests(ROOT / 'TABULA.md')
    report['digests_printed'] = len(dg)
    first = digests(ROOT / 'plates' / 'README.md')
    got = reading_digests(ROOT / 'plates' / 'readings')
    report['first_seal_readings_match_its_digests'] = len(first) == 8 and all(got[k] == first[k] for k in first)
    ok = all(p['ok'] for p in report['fields'].values()) and len(dg) == 8 and report['first_seal_readings_match_its_digests']
    if args.reading:
        got = reading_digests(args.reading)
        report['reading'] = {k: got[k] == dg[k] for k in dg}
        ok = ok and all(report['reading'].values())
    report['ok'] = ok
    print(json.dumps(report, indent=1))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
