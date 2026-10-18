# Clavicula Graduum — revised draft manuscript

`make_book.py` is the canonical editorial source. It writes `book.json` and
`reading-edition.md`; edit the generator, then regenerate both. CI checks that the
committed text is current before building the book.

D6–D10 are retained identifiers. Their [H] tags mark hypotheses and proposed
instruments, not deductions or established laws. The 17 October revision narrows
rate/rank, bypass, hidden-record, abstraction and level-count claims. Comparisons
with theology, symbolic constraints and learning architectures are labelled as
comparisons. Source inspection statements are inherited from the earlier draft;
this pass does not claim a fresh primary-source audit.

Build the serif plate reading edition with `python books/04_graduum/reading/build.py`,
then run `python books/04_graduum/build_book.py` from the repository root.
The 7 × 10 book contains native reading plates I–VIII, marked proofs IX–XI and a
withheld leaf XII. Existing cipher carriers preserve earlier wording and are not
silently re-encoded by this prose revision. Plate XII supplies no keyed ciphertext
or recoverable secret; the omission belongs to the artwork.

See `docs/EDITORIAL-2026-10-17.md` at the repository root for applied cuts and
further removal suggestions. The books remain separate works.
