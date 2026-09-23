# Stage 7a (second pass) — section 2: rewriter failure and self-edit record

- **Rewriter.** A prose-rewriter subagent (sonnet tier) was launched on `Scrap/7a2-input-s2.md` with the same brief as §3 and §§4–5. It **failed**: the run stopped with an API error when one response passed the 64,000 output-token limit, and it wrote no files. This is the same failure the first 7a pass met on §§1–2.
- **Decision.** I did not re-run it. The other two rewriters cost about 244k and 287k tokens, a rerun risked the same failure, and §2 had already received the direct structural fixes. Instead I did a self-edit pass on §2 on the rewriter's brief: the cold readers' stumble list for §2, one move per sentence, fixed terms, and no growth. The round-8 cold read checks the result, which is the test the 7a pass exists to pass.
- **Applied text:** `Scrap/7a2-applied-s2.md`, 1,458 words from 1,465.

## Changes

| ¶ | Change | Why |
|---|---|---|
| 1 | "That is exactly what persons are said not to be" → "That is what persons…" | Trim |
| definition | The sentence "A loss she is duty bound to bear for the good may be imposed, and so may a loss she agrees to bear." cut. Note 2's marker moves to the definition sentence's "beyond what she owes or agrees to bear" | It restated the display's bound. Note 2 (consent as an exception) attaches to "agrees to bear" |
| absence tests | The pill sentence split: "She also happens to lie on a pill that would cure the five. So the five could be saved in her absence, and an absence test finds nothing amiss." | One move per sentence (case load, rounds 5 and 7) |
| absence tests | The aside "Is it just another counterfactual test? It is, but it varies only the source…" becomes "The replacement test is counterfactual too, but it never removes her, so it never has to say what would fill the place she leaves empty." | Shorter, with the same claim; pays for the unpacking |
| second feature | Introduced by its fixed name: "…as important as the first: judging supply against the agent's alternatives. What a person supplies is measured against what the agent could otherwise do, not against her absence." The reason is now split into two sentences ("The reason is that the view concerns justification. A justification is a reason for one option rather than another."). The case is tied to its setting: "Take the diversion case, and suppose six people stand behind the man on the side track…" | The one-read mismatch in rounds 5 and 7 (the feature absorbed into the test). The split also breaks a lint run of four sentences of the same length |
| Alexander | "The six's escape comes from the man's body, so Alexander leaves it out. He then reckons the diversion as if the trolley would run on into the six, and so forbids it…" | Round 7 L41: the causal chain, set out in steps |
| pairs | "The patient left untreated so that the tests can run" ("the" added). A trial version naming both members of Ramakrishnan's pair was withdrawn: it cost ten words and nobody had stumbled there | Precision |
| flamethrower | "Absence tests also err in the other direction, forbidding what is permissible, as a case from … shows"; "So a view that weakens a bystander's claim only when his presence costs the defender something gives his claim full weight here, and forbids her act." | Round 7 L45: which direction, and why his claim keeps full weight. This finishes the direct rewrite made at the start of v1.11 (nineteen others restored; note 6 cut) |
