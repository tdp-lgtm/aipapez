# Stage 7a (second pass) — sections 4–5: rewriter changes and dispositions

- **Rewriter.** A prose-rewriter subagent (sonnet tier), fresh context. It saw only `Scrap/7a2-input-s4-s5.md`, the thesis, context glosses (including premises 3 and 4 verbatim), the cold readers' stumble list for §§4–5 (rounds 5–7), the register-sample paths and the hard constraints.
- **Its text:** `Scrap/7a2-output-s4-s5 (rewriter text).md`, 1,742 words from 1,804 (3.4% shorter). Its memo: `Scrap/7a2-changes-s4-s5 (rewriter memo).md`.
- **Applied text:** `Scrap/7a2-applied-s4-s5.md`, 1,789 words after the dispositions below (15 fewer than the input).
- **Cost:** about 287k tokens (23 tool uses).

## Dispositions

| ¶ | Rewriter's change | Disposition |
|---|---|---|
| §4 ¶1 | The case trimmed ("slides on ice into the path of a trolley that will otherwise paralyse five people") | Accepted |
| §4 ¶1 | "His body would slow the trolley, saving the five, but paralysing him." | **Rejected.** It put a "but" next to the following sentence's "but". Original restored |
| §4 ¶1 | "…but she refrains so his body will stop the trolley" | Accepted, with "so that" (purpose, not result) |
| §4 ¶1 | "That refusal seems wrong. Compare two trolleys, one toward the man, one toward the five, …; letting the man be hit is permissible." | **Rejected.** It makes a new four-word sentence, and "the man"/"the five" wrongly makes the two-trolley case involve the same people (the rewriter's flag 2): in Parry's case they are different people. Original restored |
| §4 ¶1 | "Quong's principle permits a failure to save a victim 'unless…'" | **Rejected.** "Permits … unless" says more than Quong's "does not prohibit … unless", which is the sentence the quotation comes from (file 09 L249). Restored |
| §4 ¶1 | Parry's claim in its own sentence with its own citation (the rewriter's flag 1); "Put the two together: on Quong's principle, nothing condemns …, yet it is wrong." | **The separate sentence and citation are accepted.** It keeps "would extinguish" (Parry's conditional form, file 06 L91). **The imperative colon-lead is rejected**; the synthesis is now its own plain sentence: "So Quong's principle cannot condemn the passer-by." Now the paragraph runs Quong's claim, then Parry's claim, then the consequence, then what is needed, one move per sentence. This is the fix for the three-party stumble flagged in rounds 5–7 |
| §4 ¶2 | "By letting the man suffer the paralysis so his body serves, the passer-by settles for him…" (agent made explicit) | Accepted, with "so that" |
| §4 ¶2 | "An account that locates the wrong in compulsion cannot cover omissions" | Accepted |
| §4 ¶2 | "therefore" cut; "all the same" cut | "Therefore" restored (it marks the inference); the cut of "all the same" accepted |
| §4 ¶3 | "the only driftwood"; "The first seems permissible, the second not" | Accepted |
| §4 ¶4 | "The view avoids Parry's difficulties with Quong's extension…"; "the switch turning a trolley"; "either" cut | **The first is rejected**: it reads as difficulties Parry himself has. Restored "The view also avoids the difficulties Parry finds in…". The rest accepted |
| §5 ¶1 | "looping back"; "judge diverting permissible"; "holding even when shown first" | First two accepted. **The third is rejected**: "shown first" has no clear subject. Restored "holding when no other case is shown first". "Argues that" and "see that" restored for register |
| §5 ¶2 | "a stopper before him"; "Frances Kamm tries to separate the cases: in diverting, …" | First accepted. **The second is rejected**: with "She argues that" gone, Kamm's claim could read as the essay's own. Attribution restored |
| §5 ¶3 | "thus" cut; "against the intuition" cut | "Thus" cut accepted. **"Against the intuition" restored** (it says what Otsuka's argument is for) |
| §5 ¶4 | "already" cut from "the man already stands on the loop" | **Rejected.** "Already" marks the step's one change (he is there from the start, not toppled). Restored |
| §5 ¶5 | "…would need a principled difference; none has been found." | Accepted |
| §5 ¶5 | "It means giving up the verdict on the toppling case or the principle that explains it, the footbridge case, and the other pairs of section 2." | **Rejected: changes the claim.** As a list it says the footbridge case itself would be given up. The original also has the counterfactual "would", since only keeping the *Loop* verdict would mean this. Restored, with "single" in "the single verdict on *Loop*" |
| §5 ¶6 | "a man lying across the only road"; "since the driver intends the car's lethal action" | First accepted. **The second is rejected** (the rewriter's flag 3): "an action of the car that will kill the man" follows the Quinn formulation the citation supports. Restored |
| §5 ¶7 | "a rescuer willing to lose an arm"; "refrains, so his body will stop the trolley"; "the two are the same conduct" | First and third accepted. **The second is rejected: it inverts the case.** Her refusal is for the purpose of the stopping, not followed by it. Restored "refrains so that his body will stop the trolley" |
| §5 ¶8 | Wholesale: "The view can tell the refusals apart. Premise 3 explains why. … So what the permission … protects is her answer to that question, and it justifies an act only when the act is itself that answer." "A prerogative points the same way"; "weight she withholds"; "though his motive is vicious"; "therefore" cut | **The derivation is kept, but not as an entailment.** The rewrite presents the assumption as following from premise 3. It does not strictly follow, since a permission to refuse might cover refusals made for any reason. So the essay keeps its honest framing: "on one assumption: that the permission not to give justifies an act only when the act is the agent's answer to the question that premise 3 makes hers. Premise 3 supports the assumption. It gives her the standing to settle, by agreeing or refusing, whether … so what the permission protects is her answer to that question." This keeps the rewriter's clearer chain of steps, and names the premise-3 question in the assumption itself, so the support is visible. **"Premise 3 explains why." rejected** (a new four-word sentence). **"Though his motive is vicious" accepted**; it fixes the round-7 register bump. "The nature of a prerogative" and "weight she does not give them" restored (plainer than "withholds"; the rescuer does not weigh her arm at all). "Therefore" restored |
| note 8 | "Of a man whose body would stop a trolley" | Accepted |
| note 9 | "the other four could still justify diverting" | **Rejected.** People do not justify; their lives do. Restored "the other four lives" |
| §5 ¶2 | The citation-authority sentence ("Otsuka and Choo reject…") left alone, as asked | No change |

## The rewriter's flags

1. **Where Parry's citation goes.** It goes on his claim's own sentence (accepted).
2. **"The man"/"the five" in the two-trolley case.** Rejected: that case involves different people.
3. **"The car's lethal action".** Rejected: the original follows Quinn's formulation.
