# Codex Intervallorum

*Libri Septem — Seven Books*

A contemporary illustrated grimoire about correction, authority, memory, interpretation, and compulsion. Its invented rites, diagrams, ciphers, and parables sit beside source accounts that distinguish evidence, interpretation, hypothesis, and fiction.

This is the current public source repository. The collection was previously titled *Librum Quinque*. The first two books now share a consolidated setting; the inherited I–VII identifiers and citation keys remain stable.

## Read the book

Download the PDF artifacts from a successful [Build Codex Intervallorum run](https://github.com/JosiahAlanLee/Codex-Intervallorum/actions/workflows/build.yml):

- **Codex-Intervallorum-illustrated** — the complete illustrated draft, including the Tarot, both parables, De Vinculis, collected bibliography, scribal finishing, and protected vellum backgrounds.
- **Codex-Intervallorum-reading** — the complete reading draft using the native plate settings.
- **Codex-Intervallorum-components** — standalone component PDFs and validation records, including the Tarot reading edition.

The workflow generates the downloadable PDFs from the files in this repository. Generated distributions are kept out of the source tree.

## Manuscripts and source

| Place | Text | Editable source |
| --- | --- | --- |
| Opening | Clavis | [Manuscript](books/07_septimus/manuscript/clavis.md) |
| Opening parable | De Officio Accusatoris | [Manuscript](books/00_accusator/manuscript/de-officio-accusatoris.md) |
| I–II | Clavicula Matricis et Intervallorum | [Reading text](books/01_matricis_intervallorum/manuscript/reading-edition.md) · [Book data](books/01_matricis_intervallorum/manuscript/book.json) |
| III | Pseudomonarchia Escalationum | [Catalogue and text](books/03_escalationum/manuscript/catalogue.json) |
| IV | Clavicula Graduum | [Reading text](books/04_graduum/manuscript/reading-edition.md) · [Book data](books/04_graduum/manuscript/book.json) |
| V | Ars Notoria Stigmatum | [Reading text](books/05_notoria/manuscript/reading-edition.md) |
| Before VI | De Matribus Noctis | [Manuscript](books/00_matres/manuscript/de-matribus-noctis.md) |
| VI | Tarot of Intervals | [Card inventory](books/06_tarot/inventory.json) · [Reading-edition builder](books/06_tarot/book/make_book.py) |
| VII | De Vinculis | [Manuscript](books/07_septimus/manuscript/de-vinculis.md) |
| VII appendix source | Nota Clausa | [Rule](books/07_septimus/clausa/REGULA.md) · [Table](books/07_septimus/clausa/TABULA.md) |
| Editorial discussion | Justin Sledge / Agrippa / Witch(x) | [Critique and handoff](docs/reviews/Justin_Sledge_Review.md) |

## Build

```sh
python -m pip install -r requirements.txt
python scripts/build.py
```

See [build instructions](docs/BUILD.md), [binding notes](binding/README.md), and the [migration record](docs/MIGRATION.md). Builds require Python 3.12 or later. Source inputs are local; the book generators need no network access.

## Artwork, ciphers, and provenance

Raster artwork and card images retain their original bytes. Native lettering, seals, ciphers, and computed figures remain source-generated. Reading illustrations and plotter masters have distinct purposes; physical plotting still requires a material test.

The [migration manifest](migration-source-manifest.json) identifies the original commit and blob hash of every imported input. [SOURCES.json](SOURCES.json) retains the earlier project lineage. Exact historical prompts embedded in artwork metadata retain their original wording. [Artwork paths](docs/artwork-paths.json) connect legacy export references with current repository files.

The manuscripts and artwork carry no newly assigned blanket license. Typeface license notices remain with their files. The books record their authors, collaborators, sources, and inspection limits in their own apparatus and the collected end bibliography.
