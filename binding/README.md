# Omnibus binding

`python binding/bind.py` produces `out/Codex_Intervallorum_reading.pdf`. Run
`python binding/validate.py binding/out/Codex_Intervallorum_reading.pdf` afterward.
The book workflow builds the component PDFs before binding them.

The active opening is the single I-II component, *Clavicula Matricis et
Intervallorum*. Build it with `python books/01_matricis_intervallorum/build.py`.
The two earlier directories are source editions and are not included separately.

The Clavis opens both bindings. De Vinculis is Book VII, immediately after
Book VI. Build and validate the Septimus PDFs with
`python books/07_septimus/build.py` and `python books/07_septimus/validate.py`.
Their common register and preparation record are consolidated once. The binder
reconnects bracketed Septimus citations to their reflowed bibliography entries.

The Nota Clausa closes Book VII in both bindings (`bind.CLAUSA`): its own
unnumbered component after De Vinculis, last before the end bibliography. Build
and validate it with `python books/07_septimus/clausa/build.py` and
`python books/07_septimus/clausa/validate.py`. It has no register. Its README's hand
line, what it withholds and its fairness record are filed with the production
notes. Its leaves are excluded from pen finishing, and validation checks that it
follows De Vinculis with its seven fields still vector plates.

De Officio Accusatoris, an unnumbered parable, follows the Clavis in both bindings
(`bind.ACCUSATOR`). Build and validate it with `python books/00_accusator/build.py`
and `python books/00_accusator/validate.py`. Its register joins the end bibliography
under the `Acc/` prefix; its single preparation leaf moves to the production notes.

De Matribus Noctis, a second unnumbered parable, stands before Book VI in both
bindings (`bind.MATRES`). Build and validate it with `python books/00_matres/build.py`
and `python books/00_matres/validate.py`. Its register joins the end bibliography
under the `Mat/` prefix, and its preparation leaf moves to the production notes,
filed before Book VI's. `backmatter.PARABLE_REGISTERS` names each parable's register.

De Potestate et Accusatione is Book VI in both bindings (`bind.POTESTATE`), in place
of the Tarot of Intervals, which is kept as a separate volume. `scripts/build.py` draws
its plates (`plates/tabulae.py`, `plates/reading.py`) and then builds and validates it
(`build.py`, `validate.py` in `books/06_disputationes`).
Its register (`backmatter.BOOK_VI_REGISTER`) joins the end bibliography under the
`VI/` prefix and its preparation leaf moves to the production notes. As for Septimus,
the binder points each bracketed key at its reflowed entry; a Book VI key link it
cannot read, or that does not match the entry it pointed to, stops the build.

## One end bibliography

The active binding rebuilds the references from the current manuscript sources
using `backmatter.py`, rather than copying pages in several original settings.
The combined opening uses that same renderer for its standalone bibliography.

The entries share IM Fell headings, EB Garamond body text, spacing, paper and ink.
Author-name forms are normalized where the supplied record identifies them.
Publication details precede inspection and use notes. Complete matching citations
share an entry; distinct inspection accounts and editions remain attributable.
Keys retain their book prefix: I-II/B1 and IV/B1 are different references.

The source trail includes Matricis et Intervallorum's contextual reading list,
Escalationum's formal debts, Graduum's reference register, and Notoria's source
trail when that book is included. Missing bibliographic facts are not invented.
No stronger verification is claimed by changing the setting.

Preparation dates, recipient and maker credits, and the selected workshop records
follow the references in the same back section. They no longer occupy title-page
bylines or dated running heads. Cipher keys, claim-level source notes, and plate
readings stay beside their subjects.

## Source leaves and parity

Book-specific heading selectors locate the dedicated source leaves. A recognized
book whose register cannot be found fails the build instead of silently dropping
its bibliography. If a builder changes the register's headings or introduces a new
section after a closing register, update its selector and its relocation test.

The binder preserves the original local folios. It may insert a blank where an
odd number of reference leaves were removed so following prose retains its
original page side. Bibliography leaves also keep their original page sides.
Physical page ranges and PDF bookmarks describe the new order.

The log records source hashes, body maps, the original register and production
leaves, metadata-removal rectangles, source-input hashes, and new bibliography
entry ranges. `bibliography-records.json` preserves the compiled reference records.
Validation checks coverage of every source leaf, matching body text after only
the declared metadata removals, every reference key and inspection account,
end placement, uniform fonts, page bounds, the Nota Clausa's place and seven fields, all seven Septimus facing pairs, both
Septimus illuminations, the nine Book VI plates on versos facing their sections, and
the citation destinations of both. The Tarot's checks remain for that volume if it is
bound again: every facing pair, and a redundant blank before its first pair that can
be omitted together with its moved note. The original component PDFs remain unchanged
by binding.

The older relocation-only binder remains available for archival components that
do not select the consolidated opening; its tests preserve that compatibility.

## Scribal finishing of the illustrated binding

The illustrated binder runs `scribal.py` after compaction. It adds occasional
open pen loops beside prose capitals, short terminal strokes, and outer-margin
pen trials. Forms, proportions and ink weight vary deterministically by book and
local source folio, so a pagination change does not reshuffle the whole hand.
The four large full-scene illustrations receive matching external hairline
mounts. Their image bytes, internal borders and complete pictures are retained.

The pass does not alter letterforms, regenerate artwork, or add pseudo-text.
The bibliography, cipher keys, inscriptions, working diagrams (Book VI's plates
among them) and blank alignment leaves retain their existing setting, as Tarot
leaves would if that volume were bound. Proposed marks must clear every
text span and image, and a rendered paper check also detects vector carriers.
Marks that do not fit are omitted. No white patches or erasure are used.

`scribal-log.json` records every marked source/physical folio and addition box.
Before accepting the output, the pass checks all pages for exact text records,
image data and placement, original vector paths, links, outlines and trim. On
marked leaves, a 144-dpi comparison must show no change outside those boxes.
The finished PDF is tagged to prevent accidentally applying the pass twice.
The existing binding validation still runs after the pass in CI.

To compare an existing unadorned binding with a separate finished copy:

```bash
python binding/scribal.py path/to/original.pdf path/to/finished.pdf
```

Keep the original `binding-log.json` beside the input. Build the illustrated
binder normally to incorporate later source edits; do not use a previously
finished PDF as the input. Source editions and plotter masters are untouched.

## Vellum grain and ink blemishes

The illustrated binder follows its pen finishing with `vellum.py`. It adds a
transparent paper layer: several scales of smooth noise, fine grain, sparse short
fibres and a slight edge variation. Existing paper colour remains dominant.
About one leaf in seven also receives a tiny, irregular group of faint ink
spots, and only if a clear site exists within the outermost 25-point margin.
Texture is repeatable by book and local source folio; `--seed` selects a different
realisation. Front matter and other leaves use a source-content fingerprint.

This is a background-only pass. A rendered mask protects text and diagram
strokes, cipher carriers and the preceding scribal additions, with a one-point
buffer. Complete raster images receive a three-point exclusion zone. Blotches
must also clear whole text spans by three points. Grain continues through the
surrounding paper without leaving pale text-block rectangles. Opacity fades
toward protected zones and is zero inside them. Dense non-paper
leaves are skipped. The source art, cipher geometry and plotter masters stay
unchanged; the reading PDF retains its text, vectors, links and outlines.

```bash
python binding/vellum.py path/to/original.pdf path/to/vellum.pdf
python binding/vellum.py path/to/original.pdf path/to/another.pdf --seed 17
python binding/vellum.py path/to/original.pdf path/to/full-grain.pdf --profile full
```

If present, keep `binding-log.json` beside the input to seed body pages by source
identity. The standalone tool also works on an ordinary unrotated reading PDF
without that log. The pass refuses to process its own finished output twice.
It writes through a temporary file and verifies the saved PDF before replacing
the output. `vellum-log.json` records every leaf, spot box, seed and verification
result. Checks require exact source text, paths, images, links, outline and page
geometry, plus exact rendered protected pixels at 96 dpi. Rebuild the binding to
change the noise or seed. Background texture adds raster data and PDF file size;
source typography and diagrams remain at their original resolution.
The default `light` profile uses half-strength pigment, including margin spots,
and omits independent per-pixel noise. The smooth fields and sparse fibres remain,
with the same protection resolution. The earlier finish is available as `full`;
the selected profile is recorded in the log. The illustrated build accepts
`--vellum-profile full` to select it.
Texture images are explicitly tagged; binding validation excludes only those
backgrounds from its illustration counts and illumination-digest comparisons.

