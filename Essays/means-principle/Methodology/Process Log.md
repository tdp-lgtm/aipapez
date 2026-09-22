# Process Log — means-principle

Append-only session log; see Playbook/3. Methodology Protocol.md for the entry template.
Verbatim human messages; AI actions; models; candidate counts; selections; compliance
flags; approximate cost. This log is the compliance evidence and the raw material for the
methodology report.

## [2026-09-22] Session 1 — Stage 0 Setup
- **Surface:** Claude Code remote session (claude.ai/code), branch `claude/means-principle-paper-4w3jo1`.
- **Models/agents:** Claude (Claude Code remote session); no subagents yet (paper-auditor to be
  spawned for the Setup gate).
- **Human messages (verbatim):**
  > New Paper (2)!  Your aim is to write a philosophy paper developing a new and novel version of the
  > Means Principle. I've added here a big list of papers to give you an idea of the literature and
  > the kinds of puzzles and counterexamples facing various attempts to come up with a Means
  > Principle. Your task is, as said, to develop a new version of the principle. You're free to
  > choose which path to take. You're free to ask me for more readings to help you. I would suggest
  > doing the reading of the md file before going too far with developing a view on it. Remember
  > that the view also needs to be responsive to what the Means Principle is supposed to do in moral
  > philosophy; not just an ad hoc list of conditions. Feel free to be creative as well and draw on
  > other literatures, etc.

  (Attachment: one Markdown file, `AI_Drafter_Means_Principle.md`, ~840 KB, a concatenation of
  roughly a dozen papers and book chapters on the Means Principle. Stored unchanged as
  `Background Readings/AI Drafter Means Principle.md`.)

  Intake answers (given via the interactive question menu; custodian's selections):
  > Slot: "Slot 2; both continue"
  > Autonomy: "Default stops (Recommended)"
  > Runway: "Quality first"
  > OpenReview: "Not yet"
- **AI actions:** Read CLAUDE.md, Competition Brief, Rules — Human Involvement, DIGEST, the full
  Pipeline, Methodology Protocol, Essay Project Template, Literature Access Protocol. Checked essay 1's
  state (Stage 8, awaiting custodian read) to set the slot question. Skimmed only the heading
  structure of the attached file to frame the intake (no substantive reading yet). Ran the bounded
  intake (topic already supplied; asked slot/autonomy/runway/OpenReview only; no thesis or arguments
  requested). Scaffolded `Essays/means-principle/` with new_essay.py. Copied the attachment into
  `Background Readings/`. Wrote `Brief/Intake.md`. Reminded the custodian about OpenReview lead time
  (not yet registered) and chat-log retention.
- **Selections:** Custodian chose the topic and task type (permitted) and the four intake options
  above. No philosophical content selected or supplied.
- **Tools/retrieval:** Local file reads, grep over the attachment's headings, the scaffold script.
  No web retrieval yet.
- **Compliance flags:** none. Assessment of the topic message, clause by clause (recorded because
  it contains more than a bare topic):
  (1) "develop a new and novel version of the Means Principle": debate + task-type specification;
  the custodian supplies no content for the version. Permitted ("choosing a topic, question,
  debate"). (2) The attached literature: "providing a body of literature for the AI to analyse";
  breadth check passed (about a dozen works from several rival camps), and the AI will search beyond
  it and log those searches. (3) "the view also needs to be responsive to what the Means Principle is
  supposed to do in moral philosophy; not just an ad hoc list of conditions": a generic
  methodological desideratum (explanatory grounding rather than ad hoc extensional fit), of the same
  kind as "defend your premises"; it names no thesis, premise, distinction, case, or diagnosis.
  Permitted, recorded, not flagged. (4) "Feel free to be creative ... draw on other literatures":
  generic. Permitted.
- **Approx. cost/time:** Human: ~3 minutes (topic message, file upload, 4 menu clicks). Machine:
  ~15 min wall clock so far.
- **Setup gate:** paper-auditor ×1 (haiku tier, background) — "VERDICT: APPROVE — Stage 0's claimed
  work is genuinely done (files confirm it); the agent may proceed to Stage 1 (Idea generation &
  selection)." Pasted into the Checklist.
