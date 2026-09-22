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

## [2026-09-22] Session 1 (cont.) — Stage 1 reading of the provided corpus; Idea Generation
- **Models/agents:** Claude (Claude Code remote session). Subagents: paper-auditor ×1 (haiku tier) for
  the Setup gate (logged above). No subagents used for reading or idea generation: the main agent read
  every provided work itself.
- **Human messages (verbatim):** none this segment.
- **AI actions:**
  - Split the custodian's attachment into 11 per-work files in `Background Readings/Converted text/`
    (line ranges recorded in the file names' source; word counts 7.7k–17k each, ~142k words total).
  - Read all 11 works in full (Quong 2020 ch. 7; Parry 2023; Tadros 2011 ch. 6; Tadros ch. 6 of the
    war book; Ramakrishnan 2016; Walen 2014; Cullity 2018 ch. 10; Parfit 2011 ch. 9; Guerrero 2014;
    Kahn 2024; Christensen 2026). Wrote structured notes per work plus a cross-corpus synthesis
    (functions of the Means Principle F1–F6; unmet demands D1–D6; recurring unexploited ideas) in
    `WIP Docs/Literature Map/Reading Notes — Provided Corpus.md`.
  - Generated 12 thesis candidates (C1–C12), each with the P/Q/R one-sentence test, contribution type,
    originality hypothesis, and case verdicts (`WIP Docs/Candidates/Thesis Candidates v0.1.md`).
  - Stress-tested the flagship (C1, the Spending View) against ~40 corpus cases. Negative result logged:
    a first reading of its replacement test permitted Loop but also permitted a trapdoor version of
    Bridge (clear counterexample); the test was re-specified (existential reading), and C1 now condemns
    Loop. Also killed C11 (counterexample: an any-body Bridge) and C12 (general average does not track
    the means/side-effect line; compensability ≠ permissibility); C8 reduced to an illustration.
  - Pre-screen verdicts: 4 advance (C1, C3, C2, C6), 5 merged into C1 (C4, C5, C7, C9, C10), 3 killed
    (C8, C11, C12).
  - Wrote 4 ranked Argument Sketches with central arguments, main objections, and cruxes
    (`WIP Docs/Candidates/Argument Sketches v0.1.md`): A Spending View (recommended), B Keeping and
    Taking, C Jurisdiction View, D Levers.
- **Selections:** none yet (Checkpoint 1 pending). AI ranking: A > B > C > D.
- **Tools/retrieval:** WebSearch ×33 (WebFetch blocked: `philpapers.org` → EGRESS_BLOCKED; same
  environment limit as essay 1). Queries, in order: (1) "The Scope of the Means Principle" JMP symposium
  [→ Parry 2023, JMP 20(5–6): 439–460]; (2) "Consent and the Mere Means Principle" JVI [→ Kahn 2024,
  JVI 58(3): 515–533]; (3) Tadros "To Do, To Die, To Reason Why" "The Significance of Intentions"
  [book confirmed; chapter not confirmed]; (4) "means principle" harmful use new account 2023–2025;
  (5) means principle + Raz "normal justification thesis" [no hit]; (6) DDE/means principle + unjust
  enrichment/restitution [no hit]; (7) agent-centred prerogative + right reasons/motive + means
  principle [no hit]; (8) "forced gift"/"involuntary sacrifice" + means principle [no hit];
  (9) means principle rationale (PhilPapers/PhilArchive domains); (10) Walen "Restricting Claims
  Principle Revisited" [→ L&P 35 (2016) 211–247; "toolkit baseline"]; (11) Kaczmarek & Lloyd 2025 AJP
  [not relevant]; (12) Sinclair & Quong "Still in Need of a Rationale" [unpublished; no hit];
  (13) Liao & Barry critique [→ L&P 39 (2020) 503–526]; (14) replies to Ramakrishnan; (15) trespass/
  nuisance and Calabresi–Melamed + means principle [no hit]; (16) prerogatives "for the right reason";
  (17) abuse of rights + prerogative; (18) Walen toolkit + Liao & Barry on property; (19) Hecht
  "Activating the Right to Be Rescued" [JMP symposium]; (20) pre-emption/authority + using persons
  [no hit]; (21) Ripstein usurpation; (22) "not made legal by what it turns up" + moral philosophy
  [no hit]; (23) hostage/terror/sanctions leverage + means principle [no hit]; (24) Scheffler
  prerogative + motive; (25) Kamm PPH/DTE + Otsuka + Loop; (26) Kant price/dignity + means principle;
  (27) Walen 2022 reply [→ L&P 41 (2022) 627–638]; (28) Choo 2025 [→ PPR 111 (2025) 195–215: no
  defence of the MP/DDE against Loop succeeds]; (29) "harmfully using" 2022–2025; (30) beneficiaries
  owe restitution for use [no hit]; (31) "substitute"/replacement test + Loop + Kamm substitution
  [Kamm's substitution/subordination distinction is different]; (32) Øverland "Moral Obstacles"
  [→ Ethics 124 (2014) 481–506, victim-centred]; (33) Alexander "The Means Principle" [→ 2016; frames
  the MP as "a jurisdictional limitation" — lowers C2's originality].
- **Compliance flags:** none (no custodian input this segment).
- **Approx. cost/time:** Human: 0 minutes this segment. Machine: long segment (~2.5–3 hours wall
  clock); reading ~190k tokens of source text plus notes, 33 searches.
