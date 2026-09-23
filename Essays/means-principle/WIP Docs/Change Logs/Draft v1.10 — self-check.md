# Draft v1.10: self-check (fixes after the Stage 7c round 6 cold read)

AI-authored, 2026-09-23. Compares `WIP Docs/Drafts/Draft v1.10.md` with `Old versions/Draft v1.9.md`, against `Scrap/7c-report-round6.md` (9 items; one-read test passed).

- **Trend:** 14 → 13 → 11 → 10 → 10 → 9.
- **What round 6 confirms about round 5's structural fixes:**
  - Otsuka's chain, flagged in every earlier round, is no longer flagged. The reader singled it out as a dense stretch that "close[s] on a sentence that states the paragraph's payoff".
  - Round 5's bare-label problem is gone. What remained was a drift between the two numbers (six and twenty), fixed below.
- **Two spots flagged in two rounds, fixed at the root this time:**
  - the last note in §5 (rounds 5 and 6);
  - the support for the permission-as-power assumption (rounds 4 and 6).

## Each item and its fix

| # | Item | Fix in v1.10 |
|---|---|---|
| 1 | §1: two critiques in one sentence; "his" | Separated: "Ramakrishnan takes his criterion to be primitive. Quong's rationale for his criterion attaches to use, which *Smoke* shows to be the wrong target." The next sentence now reads "The rationale others have sought, for its part, comes with no criterion". "Others" points back to "Others have sought a rationale", so it cannot be read as Quong's rationale |
| 2 | §3: Quong's dilemma is hard to trace | One sentence per horn, as in Quong's text (file 09 L127: "This rationale, however, confronts a dilemma…"). The sentences are "Quong presses a dilemma against it. If compelling her means imposing costs she is not duty bound to bear, Tadros's version is the simplest form again. If it means using her body or property without her consent or duty, the explanation 'amounts to saying: …'". The first horn now uses the simplest form's own wording ("not duty bound to bear"), so the reader can see it is "the simplest form again" |
| 3 | §3: the bear/supply hinge lands only with premise 3 in mind | Tied to the permission's name: "It does not: it limits what she must give, that is, what of hers must serve others and what she must do for them." The application follows: "…nothing of his serves the five". The wording matches the premise 4 paragraph ("what she must do, and what of hers must serve"), which follows directly |
| 4 | §4: Parry's argument is compressed | The missing step is now stated: "Parry argues that the five's claims would extinguish such a right, so Quong's principle cannot condemn the passer-by. He concludes that the principle must help determine rights rather than merely follow them." Checked against Parry (file 06 L91, L101–105): the means principle "doesn't simply *track* a pre-existing account of our rights, it also *informs* the initial assignment of rights" |
| 5 | Six vs twenty drift | Numbers now appear only in the running example (six; also Alexander's number). Ramakrishnan's case is "a similar case". Later references read "when people stand behind the man on the side track" (§2, §3 twice) or "when people stand behind the man" (§5). "On the side track" separates him from the man at the door in the same §3 passage |
| 6 | §5 notes run; Christensen "broke it" | Note 12 is cut to Walen's forfeiture view, which is its link to the enemy case in the text. Christensen's passer-by and the spiteful donor are removed. Christensen 2026 is removed from the references, since nothing else cites it. The main text's "where conduct would otherwise spend someone" still sets the scope that the donor illustrated |
| 7 | Permission-as-power reads as fitted to the case | Three changes. **(a)** The objection now states the contrast the assumption must explain, as Parry draws it (file 06 L125): "Her refusal seems wrong, yet a refusal made only to keep her arm would be permissible, and the two refusals are the same conduct." **(b)** The support is now argued rather than gestured at: "The assumption fits premise 3: that premise makes the question hers to settle, and to settle a question is to decide it." The prerogative point is kept as its own sentence. **(c)** The explanation now covers both refusals: "Had the rescuer refused to keep her arm, her permission would have justified the refusal. She in fact refuses for what the man's body will supply, so her permission does not justify what she does." The assumption is unchanged; only its statement and support are fuller. The referee loop will test it |
| 8 | §2 opens with the log before stating its point | "The difference between a resource and a casualty shows what spending is." now precedes the log and the tree |

## Process notes

- **Stage 7 rule on real rewriting.** The rule is to send any section needing real rewriting back through 7a (the prose-rewriter). This round's fixes are sentence-level, so they go straight to the round-7 cold read, which also checks register. The larger rewrite in v1.9 (Otsuka's chain) also went straight to a cold read, and round 6 found no friction or register bump in it.
- **The motive reply adds support to an existing assumption.** It adds no new argument. The added premise-3 link restates the Crux Memo v0.2 §5 reasoning ("a prerogative is authority over one's *own* trade-off, exercised only by acting on it"), which is AI-authored work from Stage 3.

## Deterministic checks

- **Displays:** Display 1 and Display 2 are byte-identical to v1.9.
- **Notes:** [^1]–[^12] referenced and defined, in order.
- **Quotations:** a Counter diff against v1.9 finds no change to any quotation in the body. The one removal is the quoted title of Christensen 2026 in the references.
- **References:** 21 entries, all cited; no in-text citation lacks an entry.
- **Diff:** 14 insertions, 16 deletions, all in the rows above.
- **Words:** 5,825 before the abstract (+11). With a 150-word abstract the total is about 5,967, so about 33 words of reserve remain. Referee-driven additions must be offset, and the Stage 10 length pass owns the reserve.
- **Lint:**
  - triads 15 (0.8/300w), now within budget;
  - short sentences 6, the same six as before (three false positives, three deliberate verdicts);
  - no other flags.

## Ledger

| Section | 7c-6 |
|---|---|
| 1 | FIXED (1) |
| 2 | FIXED (5, 8) |
| 3 | FIXED (2, 3, 5) |
| 4 | FIXED (4) |
| 5 | FIXED (5, 7) |
| 6 | PASS |
| notes | FIXED (6) |
