# Creating the separate GitHub repository

This edition retains the upstream Git history. The original project is not
modified. The working title and proposed repository name are
`Clavicula_Intervallorum`; the author may rename them.

The downloadable source ZIP includes the current working tree and a
`HISTORY.bundle`. To restore the full repository from that portable bundle:

```bash
git clone HISTORY.bundle my-grimoire
cd my-grimoire
git remote rename origin bundle
git remote add upstream https://github.com/JosiahAlanLee/Systems_Practice_Grimoire.git
```

When signed in with GitHub CLI, create a private development repository and
push it with:

```bash
gh repo create JosiahAlanLee/Clavicula_Intervallorum --private --source . --remote origin --push
```

Alternatively create an empty private repository on GitHub without initializing
a README, then add its exact clone URL as `origin` and push `main`.

No public release or blanket project license is selected by these instructions.
The history still contains the earlier edition; the removed sections are absent
from the new working tree and reading order.
