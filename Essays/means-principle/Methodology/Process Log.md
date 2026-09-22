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

## [2026-09-22] Session 1 (cont.) — CHECKPOINT 1 (thesis selection)
- **Models/agents:** Claude (Claude Code remote session). No subagents this segment.
- **Human messages (verbatim):**
  > (via the interactive menu, question "Which thesis should this essay develop?", free-text answer)
  > "A sounds most interesting but please explain the two caveats in more details before proceeding"

  > (via the interactive menu, question "With those caveats in view, how should I proceed?")
  > "Go ahead with A (Recommended)"
- **AI actions:** Presented the four ranked sketches in plain English (A Spending View, recommended;
  B Keeping and Taking; C Jurisdiction View; D Levers). At the custodian's request, explained the two
  caveats flagged in Sketch A (AI-authored explanation): (1) overlap with Ramakrishnan's Utility for
  harms to persons, and how the essay would handle it (state it up front; rest originality on the
  rationale, the property scope, the duty-bounded "disabling" structure, and the use/spend
  distinction; read Walen 2016/2022, Øverland 2014, Alexander 2016 to confirm); (2) the Loop verdict
  (why the view cannot permit Loop without permitting a trapdoor Bridge; how it would be defended; the
  Choo 2025 risk). Offered a follow-up choice (proceed with A / switch to B / switch to C or D). Saved
  the selected sketch to `Brief/Argument Sketch.md`. Reminded the custodian about OpenReview.
- **Selections:** Custodian selected Sketch A (the AI's top-ranked option) from 4 AI-generated sketches.
  The custodian's first message asked for an explanation of caveats the AI itself had flagged; it
  supplied no philosophical content.
- **Tools/retrieval:** none this segment.
- **Compliance flags:** none. The first message is a request for clarification of AI-generated
  material (permitted: "asking the AI to ... expand on this point"); the second is a selection among
  AI outputs (permitted).
- **Approx. cost/time:** Human: ~3 minutes (reading summaries, two menu answers). Machine: ~10 min.

## [2026-09-22] Session 1 (cont.) — Auditor gate: Idea Selection
- **Models/agents:** paper-auditor subagent (haiku tier), fresh context; asked to verify the Stage 1
  rows against the files on disk (candidates, logged searches, sketches, Checkpoint 1 log and
  compliance).
- **Human messages (verbatim):** none this segment.
- **AI actions:** Ran the gate; recorded the verdict on the Checklist.
- **Result:** "VERDICT: APPROVE — Stage 1 (Idea Selection)'s claimed work is genuinely done (files
  confirm it); the agent may proceed to Stage 2 (Literature Review)." The auditor reported no
  discrepancies (12 candidates; 33 numbered searches; 4 ranked sketches with premise-form arguments,
  objections, cruxes; both CP1 messages verbatim; no philosophical substance in custodian input).
- **Compliance flags:** none.
- **Approx. cost/time:** Human: 0. Machine: ~2 min (auditor ~45k tokens, 16 tool calls).

## [2026-09-22] Session 1 (cont.) — Stage 2 opens: literature search and source requests
- **Models/agents:** Claude (Claude Code remote session). No subagents this segment.
- **Human messages (verbatim):** none this segment.
- **AI actions:**
  - Re-read Pipeline Stage 2 and the Literature Access Protocol.
  - Re-read Ramakrishnan's key cases (Heart Attack\*\*, Room, Drowning, Six Heart Attacks; file 01
    L107–175) against the Spending View's test: all sorted as intended; noted that the Tracks case is
    handled without a special clause if "supplying a good" is read relative to the agent's actual
    alternatives (to be worked out in the crux memo).
  - Fetched and read a publicly posted, abridged course copy of Quinn 1989 (saved with provenance as
    `Converted text/12 Quinn 1989 (abridged…).md`). Finding (AI's own reading): Quinn's rationale for
    the DDE already contains the idea that people "usefully involved ... only at the cost of"
    something protected by their rights should serve only voluntarily, with an exception for strong
    obligations. Consequence for originality: Quinn is the ancestor of the Spending View's rationale
    and must be credited; the essay's originality claim must rest on what Quinn lacks (an objective,
    victim-centred test that handles omissions such as Ramakrishnan's Heart Attack, which Quinn's own
    counterfactual gets wrong; the property scope; the rescue-rights role; the derivation from the
    prerogative).
  - Found an independent practice that draws the Spending View's line: research-ethics guidance on
    placebo controls (Millum & Grady 2013, condition that participants not "forgo treatment they
    would otherwise receive"; Declaration of Helsinki placebo paragraph), and randomization under
    scarcity. Candidate evidence against the "arbitrary causal structure" worry.
  - Found prior work on the prerogative-to-restriction inference (Mack 2005; cf. Muñoz 2021; Lazar
    2019; Scheffler's asymmetry thesis), which bears on the rationale planned for the crux memo.
  - Wrote the prioritized request table in `Background Readings/REQUESTS.md`: 10 must-have and
    8 nice-to-have sources, one line each on why, with free links where known.
- **Tools/retrieval (numbering continues from Stage 1):** (34) "means principle" 2025–2026 [no new
  MP work found]; (35) Choo 2025 [title and pages confirmed, PPR 111(1): 195–215]; (36) Liao & Barry
  2020 [title confirmed; Walen 2022 reply]; (37) Alexander 2016 [confirmed; MP forbids using others'
  bodies, labors, talents, or rightful resources without consent; "jurisdictional limitation on the
  reach of strong (legitimately enforceable) moral obligations" (search summary)]; (38) WebFetch
  digital.sandiego.edu [EGRESS_BLOCKED]; (39) WebFetch onlinelibrary.wiley.com [EGRESS_BLOCKED];
  (40) opportunistic/eliminative 2024–2025 [Lazar 2015 *Sparing Civilians* chapter; nothing new on
  the MP]; (41) "harmful use" 2024–2025 [no hit]; (42) Øverland 2014 abstract [victim-centred;
  circumstances of those harmed]; (43) Quinn 1989 [record and course copies]; (44) WebFetch of the
  MIT course copy of Quinn [PDF obtained, abridged; text extracted]; (45) Otsuka 2008 [confirmed; LSE
  eprint]; (46) Liao, Wiegmann, Alexander & Vong 2012 [confirmed; Loop intuitions vary with context];
  (47) Lazar 2019 [confirmed]; (48) mere means + placebo + scarcity [Millum & Grady's four cases;
  Helsinki]; (49) "need not give"/"may not take" + prerogatives [SEP entry; Mack 2005 abstract];
  (50) prerogatives, restrictions, hybrid theory [Scheffler's asymmetry thesis]; (51) Millum & Grady
  2013 [confirmed; condition (4) quoted in search summary]; (52) randomization under scarcity (Ebola,
  COVID) [randomization defended as equitable allocation of scarce products that also yields data];
  (53) Muñoz 2021 [confirmed; PPR 102(3): 608–623]; (54) Mack 2005 [abstract: the prerogative's
  rationale is unsatisfied without restrictions]; (55) WebFetch philarchive.org [EGRESS_BLOCKED];
  (56) prerogative grounds the MP [no hit making this specific link]; (57) Kamm, *Morality,
  Mortality* II, "Prerogatives and Restrictions" [chapter exists; not read]; (58) Thomson 1985
  [confirmed, YLJ 94: 1395–1415]; (59) Kamm 2007 chapters [ch. 4 DDE/DTE, ch. 5; DTE permits Loop];
  (60) Steinhoff 2019 [confirmed, CLP 13(1): 1–25; sceptic about rationales]; (61) Helsinki placebo
  paragraph [text found in search summary]; (62) WebFetch openyls.law.yale.edu [EGRESS_BLOCKED];
  (63) WebFetch psy.vanderbilt.edu [EGRESS_BLOCKED]; (64) Tadros 2020 table of contents [ch. 6 "The
  Significance of Intentions" confirmed = file 02]; (65) Mack 2005 pages [SPP 22(1): 357–393];
  (66) Walen 2019 book [confirmed; ch. 3 on SSRN]; (67) Hecht 2023 [Lisa Hecht, JMP 20(5–6)];
  (68) WMA Declaration of Helsinki 2024 [official page].
- **Compliance flags:** none (no custodian input this segment). The request list was composed
  entirely by the AI.
- **Approx. cost/time:** Human: 0. Machine: ~40 min; 35 searches/fetches.

## [2026-09-22] Session 1 (cont.) — Stage 2: crux memo, Literature Map, lenses E/Ac
- **Models/agents:** Claude (Claude Code remote session). No subagents this segment.
- **Human messages (verbatim):** none this segment. The AI sent the custodian a bundled, plain-English
  request for sources (the REQUESTS list) and an OpenReview reminder; no reply yet.
- **AI actions:**
  - Wrote `WIP Docs/Plan/Crux Memo v0.1.md` (AI-originated), which settles the crux before the Plan:
    - A rationale R: the prerogative over giving assigns each person the trade-off between what she
      supplies and its cost to her; non-hollowness; the exact shape is spending.
    - A precise test: supply relative to the agent's alternatives; existential replacement for cost.
    - A working verdict table over ~34 cases from the corpus.
    - A new treatment of Loop. In Thomson's own stipulation the five's bodies protect the one, so not
      diverting would also spend; when every option spends, the protected claims are weighed, as in
      Switch; asymmetric loops are forbidden.
    - An account of when intentions matter (only where a prerogative is relied on).
    - A list of objections to plan for.
  - Re-read Cullity 2018 (file 11 L171, L233–252, fn 45) and Tadros 2011 (file 03 L85–105, L193–277).
    Finding: both already restrict Thomson's 2008 prerogative argument to using, and Tadros already
    speaks of side-effect victims as not contributing and not required to "expend" their lives. The
    originality claim was narrowed accordingly: the novelty is the scope result (supplying at a
    cost), not the family of argument.
  - Found and saved a complete, publicly posted copy of Thomson 2008 (file 13; journal pagination
    recoverable from running heads). Added it to REQUESTS as #19, marked RECEIVED (no custodian
    action needed).
  - Wrote `WIP Docs/Literature Map/Literature Map v0.1.md`:
    - landscape as two tracks (criterion vs rationale);
    - positions tables;
    - cross-cutting disputes;
    - adjacent literatures (research ethics);
    - the open niche;
    - ranked interlocutors;
    - provisional originality verdict: OPEN with a narrowed claim, with conditions that would close it
      tied to requested sources #1, #3, #5, #7.
  - Ran lenses E and Ac (findings recorded in the Literature Map §6 and on the Checklist).
  - Corrected four source file names after verification (01 Ramakrishnan 2016; 02 Tadros 2020 ch. 6;
    06 Parry 2023; 08 Kahn 2024). Documents cite by file number, so no references changed.
- **Tools/retrieval:** (69) Thomson 2008 bibliographic check [PPA 36: 359–374]; (70) WebFetch of the
  MIT course copy of Thomson 2008 [PDF obtained; text extracted; complete]; (71) search of the same
  course host for further readings [only lecture notes; nothing used].
- **Compliance flags:** none (no custodian input this segment).
- **Approx. cost/time:** Human: 0. Machine: ~1.5 hours (memo and map drafting; re-reading ~15k words
  of corpus).

## [2026-09-22] Session 1 (cont.) — Auditor gate: Lit Review
- **Models/agents:** paper-auditor subagent (haiku tier), fresh context. Asked to verify the Stage 2
  rows against the files on disk, including 5 spot-checks of line references.
- **Human messages (verbatim):** none this segment.
- **Result:** "VERDICT: APPROVE — Stage 2 (Literature Review)'s claimed work is genuinely done (files
  confirm it); the agent may proceed to Stage 3 (Plan)." No discrepancies reported; all 5 spot-checked
  line references were accurate.
- **Note:** while the gate ran, the AI added REQUESTS row 20: paginated originals of five
  already-provided works, for pinpoint quotes; MED priority; not yet pinged. The auditor saw the
  19-row table.
- **Compliance flags:** none.
- **Approx. cost/time:** Human: 0. Machine: ~3 min.

## [2026-09-22] Session 1 (cont.) — Stage 3: Plan v0.1 and the six lenses
- **Models/agents:** Claude (Claude Code remote session). No subagents this segment.
- **Human messages (verbatim):** none this segment.
- **AI actions:**
  - Read the planning guidance: DIGEST (full); Style Guide (apparatus budget, structure, dialectical
    engagement); `Craft/journal-craft.md` (full); `Craft/intro-playbook.md` (full);
    `Craft/moves-catalog.md` Part 1; `prose_lint.py` budget checks.
  - Wrote `WIP Docs/Plan/Plan v0.1.md` (AI-originated):
    - thesis in P/Q/R, compressed, and full (Display 1);
    - the move (supplying vs bearing);
    - why this version is the sharpest, mapped to the functions the corpus assigns the principle (F1–F6);
    - the central argument P1–P4 → C (Display 2) with defense locations;
    - a 7-section plan with budgets summing to 5,650 words;
    - dialectical structure (Loop is the dedicated objection section);
    - apparatus budget (1 named view; 1 coined term; 3 named cases; 2 displays);
    - four Moves Catalog architectures;
    - source dependencies and fallbacks.
  - Ran all six lenses; findings and fixes are recorded in Plan §10. Display 1 and P2 were rewritten,
    and P3 now carries the duty bound. Footnote slots were reserved for Walen's toolkit baseline and
    for Liao & Barry. Parry line references were corrected (L231–259) in the Plan, the Literature Map
    and the Crux Memo.
  - Verified the Plan's line references against the files on disk (Parry L67–105, L121, L171–195,
    L231–259; Christensen L211; Quong L125–127, L299–305).
- **Tools/retrieval:** (72) WebFetch wma.net for the Declaration of Helsinki [EGRESS_BLOCKED; stays on
  REQUESTS #18].
- **Compliance flags:** none (no custodian input this segment).
- **Approx. cost/time:** Human: 0. Machine: ~1 hour.

## [2026-09-22] Session 1 (cont.) — Auditor gate: Plan; Plan v0.2 (post-gate corrections)
- **Models/agents:** paper-auditor subagent (haiku tier), fresh context, for the Plan gate.
- **Human messages (verbatim):** none this segment.
- **Result:** "VERDICT: APPROVE — Stage 3 (Plan)'s claimed work is genuinely done." The auditor:
  - verified every required element;
  - added the budgets up to 5,650 words;
  - confirmed the apparatus is within budget;
  - confirmed the six lens findings;
  - confirmed consistency with Sketch A and the changelog;
  - spot-checked 4 line references, all accurate.
- **AI actions after the gate:** made Plan v0.2 (v0.1 moved to `WIP Docs/Plan/Old versions/`).
  Corrections found while re-checking case sources:
  - The liability case is Tadros 2020's Mines (file 02 L301–305).
  - The sliding-man case is Parry's, adapted from Tadros 2011 p. 122 (file 06 fn 13).
  - §5 adds a reply to Walen's objection that the Means Principle leaves Thomson's symmetric loop a
    tragic dilemma (file 07 L215, fn 35).
  - Costa 1987 added to REQUESTS as #21 (nice-to-have).
  Deterministic self-check: the diff between v0.1 and v0.2 shows exactly these five changes plus the
  title and changelog lines.
- **Compliance flags:** none.
- **Approx. cost/time:** Human: 0. Machine: ~10 min (auditor ~62k tokens).
