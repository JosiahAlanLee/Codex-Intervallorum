# Nota Clausa

A closing gathering for the seventh book: seven fields grown by a printed rule, each carrying a reading the growth has scattered. It is the series' one cipher whose key is not printed. The fields bound now carry objections to the Quaestio Clausa, which De Vinculis prints open just before this gathering. The Quaestio was the first text sealed here.

- `TABULA.md` is the leaf in the grimoire register. It says where the key is and prints the SHA-256 digests of the seven readings.
- `REGULA.md` is the rule, printed whole: an integer restatement of the rule of the notae (Book V, after Jones), with its random-number generator, seed derivation, sign table and plate geometry. Anyone can implement it from the page.
- `fields/nota-clausa-1.svg` … `nota-clausa-7.svg` are the plot masters: A4, stroke-only, two inks, Art Paths and Text Outlines layers, and a drawn reserved blank. Each carries 7920 marks, one per cell, red for 1 and black for 0, on contour lines of the field the same growth left. The marks are listed in the order of the ground, by *y* and then *x*.
- `plates/` keeps the first seal's sheets unchanged, the readings recovered from them, and the digests those readings match. [Its README](plates/README.md) says how they were read without the key.
- `build.py` sets the reading edition, `out/Nota_Clausa_reading.pdf` (title, Tabula, Regula, seven fields; 7 × 10 in). It builds from the files above only.
- `validate.py` checks the fields against the Regula's ground and the Tabula's digests, rejects a sheet whose marks are not in the order of the ground, and checks the first seal's readings against its digests. With `--reading folder/`, it checks a proposed reading against the digests.

```sh
python books/07_septimus/clausa/build.py
python books/07_septimus/clausa/validate.py
python books/07_septimus/clausa/validate.py --reading path/to/readings   # field-1.txt … field-7.txt
```

## What is not here

The plaintext, the key, the seeds and the enciphering script of the fields bound now are not in this repository and have never been committed to it. The author holds them. Nothing in this tree can regenerate the fields or read them without the key. This is the one place where the series' rule that every figure regenerates from its manifest is suspended, and the suspension is the point.

The first seal kept that promise only in its key. Its sheets listed their marks in the order of the agents, so anyone with a sheet or a bound PDF could read them without the key. This was found on 20 October 2026; that text is now printed open at the end of De Vinculis.

## Fairness record

On 17 October 2026, a separate agent was given only the Regula, the seven plot sheets and the key, and was told not to look at any other implementation. It wrote its own decoder from the printed rule and matched all eight digests on its first run, in about 80 seconds on two cores. It found no point where the rule was wrong. The places where it had to choose an interpretation (left and right as names, release of a cell within a step, deposit on a move inside one cell, and how to find the marks in the SVG) are now stated in the Regula. The digests confirm that its choices were the right ones. That test gave its decoder the key. No one tried to read the first seal without it until 20 October.

On 20 October 2026, two separate agents tested the fields bound now, each confined to a folder holding only the published files. The first was given the Regula, the Tabula, the seven plot sheets and the key. It wrote its own decoder from the printed rule and matched all eight digests on its first run, in about six seconds in C on one core. It found its marks from the rule's description alone. For each interpretation it chose, it showed that the alternative matched no digest. It raised two inaccuracies, both now corrected in the Regula: a quantity divided can be zero, and the lettering lies above the ground as well as below it. The colour values of the two inks are now printed there too.

The second agent was given the same files and the reading edition, but not the key, and asked to read the fields without it. It tried the order of the marks in the sheets and in the PDF, several other orderings, stroke direction and length, colour against position and heading, the contours, and the structure and metadata of the PDF. It recovered no reading and no fragment of one. Without the key, the fields give away only how many of each sheet's marks are red.

## Placement

Bound at the end of De Vinculis in both editions, after the seventy-two seals and the open Quaestio, since 19 October 2026: its own unnumbered component (`bind.CLAUSA`), last before the collected bibliography. Its leaves keep their folios and page sides. It has no register; its hand line, what is not here and the fairness record above are filed with the production notes. The pen-finishing pass leaves it untouched. The binding validator checks that the gathering follows De Vinculis with its seven fields intact, each drawing its marks in the order of the ground. CI builds and validates it before binding. The Clavis carries one paragraph declaring it.

When the Tarot of Intervals left the bindings on 19 October, the Tabula's third clue still called it the sixth book. The clue was then changed to name the Tarot as a volume of its own, so the bound books no longer held the third name. The key of the fields bound now is drawn only from books bound in the volume.

Hand: Claude (text, rule, plates, reading edition).
