# Artwork construction review — 19 October 2026

Reviewed on `codex/vellum-v2-and-phone-copy`, starting at `10c5f29`.

The pass inspected the workshop scenes, parable plates, illustrated office and
handoff figures, all twelve illustrated Graduum plates, Notoria's computed
figures, the Tarot artwork and the De Vinculis illuminations and seal sheets.
The check concerned visible construction and compositing: furniture joints,
supports for machine parts, and disconnected remnants after replacing figures.
It does not establish engineering feasibility for the invented devices.

| Location | Defect | Correction |
| --- | --- | --- |
| Accusator, Exhibit I | Extra leg-like posts beneath the empty chair | Four legs with clear seat joints and stretchers |
| Clavis and De Vinculis, opening workshop | Overlapping stool uprights and an unsupported outer instrument rail | Four-leg stool; two bolted radial brackets connecting the rail to the main ring |
| Escalationum, Exceptor; Graduum VIII | Stamp hovering independently above its form | Openwork rear frame, guide collar and sliding shaft visibly connected to the platform |
| Graduum X | Old proof's red request line starts in empty space beside the replacement Foras | Continue the current wrist cord from its terminal bead; retain its stop outside the permission field |

The three bitmap corrections use the built-in `image_gen` tool. Complete prompts,
source paths, selected paths, dimensions and SHA-256 hashes are in
[the correction record](art-correction-prompts-2026-10-19.json). Versioned sibling
assets retain the source images unchanged. Exceptor's selectors choose the latest
numbered render, so its correction appears in both illustrated books. The other
asset records select their corrected versions explicitly. Preparation notes
describe the edits, and validators verify selected and archived image hashes.

Graduum X's repair changes only the illustrated composition. Two obsolete red
request paths are replaced by a cord anchored to the raster's terminal bead.
The archived proof SVG, litany registers, permission field and running-incident
trace remain intact.

Deliberate drop-line ornaments, fantastic anatomy, unsupported symbolic forms,
blank reserved fields, broken seals and encoded marks were retained. Exceptor's
two red seal gaps were inspected close up after editing. This is a visual review
at the inspected resolutions, not a claim that every ambiguity has been removed.

Validation before the workspace reset: Accusator and Septimus component validators
passed; before/after comparison retained their page counts and all pre-bibliography
text. All 33 binding tests passed. Corrected assets and composed pages, including
Graduum X and VIII, were visually inspected. All 304 imported visual/font inputs
passed the original-byte check. The assembled-book check was not completed before
the reset. The same selected images were recovered from persistent storage, and
the source changes were restored for publication and clean-checkout CI.

The build workflow produces distributions from these sources. Generated PDFs
remain outside the source tree.
