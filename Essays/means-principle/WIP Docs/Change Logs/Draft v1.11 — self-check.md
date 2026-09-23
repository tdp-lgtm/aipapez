# Draft v1.11: self-check (response to the Stage 7c round 7 cold read: a second 7a pass)

AI-authored, 2026-09-23. Compares `WIP Docs/Drafts/Draft v1.11.md` with `Old versions/Draft v1.10.md`, against `Scrap/7c-report-round7.md` (10 items; one-read test passed with two mismatches).

- **Why this round is different.** Six rounds of spot fixes had levelled off at 9–10 (14 → 13 → 11 → 10 → 10 → 9 → 10). Each fresh reader sampled about ten mostly new stumbles from the case-heavy middle. The reader's scale calls the 6–15 band "another rewrite round", and Stage 7 sends sections needing real rewriting back through 7a. So v1.11 has three parts:
  1. **Direct structural fixes** for the recurring causes;
  2. **a second 7a pass** by fresh rewriters on §3 and §§4–5;
  3. **a self-edit pass on §2**, on the same brief, after §2's rewriter failed at the output limit.

## 1. Direct structural fixes

| Recurring issue | Fix |
|---|---|
| The second feature gets absorbed into the replacement test (one-read mismatch, rounds 5 and 7) | Previewed in §1's thesis paragraph: "And what a person supplies is judged against the agent's alternatives, not against her absence." It is introduced in §2 by its fixed name, "judging supply against the agent's alternatives", and that exact phrase is used everywhere it is invoked: §2 (four places), §3, §5 and §6's summary, where both features are now named ("The replacement test, together with judging supply against the agent's alternatives, …") |
| Ramakrishnan blurred with the absence theorists (round-7 mismatch) | "Absence tests fail, as Ramakrishnan himself shows. In one of his cases…". Verified: file 01 L121–129, where he rejects Opportunism, the absence principle, with the pill case |
| The flamethrower case (round 7 L45; note 6 an apparatus item) | Restored to its source: the woman defends herself **and nineteen others** (file 29 L67, L169). v1.10 had dropped the nineteen, which would make the permissibility verdict doubtful (one innocent killed to save oneself alone). The case is made self-contained: the direction of the error is named ("forbidding what is permissible"), the counterfactual is in steps, and the mechanism is stated ("a view that weakens a bystander's claim only when his presence costs the defender something"), checked against Liao and Barry's account (file 29 L75, L178). "The replacement test gets it right" is corrected to "Judging supply against the agent's alternatives gets it right", the feature that does the work. Note 6 is cut, and Øverland 2014 leaves the references |
| §4 ¶1's three-party exchange (rounds 5, 6, 7) | One move per sentence: Quong's condition, then Parry's claim with its own citation, then "So Quong's principle cannot condemn the passer-by.", then what is needed. Parry's meta-conclusion (that the principle helps determine rights) is dropped; the argument does not need it |
| The hospital's rule (round 7 L69, L89) | In §3, the tension is now inside the rule's own sentence ("…take one anyway, refused or not, …"; wording from the §3 rewriter). In §4 it is recapped: "the hospital's rule from section 3, applied to an omission" |
| §1's elimination sentence (round 7 L13) and credit string (round 7 L21) | The case sentence now names each candidate in turn ("uses his body …, and in both she kills him rather than letting him die"). The four-name credit string is replaced by "(section 3)", where Mack and Alexander are credited in the text and Tadros and Walen in note 7 |
| The motive reply (rounds 4, 6, 7: "asserted rather than derived") | Rewritten in plain terms without "power". The assumption is stated as "the permission not to give justifies an act only when the act is the agent's answer to the question that premise 3 makes hers". Premise 3's support is spelled out: the permission protects her answer, and the rescuer "had answered it in favour of giving". The honest framing "on one assumption" is kept: the §4–5 rewriter's version presented the assumption as following from premise 3, which it does not strictly do |

## 2. The second 7a pass

- **§3.** Rewriter output 1,427 words (from 1,480). Applied: 1,480 words. Dispositions in `Scrap/7a2-changes-s3.md`.
  - Kept: each horn of Quong's dilemma names its charge; the Thomson epigram is replaced by the inference it hid; the hospital's rule carries its own tension; the sentence splits.
  - Rejected as meaning changes:
    - "Both horns" (wrong referent);
    - the replacement test restated as "something else could have supplied the good" (it changes the test);
    - "only"/"exactly" dropped from premise 4's reason (it weakens the biconditional);
    - "no value can answer that complaint" (an overstatement);
    - "a cost falls on" (loses "impose").
- **§§4–5.** Rewriter output 1,742 words (from 1,804). Applied: 1,789 words. Dispositions in `Scrap/7a2-changes-s4-s5.md`.
  - Kept: the one-move-per-sentence §4 ¶1; "though his motive is vicious" (the round-7 register bump); trims.
  - Rejected as meaning changes:
    - "refrains, so his body will stop" (turns purpose into result);
    - the list "the principle that explains it, the footbridge case, and…" (it would give up the footbridge case);
    - Kamm's claim stripped of "She argues that";
    - Quong's "does not prohibit" becoming "permits";
    - "the man"/"the five" in Parry's two-trolley case (different people there);
    - the motive assumption presented as entailed.
- **§2.** The rewriter failed with an API output-limit error and wrote nothing. Self-edit record in `Scrap/7a2-changes-s2.md`: 1,458 words from 1,465.
- **Cost.** The rewriters used about 244k tokens (§3) and 287k (§§4–5); the §2 run's use before failing is not reported. This is far above the first 7a pass.

## 3. Checks

- **Displays:** Display 1 and Display 2 are byte-identical to v1.10.
- **Notes:** [^1]–[^11] referenced and defined in order (old note 6 cut; notes 7–12 become 6–11).
- **Quotations:** a Counter diff against v1.10 finds no change to any quotation in the body. The one removal is the quoted title of Øverland 2014 in the references.
- **Citations:**
  - Two citation parentheticals were removed, both intended: the four-name credit string in §1, now "(section 3)", and note 6's "(Liao and Barry 2020, [p.])".
  - `(verify)` tags: 3, unchanged.
  - `[p.]` placeholders: 62 → 61 (note 6).
- **References:** 20 entries, all cited; no in-text citation lacks an entry.
- **Diff:** about 38 insertions and 42 deletions, all accounted for in the tables above and in the three `Scrap/7a2-changes-*` files.
- **Words:** 5,793 before the abstract, down from 5,825 (−32). With a 150-word abstract the total is about 5,935, leaving about 65 words of reserve.
- **Lint:**
  - triads 15 (0.8/300w), within budget, after three clause chains introduced this round were undone;
  - uniform-length run 3, within budget, after the second-feature paragraph's reason was split;
  - short sentences 4: two false positives ("*Smoke*.", "*Wedge*.") and two deliberate verdicts ("Diverting is permissible.", "The analogy fails."). "Absence tests fail." is no longer a separate sentence.

## Ledger

| Section | 7c-7 / 7a-2 |
|---|---|
| 1 | FIXED (items 1, 8; the second-feature preview) |
| 2 | FIXED (items 2, 3; the mismatches; self-edit pass) |
| 3 | FIXED (items 4, 9; 7a pass) |
| 4 | FIXED (items 5, 7; 7a pass) |
| 5 | FIXED (items 6, 10; 7a pass) |
| 6 | TOUCHED (both features named) |
| notes | FIXED (note 6 cut; notes 8–9 trimmed) |
