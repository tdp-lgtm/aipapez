# Stage 7a — section 3: rewriter change table and dispositions

- **Rewriter.** A prose-rewriter subagent (sonnet tier), fresh context.
  - **Inputs:** only `Scrap/7a-input-s3.md`, a one-sentence thesis, a glossary of terms from sections 1–2, the register-sample paths, and the hard constraints.
  - **Calibration:** model-paragraphs, the Style Guide, prose-principles, ai-tells and the two register samples.
- **Its text:** `Scrap/7a-output-s3 (rewriter text).md`, 1,400 words by `word_count.py` against 1,455 in the input, a cut of 3.8%.
- **Applied text:** `Scrap/7a-applied-s3.md`, 1,449 words after the dispositions below.
- **Its self-report:** it checked by script that the quotations, the display block, the citations, the footnote markers and the (verify) tag are all byte-identical to the input.

## The rewriter's changes (condensed from its table) and my dispositions

| Where | Change | Rule it cited | Disposition |
|---|---|---|---|
| Opening ¶ | "such a principle" → "the means principle" | Antecedent | Accepted. Ramakrishnan doubts deeper explanations for his principle and for similar deontological principles (file 01 L237) |
| Opening ¶ | The conditional "If a principle's best version is…" → a flat premise with "so" | Inference marker | Accepted. The clinic states this premise flat (S1) |
| Premise-locations ¶ | "…only spending settles the question for her" → "…settles it" | Concision | **Rejected.** "It" could be read as "the test". Restored |
| Premise 3 ¶ | Split into three paragraphs: the claim, the argument, the owed part with credits | One claim per paragraph | Accepted, with four restorations: "this permission **not to give**" (the fixed term the later paragraphs rely on must be introduced here); the bridge "The permission's point explains why." (without it the Walen quotation reads as a non sequitur); "settling only who does the taking" (the rewriter's "who takes it" had an ambiguous "it"); "pair the permission with the principle in the same way" (the rewriter's "the two" had no clear antecedent) |
| Quong ¶ | "Read as…" → "On one reading… On another reading…", main clause first | Sentence order; parallel form | Accepted |
| Reply ¶ | Semicolons → full stops; "is not my rationale" | Concision | Accepted. "what she must bear" → "what a person must bear" (antecedent) |
| Premise 4 ¶ | Split into three: mechanism; scope and complaints; Steinhoff | One claim per paragraph | Accepted. Two corrections: "Not all harms are covered" → "The permission does not protect against every harm" (the rewriter's version did not say what does the covering); "The complaints differ accordingly." restored as the bridge to the contrast |
| Premise 4 ¶ | The two rhetorical questions flattened ("This is because…"; the question about all harms removed) | Question pivot answered flatly | Accepted. This uses up §3's sub-dialogue allowance with no loss |
| Thomson ¶ | "…; turning…" → "…, but turning…" | Disambiguates "serve" | Accepted |
| Ramakrishnan ¶ | Split into objection and reply; "strikes him as" → "he finds" | One claim per paragraph; plain verb | Accepted |
| Ramakrishnan ¶ | "It does so in a fine-grained way: his principle lets…" → "His own principle is fine-grained too. It lets…" | Antecedent | **Rejected: changes the point.** The rewrite reads as a tu quoque ("his principle has the same fault"). Ramakrishnan himself notes the fine grain as a cost of his own principle (file 01 L275). Restored as "It does so in a fine-grained way, as Ramakrishnan notes of his own principle, which lets…" |
| Reply ¶ | "the test for being made to give has this shape" → "The test has this shape" | Concision | **Rejected.** This is the rewriter's flag 1: the reader cannot tell whether "the comparison with alternatives" and "replacement" are one test or two. Rewritten to name both as the view's two features, in the terms of §2: "judging supply against the agent's alternatives … and the replacement test …" |
| note 9 | "Lazar … grounds … similarly" | Concision | **Rejected** as vaguer. Restored "in the same considerations" |

## Flags the rewriter raised, and what I did

1. **Are "the comparison with alternatives" and "replacement" one test or two?** They are the view's two features, as §2 names them. The sentence now says so, in §2's terms (see the table).
2. **Nine body paragraphs became fourteen.** Accepted: each new paragraph carries one claim. The rhythm will be checked at 7c.
3. **Is "Uwe Steinhoff" his first mention?** Checked: yes, §3 is his first mention. Ramakrishnan is introduced in full in §1.
4. **Length: 3.8% shorter.** Accepted. After my restorations the section is 9 words shorter than its input. 7b owns the cut.
