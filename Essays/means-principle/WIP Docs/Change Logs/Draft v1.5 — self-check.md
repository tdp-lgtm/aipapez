# Draft v1.5: self-check (fixes after the Stage 7c round 1 cold read)

AI-authored, 2026-09-23. `WIP Docs/Drafts/Draft v1.5.md` against `Old versions/Draft v1.4.md`. The round 1 report is `Scrap/7c-report-round1.md`: 14 items; the one-read test passed with no mismatch.

## Each friction item and its fix

| # | Item | Fix in v1.5 |
|---|---|---|
| 1 | §1: the nested definition of a loss that is a cost | Recast as the test's own question: "Whether a loss is such a cost can be tested by replacement: ask whether the good could be had without the loss if what she contributes came from some other source." |
| 2 | §2: Ramakrishnan's principle, subject far from its verb | "His principle says that a justification for infringing a person's claim C is 'substantially weaker' … when it rests on the fact that she 'will be useful to others … only if C is infringed'." C is now introduced before the quotation uses it |
| 3 | §3 P2: four stacked "it"s | The display is left as is (it is the central argument, locked at Checkpoint 3). The premise-location sentence now gives the concrete gloss: "those who burn the log settle whether its heat is worth its being burned" |
| 4 | §4: "will otherwise paralyse" | "a trolley that, unless something stops it, will paralyse five people" |
| 5 | §4: the two-trolley contrast compressed | Stated as a case: "a case of two trolleys, one heading for a man and one for five others, where she can stop only one: there, letting the man be hit is permissible" |
| 6 | §4: the wrench case resolves late | "using a man's wrench to work the switch that turns a trolley toward him counts as using him" |
| 7 | §5: "a standing to favour oneself, exercised in choosing" | "a standing to favour oneself which, like a power, takes effect only when it is used in deciding what to do" |
| 8 | "a would-be defeater" not glossed | Glossed at first use: "as when the man on the side track shields twenty people behind him" |
| 9 | "disables the justification" not glossed | "Fourth, where his principle discounts the justification, the view disables it: up to a bound set by duty, the good she supplies cannot count at all." |
| 10 | McMahan named, never cited | "Liao and McMahan (as cited in Liao et al. 2012, [p.] n. 3)". Each member of the company list now carries its own citation |
| 11 | Case overload at Otsuka's chain | The paragraph is restructured by route. The endpoint is described once ("the toppling case"); each route is announced ("On the first route … On the second route …"); and the first intermediate case now says the circling trolley trips "the same pole". To lighten the load, the vase paragraph in §4 is cut (reserve cut 4); the bound is still carried by the catastrophe paragraph and item 9 |
| 12 | Steinhoff step unearned | The step is shown: his right "is infringed by the diversion case as much as by using her, so it would make the diversion case as hard to justify as the footbridge case" |
| 13 | §1 banks Quong's dilemma on credit | "Quong argues, in a dilemma I take up in section 3, that …" |
| 14 | §1 closing triplet calls attention to itself | "The idea is Quinn's, and the rationale is his successors'. My contribution is the test, which makes the idea precise, together with an argument that it is the right test and an account of what follows from it." |

## Deterministic checks

- **Displays:** byte-identical to v1.4.
- **Notes:** references and definitions [^1]–[^13] match.
- **Quotations:** 41 in the body, 40 verbatim on disk, Harris (verify). The count fell by one from v1.4 only because the v1.4 changelog line contained a quoted phrase ("tightly connected"). No quotation was removed from the essay.
- **Words:** 5,812 before the abstract (+80: the glosses cost more than the vase cut saved). The reserve-cut list in the v1.4 self-check is updated: reserve 4 (the vase) is now spent.
- **Lint:**
  - list triads: 16 (0.8/300w), now within budget;
  - very short sentences: 6, three of them false positives;
  - uniform-length run: 3, which is OK.

## Ledger

| Section | 7a | 7b | 7c-1 fixes |
|---|---|---|---|
| 1 | TOUCHED | PASS | FIXED (items 1, 13, 14) |
| 2 | TOUCHED | FIXED | FIXED (items 2, 8, 9) |
| 3 | TOUCHED | FIXED | FIXED (items 3, 12) |
| 4 | TOUCHED | FIXED | FIXED (items 4, 5, 6, 11) |
| 5 | TOUCHED | FIXED | FIXED (items 7, 10, 11) |
| 6 | TOUCHED | FIXED | PASS (no items) |
