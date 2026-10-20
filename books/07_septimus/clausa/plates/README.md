# The first seal

The seven sheets in this folder are the Nota Clausa as it was sealed on 17 October 2026 and bound from 19 October. They are kept unchanged, as the imported originals. The fields bound now are in [`../fields/`](../fields/).

## How it was read without the key

The sheets list their 7920 marks in the order of the agents, not of the ground. Reading the colours in the order the marks appear in each file, six to a sign through the Regula's table, gives the seven readings without regrowing anything or knowing the key. A bound PDF draws them in the same order. The digests confirm it: the readings filed in [`readings/`](readings/) were recovered that way on 20 October 2026, and every one matches the digest the first Tabula printed for it.

Gemini (Argon), reviewing through the author, had proposed sorting the marks by cell. Claude then checked the order and found it carried the reading. The fault was in Claude's original plate script, which wrote the marks as the agents were numbered. The fairness test of 17 October gave its decoder the key, so it never tried to read without one.

At the author's direction the text these sheets carry, the *Quaestio Clausa*, is printed open at the end of De Vinculis, transcribed from the readings filed here. The new fields carry a different text under a different key.

## Digests printed by the first Tabula

SHA-256 of each field's reading, as the Regula's clause 21 defines it, and of the seven joined.

| Field | Digest |
| --- | --- |
| I | `77152cc64a6b4a56722cef6e12a89eef24f3c0c74568ebe8a53f4b437a9899cb` |
| II | `a1e6f45fee51db6bcb9b3d9b76dac9dd59df2fcd5b457252d4852a089f4ecfab` |
| III | `e27815eb5f18dcacebe8202af14feb4794cd53e390a25406ba0d6824e27b2918` |
| IV | `84364b13fcce7860b3a3907260073d3290b4a63cde24cd6262f9f51cc9b10397` |
| V | `8e6bc0485207ee3c1d485699aa6fe99d34dbfd83a52677578df10ca7e4d2bb8f` |
| VI | `3ef4aa68b719245a9fb6f63d8172cf1f53a3a2d992ee28dc50e5499b1bd4547f` |
| VII | `1055904a611d318914b5a8b0fb32a075bb46fa430dffd404150490e5e0d0d198` |
| All seven | `c02a25b3011fad32f262bc6cfa6a51e853dfd30ff5643e3d90fe250c56bc628b` |

`python books/07_septimus/clausa/validate.py` checks the filed readings against these digests.
