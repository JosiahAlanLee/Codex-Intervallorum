# Building Codex Intervallorum

Use Python 3.12 or later. From the repository root:

```sh
python -m pip install -r requirements.txt
python scripts/build.py
```

The script builds the component books in dependency order, runs their existing tests and validators, then assembles both editions. It checks the new cover and PDF metadata and verifies that imported visual inputs retain their original Git blob hashes.

| Edition | Generated PDF |
| --- | --- |
| Reading draft | `binding/out/Codex_Intervallorum_reading.pdf` |
| Illustrated draft, with scribal and vellum finishing | `binding/out/illustrated/Codex_Intervallorum_illustrated.pdf` |

For one edition, use `python scripts/build.py --edition reading` or `python scripts/build.py --edition illustrated`. Individual book builders remain available in their existing directories.

The illustrated edition defaults to lighter vellum: half-strength pigment and
smooth fields without independent pixel noise, reducing texture overhead while
keeping the existing text, cipher, diagram and artwork protection at 96 dpi.
Use `--vellum-profile full` to reproduce the earlier, denser finishing.

The [build workflow](../.github/workflows/build.yml) uploads both omnibus editions and their validation logs. It also uploads the standalone Book VI, Clavis, De Vinculis, Nota Clausa and parable PDFs, and the Tarot reading edition, now a separate volume. Download the artifact for a successful run from [GitHub Actions](https://github.com/JosiahAlanLee/Codex-Intervallorum/actions/workflows/build.yml).

Generated PDFs, previews, HTML readers, build logs, and caches are ignored. One historical PDF remains a checked-in input: `books/01_matricis/pdf/Clavicula_Matricis_ereader.pdf`. The consolidated opening mounts five boards from it. Its original bytes and the inherited cipher module are retained.

Book III's output-based tests run after its generator. A committed generated PDF is no longer required to begin a clean build. The native Graduum sources and the three retained proof SVGs supply its plates; their ciphers remain separate from raster illustrations.

Book VI's nine plates are generated from their code before the book: the plot masters into `build/vi-plates`, validated, and the serif reading edition into `books/06_disputationes/plates/reading/`, which is ignored. Tabula IV reads the gate-and-window results table, Tabula V a vendored copy of the incident case data, and Tabula IX counts the manuscript as it stands.

The [migration record](MIGRATION.md) describes source scope and provenance. The [binding notes](../binding/README.md) describe bibliography relocation, pagination, scribal finishing, and vellum protection.
