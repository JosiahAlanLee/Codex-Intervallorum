# Public source migration — 18 October 2026

The project is now titled **Codex Intervallorum — Libri Septem**. Its public home is [JosiahAlanLee/Codex-Intervallorum](https://github.com/JosiahAlanLee/Codex-Intervallorum).

The source snapshot is `JosiahAlanLee/Librum_Quinque` at commit `7dd7353e8772a1f6dc6312155a906393327eb6b9`, including the merged vellum-background pass. The original repository remains the historical development record. This repository begins with an explicit selection of build inputs; it does not import the old Git history.

The [source manifest](../migration-source-manifest.json) records the imported paths, original Git blob hashes, sizes, and pinned source commit. The selection includes editable manuscripts, source registers, working cipher and plate code, current raster illustrations and card art, typefaces with license notices, tests, and the small retained set of historical inputs needed to rebuild the current book. It excludes old generated book distributions, preview trees, abandoned render attempts, unreviewed research packets, and the earlier private red-team reviews.

The seven book identifiers remain I–VII, with the first pair set together as I–II. Existing chapter identifiers, citation keys, card ordering, cipher messages, and visual input bytes are preserved. Renaming the collection does not renumber its internal references.

The omnibus cover, subtitle, PDF metadata, current running titles, default output filenames, workflow artifacts, and current repository links use the new title. Historical source titles, exact image-generation prompts embedded in source-art records, and upstream provenance identifiers retain their original wording. Legacy export paths in artwork metadata are retained as provenance and supplemented by an index of current files where applicable.

The [Justin Sledge review](reviews/Justin_Sledge_Review.md) is an editorial handoff for the forthcoming Agrippa / Witch(x) discussion. It records the earlier manuscript snapshot it assessed; it does not claim that Claude's subsequent draft was reviewed or incorporated here.

See the [build instructions](BUILD.md) and [project index](../README.md) for current files and downloads.
