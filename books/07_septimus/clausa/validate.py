#!/usr/bin/env python3
"""Public geometry and ordering checks for the Nota Clausa. Needs no key.

1. Each plot sheet carries 7920 marks, one per cell, every cell inside the arena of the
   Regula, in the two inks only.
2. Mark paths are spatially ordered and the document-order shortcut fails to match
   the field's published digest. The recovered shortcut text is never printed.
3. The Tabula prints eight digests.
4. Optionally, a proposed reading is checked against those digests:
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

from plate_order import N, document_order_digest, inside, marks_from_text, spatially_ordered

ROOT = Path(__file__).resolve().parent


def marks(svg_path):
    """The marks of one plot sheet: {(x, y): bit}."""
    return marks_from_text(Path(svg_path).read_text())


def digests():
    rows = re.findall(r'^\| (I|II|III|IV|V|VI|VII|All seven) \| `([0-9a-f]{64})` \|$', (ROOT / 'TABULA.md').read_text(), re.M)
    return dict(rows)


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument('--reading', help='folder holding field-1.txt ... field-7.txt')
    args = ap.parse_args(argv)
    report = {'plates': {}}
    dg = digests()
    roman = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']
    for k in range(1, 8):
        source = (ROOT / 'plates' / f'nota-clausa-{k}.svg').read_text()
        m = marks_from_text(source)
        outside = [c for c in m if not inside(*c)]
        ordered = spatially_ordered(source)
        leaks = len(m) == N and document_order_digest(source) == dg.get(roman[k - 1])
        report['plates'][roman[k - 1]] = {'marks': len(m), 'red': sum(m.values()), 'outside_arena': len(outside),
                                          'spatially_ordered': ordered, 'document_order_leak': leaks,
                                          'ok': len(m) == N and not outside and ordered and not leaks}
    report['digests_printed'] = len(dg)
    ok = all(p['ok'] for p in report['plates'].values()) and len(dg) == 8
    if args.reading:
        texts = [Path(args.reading, f'field-{k}.txt').read_bytes() for k in range(1, 8)]
        got = {roman[k]: hashlib.sha256(t).hexdigest() for k, t in enumerate(texts)}
        got['All seven'] = hashlib.sha256(b''.join(texts)).hexdigest()
        report['reading'] = {k: got[k] == dg[k] for k in dg}
        ok = ok and all(report['reading'].values())
    report['ok'] = ok
    print(json.dumps(report, indent=1))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
