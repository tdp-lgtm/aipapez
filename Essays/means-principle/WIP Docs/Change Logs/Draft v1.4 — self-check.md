# Draft v1.4: self-check (Stage 7b, condense and tell-strip)

AI-authored, 2026-09-23. `WIP Docs/Drafts/Draft v1.4.md` against `Old versions/Draft v1.3.md`. The pass walked §6 → §1, the opposite direction to 7a.

## What was done

- About 40 phrase-level cuts and merges across all six sections (the diff is the record). The main moves:
  - Six very short sentences merged into their neighbours: "It is not.", "It is.", "Yet it seems permissible.", "That seems wrong.", "The Spending View can.", and "The complaints differ accordingly." (now introduces the contrast after a colon).
  - "This faces a dilemma" → "This reading faces a dilemma".
  - The Choo reply tightened: "it should be the verdict on *Loop*, since…"; "I concede the cost; this is the one case…".
  - The "owed" half of premise 3 folded back into the kidney-rule paragraph.
  - The two Steinhoff citations consolidated into one.
  - Parry's externalities point compressed to one sentence. The note on Walen's "tightly connected" test and the clause about duties growing with holdings were cut. Notes renumbered 1–13.
  - The conclusion takes the model-paragraph form ("Within its scope, though, the conclusion stands: …").
- AI-tells sweep against `Craft/ai-tells.md`:
  - no banned phrases, no em dashes outside quotations, no "not only";
  - no colon reveals added;
  - no participial tack-ons found;
  - the only rhetorical question left in the body is the §2 pivot "Is it just another counterfactual test?", with §3's opening question.
- The apparatus and snap budgets are unchanged: 1 named view, 3 named cases, 2 displays, 0 coinage moves. The one pointed landing is the final sentence.

## Deterministic checks

- **Displays.** The Spending View and the central argument are byte-identical to v1.3.
- **Notes.** References and definitions [^1]–[^13] match, in order.
- **Quotations.** 42; 41 verbatim on disk; Harris remains (verify).
- **Words.** 5,732 before the abstract (§1 876, §2 1,302, §3 1,414, §4 626, §5 908, §6 145, notes 450). `word_count.py` reports 5,797 including the changelog line. With a 150-word abstract, about 5,880.
- **Target.** The target of ≤ 5,550 was **not met**. Phrase-level condensing stalls at about 5,730 without cutting arguments or engagement. The cuts below are reserved for Stage 9–10, to be used if referee-driven additions need the room.

### Reserve cuts (about 230 words, in order of preference)

1. Steinhoff's alternative right, in §3 (about 35 words).
2. The *Loop* company list moved from the text into note 12 (a net saving of about 5; the body is 35 words shorter).
3. Parry's externalities sentence, in §4 (about 30).
4. The vase paragraph, in §4 (about 65), with the bound kept by the catastrophe paragraph and the fourth difference from Ramakrishnan.
5. In the notes: Lazar (13), Costa and the order effects (25), the spiteful donor (15).
6. The last clause of the §1 two-tracks paragraph (about 16), since §3 states Quong's dilemma.

## prose_lint report (v1.4, final)

```
OK    banned phrases 0 · em dashes 0 · "not only" 0 · "not X but Y" 0
FLAG  list triads 17 (0.9/300w)   [<= 0.8]
FLAG  fragments (<=4 words) 6     [<= 3]
OK    uniform-length run 3 · openers 32% · punchy endings 16% · named views 1 · italic case names 3 · coinage moves 0 · displays 2
```

- **List triads: dispositioned as mostly false positives.** Inspected one by one, 12 of the 17 matches are clause chains of the form ", clause, and clause", not lists. The 5 real three-item lists are each a natural enumeration: the roadmap's scope sentence; "a test …, an argument …, and what follows"; the conclusion's "the opening pair, the canonical pairs and the cases …"; Thomson's three options; Christensen's three conditions. No paragraph has more than one.
- **Very short sentences: 6 matches, of which 3 are false positives.** The case labels "*Smoke.*" and "*Wedge.*" and the split at "S. Matthew". The 3 real ones ("Absence tests fail.", "Diverting is permissible.", "The analogy fails.") are flat verdicts after a case or argument, the form the model paragraphs prescribe, and they sit in three different sections. This is within budget once the false positives are excluded.

## Per-section ledger (Stage 7)

| Section | 7a (walked §1 → §6) | 7b (walked §6 → §1) |
|---|---|---|
| 1 | TOUCHED | PASS (no change needed after 7a) |
| 2 | TOUCHED | FIXED (short sentences merged; the uniform-length run broken; one case compressed) |
| 3 | TOUCHED | FIXED (merges; Steinhoff citations; "This reading") |
| 4 | TOUCHED | FIXED (merges; externalities compressed; vase tightened) |
| 5 | TOUCHED | FIXED (Choo reply; second objection; motive paragraph) |
| 6 | TOUCHED | FIXED (conclusion form; "at a stated cost") |

§1 is the only PASS in 7b, and the reason is stated. §1 was the last section 7b reached. The rewriter had already cut its register problems, and a second read found no condensable phrase that did not cost precision in the cases. This is not a final-quartile collapse: the final quartile in 7b's walking order is §2–§1, and §2 was FIXED.
