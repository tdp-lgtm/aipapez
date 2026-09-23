# Draft v1.8: self-check (fixes after the Stage 7c round 4 cold read)

AI-authored, 2026-09-23. Compares `WIP Docs/Drafts/Draft v1.8.md` with `Old versions/Draft v1.7.md`, against `Scrap/7c-report-round4.md` (10 items; one-read test passed).

- **Trend:** 14 → 13 → 11 → 10.
- **Recurring spots**, each flagged by two or more readers and fixed at the root this round:
  - the §1 two-tracks paragraph;
  - the wording of P2;
  - Quong's dilemma;
  - name density in the notes.

## Each item and its fix

| # | Item | Fix in v1.8 |
|---|---|---|
| 1 | §1 two tracks: too many names | The four rationale credits (Mack, Tadros, Alexander, Walen 2022) move to the thesis paragraph's credit sentence. The tracks paragraph now reads "Some have sought a criterion … Others have sought a rationale … Neither line is complete on its own" |
| 2 | P2's predicate is buried | P2 reworded, **content unchanged**: "To treat something as a resource for others at its expense is to treat as theirs to settle the question whether a good it can supply them is worth what supplying that good costs it." The noun phrase "the question whether …", which P3 picks up with "that question", is kept. This is the only change to Display 2; the diff confirms it |
| 3 | Quong's dilemma is nested | Unnested: "In its simplest form … Tadros's version … But either compelling means imposing unowed costs, which is the simplest form again, or it means using …" The next paragraph now reads "Both versions … the simplest form" |
| 4 | Six-behind: why the six are safe either way | "If the agent does not divert, the trolley never reaches the side track, so the six are safe either way; their safety is therefore no respect in which diverting is better." |
| 5 | "The case of twenty behind" is never described | Introduced as "the same case with twenty people standing behind the man" |
| 6 | Note 6 names moral obstacles without saying what they are | Glossed: "on which a bystander whose presence raises the cost of self-defence has a correspondingly weaker claim against being harmed", from Liao and Barry's statement of the view (file 29 L165–181) |
| 7 | Note 12 name overload | Thinned to three names with their citations and Thomson's symmetric original. Costa 1987 (never received, request #21), Walen 2014 and Liao et al. 2012 are dropped and removed from the references, since nothing else cites them. A script check confirms every remaining reference is cited |
| 8 | Motive assumption has thin support | Support added: "So does the nature of a prerogative: it permits her to give her own interests extra weight, and weight she does not in fact give them cannot justify what she does." |
| 9 | Note 10 read as bearing on *Loop* | Clarified: "In *Loop* as described, his body supplies the whole of the five's rescue …" The partial-supply point concerns only variants, which are set aside |
| 10 | "Not X but Y" recurs | The conclusion's first sentence drops "not using them". The antithesis now appears once in the thesis and once in the final sentence (the essay's earned landing) |
| aside | "(verify)" tags | Kept until the Stage 10 citation audit discharges them. They are process markers, not prose |

## Other changes in this version

- The Steinhoff sentence in §3 is cut for length. His scepticism about rationales is still acknowledged in §3's opening sentence, and the essay's rationale is its answer to it.
- "Neither line is complete" became "Neither line is complete on its own", so it is no longer a four-word sentence.

## Deterministic checks

- **Display 1:** byte-identical.
- **Display 2:** one line changed (P2, wording only).
- **Notes:** [^1]–[^13] match.
- **Quotations:** 37, identical to v1.7 (Counter diff empty). Harris is still marked (verify).
- **References:** 24 entries, all cited.
- **Words:** 5,780 before the abstract.
- **Lint:**
  - triads 17 (dispositioned as before);
  - short sentences 6 (3 false positives);
  - uniform-length run 3 (OK).

## Ledger

| Section | 7c-4 |
|---|---|
| 1 | FIXED (1) |
| 2 | FIXED (4, 5) |
| 3 | FIXED (2, 3; the Steinhoff cut) |
| 4 | PASS |
| 5 | FIXED (8) |
| 6 | FIXED (10) |
| notes | FIXED (6, 7, 9) |
