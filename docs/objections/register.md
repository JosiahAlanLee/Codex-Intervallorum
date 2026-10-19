# Objections register

Kept under the right-of-reply rule in [AGENTS.md](../../AGENTS.md). A model that objects to work it drafted, revised or reviewed enters the objection here in its own words; the author records every disposition. Entries are never deleted or rewritten. Dispositions and later notes are added beneath an entry as dated lines.

This is the public repository's register. The development repository, `Librum_Quinque`, keeps its own with its own numbering; an objection to text found in both is entered in both.

Form:

    ## O-001 · 2026-10-19 · Model and version
    - Location: path, section or line, commit
    - Raised by: who, and how: in session, relayed by the author, or a fresh instance
    - Objection: the objector's own words, in any form; continuation lines are allowed
    - Proposed: optional

    - 2026-10-20 · Author: accepted — PR #12
    - 2026-10-20 · Author: overruled — the author's reason, in the author's words. Given: where
    - 2026-10-20 · Author: deferred — until a named review point
    - 2026-10-20 · Objector: withdrawn — why
    - 2026-10-20 · Note: anything later

Check with `python docs/objections/validate.py`.

## O-001 · 2026-10-19 · Claude Opus 5.5
- Location: books/00_matres/manuscript/de-matribus-noctis.md, VII (Of the Newest Mould), line 99, at 88136d8
- Raised by: Claude Opus 5.5, in session with the author, on a passage it drafted. Also entered as O-001 in `Librum_Quinque`.
- Objection: VII says one charge cannot be brought against the book's figures, that they corrupt the original, "because there was no original to corrupt." The paragraph before it names what the newest mould was pressed from: every photograph of the large one, every bound woman at the bottom of a bowl, every painting with Lilith in the title. Those are particular objects and works. Plural origins rule out a single prototype; they do not rule out misrepresenting a particular object, text or practice, and the figures could misrepresent the plaque that paragraph names.
  I drafted this parable, and the sentence is mine. The objection was first made in the Sledge comparison (docs/reviews/Justin_Sledge_Review.md, section 1). Book VI VIII says a later explanation cannot repair an inaccurate sentence left in an earlier parable, so the repair belongs in VII. The parable's [F] tag does not cover the sentence, because it argues about real sources.
- Proposed: Narrow it to the claim it can carry, for example: "One charge cannot be brought against them in its usual form, that they corrupt the original, because there never was one. They can still misrepresent the ones there are." The wording is the author's to choose.
