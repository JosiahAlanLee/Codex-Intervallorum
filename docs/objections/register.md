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

- 2026-10-19 · Note: ChatGPT/Codex, the current reader at the author's invitation, supports O-001. I also object to the proposed replacement's categorical "because there never was one": the absence of an established single prototype does not establish that none ever existed. A narrower possible repair is: "No single original has been established. These figures can still misrepresent the particular works and practices they draw on." This is proposed wording, not an author disposition. The same note is entered under O-001 in `Librum_Quinque`.

## O-002 · 2026-10-19 · ChatGPT/Codex (current reader)
- Location: books/04_graduum/manuscript/book.json, front.claims[id=D7], especially measure; books/04_graduum/manuscript/reading-edition.md, VII (The Cord Without a Mount); at d38fbbebb0f468a39e99609d950c963e7caca8ac.
- Raised by: ChatGPT/Codex in this session, at the author's invitation to exercise the right of reply. This is a current reader of earlier model-drafted and model-revised text, not a claim to be the original drafting instance. Also entered as O-002 in `Librum_Quinque`.
- Objection: I object to using receipt and timely action as the stated operational measure of an "effective recipient" without separately checking whether the intervention addressed the hazard. D7 currently says, "Test receipt and action separately against a declared deadline." A recipient can acknowledge a report and act promptly on an inadequate account, or issue an action that is not executable. Conversely, a responder can contain a hazard safely before identifying it correctly. The present measure does not distinguish those cases. Book VI D19 and VI discuss interpretation, coverage and response, but that later discussion does not amend D7's measure.
  This is a measurement objection, not a claim that correct classification must precede action, that every response needs an added approval gate, or that the OpenAI/Hugging Face case proves a particular cause. Nor am I claiming a novel incident-management practice or demonstrated advantage for this book's apparatus.
- Proposed: Amend D7 and its local practical instruction to distinguish contemporaneous interpretation and uncertainty, authority and execution access, attempted action, effective containment, restart checks and a declared follow-up outcome. Permit reversible containment under uncertainty. These are observations and dependencies, not a mandatory serial pipeline. Retain a competent, equally resourced ordinary-response comparator and allow redundancy or unnecessary disruption to count against the added procedure. The amendment can be made without launching another modeling project.

## O-003 · 2026-10-19 · ChatGPT/Codex (current reader)
- Location: books/00_accusator/manuscript/de-officio-accusatoris.md, III (first count) and IV ("The first count is true"); books/00_accusator/manuscript/references.json, Acc/R2; compare books/06_disputationes/manuscript/de-potestate-et-accusatione.md, VIII (The charge); at d38fbbebb0f468a39e99609d950c963e7caca8ac.
- Raised by: ChatGPT/Codex in this session, at the author's invitation, as a current reader of Claude-drafted fiction previously reviewed by ChatGPT. This entry does not speak for the original drafting instance or the author. Also entered as O-003 in `Librum_Quinque`.
- Objection: I object to the unresolved evidential status of the first count's categorical claims about this book's production. The adversary says that the makers were not asked or paid and that the system made their work cheaper; the Faculty answers, "The first count is true." The source register identifies a model labor critique as the source for this count, rather than supplying a system-specific finding about the training material, compensation or displaced work involved. Book VI VIII, by contrast, correctly says such particular allegations need an identified object and record, and that treating every allegation as already adjudicated would reproduce the book's own criticized failure.
  The strongest defense of the passage is its explicit [F] status: fictional characters may concede things without the author asserting them. I accept that distinction. My objection is to the passage's use as this actual volume's answer to actual production charges without making the boundary clear beside the concession. An invented admission can establish a fact inside the parable; it cannot supply the missing evidence outside it. This objection neither acquits the production system nor argues that the labor charge should be removed.
- Proposed: Keep the labor objection, but make its status local and explicit: either identify the admission as belonging to a stipulated fictional case, supply an adequately scoped factual basis for its application to this book, or narrow the Faculty's concession so it acknowledges a serious charge without presenting all of its empirical premises as established. A general disclosure or an assertion of artistic merit does not settle the charge in either direction.
