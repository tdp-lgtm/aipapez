# Draft v1.1: self-check (Stage 6 Pass 1)

AI-authored, 2026-09-22. A deterministic self-check of `WIP Docs/Drafts/Draft v1.1.md` against `Old versions/Draft v1.0.md`: the diff must match the changelog. This pass was preceded by a fresh read of `Playbook/Craft/model-paragraphs.md`.

## 1. What the pass did (the changelog, itemized)

| Change | Where (v1.0 → v1.1) | Kind |
|---|---|---|
| Support for *Smoke* made precise: "cannot be what turns a permissible killing into a wrongful one", replacing "cannot turn a permissible act into a wrong one". A harmless use might be a minor wrong of its own; the claim needed is only that it cannot make the killing wrongful | ¶1.2 (D05) | Precision fix |
| Quong's formulation shortened to its operative clause; the case with the structure of *Smoke* kept | ¶1.2 (D06) | Cut |
| "a relation he takes as primitive" → "Ramakrishnan takes his criterion to be primitive" (he calls his principle, not the relation, underivative: file 01 L237) | ¶1.3 (D07) | Precision fix |
| The thesis paragraph no longer repeats the beam verdict for *Smoke* ("as I noted"); credit citations moved to ¶1.3 | ¶1.4 (D08) | Cut (repetition) |
| The driving example moved out of the scope paragraph (it is treated in §5) | ¶1.5 (D09) | Cut (repetition) |
| "It rests on a difference…" removed; the log sentence reworded | ¶2.1 (D10) | Cut |
| The replacement test paragraph no longer re-applies the test to the pair; new note 3 on Quong's "relevantly similar body or property" clause (file 09 L49) | ¶2.3 (D14) | Cut; addition |
| The pill case compressed | ¶2.4 (D15) | Cut |
| The Alexander correction compressed to one sentence | ¶2.5–2.6 (D16) | Cut |
| "Use is neither necessary nor sufficient" merged into the canonical-pairs paragraph | ¶2.7 + ¶2.9 (D17 + D19) | Merge |
| Liao and Barry's two cases compressed | ¶2.8 (D18) | Cut |
| Credit list shortened; Tadros and Walen 2022 moved to note 8 with Lazar | ¶3.2 (D24) | Cut |
| "What should be blocked is narrower" wording | ¶3.4 (D26) | Tighten |
| "Others may divert a trolley onto her that she need not divert onto herself" moved from ¶3.5 to the Thomson paragraph, where it answers her argument | ¶3.5 → ¶3.6 (D27 → D28) | Move |
| The Steinhoff paragraph folded into the end of the premise 4 paragraph | ¶3.7 (D29 → D27) | Merge |
| The Ramakrishnan quotation shortened; reply compressed | ¶3.8–3.9 (D30) | Cut |
| The sliding-man and omissions paragraphs compressed; "slow the trolley enough to save the five" follows Parry's wording (file 06 L67) | ¶4.1–4.2 (D31–D32) | Cut; accuracy |
| Parry's externalities worry compressed | ¶4.4 (D34) | Cut |
| Choo's robustness points compressed into one sentence | ¶5.1 (D36) | Cut |
| The *Loop* defence split into two paragraphs (Otsuka's routes; the reply to Choo and the concession); Alexander added to the company (file 25 L45, his note 8) | ¶5.3 (D38) | Split; addition |
| The person-in-the-path paragraph no longer repeats "one constraint among several" | ¶5.4 (D39) | Cut (repetition) |
| The intentions explanation compressed | ¶5.6 (D41) | Cut |
| Note on the cave and parking cases cut (low value; the view's silence on such cases is stated in the text) | old note 12 | Cut |
| Notes 3, 9, 12, 13 shortened; notes renumbered | notes | Cut |

No argument was removed. Every outline bullet still maps to a paragraph, except the cave and parking cases (formerly a note to ¶5.4), which this pass cut for length.

## 2. Deterministic checks

- **Diff.** `git diff --no-index --stat`: 44 insertions, 45 deletions, all in the rows above. Every changed paragraph appears in the table.
- **Words.** 6,459 → 5,761 before the abstract (§1 859, §2 1,295, §3 1,419, §4 599, §5 944, §6 152, notes 483 in 13 notes). A 150-word abstract would bring the total to about 5,910, under the 6,000 cap. The 7b condense pass targets a further 3–5% to leave room for referee-driven additions.
- **Quotations.** A re-run of the quotation script found 42 quotations; 41 are verbatim on disk; Harris's "survival lottery" remains (verify), REQUESTS #22.
- **Notes.** References [^1]–[^13] and definitions [^1]–[^13] match, in order.
- **Lint.**

```
OK    banned phrases 0 · em dashes 0 · "not only" 0 · "not X but Y" 0
FLAG  list triads 20 (1.0/300w)   [<= 0.8]
FLAG  fragments (<=4 words) 12    [<= 3]   (3 false positives: case labels, "S. Matthew")
FLAG  uniform-length run 5        [<= 3]
OK    openers 30% · punchy endings 21% · named views 1 · italic case names 3 · coinage moves 0 · displays 2
```

  All three FLAGs are deferred to the 7b condense and tell-strip pass, which owns them. The triad density rose because the text got shorter while the lists stayed.
