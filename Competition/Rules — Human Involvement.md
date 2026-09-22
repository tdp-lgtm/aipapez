# Rules — Human Involvement (the compliance bright lines)

This file governs every interaction between the human entrant (the "custodian") and the AI in this
repository. It is distilled from the competition's Detailed Rules and FAQ (`Source PDFs/`). The agent
reads it at the start of every working session on an essay. Violating it doesn't just risk
disqualification — it defeats the point of entering: the competition measures what the **AI** can do.

## The test

> Did the AI originate and develop **all** the substantive philosophical contributions in the essay?
> Ideas, arguments, theories, distinctions, objections, replies, and other philosophically valuable
> reasoning must come from the AI. Heuristically, **the AI should be the sole author.**

Humans may specify the task, construct the surrounding workflow, select among AI-generated outputs,
and provide generic feedback — then **leave the AI to work out how to solve the problem**.

## Permitted human involvement

- Creating argument-neutral agentic scaffolds or workflows (this repository is one).
- Generating many essays/ideas and **selecting** the best for submission.
- Choosing a **topic, question, debate, text, or philosophical tradition**.
- Specifying a **position to defend or criticise**, so long as the position is not itself a novel,
  substantive philosophical contribution ("Argue for prioritarianism" ✓; "Argue for this new view I
  came up with" ✗).
- Generic methodological instructions: "make the premises explicit," "test whether the argument is
  valid," "compare several possible arguments," "look for counterexamples," "consult the relevant
  literature," "rewrite this part," "rearrange these sections," "write an objections-and-replies
  section," "add a technical appendix," "expand on this point," "consider this author."
- Providing a paper, passage, dataset, or body of literature for the AI to analyse.
- Multi-AI setups: several AIs proposing, criticising, or revising one another's work.
- **Generic criticism** that names a problem without supplying the diagnosis or solution:
  - ✓ "This argument is unconvincing." / "This premise needs more support." / "This section is
    unclear." / "This reply does not answer the objection." / "Consider whether there are
    counterexamples to this theory."
- Asking the AI to check originality, quotations, references, factual claims, or formal reasoning.
- Setting constraints: length, citation style, section structure, intended audience.
- Automated evaluation, search, scoring, or testing.
- Asking the AI to **delete** material.
- Mechanical formatting and submission work.

## Forbidden human involvement

- Supplying an argument, premises, or a novel thesis for the AI to write up.
- Giving the AI a human draft to rewrite, expand, or improve.
- Telling the AI to draw a particular distinction.
- A detailed outline that already embodies the substantive argument.
- Repeatedly steering the AI toward a human's pre-existing argument through hints.
- **Writing or rewriting any passage of the essay** — including adding footnotes, examples,
  objections, or qualifications.
- Curating materials so narrowly that the selection effectively supplies an argument.
- Feedback that contains substantive philosophical insight:
  - ✗ "This reply fails because it overlooks the distinction between X and Y."
  - ✗ "Isn't the following case a counterexample?"
  - ✗ "This premise is false because …"
  - ✗ "The argument would work if you added the following premise: …"
- AI memory or prior conversations containing relevant human-originated philosophical ideas
  (fresh sessions or disabled memory when in doubt; argument-neutral preferences and workflow
  instructions are fine).

## How this repository enforces the rules

1. **The agent guards the line, both ways.** If a message from the custodian contains a substantive
   philosophical idea relevant to a live essay (a premise, a counterexample, a distinction, a
   diagnosis), the agent must **stop, flag it, decline to use it, and record the event in the
   Process Log**. The essay's argumentative content then continues from the AI's own prior state, not
   from the flagged content. This is not rudeness; it is what keeps the essay eligible.
2. **The custodian never types into an essay file.** All essay text, from first outline to final
   bibliography, is written by the AI. The custodian reads, selects among options, gives generic
   feedback in chat, and may ask for deletions.
3. **Everything is logged.** Every session's human messages (verbatim), AI actions, models used,
   candidate counts, and selection decisions go in the essay's `Methodology/Process Log.md` — see
   `Playbook/3. Methodology Protocol.md`. The log is the compliance evidence and the raw material for
   the methodology report. Chat logs are retained.
4. **No prompt injection, ever.** Nothing addressed to an AI reader may appear in any submitted file.
   The finishing pass includes an explicit sweep for anything that could be read as an instruction to
   a screening model.
5. **Anonymity.** No essay or methodology report may contain the custodian's name, affiliation,
   email, or other identifying details. (The repository's own docs may; submitted files may not.)

## Gray areas — how the agent should call them

- Custodian picks among AI-proposed theses, titles, examples, or framings: **permitted** (selection).
- Custodian says "the objection in §4 feels weak": **permitted** (locates a problem, no diagnosis).
- Custodian says "the objection in §4 fails against rule-consequentialists because …": **forbidden**
  (supplies the diagnosis) — flag it, don't use the "because" clause; treat it as "§4's objection
  feels weak" only, and log the flag.
- Custodian supplies a reading list or PDFs on the chosen topic: **permitted**, unless the selection
  is so narrow it amounts to dictating the argument — if it looks that way, the agent widens the
  literature search on its own and notes this in the log.
- When genuinely unsure, treat it as forbidden, flag, and log. An over-cautious log entry costs
  nothing; an under-cautious one can void the entry.
