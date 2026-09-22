# Blind referee templates — competition edition

Rules that make a prompt genuinely blind:

- Give the referee ONLY: its disciplinary lens, the venue description (fixed below), and the
  manuscript file path.
- NEVER name the essay's own design features, arguments, or terminology in the prompt (naming the
  literatures that define the LENS is fine; naming what the ESSAY does is not).
- Fresh agent instance every round; never show prior reports.
- Round 2+ adds one case-for-acceptance reader.
- Rounds iterate to convergence — the loop and its stopping rule live in Pipeline Stage 9. A
  desk-reject screen (editor persona) precedes round 1; the pre-submission readiness check = one
  simulated AI screening (grading strictly by the six published criteria) plus one blind generalist
  read after Stage 10.

The `{VENUE}` slot is always filled with:

> the AI Philosophy Competition — essays judged by a panel of academic philosophers on clarity,
> quality of argumentation, significance, originality, engagement with the literature, and accuracy
> and scholarship; max 6,000 words

Per-essay slots are `{LENS FIELD}`, `{LENS DOCTRINE LIST}` (the literatures the lens brings — NOT the
essay's uses of them), and `{MANUSCRIPT PATH}`. The standard trio for a philosophy essay: (1) a
specialist in the essay's sub-field (the hostile expert); (2) a broad philosophy generalist
gatekeeper; (3) a foundations/adjacent specialist who pressure-tests the deepest commitments.

Track convergence across rounds in `WIP Docs/Referee Reports/`: one line per concern, which rounds
raised it, cleared/open. Convergence across fresh readers is the readiness signal.
