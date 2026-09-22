# Stage 7a — sections 4–6: rewriter change table and dispositions

- **Rewriter.** A prose-rewriter subagent (sonnet tier), fresh context. It was given only `Scrap/7a-input-s4-s6.md`, a one-sentence thesis, a short glossary of terms from earlier sections, the register-sample paths, and hard constraints: no growth in length, quotations and citations fixed, case names fixed. It calibrated on model-paragraphs, the Style Guide, prose-principles, ai-tells and the two register samples.
- **Its text** is in `Scrap/7a-output-s4-s6 (rewriter text).md`: 1,927 words, from 1,948, which is 1.1% shorter.
- **The text I applied** is `Scrap/7a-applied-s4-s6.md`: 1,969 words, after the dispositions below.
- **Its self-report.** It checked mechanically that quotations, citations, footnote markers and `[p.]` counts are unchanged.

## The rewriter's changes (condensed from its table) and my dispositions

| ¶ | Change | Rule it cited | Disposition |
|---|---|---|---|
| §4¶1 | "adapting a case of Tadros's" → "adapting Tadros's case"; the verdict sentence split from the contrast case; the semicolon before Parry's reply split | Concision; unpack | Accepted. "refrains so his body will stop" → "so that" (purpose, not consequence) |
| §4¶2 | Wholesale unpacking; "whether it serves at that cost" → "whether serving is worth that cost"; "Were X supplied" → "If X supplied" | Unpack; term check | Accepted, except that ";" becomes ", so" before "his paralysis is the cost…" (restores the inference), and "so his body serves" → "so that his body serves" |
| §4¶3 | "without strain" → "too"; "a pair of cases" → "two cases" | Concision | Accepted |
| §4¶4 | "avoids the costs Parry finds" → "the difficulties" (avoids a pun on the essay's term "cost"); colons split | Term check | Accepted |
| §4¶4 | "the duties that bound the principle" → "the duties the principle imposes" | Ambiguity | **Rejected: changes the claim.** The duties are inputs that set the principle's bound, not duties the principle imposes. The ambiguity is fixed instead: "the duties that set the principle's bound" |
| §4¶5 | Vase case split into a supposition and its analysis | Unpack | Accepted |
| §5¶1 | *Loop* split into short sentences; Choo's robustness points split | Unpack | Accepted. The colon makes the unprimed data the control for order effects, which matches Choo (file 28 L153) |
| §5¶2 | Kamm attribution moved out of a mid-clause interruption; "The same comparison…" | Unpack; antecedent | Accepted |
| §5¶3 | Otsuka paragraph split at its joins; "Otsuka calls it 'morally indistinguishable'" makes the attribution explicit | Unpack | Accepted |
| §5¶4 | "Neither point reaches the chain, which…" split into two sentences; "the principle that explains the wider set … forbids diverting" → "The principle that forbids diverting also explains the wider set…" | Unpack | Accepted in part. The split is kept. The last sentence is rewritten to keep the inference explicit: "…and has an independent rationale, so it is the verdict on *Loop* that should yield" |
| §5¶5 | Split; "in need of rescue" → "needing rescue" | Unpack; concision | Accepted |
| §5¶6 | Three-verb sentence split | Unpack | Accepted, with "refrains, so his body will stop" → "refrains so that his body will stop" (purpose) |
| §5¶7 | "used in choosing" → "exercised in choosing" (avoids a clash with the rival term "use"); the ellipsis filled | Term check; unpack | Accepted. "He acts permissibly" → "On the view, he acts permissibly", to mark the verdict as the view's |
| §5¶8 | Colon split; "the content of duty" → "duty's content" | Concision | Accepted |
| §6 last sentence | "the price of what it gives" → "the cost of what it supplies" | Term check (no variation on the key terms) | Accepted: the landing now uses the argument's own terms |
| notes 12, 14 | Colon split; subject un-buried; "give" → "supply" | Unpack; term check | Accepted |

## Flags the rewriter raised, and what I did

1. **Length: 1.1% shorter, not 5%.** Accepted. The 7b condense pass owns the cut.
2. **"a prior right to be rescued" is used cold in §4¶1.** Fixed by glossing Quong's condition in his words: his principle "does not prohibit failures to save a victim unless the victim has a right to be rescued or provided with resources" (file 09 L249).
3. **"the ordinary duty of easy rescue" is undefined.** No change. It is a standard phrase whose meaning ("rescue at little cost") is on its face; the thesis's bound introduces duties generally.
4. **Note 12 (only the supplied part of a good is disabled).** This is known and flagged as undeveloped by design. Left for the referee loop.
5. **Two substance-adjacent edits** ("costs" → "difficulties"; the final sentence). Both were checked; neither changes a claim.
