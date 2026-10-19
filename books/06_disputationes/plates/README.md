# Plates of De Potestate et Accusatione

Nine native plates for Book VI, drawn by procedure in the series' plotter conventions: an A4 sheet, stroke-only, two layers (Art Paths, Text Outlines), two inks (`#161918`, `#a32b24`), a drawn reserved blank, the plate's [F] sentence in the twelve-mark hand at a per-plate shift, and the frame drawn as a scale whose ticks carry, in the biliteral cipher, the sentence that would count against the plate's claim. No figure of a person is drawn. No image-generation model was used.

| Tabula | Title | Section | Carries | Hidden in the frame |
| --- | --- | --- | --- | --- |
| I | The Three Powers | I | no data; seeds 15, 16, 17 | THE THREE ARE HELD BY ONE HAND |
| II | Near Misfortune | III | no data; seed 1619 | BLAME FOLLOWS CAUSE NOT CONTACT |
| III | The Weft | IV | no data; seed 1972 | THE WARP STANDS WITHOUT THE WEFT |
| IV | Two Ledgers | V | the gate-and-window results table, every cell | DELAY IS BOOKED AND THE GATE STAYS |
| V | A Channel Seen | VI | the incident case record's timeline and codings | RECLASSIFIED WITHOUT DELAY |
| VI | The Wear Theory | VII | the Supreme Court of Japan's judgment of 8 February 2012 | THE ASSIGNMENT MATCHED THE CONTRIBUTION |
| VII | The Station | VIII | the refusal specimen, run on every case | THE OFFICE NAMES THE ORGANISERS |
| VIII | The Rule | IX | no data; the proposed rule drawn as an instrument | AN INDEFINITE HOLD IS AN EXCLUSION |
| IX | Bounds | XI | this book's manuscript, every sentence counted | THE RECORD CHANGED NO DECISION |

The hidden sentences follow Graduum's rule: each is the falsifier of the claim its plate draws. The Clavis says where to begin reading a frame; the caption strip's shift is in each plate's `build-meta.json`.

## Files

- `viplate.py` — the furniture: Graduum's `Plate` (`common/plot/plate.py`) with this book's running title, a guard that refuses lettering off the field or with an apostrophe (the stroke face has none), and an export that records whether the plate carries data and from where. The validator is Graduum's, unchanged.
- `tabulae.py` — the nine plates. Data plates read their records at build time: `books/01_matricis_intervallorum/models/gate_window/results.csv` through that model's own `verdict.py`; `vendor/case.json`; `vendor/refusal.py`; and `manuscript/de-potestate-et-accusatione.md`. Tabula VI's dates and counts are the judgment's, written into the script with the sentence each comes from.
- `vendor/refusal.py` — the refusal specimen, copied unmodified from this repository's `books/02_intervallorum/generator/refusal.py` at `3529a77` (identical at `7926e1b`; SHA-256 `290aeee83267718fad8a0ef6e10cfd785f1e9876f1321fd3c8c42a72277cc0b6`), so the plate keeps the version the text read.
- `vendor/case.json` — the incident case record's data file, copied unmodified from the development repository (`JosiahAlanLee/Librum_Quinque`, `cases/2026-07-openai-hugging-face/case.json` at `f0d4f65`; SHA-256 `d575640702beaa02848f27f6f72e55995f9aa4bcff95544e140a56c604e0f78d`). Tabula V draws its timeline and codings. The record's README and validator are not part of this public source selection; its quoted book passages are those of the development repository at that commit.
- the plot masters, written by `tabulae.py all <dir>` (`scripts/build.py` uses `build/vi-plates`): the master SVG, black and red A4 passes, art-only and text-only layers, a PNG preview, `build-meta.json`, `validation.json` and a type audit. Generated, not committed.
- `reading.py` — the serif reading edition for the bound book: the same plates lettered in IM Fell English outlines, rendered on the series ground as one-page PDFs and PNG previews in `reading/`, with `reading-edition.json`. Generated, not committed; the book's builder reads them.

## Build

`scripts/build.py` runs both before the book. Alone, from the repository root:

```sh
python books/06_disputationes/plates/tabulae.py all books/06_disputationes/plates/out    # plot masters, each validated
python books/06_disputationes/plates/reading.py                                          # the reading edition
```

Tabula IX counts the manuscript, so any change to the tagged text redraws it; rebuild the plates before the book.

## Limits

Untested on a physical plotter. Tabula IV holds about 9,200 strokes and Tabula I about 3,000, most of them short; plot time will be long. The reading edition's lettering is filled outlines and is not plottable; the plot masters are.
