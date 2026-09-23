# Stage 7a (second pass) — section 3: rewriter changes and dispositions

- **Rewriter.** A prose-rewriter subagent (sonnet tier), fresh context. It saw only `Scrap/7a2-input-s3.md`, the thesis, context glosses, the cold readers' stumble list for §3 (rounds 5–7), the register-sample paths and the hard constraints.
- **Its text:** `Scrap/7a2-output-s3 (rewriter text).md`, 1,427 words from 1,480 (3.6% shorter). Its memo: `Scrap/7a2-changes-s3 (rewriter memo).md`.
- **Applied text:** `Scrap/7a2-applied-s3.md`, 1,480 words after the dispositions below. The display is byte-identical to the input.
- **Cost:** about 244k tokens (28 tool uses), far above the earlier runs.

## Dispositions

| ¶ | Rewriter's change | Disposition |
|---|---|---|
| 1 | The two sceptics merged into one sentence; "My answer follows." | **Merge accepted, reworded**: "Ramakrishnan and Uwe Steinhoff both doubt that the means principle has any deeper rationale" (the rewriter's "doubt any deeper rationale" was ungrammatical). **"My answer follows." rejected** as a new three-word sentence; restored "My answer is the following argument." |
| 2 | "the analysis of the log and the tree"; "Premise 3 is inherited; I defend it below"; "this section argues" | Accepted |
| 3 | "familiar" cut; "Premise 3 adds: this permission…" | First accepted. **The colon version rejected** (a colon reveal); restored "Premise 3 adds that…", which also introduces the fixed term "the permission not to give" |
| 4 | The hospital's rule: "…take one anyway, refused or not, …"; "Every refusal stands, and the kidney is taken regardless." cut as redundant; note 6's marker moved to the rule sentence | Accepted. The rule now carries its own tension, which fixes the round-7 stumble. The marker sits on the rule it compares with Harris |
| 4 | "would settle the question for them, not for her" | Accepted with a clarity fix: "would leave the question for them to settle, not her". "Settle the question for them" could be read as "on their behalf" |
| 4 | "Quinn's exception" (gloss cut) | **Rejected.** Restored "for strong moral obligations": the reader last saw Quinn's clause in §1 |
| 4 | "pair the permission with the principle" ("in the same way" cut) | Accepted |
| 5 | "In its simplest form: 'if Y…'" | **Rejected** (a verbless fragment before a colon). Restored "In its simplest form, the rationale says:" |
| 5 | Each horn names its charge: "…collapses back into the simplest form and inherits its problem"; "the explanation is circular: it 'amounts to saying…'" | Accepted. This fixes the round-6 stumble (which horn produces which charge) |
| 6 | "Both horns assume…" | **Rejected: wrong referent.** The sentence concerns the two versions of the rationale (the simplest form and Tadros's), not the two horns of Quong's dilemma, and the second horn does not make that assumption. Now: "Both versions of the rationale assume…", so it cannot be read as the horns |
| 6 | "how much a person may be made to bear"; "It does not. It limits what she must give: what she must do, and what of hers must serve others." | **The reorder is accepted.** It matches the premise 4 paragraph's order. **The rest is rejected:** the original "what a person must bear" is kept, since it parallels "what she must give". The colon is kept too, to avoid a new three-word sentence. Now: "It does not: it limits what she must give, that is, what she must do and what of hers must serve others." |
| 6 | "In the diversion case, a cost falls on the one…" | **Rejected.** "Imposes" is the simplest form's own verb ("wrong to impose C on Y"), and the reply depends on the match. Restored "The diversion case imposes a cost on the one…" |
| 6 | The replacement test restated as "whether something else could have supplied the good without her loss" | **Rejected: changes the test.** The test replaces her contribution, not the good. Restored the exact statement, which matches §2 |
| 6 | "Spending is wrong because it overrides…"; "This meets…" | Accepted |
| 7 | The lead-in "This is because the permission protects two things" cut; "only" and "exactly" dropped | **Rejected: weakens premise 4's defence.** The lead-in is the reason premise 4 holds, and "only"/"exactly" carry the biconditional that premise 4's "exactly when" needs. Restored, and the rewriter's direct naming ("what she must do", "what of hers must serve") is kept in place of "the first"/"the second" (the rewriter's flag 2) |
| 8 | "The complaints differ: … no value can answer that complaint." | **Rejected: overstates the claim.** Only the value of what was taken cannot answer it; a duty can, within the bound. Restored |
| 8 | "is harmed; that complaint is weighed" | Accepted |
| 9 | The epigram "The argument slides from serving to doing" replaced by naming the inference that remains once the analogy fails | Accepted with precision fixes: "…what remains is an inference from what he would not do to himself to what he may not do to another, and it fails: …". This fixes the round-7 register bump. "Would not" matches the essay's own report of Thomson; "fails" replaces "is false", since an inference is not false |
| 10 | Unchanged (the rewriter's flag 4: "a would-be defeater" is dense) | No change. It is Ramakrishnan's phrase, and the case follows at once |
| 11 | "this fine-grainedness"; the compound sentence split in two; "Giving is structural"; "not thereby arbitrary" | The split and "thereby" are accepted. "This fine grain" replaces "fine-grainedness". **"Giving is a structural notion" restored**: the claim is about the notion |

## The rewriter's flags

1. **Note 6's marker moved.** Accepted (see ¶4).
2. **"Protects two things" cut.** Restored (see ¶7); the phrase is the reason for premise 4.
3. **"Refused or not" carries the fix.** Kept. The round-8 cold read tests it.
4. **"A would-be defeater".** Left unchanged (see ¶10).
