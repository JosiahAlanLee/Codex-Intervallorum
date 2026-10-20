# First plates from the Codex palette

These native plates implement two proposals from Claude's
[research packet](https://github.com/JosiahAlanLee/Generative_Art/blob/d2f8a957826bbe42235fb8a39524be774286139d/docs/CODEX_PALETTE_RESEARCH.md).
They build offline from this repository's existing catalogue and stated model inputs.
No checkout of the art repository is required.

`guilloche.py` is retained unchanged from the packet's
[original module](https://github.com/JosiahAlanLee/Generative_Art/blob/d2f8a957826bbe42235fb8a39524be774286139d/lib/codex_palette/guilloche.py),
SHA-256 `e4a28ec0de2a1b274160ddbc2bb6b51b77cb8b8a4f528f4099c3ca6306a0eb00`.
Its source notes point to Holtzapffel (1884), volume V, and Craig's
[Bridges 2006 paper](https://archive.bridgesmathart.org/2006/bridges2006-203.pdf).
The packet and module were developed with Claude. The compositions, exact table,
book integration, and reading keys here were prepared with ChatGPT/Codex.
This attribution does not relay a right-of-reply response from Claude.

## Book III: Of the credentials

The plate follows the catalogue's seven stations clockwise from Foras at the top.
Each office's authority controls rosette passes (`3 + 4 * authority`) and lobes
(`6 + 2 * authority`); legions control rim reeds; competence controls red centre
rings. Each passage has three black wave strands and one red strand, with full
cycle count equal to its legions and red phase `30 * mark` degrees. Bands are
clipped outside the seals, so their visible cycle counts are shorter.

This is a declared mapping of fictional values, not a measurement of an actual
organization or a working security credential. The original paired-seal key is
unchanged. The native reading PDF, HTML, Markdown and illustrated builder all
receive the plate and its following key. The existing plot exporter also makes
black, red and combined A4 stroke-only versions, without the filled lettering.
`credentials-data.json` records the input values and mapping alongside the SVG.

## Book V: A table of possible endings

Rows are primary figures; columns are resulting figures, each in binary order
0–63, bottom line bit 0, yin 0, yang 1. This modern arrangement is not King Wen
order or a historical reconstruction.

The integer joint table multiplies the six independent line weights. The adopted
yarrow input is `(1, 5, 7, 3)` for old yin, young yang, young yin and old yang,
with denominator `16**6`. The fair three-coin comparison is `(1, 3, 3, 1)` with
denominator `8**6`. These are the manuscript's stated idealized inputs; this
implementation does not establish the physical stalk procedure or a reading rule.

For numerator `n` and maximum `M = 7**6`, the cell's hatch count is
`min(7, 1 + floor(6 * log(n) / log(M)))`. It is an ordinal logarithmic scale,
not a linear probability scale. The implementation compares exact integer
thresholds `7**1` through `7**6`, avoiding floating-point boundary errors.
Red outlines mark `primary == resulting`.
Equal left ticks mark the uniform primary marginal. The lower red bars use a
linear scale for resulting marginals; their black reference line is `1/64`,
the uniform coin-model marginal. Seven swatches label the hatch grades.

The complete integer tables, denominators, marginal numerators, grade matrix
and scope are embedded in the SVG metadata and saved to
`nota-transitions-data.json`. The PDF renders that same SVG, including an
auditable twelve-sign strip. This exact calculation is separately classified
from the five computed trace fields in the book's build manifest.

## Build and check

From the repository root, using its installed requirements:

```sh
python books/03_escalationum/generator/build.py
python books/03_escalationum/illustrated/build.py
python books/05_notoria/reading/build.py
python books/05_notoria/manuscript/make_book.py
python books/05_notoria/manuscript/check_math.py
python books/05_notoria/manuscript/make_book.py --validate
python -m unittest discover -s common/illustrations/tests -v
```

The shared tests compare every integer cell in both models with the manuscript's
independent `Fraction`-based enumeration of all 4,096 casts. The usual book
validators check serialized geometry, text placement, cipher round trips and
artifact hashes. Physical pen plotting has not been tested.
