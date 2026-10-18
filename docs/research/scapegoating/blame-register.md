# Witch(x): Blame Register

Originally prepared against the manuscript titled *Librum Quinque*; historical titles below retain that context.

**Prepared:** 18 October 2026, by Claude (Anthropic) at the author's request  
**Manuscript read:** `JosiahAlanLee/Librum_Quinque` at commit `eb2eeaf`, the development repository  
**Line numbers:** re-keyed to this repository at commit `6df7ad3`; no cited line differs between the two trees  
**Status:** research for review; no manuscript changes made

## Scope and location key

The bound text already holds most of a model of scapegoating. Book III supplies where blame lands, De Officio Accusatoris supplies the accuser's office, and Books I–II, IV and VII supply rules against both. The word *witch* occurs once in the whole bound text, in Book III's register of debts (III:802).

Read at commit `eb2eeaf` (main, merged 18 Oct 2026, 01:20 CDT): every bound reading text in full, the Tarot commentary fields, and every source register. Cut and archived material and the Book VII research ledger were searched, not read in full. Every quoted fragment below was checked by script against its cited line at that commit, and again in this repository after re-keying. Paths marked † are in the development repository only; the migration did not import them ([migration notes](../../MIGRATION.md)).

A blame claim here is any passage on where fault lands, who assigns it, on what evidence, or what stops it. Tags are the books' own: \[E\] evidence, \[D\] definition or deduction, \[H\] hypothesis, \[V\] adopted value, \[F\] fiction. Book III and De Vinculis's commentaries carry no tags (—); Book III states that all its offices, minutes and voices are invented (III:837). **Reading:** marks my interpretation, not the text's claim.

| Key | File (line numbers refer to it) |
| --- | --- |
| I–II | [`books/01_matricis_intervallorum/manuscript/reading-edition.md`](../../../books/01_matricis_intervallorum/manuscript/reading-edition.md) |
| III | Generated `books/03_escalationum/output/reading-edition.md`; tracked source: [`manuscript/catalogue.json`](../../../books/03_escalationum/manuscript/catalogue.json) |
| IV | [`books/04_graduum/manuscript/reading-edition.md`](../../../books/04_graduum/manuscript/reading-edition.md) |
| V | [`books/05_notoria/manuscript/reading-edition.md`](../../../books/05_notoria/manuscript/reading-edition.md) |
| VI | [`books/06_tarot/major-arcana/deck.json`](../../../books/06_tarot/major-arcana/deck.json), [`swords/swords.json`](../../../books/06_tarot/swords/swords.json) (cited by card) |
| Cl | [`books/07_septimus/manuscript/clavis.md`](../../../books/07_septimus/manuscript/clavis.md) |
| VII | [`books/07_septimus/manuscript/de-vinculis.md`](../../../books/07_septimus/manuscript/de-vinculis.md) |
| Acc | [`books/00_accusator/manuscript/de-officio-accusatoris.md`](../../../books/00_accusator/manuscript/de-officio-accusatoris.md) |
| Mat | [`books/00_matres/manuscript/de-matribus-noctis.md`](../../../books/00_matres/manuscript/de-matribus-noctis.md) |
| EDITORIAL | `docs/EDITORIAL-2026-10-17.md` † |

Book III's line numbers refer to the generated reading text, which is intentionally absent from a clean source checkout. Run `python books/03_escalationum/generator/build.py` from the repository root to produce it. The table links to its tracked input so source navigation also works before a build.

## Where blame lands

In the text, blame lands on whoever knew first, and the office that could act is written out of the finding. CULPAX states the rule; BAEL's binding states the immunity.

| Where | Tag | The text | Mechanism |
| --- | --- | --- | --- |
| III:32 | — | “Authority rises at each landing. Competence in this particular fault and exposure to blame both diminish.” | The gradient: blame falls as permission rises |
| `catalogue.json`, tiers | — | FORAS: authority 0, competence 6, liability 6 … BAEL: 6, 0, 0 | Stipulated and exact: liability = competence = 6 − authority at all seven stations |
| III:14 | — | “we added a signature. The signatures rose through the building. The hands stayed where they were.” | Accountability records climb; the work stays down |
| III:516–522 (CULPAX) | — | “She giveth the first observer the title of accountable owner.” Binding: “The earliest timestamp and one individual's name.” Effect: “Attached the accumulated delay to the worker who first recognized the fault.” | The landing rule: first knowledge, not control, selects the name |
| III:604–608 | — | “The return strokes bypass every office and land on the first observer.” … “Inside was the question: why did you not act? The return address was his own.” | Delay returns to the knower as a question addressed to himself |
| III:630–643 (BAEL) | — | Binding: “a change window bearing his signature; no finding that names the signature as a cause.” Effect: “Withheld the only effective authority until the deadline passed, then asked why the operator had waited.” Then “A new ticket was opened to establish when Foras had known.” | Immunity written into the binding; the inquiry asks when the worker knew |
| III:773 | — | “He asked why the traveler had not used the ordinary road.” | The gatekeeper questions whoever came through |
| III:484 (PAIMON) | — | “He can appoint an owner to every risk and retain none himself.” | Ownership assigned downward, never held |
| III:756, 762 (POSTHUM) | — | “He discovereth approval in an earlier silence once the outcome is known.” Effect: “Recorded retrospective support for the repair and prospective blame for its lateness.” | Hindsight turns silence into consent and lateness into fault |
| III:666 (INSTANTOR) | — | “Made the operator restart the wrong component to provide immediate visible action.” | The executive's error, done by the operator's hand |
| III:64 (FORAS) | — | “Located the fault in four minutes; left it running while permission was sought.” | The frontline office's own entry, in the grammar of a charge (see Tensions) |
| III:371, 382, 845 | — | OROBAS binding: “A named owner, a consulted owner, and an owner empowered to decide which owner should be named.” Also: “The incident itself had no department because incidents were temporary.” Last line: “The ticket is now owned by the team investigating why it had no owner.” | Naming the owner is itself an office; the incident never has one |
| I–II:375 | — | “The person nearest the door answered. On their return they addressed every instruction to that person, and called the arrangement leaderless.” | Visibility read as authority: the nearest person gets the office |
| I–II:393 | \[E\] | Freeman describes “public attribution of spokesperson roles where a movement had not selected official representatives” | The office assigned from outside |
| I–II:49, 199 | \[V\] | “An institution can preserve its organization by transferring damage to workers, dependents, or a habitat.” Also: “A successful bypass can transfer risk to someone outside the former approval chain.” | Cost and risk transfer, the material side of blame |
| Acc:17, 19 | \[F\] | “A later scribe, retelling it, wrote that the adversary had moved the king instead.” Also: “Later readers needed a fall for the adversary and borrowed the king’s.” | Blame moved by redaction (2 Sam 24:1 to 1 Chr 21:1); a culprit's history built from another's text |
| Acc:119, 121 | \[F\] | “He answered truthfully that there was no general.” Also: “Parliament answered the frame-breakers with a statute that made their work a hanging matter.” | Authority wants a ringleader; the movement offers a fiction; the statute makes the act capital |
| VII:12, 241 (V7) | —, V7 | People improvise and exercise care “while the reasons they offer about their own conditions are treated as irrelevant.” V7: “A relation may require a party's judgment while withholding standing for that judgment to contest the terms of the relation.” | The precondition: judgment demanded, standing withheld |
| VII:196 | — | “An automaton can hide work by presenting its result as the property of an object.” | The credit side: success goes to the mechanism |
| IV:143; plate VIII | —, \[F\] | Graduum VI: “The environment's thread runs to the first landing and is caught in Culpax's funnel.” In plate VIII Culpax shouts at 6 arcs, Foras at 1, Choraz at 9 ([`tabula_viii.py`](../../../books/04_graduum/plates/viii-native/tabula_viii.py):42–44). | Culpax reused: the reward is caught high, and the blamer is loud |
| Cl:15 | — | Book III's demons can “classify, delay, redirect, certify and survive the consequences of those acts.” | Surviving consequences is an office's talent |
| VI: The Operator; The Empty Seat | — | Reversed meanings: “capability denied authority”; “Unreachable power; deference to an empty office.” | The worker card and the absent authority |

## Who charges, and on what evidence

The accuser holds a salaried office, and the record is made against the petitioner. Tone is entered as evidence, a second account counts as inconsistency, and dependent reports count as independent.

| Where | Tag | The text | Mechanism |
| --- | --- | --- | --- |
| Acc:9, 15 | \[F\] | The adversary holds office “by appointment, under a description of duties, at a salary.” “He was paid from the treasury of the court he argued before.” He discloses this “because it was the defect in his office and he preferred it on the record.” | The accuser's interest, disclosed but not removed |
| Acc:53 | \[F\] | “A confession is evidence, not a defense, and I ask that it be entered for the prosecution.” | The prosecutor's rule for candor; the exhibit is the book's own workshop confession |
| Acc:81, 87 | \[F\] | Every drawing is marked “once as an exhibit for the prosecution and once as an exhibit for the defense.” The Faculty answers that the count is open, “not standing.” | Double-edged evidence; open versus standing counts |
| Acc:109; III:20, 97 | \[F\]; — | “I can bring a charge. I cannot withhold a hand, stop a line, or break a frame.” Book III: “I have left an empty place for the officer empowered to stop the work.” “No seal was issued, as stopping work was not among the approved reasons for summoning an officer.” | The charging office exists; the stopping office does not |
| Acc:135, 139 | \[F\] | Job: “What will you take from them to find out?” Later: “The court permitted it last time.” | The test's cost falls on those tested |
| III:134 | — | “The ticket was angry before anyone had contradicted it. This was recorded as its opening tone.” | The record characterizes the petitioner |
| III:166, 168 | — | “Both were accurate. Only the second appeared in the report.” “The keeper of clocks was commended for reducing the age of the incident. He had not touched the broken thing.” | Record selection; credit for the clock |
| III:253 | — | Retellings are sent to separate departments “so that no department could establish why the jar was empty.” | A distributed record prevents attribution of cause |
| III:407 (SCRIPTORAX) | — | “Converted the operator's warning into a step that the replacement could execute but could not interpret.” | The warning survives without its author |
| III:425 (REDACTH) | — | “Removed the shared identifier that showed four failures had one cause.” | Removing the common cause leaves four local faults |
| III:446 (CONSENTH) | — | “Mistook consultation for authorization; sent the unapproved work forward as agreed.” | Consultation recorded as consent |
| III:488, 597 | — | PAIMON's seal: “A box that sends a report to itself and receives it as independent assurance.” ABSENTIEL: “Presented five dependent routes as five independent safeguards.” | Dependent evidence counted as independent |
| III:687 (PROBATOR) | — | “Required proof obtainable only after the repair; withheld permission to repair.” | Two bars: proof to act is unmeetable; proof to blame is a timestamp (III:518) |
| III:701 (VELAROTH) | — | Binding: “A one-line summary without subordinate clauses.” | The compression that drops an exculpating clause |
| III:497 | — | “The proposed repair was displayed in green because it had an owner.” | Status follows ownership, not condition |
| III:499; I–II:263, 285 | — | The vote is unanimous after the fifth plan's “only reader had been allowed to leave.” I–II: “The fifth plan did not vote against the others. It could no longer be read.” | Unanimity produced by absence |
| V:309–323 | — | Book III's seven offices condemn a leaf. One “found both that the answer lacked an author and that the author had concealed the answer.” The Fourth Office's mouths require “a single account”, then “an independent account”, then find “the existence of two accounts to be an inconsistency in the applicant.” “The order was unanimous. The minutes record seven different grounds.” | Contradictory findings kept; corroboration counted against the accused; unanimity without shared grounds |
| V:315, 317 | — | “the Office had no means of receiving an appeal from a place.” “Everything behind them was entered as having failed to appear.” | No appeal route; absence entered by default |
| V:73 | — | “The gate did not move. The reader crossed the table.” | Cause read from the reader's position, not the object |
| VII:122, 128 | — | “A workplace survey can invite candour while exposing dissenters.” An institution may “route statements of injury into a category that receives no investigation.” | Testimony shaped by its channel; injury routed nowhere |
| VII:81, 112 | — | “The same silence can follow different pressures.” “Ask whether the report may cost its speaker the means to refuse.” | Silence is not consent; reporting has a price |
| I–II:229, 337 | \[F\]; \[D\] | A repair would not establish “that the person who reported this delay can do so again.” “Shorter response times may conceal rejection of difficult reports.” | The reporter's exposure |
| Mat:53 | \[F\] | The bowl's bill of divorce names the night spirit “and every other name she might have, because nobody could swear to what she was called in the next house.” | Misfortune assigned to a named non-human, by exhaustive naming |

## Rules the text already sets against it

Most counter-rules a theory would need are already written. Graduum's is the plainest: “Rank neither proves fault nor provides immunity” (IV:291).

| Where | Tag | The text | Against what |
| --- | --- | --- | --- |
| IV:291 | \[V\] | “A retrospective should examine the permissions and resources around an operator as well as the operator's action. Rank neither proves fault nor provides immunity.” | CULPAX and BAEL at once |
| IV:279 | \[H\] | “Record when a fault was diagnosable, when action became authorized and when it became feasible.” | Three timestamps against CULPAX's one |
| I–II:215, 217, 219 | \[D\], \[H\], \[D\] | “Timestamps alone cannot divide an outage into organizational and physical causes.” Ask “what evidence supports an attribution of obstruction? An unresolved authorization is not proof of malice.” “Keep three questions separate.” | Timestamp evidence; attribution in either direction |
| IV:37 (D8) | \[H\] | “Before reading a retrospective, have independent readers code contemporaneous records.” | The retrospective narrative (POSTHUM) |
| IV:281, 283, 285 | \[H\] | “Review failures without assuming that punishment supplies the missing capacity.” “Separate reporting from performance penalties.” Record “responsibility and displaced costs only where evidence supports them.” | Punitive review |
| IV:36, 169 (D7) | \[H\] | D7 is “not a claim that blame exposure is necessary.” “Timely unpunished response is evidence to retain, not an exception to explain away.” | The earlier blame-necessity version of D7 |
| I–II:279, 283 | \[E\], \[H\] | ASRS works by “separating the reporting process from enforcement functions.” “Identity-lesson separation: ask whether a lesson remains usable after unnecessary identity links are removed.” | CULPAX's binding to one individual's name |
| I–II:411, 413 | \[V\] | Bindings 8–10: “Uncertain standing must not load all error onto those possibly excluded.” “Irreversible destruction carries a proportionate burden of evidence.” “Critical decisions require effective, affordable contestation that survives the refusal or capture of the relevant gatekeeper.” | Verdicts the accused cannot contest; irreversible sanctions on thin evidence |
| I–II:367, 385 | \[H\] | “Can a later record reopen a closed finding? Can an affected person challenge a category that excluded their report?” “Record the time, cost, and conditions imposed on the complainant.” | Closed findings |
| I–II:223 | \[H\] | “Popularity, shame, and a good dashboard do not confer that authority.” | Shame as a corrective |
| Acc:93, 101 | \[F\] | The Most High's ruling: “the name of the one who weighed is to be written at its head, where no later scribe can move it.” Kept, he says, “By the court.” | The inverse of CULPAX: the decider's name, fixed; the keeper is still the court |
| VII:147 | — | “A bargain can begin under pressure. Write the conditions beside the signature.” | Signatures read later as unconditional (POSTHUM; SCRIPTORAX's signed checklist) |
| VII:52 | — | “Show the credential. Let its issuer remain available for questioning.” | BAEL's immunity |
| VII:130 (V4) | V4 | “Reports produced under strong incentives or constraints cannot by themselves establish that the relation is benign or harmful.” It also refuses “the convenience of dismissing every subordinate's account.” | Testimony under pressure, read in either direction |
| VII:245–251 | — | In the first arrangement “the receiving procedure always continues,” so “in the faulty state its only effective action is the wrong one.” Also: “scoring compliance with continue would change the question.” | A minimal model in which blaming the observer for the outcome is unwarranted |
| V:41, 45, 47, 77, 81 | — | “record the question you discover you actually asked.” “Name the reader's contribution.” “do not make a third reading whose sole virtue is to end the disagreement.” “Let the card which would spoil the story be imaginable before the story is complete.” The blank is “the space in which the reader must answer for the reading.” | The naming specialist's unrecorded part. **Reading:** a scapegoat is a third reading whose virtue is ending a dispute about causes |
| III:795 | — | “With a delegated local permission, the same repair finishes at minute 13.” | The counterfactual changes who may act, not who knew |
| VI: King of Swords; The Summons | — | “A judgment can close a matter while its grounds remain available to later examination.” Judgement reversed: “Endless summons; performance of accountability.” | Verdicts closed to review; accountability as theatre |
| Cl:57 | — | Ask “whether an interpretation has become a fact in transit” | The charge that hardens as it is retold |

## Cautions the text sets against the theory

The text also limits a theory of scapegoating in advance. The sharpest limit: an arbitrary condemnation does not make the condemned sound (V:333).

| Where | Tag | The text | Limit on the theory |
| --- | --- | --- | --- |
| V:329–341 | — | A reader writes “The offices are absurd; therefore the leaf is sound,” and another hand “crossed out therefore.” “The office's failure does not confer a gift of truth upon whatever passed outside it.” “A prohibition is not a refutation. A prohibition is not a certificate.” | A bad process does not exonerate. **Reading:** this also answers “witch hunt” claims made by the powerful |
| Mat:77 | \[F\] | The one-Great-Mother story “was a kinder story than the priests’, and it was built the same way: choose one, and call the rest her pieces.” | **Reading:** reversing a totalizing story does not establish the reversed account. Whether an executive bears responsibility still requires evidence of that executive's conduct, authority and constraints |
| IV:25; I–II:217, 269 | \[V\], \[H\], \[D\] | “no office in it need be malicious for the building to behave as drawn.” “An unresolved authorization is not proof of malice.” “It does not prove a motive in the person who controls the maintenance budget.” | Mechanism without malice; no motive read off structure |
| IV:19; III:837 | \[H\]; — | Graduum examines Book III's pattern but “does not derive a law of bureaucracy from the satire.” Book III: “The three gradients belong to the satire. Liability means exposure to organizational blame here; the book makes no claim about legal liability.” | The gradient is not yet a finding |
| VII:140 | — | “Every report has conditions of production, including a human report. If that fact were sufficient to disqualify testimony, the standard would defeat ordinary inquiry.” | Conditions of production alone do not invalidate every report. This does not establish a coerced confession's reliability about the alleged act; it may instead be evidence about the interrogation that produced it |
| VII:72 | — | Coordination under time pressure “identifies a reason for bounded delegation, a time limit, and a need for later accountability.” | Accountability is not by itself scapegoating |
| I–II:493 | \[D\] | “The book must not claim to have predicted what it only redescribed after the event.” | Fitting a scapegoat story to each incident afterwards |
| IV:233; EDITORIAL:18 | \[D\]; editorial note | The cipher is “not proof that institutional invocations inevitably carry their own indictment.” The 17 October pass cut the universal version as “not evidence that every institution encodes an indictment.” | No universal hidden charge |
| III:778 | — | “Its ability to describe the process does not place it outside it.” | The describer is implicated, including whoever writes the theory |
| Mat:99 | \[F\] | “The others stand: the hands were not asked, and nobody wrote down where the clay was dug.” | The book keeps charges against itself standing |

## Witch(x) failure modes, staged in the text

Several failures the protocol guards against have scenes in the books. Field names follow v0.5 as recorded in the 2 October protocol conversation; the protocol PDF was not reopened for this register. Neither is in this repository. This is a proposed mapping, not a verified claim of complete protocol coverage.

| Witch(x) failure or field | Where the text stages it |
| --- | --- |
| Coerced testimony counted as independent | Acc:53, confession entered for the prosecution; V:313, two accounts counted as inconsistency; VII:112, 130 |
| Malformed question answered, not rejected | III:608, “why did you not act?”; III:643, when Foras had known; V:41, record the question actually asked; I–II:219, three questions kept separate |
| Dependence | III:488, PAIMON's seal; III:597, ABSENTIEL; III:425, REDACTH; I–II:137, “An alternative is not independent merely because its drawing is different.” |
| Double-edged evidence | Acc:81, every drawing marked for both sides |
| Alternative named before the verdict | V:77, the card that would spoil the story; V:47, no third reading to end a disagreement |
| Open verdict, decisive gap | Acc:87, “open” and “not standing”; V:339, “The two do not cancel.” |
| Format compliance read as rigor | III:86, “The table passed review because it made the missing information visible.”; V:53, “A completed record does not prove that the observation was good.” |

## Tensions inside the text, left open

Seven pressure points for a theory of blame. Some concern competing commitments; others compare the satire's depicted failures with the reading text's proposed safeguards. That comparison does not by itself establish a contradiction. The questions below remain open at their stated scope.

1. **Candor.** De Officio Accusatoris enters a confession “for the prosecution” (Acc:53). Books I–II and IV separate reporting from enforcement and penalty (I–II:279, 283; IV:283); blameless reporting exists to suspend the prosecutor's rule.
2. **The landing's evidence.** CULPAX's binding is “The earliest timestamp and one individual's name” (III:518), while I–II:215 says timestamps cannot divide causes and IV:279 asks for three. The first depicts a defective attribution rule; the latter passages propose standards for investigating it. The empirical question is when an actual institution substitutes the first for the latter, and what contemporaneous records would show that substitution.
3. **The indictment field.** Every Book III entry ends with what the office actually did, a field that “must accompany any copy” (III:18) and that the commission calls “the indictment” (`books/03_escalationum/docs/COMMISSION.md`:33 †). FORAS's field reads “Located the fault in four minutes; left it running while permission was sought” (III:64), and Graduum's plate X binds that line into the litany that “cannot be copied without the indictment” (IV:223–225). **Reading:** apply VELAROTH's binding, no subordinate clauses (III:701), and “left it running” is what remains; the text does not say whether this demonstrates CULPAX or slips into it.
4. **The numbers.** The catalogue sets liability = competence = 6 − authority at every station, so competence and blame are one number. Graduum calls the pattern satire (IV:19), and the only executable specimen runs on invented minutes (III:797); nothing in the books could test the gradient yet.
5. **Reporters and the accused.** “Fading can protect reporters while weakening evidence” (I–II:443), and “Removing all provenance would instead defeat some checks” (VII:138). A rule letting the accused inspect the evidence, proposed in chat and not in the text, would expose reporters; the text says “Neither conflict has a general resolution in the diagram” (I–II:443).
6. **Move blame, or remove the name.** Book III takes its form from Weyer's catalogue (III:802), appended to a treatise against prosecuting witches. Weyer called accused witches mentally ill and treated magicians as heretics using the Devil's power ([summary](https://en.wikipedia.org/wiki/Johann_Weyer)), moving culpability rather than removing it. IV:291 refuses both moves, and Mat:77 says the inverted story is built the same way.
7. **One funnel, two directions.** Culpax names the owner downward in Book III (III:516) and catches the reward upward in Graduum VI (IV:143). **Reading:** the same office handles credit and blame; the text does not connect the two uses.

## Outside the bound text

Four things the theory needs sit outside the binding: the cut Vis Maior tract, two dropped Matricis lines, the slander spells in Book VII's research ledger, and the project's one witch-finding spirit, in an undelivered Wands draft.

| Where | Status | The text | Bearing |
| --- | --- | --- | --- |
| Vis Maior tract, `books/01_matricis/canvas/project/VisMaior-1` to `-4.dc.html` † | Excluded 17 Oct; the editorial note says “Consider an appendix, not erasure” (EDITORIAL:55) | “THE DEMON NONE WILL SUMMON AND NONE WILL CRITICIZE.” “Thereafter it cometh of itself, when the loss is no one's fault.” “In the hour of loss the storm is cursed and the clause is kept.” “Under it no one was wrong.” | **Reading:** the other exit from CULPAX's question, no one's fault instead of one individual's name. Which exit gets used may depend on whether the parties are two firms or a firm and its worker |
| Matricis `Text-4a.dc.html` (archive) † | Not carried into I–II | “The witness who is punished teaches the instrument to report calm.” | The reporting-penalty claim in one line |
| Matricis `Text-9.dc.html` (archive) † | Not carried into I–II | “The corpus selects against the claims.” A postmortem “says what its publisher can afford to say.” “Governance causes appear where someone outside can compel them: regulator investigations, inquiries and litigation.” | The text's own case for inquiry records, such as Horizon's, over vendor postmortems |
| I–II:817 | Cut in consolidation | “the unsupported causal split of outage time” is not carried into the text | The book has already retracted one attribution |
| EDITORIAL:13, 18 | Applied 17 Oct | “Remove blame exposure as a necessary condition of a working bypass.” The universal indictment claim was cut. | D7's revision; the ciphers' scope |
| `books/07_septimus/research/a-grimoire-compulsion.md`:93–97, 113 † | Research ledger; not cited in De Vinculis | In a PGM slander spell the operator “announces the slander” of a woman, NN. Betz's note 314, as reported: “shifting blame for the ritual violation onto the target is a motif found in numerous older Egyptian texts.” The ledger infers the god “is manipulated into hostility by a false report, a third route besides command and contract.” Naether (2023), abstract only: “It analyses how practitioners shift blame.” | **Reading:** a slander spell is a scapegoat operation run as an escalation. Access: Betz full-text snippets and Naether's abstract. That *diabolē* (slander) is the root of *diabolos* (the accuser) is from memory |
| `books/07_septimus/research/c-organizational-compulsion.md`:145–146 † | Research ledger | Elish read at PDF level with page cites: the crumple zone “protects the integrity of the technological system”; “Therac-25 as a contrast case where no crumple zone formed.” | A negative case from the book's main blame source; the registers still list Elish at abstract level |
| `books/03_escalationum/docs/COMMISSION.md`:17, 33 † | Project record | “Blame rolls downhill and lands on the frontline worker who could fix the problem.” “That field is the indictment. Anyone who copies the table as procedure copies the complaint with it.” | The premise Book III was commissioned on |
| [`books/06_tarot/wands/draft/wands.json`](../../../books/06_tarot/wands/draft/wands.json):395–400 | Claude's unbound Wands draft; the delivered Queen of Wands is Sallos, “The Open Court” ([`wands-delivered.json`](../../../books/06_tarot/wands/delivered/wands-delivered.json):192) | Vine, the Goetic spirit drafted for the Queen of Wands, “discovers witches and things hidden.” Reversed: “The finding-out turned inward on the household; walls thrown down to see who was behind them.” | The project's one witch-finder, drafted and not delivered |

## Bibliography: present and absent

The registers hold Elish, Weyer's catalogue and Freeman, but none of the standard literature on witchcraft accusation or on blame after incidents. René Girard is absent; the only Girard cited is the logician J.-Y. Girard.

**Present**

- Elish (III/D05, IV/EL1). Book III's check used “Elish's journal abstract and metadata” (III:832); IV/EL1 says “the paper was not inspected in this pass” (IV:325). IV/EL1's use line, “The keyboard is not the crumple zone,” has no matching passage in Book IV's reading text.
- Weyer, *Pseudomonarchia daemonum* (III/D01). The host treatise, *De praestigiis daemonum*, is not cited.
- Freeman, “The tyranny of structurelessness” (I-II/G3); NASA ASRS (I-II/N1, F43, F45); Wildavsky, *Searching for Safety* (I-II/F24), Douglas's collaborator on risk.
- Taylor and Braverman (III/D06, D07); the Luddite declaration and secondary sources (Acc/A9–A12).
- 2 Samuel 24 and 1 Chronicles 21 (Acc/A3), recalled and not rechecked; its note: “1 Chronicles 21:1 has satan without the article, which the parable flattens into the adversary.”

**Absent**

| Source | Why here | Checked in this pass |
| --- | --- | --- |
| René Girard, *I See Satan Fall Like Lightning* (1999; English 2001) | The default frame for any scapegoat theory; Acc's adversary who “was never thrown down” answers its title | From memory |
| Mary Douglas, *Risk and Blame* (Routledge, 1992), ch. 5 “Witchcraft and Leprosy”; ed., *Witchcraft Confessions and Accusations* (Tavistock, 1970) | Risk as the modern way to allocate responsibility for misfortune | Contents: [Routledge](https://www.routledge.com/products/9781315015842); argument: [summary](https://en.wikipedia.org/wiki/Mary_Douglas) |
| E. E. Evans-Pritchard, *Witchcraft, Oracles and Magic among the Azande* (1937) | Witchcraft answers why misfortune struck these people now; oracles name the witch, and Book V is the oracle volume | From memory |
| Keith Thomas, *Religion and the Decline of Magic* (1971); Alan Macfarlane, *Witchcraft in Tudor and Stuart England* (1970) | The refused neighbour becomes the suspect | From memory |
| Jo Freeman (Joreen), “Trashing: The Dark Side of Sisterhood,” *Ms.*, April 1976 | Same author as I-II/G3, on character assassination inside a movement | [Author's site](https://jofreeman.com/joreen/trashing.htm) |
| Michael D. Bailey, “From Sorcery to Witchcraft,” *Speculum* 76.4 (2001), 960–90 | Categories built for learned demonic magic applied to common sorcery | Citation: [Warwick reading list](https://warwick.ac.uk/fac/arts/history/students/modules/hi2e9/programme/revenants); argument from memory |
| Johann Weyer, *De praestigiis daemonum* (1563) | The treatise Book III's catalogue was appended to | [Summary](https://en.wikipedia.org/wiki/Johann_Weyer) |
| Sidney Dekker, *Just Culture*; Richard Cook, “How Complex Systems Fail” | Blame after incidents, from practitioners | From memory |
| Increase Mather, *Cases of Conscience* (1692–93) | Salem ended on an evidentiary rule against spectral evidence | From memory |
| Post Office Horizon record | A subpostmaster told she was the only one with Horizon problems pleaded guilty to false accounting to avoid prison; more than 700 convictions, 1999–2015 | [Hamilton](https://en.wikipedia.org/wiki/Jo_Hamilton_%28subpostmaster%29); [Birmingham](https://www.birmingham.ac.uk/news/2024/why-the-post-office-was-able-to-bring-private-prosecutions-in-the-horizon-it-scandal) |
| David Frankfurter, *Evil Incarnate* (2006) | The expert who names the conspiracy | From memory |
| Betz, *The Greek Magical Papyri in Translation*; Naether, *Journal of Cognitive Historiography* 8 (2023) | Slander spells; blame-shifting | Book VII ledger only |

De Vinculis writes “Girard's ludics” (VII:126) and “Girard's interactional perspective” (VII:251) without initials; if René Girard enters the register, both need them. Two unanimous verdicts in the text need no shared conviction: the vote after the reader left (III:499) and the order with seven grounds (V:323).

## Gaps the register shows

What the text does not hold yet is the part a theory would add.

- **No real incident.** Every incident the books narrate is invented (III:780, 797; I–II:209). The real charges in the bound text are scriptural (the census, Job), the 1812 frame-breakers, and one forgery dispute the museum settled by siding with its curator (Mat:89).
- **No demand side.** The text says where blame lands, not why an organization needs a name at all.
- **No line between accountability and scapegoating.** De Vinculis asks for “later accountability” (VII:72), and nothing says where that turns into a scapegoat.
- **No witch.** The cast is offices, an accuser and a first observer; the word occurs once, in a register of debts (III:802). The one witch-finding spirit, Vine, was drafted for the Queen of Wands and not delivered.
- **Two operations unconnected.** The false report (the ledger's slander spells) and the no-fault clause (Vis Maior) sit outside the binding, apart from CULPAX.
