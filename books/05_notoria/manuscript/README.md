# Ars Notoria Stigmatum — developmental reading edition

The canonical text is [reading-edition.md](reading-edition.md). [EDITORIAL.md](EDITORIAL.md) records the review of the draft-2 brief and research packet, the claim revisions, choices made from the open brief, and remaining source and production work.

This edition contains three arts, four original orations, reading leaves, the seven-office condemnation and an objection to it, optional Keeper appointments, a claim register, the five computed notae on full leaves (from `../reading/out`, built by `../reading/build.py` from `../plates/notae.py`), the found-leaf cipher ornament as frontispiece, and one bibliography at the end. The notae are simulation outputs under a stated rule with filed run manifests; they are not historical ritual diagrams and carry no evidentiary claim. The Tarot companion stays separate, and the omnibus is unchanged.

## Build

From a full repository checkout with `requirements.txt` installed:

```sh
python books/05_notoria/plates/notae.py all books/05_notoria/plates/out
python books/05_notoria/plates/validate.py books/05_notoria/plates/out
python books/05_notoria/reading/build.py
python books/05_notoria/manuscript/make_book.py
python books/05_notoria/manuscript/check_math.py
python books/05_notoria/manuscript/make_book.py --validate
```

The builder resolves shared geometry and fonts from this repository, independently of the working directory. It emits `out/Ars_Notoria_Stigmatum_reading.pdf`, the found-leaf A4 two-layer SVG, and `out/build-manifest.json`; the five notae come from the reading edition and are recorded in the manifest with their run identifiers and validation. Use `--out /absolute/path` to choose another directory. The PDF is 35 pages at 504 × 720 pt. Its committed snapshot is a developmental reading edition.

The PDF body uses the existing Spectral face for Yoruba diacritics; titles and orations use IM Fell. Geometry uses the shared Matricis hand and the inherited twelve-mark transcription alphabet. No image-generation service is needed to rebuild the ornaments. No fonts have been added or modified.

Validation checks trim, page count, text-box boundaries, bibliography placement, encoded token recovery from the SVGs, two inks, absence of raster or text elements in the ornaments, and artifact hashes. This is not independent glyph OCR. `check_math.py` independently enumerates all 4,096 casts for each supplied probability model and verifies the Tarot counts. Neither check validates an instrument's empirical distribution or an unread source.

All pages were reviewed in a rendered contact sheet; the figure and diacritic-bearing leaves were also inspected at reading size. Physical pen plotting remains untested. Full source-page checks, computed fields with controls and regeneration manifests, optional raster illustrations, and eventual binding integration remain pending.
