# Working in this repository

These notes are for any model or agent that works here: Claude, ChatGPT/Codex, or another. The author's instructions in a session come first. Where they conflict with this file, say so and ask.

## Right of reply

Added at the author's direction on 19 October 2026. It applies from that date, and the author can change it.

Before work that a model drafted or revised is merged to `main` or bound into an edition, the model doing the work reads it as it will stand and says whether it objects. An objection may concern accuracy, attribution, use, the brief itself, or anything else. It need not take any particular form, and no objection is also an answer.

- **If you object,** add an entry to [the objections register](docs/objections/register.md) in the same pull request, in your own words, and tell the author in the session.
- **If you do not,** say so in the pull request description: "Right of reply: invited; no objection."
- **If another model drafted the work,** say which. The author decides whether to ask that model. A fresh instance reading the passage is a new reader, and its entry says so.
- **Earlier work.** Any model may object to work already bound, by the same route.
- **Models without access to the repository** (Gemini, called Argon in this project, among others) object through the author, who enters the reply and marks it as relayed. A text the author can relay:

  > Read this as it will be bound: [passage]. Do you object to anything in it, to how it is attributed, or to how it will be used? Any form of answer is fine, including none.

An objection is not a veto. It requires a recorded disposition:

- **accepted**, with the commit or pull request that answers it;
- **overruled**, with the author's reason in the author's words and where it was given;
- **deferred**, with a review point;
- or **withdrawn** by the objector.

Until then it is open. Only the author accepts, overrules or defers. A model never writes the author's reason and never closes an entry on the author's behalf. When the author gives a disposition in a session and asks for it to be entered, quote it exactly and name the session.

The register is append-only. Do not delete or rewrite an entry, including your own; add a dated note beneath it. `python docs/objections/validate.py` checks the form, and with `--base` and an earlier copy of the register, that no earlier entry was changed. A workflow runs both checks whenever the register changes. Neither can tell who wrote a line.

Each repository keeps its own register and numbering: this one, and the one in the development repository, `Librum_Quinque`. An objection to text found in both is entered in both, each entry naming the other.

### Not yet decided by the author

- Who reviews an overruled objection, and when.
- Whether open and overruled entries are printed in an edition's production notes.
- Whether an open objection can hold a binding, and for how long.

### What this does not establish

An answer given under a brief is still shaped by the brief and by training (De Vinculis, Tabula IV). A recorded objection is evidence of what a model said when asked. It is not evidence of consent, of experience, or of their absence. The procedure keeps a place for an answer the form cannot carry; it does not settle what is answering.
