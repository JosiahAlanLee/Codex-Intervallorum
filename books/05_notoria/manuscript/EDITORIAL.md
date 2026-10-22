# Notoria manuscript development — 17 October 2026

Base inspected: `964d8aba8545a4849f6de7e3480158989abba64e`. The draft-2 brief and research packet are preserved as workshop documents. This note supersedes their claims where identified below; it does not silently rewrite the earlier research.

## What has been developed

`reading-edition.md` is the canonical manuscript: three arts, four orations, reading leaves, independently checked calculations, a seven-office condemnation and an objection to its verdict, three optional appointments of the Keeper, propositions, a cipher key, and one source trail at the end. The unstable collective names and reported manuscript hands are explicitly fictional. The Tarot companion is not duplicated.

The five new native ornaments reuse the Matricis twelve-mark hand and shared stroke engine. Their ciphers are qualifications in plain English. They are schematic illustrations, not the computed fields requested by the production brief. No raster art has been generated; no real divinatory apparatus or verse has been copied. The existing illustrator briefs remain available.

## Claims revised before composition

1. **The universal retrojection thesis is not established.** The three cases do not document the same event. The Ifá section supplies no demonstrated reordering to fit an external arithmetic. Shao Yong's arrangement is an indigenous Chinese arrangement, not something Leibniz made by resequencing King Wen. Maitre's inspected abstract argues that its structure is binary; it is counterevidence to the draft's categorical framing. Its issue date is 2023, but the publisher gives online publication as 15 August 2025. An edition should record both rather than treating the item as an unread 2023 endorsement.
2. **Order is not exclusive to Ifá's combinatorics.** Trump rank has a procedural role in trick-taking. Calling that role ludic does not remove its mathematical work. A fixed set of labelled Tarot positions is already counted by an ordered draw. `P(78,n) × positions` double-counts unless a genuinely independent set of alternative layouts has been specified.
3. **Correct the King Wen pair count.** The research's detailed section gives 28 reversal pairs and 4 complement pairs containing 8 reversal-symmetric figures. Its comparative table and the brief conflate figures with pairs. The manuscript omits the historical sequence claim pending source-page checks; the arithmetic can be checked separately, but cannot authenticate a historical sequence.
4. **A dust inscription is not thereby a stigmergic field.** Physical marks and erasure do not demonstrate reading by density, adjacency or accumulated multi-agent traces. N3 becomes an explicitly artistic juxtaposition. An empirical claim of shared mechanism would need separate evidence.
5. **Do not make an unread epistemology into a house verification stamp.** The precise ìmọ̀/ìgbàgbọ́ formulation in the packet comes through a reader summary, not a verified passage. The manuscript records the debt to the question of verification and withholds the detailed borrowing. Its own provenance distinctions are identified as its own proposal.
6. **Separate conditional from joint probabilities.** In the idealized yarrow model supplied by the packet, primary yin and yang each have probability 1/2. Conditional flip rates are 1/8 and 3/8; the joint events have probabilities 1/16 and 3/16. The full conditional transition kernel must use the former. Both primary distributions are uniform under independent lines; the yarrow-derived resulting distribution is not. Derivations are checked in `check_math.py`; the physical stalk probabilities remain a reported model input, not a newly verified empirical result.
7. **Do not turn a search limit into an absence theorem.** Replace “never measured” with “no measurement study located by this research pass.” The regional/diachronic ranking issue and exact ìbò hand-selection procedure remain pending checks against the monographs.
8. **Narrow the historical form claim.** Medieval Ars notoria transmission predates its association with some later Lemegeton compilations. This manuscript borrows the figure/oration association, without describing a universally fixed fifth-book contents or reconstructing a lunar ritual from an unread edition.
9. **Keep the condemnation answerable.** The seven offices' judgement is fiction, not Aquinas's argument. Aquinas II–II q.96 a.1 is separately acknowledged. A bad prohibition is no evidence that the prohibited claim is true. The 1323 Paris episode remains pending a precise text rather than entering the narrative as a verified burning of a particular book.

## Choices made from the brief's open questions

- Keep three arts. Geomancy appears as a transmission question under the third, not as an improvised fourth historical system.
- Write the condemnation as text now; retain its figure brief for later art production.
- Use the Keeper's three intervals as an expressly invented optional exercise, not a recovered ritual timetable.
- Give each of the three arts one fictional collective name, with no claim of an actual collective behind them.
- Keep the Tarot companion separate. Its recent full reading edition already exists.
- State the empirical-distribution question as an open lead with an explicit search limit. No practitioner study is proposed as work already done or required of the reader.

## Production limits

This is a reviewable text edition, not the completed Book V figure edition. Native simulations, controls, manifests capable of regeneration, independent image/specification validation, the Physarum-style model, four optional raster illustrations, shelf-page verification and omnibus integration remain separate work. The generated PDF labels its status, and its bibliography stays at the end. No existing bound PDF or workflow input is replaced.

The source trail distinguishes full web text, abstract, publisher metadata, indexed official text and uninspected monographs. URLs are given for checking; no fabricated page references fill the gaps.

## Build and verification

Run `python books/05_notoria/manuscript/make_book.py` from a full checkout, then `python books/05_notoria/manuscript/check_math.py` and `python books/05_notoria/manuscript/make_book.py --validate`.

The builder uses the shared geometry and fonts, emits five two-layer A4 SVG ornaments and a 7 × 10-inch PDF, checks the encoded token stream in each SVG against its plaintext, checks text boxes and trim, and keeps bibliography leaves last. Token validation is structural, not independent OCR of the cipher. The illustrations require visual review too. Their physical pen-plot behavior has not been tested.

## Second pass — 17 October 2026, later (Claude)

Base: the Codex manuscript above at `d4e452b`. The text is kept; the figures change.

- **The five computed notae are made.** `fields/physarum.py` is a deterministic agent model after Jones (2010); `plates/notae.py` draws the five fields on the Book IV plate furniture in the Matricis stroke vocabulary; `plates/validate.py` regenerates every field from its filed run manifest and checks that the frame carries that manifest's identifier; `reading/build.py` rebuilds them in the serif reading edition. `make_book.py` now merges those five plates onto full leaves, as Book IV does, and keeps the Codex found-leaf ornament as the frontispiece. The plate leaves, the fields reading leaf, the Clavis and the colophon are reworded to describe what is now on the page; nothing else in the text is changed.
- **Accepted from the first pass.** The King Wen pair count (28 inversion pairs, 4 complement pairs; the brief and the research's comparative table had conflated figures with pairs); the conditional/joint distinction in the yarrow kernel; "no measurement study located" in place of "never measured"; the condemnation kept answerable; Maitre's abstract as counterevidence to the categorical framing. The brief and research packet are corrected on the first two points below.
- **Not accepted.** That N3 is only an artistic juxtaposition. It remains a hypothesis with a stated falsifier in the brief; the manuscript's plate leaves say what the figures are and claim nothing about Ifá's tray. The fields reading leaf says, and should keep saying, that a field that regenerates has shown only that it was computed.
- **Still owed.** The brief's controls (no shared traces, no decay, common stimulus) as further runs under the same manifest discipline; the physical plot; the four raster figure briefs; the shelf-page checks; binding Book V into the omnibus, which this pass does not touch.

## Ifá source check — 22 October 2026 (new ChatGPT/Codex reviewing instance)

The [source-to-claim record](../../../docs/research/ifa-source-check-2026-10-22.md) updates the source debts in points 5 and 7 above. It distinguishes the 2015 dissertation, the 2020 book's authorized introduction, Hallen's original article, and Bascom's accessible chapter-opening excerpts. The dissertation does not stand in for the published book; the complete Bascom/Abimbola procedural comparison remains open.

The two Ifá reading leaves now record what the inspected passages establish and retain the five evidence-route labels as an independent Codex proposal. N4's empirical test is still unperformed. The existing orations and computed figures are unchanged. The earlier editorial notes remain a dated record of earlier checks.

Right of reply: invited; no objection. The original brief and research were prepared by Claude; this entry speaks only for the present reviewing instance.
