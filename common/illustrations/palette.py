"""Native book plates developed from Claude's Codex palette research.

Guilloche constructions are retained in guilloche.py; the composition and
finite probability table are adapted/implemented with ChatGPT/Codex. These
are declared visual mappings, not recovered historical ritual diagrams.
"""
import html
import json
import math

import numpy as np
from shapely.geometry import LineString, Point
from shapely.ops import unary_union

from . import guilloche


class Plate:
    def __init__(self, title, width=170, height=220, ink="#161918", red="#a32b24"):
        self.title, self.width, self.height = title, width, height
        self.ink, self.red, self.paths = ink, red, []
        self.metadata = {}

    def add(self, points, red=False, width=.12):
        p = np.asarray(points, float)
        if len(p) < 2:
            return
        if p.ndim != 2 or p.shape[1] != 2 or not np.isfinite(p).all():
            raise ValueError("finite Nx2 geometry required")
        if (p < 0).any() or (p[:, 0] > self.width).any() or (p[:, 1] > self.height).any():
            raise ValueError("plate geometry outside trim")
        self.paths.append((p, self.red if red else self.ink, width))

    def ring(self, centre, radius, red=False, width=.12):
        t = np.linspace(0, math.tau, max(36, int(radius * 9)))
        self.add(np.column_stack([centre[0] + radius * np.cos(t),
                                  centre[1] + radius * np.sin(t)]), red, width)

    def svg(self, extra=""):
        out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.width}mm" '
               f'height="{self.height}mm" viewBox="0 0 {self.width} {self.height}">',
               '<title>' + html.escape(self.title) + '</title>',
               '<metadata>' + html.escape(json.dumps(self.metadata, sort_keys=True)) + '</metadata>']
        for name, color in (("ink", self.ink), ("red", self.red)):
            out.append(f'<g id="{name}" fill="none" stroke-linecap="round" stroke-linejoin="round">')
            for points, stroke, width in self.paths:
                if stroke != color:
                    continue
                d = "M" + " L".join(f"{x:.3f},{y:.3f}" for x, y in points)
                out.append(f'<path fill="none" stroke="{stroke}" stroke-width="{width:.3f}" d="{d}"/>')
            out.append('</g>')
        return '\n'.join(out + [extra, '</svg>', ''])


def station(i):
    angle = -math.pi / 2 + i * math.tau / 7
    return np.array([85 + 57 * math.cos(angle), 106 + 57 * math.sin(angle)])


def credentials(book, ink="#201d19", red="#b43628"):
    """Catalogue data directly drives the seven rosettes and 21 passage bands."""
    plate = Plate("Of the credentials", ink=ink, red=red)
    exclusion = unary_union([Point(*station(t["id"])).buffer(13.1, quad_segs=24)
                             for t in book["tiers"]])
    for h in book["handoffs"]:
        a, b = station(h["source"]), station(h["target"])
        bow = np.array([85, 106]) + .38 * ((a + b) / 2 - [85, 106])
        curves = [(p, False) for p in guilloche.path_band(a, b, bow, 1.5, int(h["legions"]), 3)]
        curves.append((guilloche.path_band(a, b, bow, 1.5, int(h["legions"]), 1,
                                          phase0=math.radians(30 * h["mark"]))[0], True))
        for p, red_path in curves:
            clipped = LineString(p).difference(exclusion)
            for part in (clipped.geoms if hasattr(clipped, "geoms") else [clipped]):
                if part.geom_type == "LineString" and len(part.coords) > 1:
                    plate.add(np.asarray(part.simplify(.01).coords), red_path, .10)
    for t in book["tiers"]:
        c, authority = station(t["id"]), int(t["authority"])
        lobes = 6 + 2 * authority
        for p in guilloche.rosette(c, 4.2, 10.1, 3 + 4 * authority, lobes,
                                   .55 + .08 * authority, math.pi / lobes / 2):
            plate.add(np.asarray(LineString(p).simplify(.01).coords), width=.10)
        plate.ring(c, 11.3)
        plate.ring(c, 12.5, width=.14)
        for p in guilloche.reeded_rim(c, 12.45, int(t["legions"]), .9):
            plate.add(p, width=.10)
        for k in range(int(t["competence"])):
            plate.ring(c, .6 + .5 * k, True)
    plate.metadata = {
        "kind": "declared catalogue mapping", "offices": 7, "passages": 21,
        "mapping": {"passes": "3 + 4 * authority", "lobes": "6 + 2 * authority",
                    "rim_reeds": "office legions", "centre_rings": "competence",
                    "wave_crests": "passage legions", "red_phase_degrees": "30 * mark"},
        "tiers": [{k: t[k] for k in ("id", "name", "authority", "competence", "legions")}
                  for t in book["tiers"]],
        "handoffs": [{k: h[k] for k in ("source", "target", "legions", "mark")}
                     for h in book["handoffs"]],
    }
    return plate


def transition_counts(weights):
    """Integer joint weights for the 64x64 binary-ordered primary/result pairs.

    weights are old yin, young yang, young yin, old yang, in that order.
    The least significant bit is the bottom line; yin=0 and yang=1.
    """
    if len(weights) != 4 or any(type(w) is not int or w < 1 for w in weights):
        raise ValueError("four positive integer weights required")
    pair = ((weights[2], weights[0]), (weights[3], weights[1]))
    return [[math.prod(pair[(a >> k) & 1][(b >> k) & 1] for k in range(6))
             for b in range(64)] for a in range(64)]


def transition_table():
    """Joint idealized yarrow weights, with both model marginals retained."""
    plate = Plate("A table of possible endings")
    yarrow, coin = transition_counts((1, 5, 7, 3)), transition_counts((1, 3, 3, 1))
    denominator = 16 ** 6
    columns = [sum(row[b] for row in yarrow) for b in range(64)]
    x0, y0, cell = 23., 28., 2.
    # M = 7**6, so the six log-grade thresholds are exact powers of seven.
    # Compare integers to avoid rounding a cell onto the wrong grade boundary.
    thresholds = [7**k for k in range(1, 7)]
    levels = [[1 + sum(value >= cut for cut in thresholds)
               for value in row] for row in yarrow]
    for a in range(64):
        for b in range(64):
            x, y, count = x0 + b * cell, y0 + a * cell, levels[a][b]
            for k in range(count):
                yy = y + .24 + (k + .5) * 1.52 / count
                plate.add([(x + .24, yy), (x + 1.76, yy)], width=.09)
            if a == b:
                plate.add([(x + .14, y + .14), (x + 1.86, y + .14),
                           (x + 1.86, y + 1.86), (x + .14, y + 1.86),
                           (x + .14, y + .14)], True, .10)
    for k in range(9):
        v = k * 16
        plate.add([(x0 + v, y0), (x0 + v, y0 + 128)], width=.11)
        plate.add([(x0, y0 + v), (x0 + 128, y0 + v)], width=.11)
    # All primary figures have marginal 1/64: identical ticks at the left.
    for a in range(64):
        y = y0 + (a + .5) * cell
        plate.add([(18, y), (20, y)], width=.12)
    # Resulting marginals below: linear height, and a coin-model 1/64 rule.
    baseline, reach = 190., 24.
    top = max(columns)
    for b, weight in enumerate(columns):
        x = x0 + (b + .5) * cell
        plate.add([(x, baseline), (x, baseline - reach * weight / top)], True, .52)
    uniform_y = baseline - reach * (denominator // 64) / top
    plate.add([(x0, uniform_y), (x0 + 128, uniform_y)], width=.17)
    plate.add([(x0, baseline), (x0 + 128, baseline)], width=.11)
    # Seven hatch swatches; the facing reading leaf supplies their exact key.
    for count in range(1, 8):
        for k in range(count):
            y = 204 + (k + .5) * 2.8 / count
            x = 29 + (count - 1) * 17
            plate.add([(x, y), (x + 9, y)], width=.13)
    plate.metadata = {
        "kind": "exact finite calculation under stated weights", "binary_order": "0..63; bottom line is bit 0",
        "weights_order": ["old yin", "young yang", "young yin", "old yang"],
        "yarrow": {"weights": [1, 5, 7, 3], "denominator": denominator, "joint": yarrow,
                   "primary_marginals": [sum(row) for row in yarrow], "result_marginals": columns},
        "coins": {"weights": [1, 3, 3, 1], "denominator": 8 ** 6, "joint": coin,
                  "result_marginals": [sum(row[b] for row in coin) for b in range(64)]},
        "hatching": {"rule": "min(7, 1 + floor(6 log(numerator)/log(maximum)))",
                     "lower_bounds": [1] + thresholds,
                     "level_matrix": levels, "meaning": "ordinal log joint weight, not linear probability"},
        "red_diagonal": "primary equals resulting; no changing lines",
        "marginal_bars": "linear yarrow result probability; black rule is 1/64 (fair coin model)",
        "scope": "Idealized independent-line inputs; no validation of a physical stalk procedure, "
                 "no interpretation rule, and no historical claim for this binary arrangement.",
    }
    return plate
