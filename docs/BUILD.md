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

The [build workflow](../.github/workflows/build.yml) uploads both omnibus editions and their validation logs. It also uploads the Tarot reading edition and the standalone Clavis, De Vinculis, and parable PDFs. Download the artifact for a successful run from [GitHub Actions](https://github.com/JosiahAlanLee/Codex-Intervallorum/actions/workflows/build.yml).

Generated PDFs, previews, HTML readers, build logs, and caches are ignored. One historical PDF remains a checked-in input: `books/01_matricis/pdf/Clavicula_Matricis_ereader.pdf`. The consolidated opening mounts five boards from it. Its original bytes and the inherited cipher module are retained.

Book III's output-based tests run after its generator. A committed generated PDF is no longer required to begin a clean build. The native Graduum sources and the three retained proof SVGs supply its plates; their ciphers remain separate from raster illustrations.

The [migration record](MIGRATION.md) describes source scope and provenance. The [binding notes](../binding/README.md) describe bibliography relocation, pagination, scribal finishing, and vellum protection.
