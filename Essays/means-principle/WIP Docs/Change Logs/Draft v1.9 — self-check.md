# Draft v1.9: self-check (fixes after the Stage 7c round 5 cold read)

AI-authored, 2026-09-23. Compares `WIP Docs/Drafts/Draft v1.9.md` with `Old versions/Draft v1.8.md`, against `Scrap/7c-report-round5.md` (10 items; one-read test passed).

- **Trend:** 14 → 13 → 11 → 10 → 10. The score has levelled off, so this round fixes causes rather than symptoms.
- **Otsuka's chain.** Flagged in every round, even after v1.6 cut it to one route. It is now rewritten as a walk that changes one thing at a time, from the case everyone condemns to *Loop*. Each case is introduced by what it changes, not by a label.
- **Bare case labels.** The cases with people behind the man were labelled ("the six-behind case", "the case of twenty behind") in four places. Each place now describes the case in a few words, so there is nothing to look up.
- **The second feature.** The reader underweighted it. It is now marked "as important as the first", its inference is spelled out, and it no longer shares a paragraph with the correction of Alexander.

## Each item and its fix

| # | Item | Fix in v1.9 |
|---|---|---|
| 1 | Second feature: the inference needed a second pass | The step is now explicit: "This is because the view concerns what can justify an act, and a justification is a reason for one option rather than another. So her contribution supplies a good only if it makes the act better for others than an alternative." The feature is introduced as "a second feature, as important as the first" |
| 2 | P2: the referent of "theirs" | P2 reworded, **content unchanged**: "To treat something as a resource for others at its expense is to leave to those others the question whether a good it can supply them is worth what supplying that good costs it." "Those others" names the referent. "The question whether …", which P3 picks up as "that question", is kept. This is the only change to Display 2 (checked by script) |
| 3 | Subjunctive inversion in the replacement test | "…when the good could be had without that loss if her contribution came from some other source." The two applications with the same inversion now read "If something else, such as a heavy weight, supplied the stopping…" and "If something else held the door…". This matches §1's statement and §4's "If something else supplied the stopping" |
| 4 | "The six-behind case" is a bare label | §5 now reads "keeps diverting permissible when six people stand behind the man". The three "case of twenty behind" labels (§2 once, §3 twice) are replaced by descriptions ("when twenty people stand behind the man"; "the case where twenty stand behind the man"). No new italic name, so the case-name budget stays at 3 |
| 5 | Note 5 easy to miss | The marker now sits on the sentence the note qualifies ("…better for others than an alternative.[^5]"), not on the Ramakrishnan credit two sentences later. The note stays a note: the several-alternatives rule refines the feature but is not needed to follow the argument |
| 6 | "Not alone in doing so" is ambiguous | "…though other philosophers accept the same verdict.[^11]" |
| 7 | §4 ¶1 ends on a meta-dispute | A closing sentence says what the argument needs: "What is needed, then, is a principle that explains why the five's claims do not defeat the duty to rescue him." ¶2 now opens "The Spending View is such a principle." |
| 8 | Second-feature paragraph also corrects Alexander | Split. The correction is its own paragraph, opening "Judging supply against the agent's alternatives also corrects Larry Alexander…", which also restates the second feature |
| 9 | Otsuka's chain overloads | Rewritten as two paragraphs that change one feature at a time. **Start:** the toppling case, named as it is introduced ("In the toppling case, pushing a lever moves a pole…"), which is Otsuka's "moral fixed point". **Step 1:** "Now change how the lever works": the lever diverts the trolley onto a loop, and the circling trolley triggers the pole ("morally indistinguishable"). **Step 2:** "Now change one more thing": the man already stands on the loop. "The result is *Loop*." The "intermediate case" label is gone. The second route (Ramp, old note 11) is cut; it duplicated the chain's job |
| 10 | Note 13 is dense | Split into short sentences, with "On the view" marking whose verdict is given. "See also Tadros (2020)" is cut. Tadros 2020 is no longer cited anywhere, so its reference entry is removed |

## Accuracy check on the rewritten chain (against `Background Readings/Converted text/27 Otsuka 2008`)

- **The toppling case.** "Pushing a lever" follows Otsuka's text (L19: "you would move the pole by pushing a lever"). v1.8 said "pulling", which clashed with the quotation "you push a lever…".
- **"A man from a bridge"** follows L13 ("on a bridge over the track"). "His body stops the trolley, killing him" follows L13 ("his being hit will stop that trolley and kill him").
- **"A moral fixed point"** is verbatim (L125), "for Kamm and other non-consequentialists".
- **Step 1** matches the Loop-Bridge Case (L107: "the trolley's travelling in this circle remotely triggers the pole"). "Morally indistinguishable" and "you push a lever that causes someone to fall from the bridge" are both verbatim (L125).
- **Step 2** matches Otsuka's comparison of the two cases (L119: "you move the person into the path of the trolley in the Loop-Bridge Case, whereas you move the trolley into the path of the person in the Loop Case").
- **Kamm's point.** v1.8 said the difference was one "Kamm herself argues is insignificant". That was looser than the source. Otsuka reports that Kamm argued against its significance "in the relevantly similar context of a Lazy Susan Case" (L119). v1.9 says so: "Kamm herself has argued, of a similar case, that this makes no moral difference (Otsuka 2008, [p.])".
- **Note 25.** "Otsuka doubts that anyone can separate these cases" replaces "doubts that any principle separates these cases". It is closer to note 25 (L163), which asks whether "others succeed where Kamm has failed to distinguish the Bridge Case … from looping cases" and answers "I very much doubt it".

## Other changes in this version

- **A repeated attribution is cut.** v1.8's Choo paragraph repeated "which Otsuka calls a fixed point"; the new first step already gives the quotation.
- **Note 10 is thinned to its point.** The partial-supply variant and its verdict remain. The round-4 fix ("In *Loop* as described…") is dropped along with "I leave such variants aside". That phrase is what made the note read as unfinished, so the note is now self-contained without it.
- **Walen's forfeiture sentence in note 12 is kept as in v1.8.** An intermediate draft of this pass said "the malicious diverter … she". That wording implied Walen's case is the main text's enemy, whom the text calls "he". Walen's own case is a variant (Brenda; file 22 L111–121), so "a malicious diverter" is restored.

## Deterministic checks

- **Display 1:** byte-identical.
- **Display 2:** one line changed (P2, wording only).
- **Notes:** [^1]–[^12] referenced and defined in order (old note 11 cut; old notes 12 and 13 become 11 and 12).
- **Quotations:** a Counter diff against v1.8 shows one removal, "completely morally indistinguishable", which went with the Ramp note. Nothing was added. Harris is still marked (verify).
- **References:** 22 entries, all cited; no in-text citation lacks an entry. **Correction:** the v1.8 self-check said 24 entries. The true count for v1.8 was 23 (v1.7 had 26, and three were removed).
- **Diff:** 20 insertions, 22 deletions, all in the rows above.
- **Words:** 5,814 before the abstract, up from 5,780.
  - With a 150-word abstract the total is about 5,956, under the 6,000 cap.
  - Only about 44 words of reserve remain. The Stage 10 length pass owns this, and referee additions must be offset.
- **Lint:**
  - triads 16 (0.83/300w, just over 0.8), dispositioned as before;
  - short sentences 6, the same six as v1.8: three false positives ("*Smoke*.", "*Wedge*.", "S. Matthew") and three deliberate verdict sentences;
  - no new flags.

## Ledger

| Section | 7c-5 |
|---|---|
| 1 | PASS |
| 2 | FIXED (1, 3, 4, 5, 8) |
| 3 | FIXED (2, 4) |
| 4 | FIXED (7) |
| 5 | FIXED (4, 6, 9; the "fixed point" repeat) |
| 6 | PASS |
| notes | FIXED (5, 10; note 10 thinned; old note 11 cut) |
