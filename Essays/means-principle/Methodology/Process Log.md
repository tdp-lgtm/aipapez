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

## [2026-09-22] Session 1 (cont.) — CHECKPOINT 2 presented (paused)
- **Models/agents:** Claude (Claude Code remote session).
- **AI actions:** presented a plain-English summary of Plan v0.2 in chat and offered two menus. The
  first asked how the plan looked (approve / unclear / too ambitious / needs more support). The
  second offered a choice of opening (two clinical trials, recommended; or the literature's classic
  pair).
- **Human messages (verbatim):** the custodian dismissed both menus. The interface recorded:
  "[User dismissed — do not proceed, wait for next instruction]".
- **Selections:** none. Work paused at Checkpoint 2, awaiting the custodian's instruction. No further
  essay work done.
- **Compliance flags:** none.
- **Approx. cost/time:** Human: <1 min. Machine: ~2 min.

## [2026-09-22] Session 1 (cont.) — Custodian uploads requested readings; instruction to read and rethink
- **Models/agents:** Claude (Claude Code remote session).
- **Human messages (verbatim):**
  > @"/root/.claude/uploads/d4f07d39-2820-594b-ad4d-32c4fee8b61e/31bdd5b3-Ai_Means_Principle_Readings_2.md" Here's the md with. ton of the readings you wanted. Read it. I'll give you another chance to step back and rethink what you want to write in this essay once you've digested all these new sources as well.
- **Compliance assessment:** permitted, no flags.
  - Supplying requested literature is permitted ("providing a paper, passage, dataset, or body of
    literature for the AI to analyse"). The list was composed entirely by the AI (REQUESTS #1–#17),
    so there is no curation risk.
  - "Read it" and "step back and rethink what you want to write" are generic methodological
    instructions (compare "consult the relevant literature," "compare several possible arguments").
    They carry no philosophical content.
  - This message also answers the dismissed Checkpoint 2 menus: the plan is not approved as it
    stands; the AI is to digest the new sources and reconsider. Stage 3 stays open.
- **AI actions:**
  - Saved the upload as `Background Readings/AI Means Principle Readings 2.md` (1.26 MB,
    ~213k words).
  - Split it into 16 per-work files (`Converted text/14`–`29`) with provenance headers:
    - Walen 2016; Hecht 2023; Steinhoff 2019; Liao et al. 2012; Lazar 2019; Mack 2005;
    - Kamm 2007 chs. 5 and 4; Walen 2022; Thomson 1985; Øverland 2014; Alexander 2016;
    - Quinn 1989 (the same abridged course text as file 12; no journal pagination);
    - Otsuka 2008; Choo 2025; Liao & Barry 2020.
  - Checked for page markers: only the Kamm chapters have them.
  - Updated REQUESTS:
    - Received: #1–#5, #7–#10, #12–#15, #17.
    - Partly received: #6 (Quinn, still unpaginated).
    - Still outstanding: #11 (Millum & Grady), #16 (Walen 2019), #18 (Helsinki), #20 (paginated
      originals), #21 (Costa).
- **Next:** read all 16 works in full, write reading notes, then a rethink memo (whether to keep,
  revise, or replace the Spending View), then return to the custodian with options.

## [2026-09-22] Session 1 (cont.) — Batch-2 reading (16 works) and notes
- **Models/agents:** Claude (Claude Code remote session). No subagents, no web searches.
- **AI actions:**
  - Read all 16 works in `Background Readings/Converted text/14`–`29`.
    - In full: Walen 2016; Liao & Barry 2020; Walen 2022; Choo 2025; Otsuka 2008; Alexander 2016;
      Mack 2005; Liao et al. 2012.
    - Core sections plus searches: Øverland 2014; Thomson 1985; Lazar 2019; Steinhoff 2019;
      Hecht 2023.
    - Targeted, with page markers: Kamm 2007 chs. 4–5.
    - File 26 duplicates file 12 (Quinn, abridged).
  - Wrote `WIP Docs/Literature Map/Reading Notes — Batch 2.md`: one entry per work, each with its
    implications for the Spending View (SV). Re-read Alexander L151–161 and corrected the
    omissions point: the SV's omission structure is Alexander's; the two differ only over which
    duties of rescue exist.
- **Main findings (AI-originated assessments):**
  - **Anticipations.**
    - The rationale family: Alexander 2016's prerogative–MP corollary and "not resources" framing;
      Walen 2022's "patient-analog" of the claim not to make large sacrifices; Mack 2005's
      non-hollowness argument.
    - Parts of the criterion: Walen's tightness test for holdings; Otsuka's intention-based
      *Six Behind One* contrast.
    - The symmetric Loop point: Costa 1987, reported in Otsuka's fn 7.
  - **Retraction found.** Walen 2016 retracts Walen 2014's symmetric-Loop verdict. The Crux Memo
    and Plan v0.2 cite the 2014 view as agreement, so both need correcting.
  - **Loop.** The literature and all the survey data concern the asymmetric Loop (Choo; Liao et
    al.), and Choo's replies to the order-effect argument are strong. The SV must bite the bullet
    on the asymmetric case, by argument. The symmetric point drops to a footnote.
  - **Strongest demonstrations found.** The SV's test sorts:
    - all six of Liao & Barry's counterfactual cases that defeat Øverland's and Walen's views;
    - both of Walen's counterexamples to the absence baseline;
    - *Six Behind One* (against Alexander).
  - **Scope.** Cases where the victim is in the path of the agent's means are not spending and
    must be scoped out: Foot's *Car Rescue*, *Flamethrower 2*, *Rescue Ahead*, Steinhoff's *Car*
    cases.
- **Compliance flags:** none. No custodian input in this segment.
- **Approx. cost/time:** Human: 0. Machine: ~2 h (~500k tokens of reading).
- **Next:** a rethink memo, then options to the custodian.

## [2026-09-22] Session 1 (cont.) — Rethink memo; options presented to the custodian
- **Models/agents:** Claude (Claude Code remote session). No subagents, no web searches.
- **AI actions:**
  - Wrote `WIP Docs/Plan/Rethink Memo v0.1.md`:
    - what the 16 new works changed: anticipations, withdrawn support, new evidence, challenges;
    - originality recalibrated (the rationale family credited; the criterion, its contrastive
      grounding, and the doing-versus-serving distinction claimed);
    - four rejected directions, with reasons;
    - three options with AI estimates against the six judging criteria;
    - a recommendation (A) and next steps.
  - Checked the memo's line references against the files. Corrected two Alexander references in
    the batch-2 notes (L151 and L161, not L153 and L159).
  - Updated the Checklist (rethink row; new open row for the direction choice and Plan re-gate) and
    the Progress Log.
- **Candidates:** 7 directions considered. 4 rejected in the memo: a Loop paper, an omissions
  paper, a two-principles paper, an intentions paper. 3 offered to the custodian:
  - **A:** the criterion the rationale needs; recommended.
  - **B:** the criterion alone.
  - **C:** the rationale made precise.

  All AI-generated.
- **Compliance flags:** none. The custodian will be asked only to select among AI-generated
  options. Their reply is to be logged verbatim in the next entry.
- **Approx. cost/time:** Human: 0 so far. Machine: ~40 min.

## [2026-09-22] Session 1 (cont.) — Direction selected (rethink, Option A)
- **Models/agents:** Claude (Claude Code remote session).
- **AI actions:** summarized the rethink in plain English in chat, then asked one menu question:
  "Which direction should the essay take?" Options, all AI-generated:
  - "A: test + reason (Recommended)";
  - "B: the test alone";
  - "C: the reason alone".
- **Human messages (verbatim):** selected "A: test + reason (Recommended)". No free text.
- **Selection:** Option A of `WIP Docs/Plan/Rethink Memo v0.1.md`: the criterion the rationale needs
  ("Spending Persons", refocused).
- **Compliance flags:** none. A pure selection among AI-generated options, with no philosophical
  content from the custodian.
- **Approx. cost/time:** Human: ~1 min. Machine: ~2 min.
- **Next:**
  1. Literature Map v0.2 and Crux Memo v0.2 (corrections from the batch-2 reading).
  2. Plan v0.3 under Option A.
  3. Six lenses.
  4. Plan gate.
  5. Checkpoint 2.

## [2026-09-22] Session 1 (cont.) — Plan v0.3 (Option A): supporting documents, plan, lenses
- **Models/agents:** Claude (Claude Code remote session). No subagents before the gate.
- **AI actions:**
  - **Crux Memo v0.2** (v0.1 moved to `WIP Docs/Plan/Old versions/`):
    - §0 items 3–5 revised: Loop is now a bitten bullet; originality recalibrated.
    - §1 gains the contrastive grounding of the alternatives clause.
    - §2 gains Steinhoff's challenge and the doing-versus-serving joint, with credits to Mack,
      Alexander and Walen 2022.
    - §3 table: the Loop rows are corrected, and 11 rows are added (Liao & Barry's cases,
      *Six Behind One*, Walen's cases, the sensor case, the person in the path, *Enemy Trolley*).
    - §4 (Loop) is rewritten; §5, §6 (O11, O12), §7 and §8 are updated.
  - **Literature Map v0.2** (v0.1 moved to `Old versions/`):
    - positions tables rebuilt on the texts, with line references;
    - a new dispute, the person in the path;
    - Loop and prerogative disputes rewritten;
    - niche and originality verdict revised to "the criterion the rationale needs";
    - interlocutors re-ranked (Quong and Ramakrishnan close; eight point engagements);
    - lens findings E and Ac.
  - **Plan v0.3** (v0.2 moved to `Old versions/`):
    - thesis rebuilt with the rationale credited;
    - §2 enlarged: contrastive ground, stress test;
    - §3 rebuilt: Quong's dilemma, doing versus serving, Steinhoff;
    - §4 shrunk;
    - Loop ≈450 words inside §5, with the symmetric case in a footnote;
    - a scope objection on the person in the path;
    - budgets sum to 5,450;
    - apparatus unchanged in kind;
    - all six lenses run, with findings in §10.
  - **Correction found while checking pages.** Kamm's "new problem" passage is at file 21
    L61–65, spanning pp. 94–95; the conversion has no page markers for pp. 92–94. It was cited as
    p. 94 alone. Fixed in the Plan, the Crux Memo, the Literature Map and the batch-2 notes.
- **Tools/retrieval** (WebSearch; originality re-checks for the essay's new centre of gravity):
  - (73) "means principle harming as a means baseline agent's alternatives contrastive
    justification counterfactual victim's contribution" [only harm-baseline literature; no
    anticipation];
  - (74) "\"means principle\" \"cost of\" supplying OR contribution \"replacement\" test Liao Barry
    counterfactual victim-centered" [the Walen and Liao–Barry exchange, already read; no
    anticipation];
  - (75) "opportunistic harm \"six behind one\" OR \"tracks\" case means principle alternatives
    baseline 2023 OR 2024 OR 2025" [nothing relevant];
  - (76) "\"means principle\" \"limits of beneficence\" OR \"prerogative\" \"supply\" OR \"serve\"
    side effect Thomson \"Turning the Trolley\" reply Tadros Cullity" [SEP entries only; no
    anticipation of doing versus serving];
  - (77) "deontological constraint \"contrastive\" reasons harming as a means \"relative to the
    alternatives\" Loop trolley objective account" [general sources; no anticipation].
- **Compliance flags:** none. No custodian input in this segment.
- **Approx. cost/time:** Human: 0. Machine: ~1 h.

## [2026-09-22] Session 1 (cont.) — Plan gate (v0.3): REVISE, fixes applied
- **Models/agents:** Claude (Claude Code remote session); paper-auditor subagent for the gate.
  It ran on the **default tier** (the main session's model). No model override was passed at spawn,
  unlike the four earlier gates (Setup, Idea Selection, Lit Review, Plan v0.1), which ran on the
  haiku tier. (Corrected after the auditor's round-2 re-check, below.)
- **Gate result (auditor's verdict line, verbatim):** "VERDICT: REVISE — Plan v0.3's substantive
  work is verifiably done, but two recorded claims don't match the artifacts: (1) Plan v0.3
  italicizes *Tracks* (L144) and *Streets* (L218), which §7's apparatus list leaves out, giving 5
  italic case names against a budget of 3, so the Checklist's "apparatus within budget" is false;
  describe both plainly and list them in §7, or justify the overage; (2) Checklist row "All six
  lenses run (v0.3)" puts "Kamm page corrected" in Plan §10, which lacks it; add it to §10 Ac or
  reword the row."
- **The auditor's non-blocking observations, and what was done:**
  - Plan changelog gaps (seven sections → six; *Mines* dropped; reply to Walen's dilemma objection
    dropped; "rescue duties as inputs"): added to the v0.3 changelog.
  - The Rethink Memo wrongly said Option A had the same total budget as Plan v0.2: corrected
    (5,450 vs 5,650), with a correction note in its changelog.
  - The Progress Log lagged: updated in this segment.
  - Model versions are not named in log entries (the Methodology Protocol asks for them). Open
    until Stage 11. This session's operating rules keep model identifiers out of repository files,
    so the custodian will be asked, before the methodology report, how model details should be
    recorded.
  - Run lenses as a separate pass after writing, so they leave a diff: adopted for Stage 4.
  - Notes for the citation-auditor:
    - Alexander L161 denies only a duty to shield others with one's body. The wording was
      corrected in the Plan, the Rethink Memo, the Crux Memo, the Literature Map and the batch-2
      notes.
    - Hecht's condition is stated at L77 (heading at L75): references now read L75–77.
    - *Tracks* is at file 01 L201: added.
- **Fixes to the two required items** (v0.3 had not passed a gate, so it was fixed in place with a
  changelog line):
  1. Ramakrishnan's and Christensen's cases are no longer italicized. They are told plainly with
     line references (file 01 L201; file 05 L209) and added to §7's list of plainly told cases.
     *Mines* in the new changelog line is also left unitalicized. Check: the Plan now has exactly
     three single-asterisk italic case names (*Room*, *Heart Attack*, *Loop*).
  2. Plan §10 Ac now records the Kamm page finding (and the three gate findings), so the
     Checklist row is accurate as written.
- **Compliance flags:** none.
- **Approx. cost/time:** Human: 0. Machine: ~15 min (auditor ~199k tokens, ~10 min).
- **Next:** re-run the gate on the fixes.

## [2026-09-22] Session 1 (cont.) — Plan gate (v0.3), round 2 re-check: REVISE (model-tier record)
- **Models/agents:** Claude; the same paper-auditor subagent, resumed. It ran on the **default tier**,
  like round 1.
- **Gate result (verdict line, verbatim):** "VERDICT: REVISE — both required Plan fixes and the three
  confirmations check out, but the new Process Log entry wrongly says this gate's paper-auditor ran
  on the "haiku tier"; the spawn metadata and subagent transcript show the default tier; correct
  that line (and record this re-check and the Checklist gate row the same way)."
- **What the auditor confirmed:**
  - both required fixes are done;
  - the changelog lines match the diff d3d3f3f..1ccbd3d;
  - nothing else in the Plan changed;
  - the gate result and fixes are logged.
- **AI actions:**
  - Corrected the round-1 entry's model line to the default tier.
  - Applied the round-2 non-blocking notes:
    - Christensen's case cited at file 05 L209–211;
    - the Rethink Memo's Alexander locator cell reworded;
    - one-line correction notes added to the Crux Memo v0.2 and Literature Map v0.2 changelogs.
  - Standing practice from here: procedural gates pass the cheaper model explicitly, following the
    paper-auditor's own tiering rule and the custodian's preference for the lowest adequate model.
- **Compliance flags:** none.
- **Approx. cost/time:** Human: 0. Machine: ~6 min (auditor round 2 ~238k tokens, mostly cached
  context).
- **Next:** a narrow round-3 check of the corrected record, on the haiku tier.

## [2026-09-22] Session 1 (cont.) — Plan gate (v0.3), round 3: APPROVE
- **Models/agents:** Claude; a fresh paper-auditor subagent, spawned on the **haiku tier**
  (procedural check).
- **Gate result (verdict line, verbatim):** "VERDICT: APPROVE — Plan v0.3's recorded corrections
  are accurate; the Process Log's model-tier record is now correct; the round-2 re-check entry
  correctly documents the default-tier finding; commit 643a953's changes match all claimed fixes
  and no other changes are present; section budgets remain 5,450; the Checklist gate row remains
  unticked. The agent may proceed to fill this row and continue to Stage 4 (Layered Outline)."
- **AI actions:** filled the Checklist gate row with the verdict and each round's tier; committed at
  the gate.
- **Note:** the verdict's "continue to Stage 4" is subject to Checkpoint 2 (default checkpoints).
  The plan goes to the custodian next.
- **Compliance flags:** none.
- **Approx. cost/time:** Human: 0. Machine: ~2 min (auditor ~55k tokens).

## [2026-09-22] Session 1 (cont.) — CHECKPOINT 2: Plan approved; opening chosen
- **Models/agents:** Claude (Claude Code remote session).
- **AI actions:** summarized Plan v0.3 in plain English in chat and asked two menu questions.
  - "How does the plan look?", with options "Approve (Recommended)", "Parts are unclear", "Too
    ambitious for 6,000", "Needs more support".
  - "How should the essay open?", with options "Two clinical trials (Recommended)" and "Classic pair
    of cases".
  - Also sent a source request: Millum & Grady 2013 and the Declaration of Helsinki for the trials
    opening; paginated originals as lower priority.
- **Human messages (verbatim):**
  - Q1: "Approve (Recommended)".
  - Q2: "Classic self-written cases". Free text typed in place of the offered options.
- **Compliance assessment:** permitted, no flags.
  - Q1 is an approval.
  - Q2 is a generic preference about the form of the opening: cases written for the essay, in the
    classic thought-experiment style, rather than borrowed ones. It supplies no case, argument,
    distinction or objection. The cases will be AI-originated.
  - AI interpretation, stated to the custodian: open with a pair of cases the AI writes itself, not
    the clinical trials and not Ramakrishnan's existing pair.
- **AI actions after the checkpoint:** Plan v0.4 (v0.3 moved to `Old versions/`).
  - §1 hook: a self-written minimal pair, drafted by the AI (a firefighter uses an unconscious
    neighbour's body to hold a trapdoor, in two versions: he dies of the smoke because there is time
    to save only the five, or his body is wedged so that it crushes him).
  - Ramakrishnan's cases are told plainly with credit.
  - Research ethics becomes an optional §3 illustration.
  - Named cases: the opening pair and *Loop*.
  - **Deterministic self-check:** the diff between v0.3 and v0.4 shows exactly the changelog's items.
    The only single-asterisk italic case name left in the Plan is *Loop*; the other two names get
    chosen at 4C.
- **Selections:** the Plan is approved; the opening is the custodian's free-text choice. Next is
  Stage 4 (Layered Outline); Checkpoint 3 comes at the paragraph outline (4C).
- **Approx. cost/time:** Human: ~1 min. Machine: ~10 min.

## [2026-09-22] Session 1 (cont.) — Stage 4A: skeleton
- **Models/agents:** Claude (Claude Code remote session).
- **AI actions:** wrote `WIP Docs/Outline/Outline 4A v0.1.md` from Plan v0.4. It contains:
  - the spine;
  - a table of the six sections: job, what each recalls, what each hands on, budgets summing to
    5,450;
  - the ordered moves within each section;
  - the dependencies that fix the order;
  - lens findings for A and E.
- **Lens findings, briefly:**
  - A: the opening pair is resolved explicitly in §2; the several-alternatives question is
    assigned to 4B; §5(a) points back to §3 rather than repeating it.
  - E: every ranked interlocutor is placed; Steinhoff is limited to one full treatment; Walen's
    footnotes are consolidated to three, each with one job.
- **Compliance flags:** none. No custodian input.
- **Approx. cost/time:** Human: 0. Machine: ~15 min.

## [2026-09-22] Session 1 (cont.) — Auditor gate 4A: REVISE, fixed
- **Models/agents:** paper-auditor subagent, **haiku tier**.
- **Gate result (verdict line, verbatim):** "VERDICT: REVISE — Stage 4A's skeletal structure and Lens
  A findings are verifiably done, but Lens E's placement table is incomplete and contradicts its own
  claim."
  - The missing names were five from the Literature Map's footnote-only list: Lazar, Kahn, Guerrero,
    Parfit, Tadros 2020.
- **Fix:**
  - Added rows placing Lazar (§3 footnote, optional), Tadros 2020 (§5(c) footnote) and Kahn (§2
    consent footnote, optional).
  - Marked Parfit and Guerrero as not engaged.
  - Reworded the claim to match.
  - Changelog line added in the file. It had not passed a gate, so it was fixed in place.
- **Compliance flags:** none.
- **Approx. cost/time:** Machine: ~5 min (auditor ~67k tokens).

## [2026-09-22] Session 1 (cont.) — Auditor gate 4A: APPROVE
- **Models/agents:** paper-auditor subagent (haiku tier), resumed for the re-check.
- **Gate result (verdict line, verbatim):** "VERDICT: APPROVE — Stage 4A's required fix is verifiably
  complete. The Lens E placement table now includes every interlocutor ranked in Literature Map v0.2
  §4 (items 1–9 and the footnote-only list), with placements specified for three and explicit "not
  engaged" notes for two. The claim sentence matches the table. The file's changelog records the
  gate fix, and git diff a944683..65ef9bf shows only the required edits. The Process Log entry
  documents the REVISE verdict and the applied fix. The agent may proceed to Stage 4B (Argument
  outline)."
- **Pinpoint noted while reading for 4B:** Parry fn 12 (file 06) cites Alexander's omissions passage
  at p. 261 of the chapter, and Quinn 1989 at p. 346. Recorded for the citation audit. (verify
  against the originals.)
- **Approx. cost/time:** Machine: ~1 min (auditor ~76k tokens).

## [2026-09-22] Session 1 (cont.) — Stage 4B: argument outline
- **Models/agents:** Claude (Claude Code remote session). No subagents before the gate.
- **AI actions:** wrote `WIP Docs/Outline/Outline 4B v0.1.md`.
  - **§0 settles the terms:** contribution; supplying relative to an alternative, judged respect by
    respect (needed to keep the six-behind case permissible); comparative loss; the replacement
    test; spending; the bound.
  - **§0 also settles the several-alternatives rule** (Plan risk iii), with a test case (push the one
    vs divert onto two vs do nothing). It yields the standard deontological verdict.
  - **§1–§6:** claim-by-claim steps, 2–4 sub-arguments per section with examples and line-referenced
    sources, and the objections placed per Plan v0.4. Loop's second reason points back to §3.
  - **§7:** all six lenses.
  - **New argumentative content (AI-originated):**
    - the contrastive grounding applied respect by respect;
    - the diagnosis of Thomson 2008's Oxfam analogy as a serving case transferred to a doing case;
    - the reply to Ramakrishnan's arbitrariness worry: his "fine-grained" features are exactly what
      the test for being made to give requires.
  - Re-read, for accuracy: Quong L99–139 and L219–251; Ramakrishnan L35, L133–175, L201–209,
    L263–277; Parry L67–127, L171–195, L231–259; Steinhoff L105–121; Thomson 2008 pp. 364–365.
  - **Self-check** caught two wrong references in the first write, both corrected and noted in §7 Ac:
    - Ramakrishnan's "substantially weaker" is at L153, not L15;
    - Parry's "informs" is at L103, not L101.
- **Compliance flags:** none. No custodian input.
- **Approx. cost/time:** Human: 0. Machine: ~40 min.

## [2026-09-22] Session 1 (cont.) — Auditor gate 4B: APPROVE
- **Models/agents:** paper-auditor subagent, haiku tier.
- **Gate result (verdict line, verbatim):** "VERDICT: APPROVE — Stage 4B's claimed work is genuinely
  done (files confirm it); the agent may proceed to Stage 4C (Fat outline, v0.1)." The auditor
  spot-checked 12 line references with no mismatches.
- **Design finding while preparing 4C (AI-originated):** the opening pair in Plan v0.4 confounds
  spending with doing and allowing: the neighbour is let die in the first case and killed in the
  second. A redesigned pair makes both cases killings, uses his body in the same way in both (it
  holds the trapdoor), and varies only whether his death is the cost of that supply. In the first
  case he dies of smoke that the opening releases; in the second the trapdoor crushes him.
  Recorded in 4C v0.1, to be shown to the custodian at Checkpoint 3.
- **Approx. cost/time:** Machine: ~2 min (auditor ~78k tokens).

## [2026-09-22] Session 1 (cont.) — Stage 4C v0.1: paragraph outline (first pass)
- **Models/agents:** Claude (Claude Code remote session).
- **AI actions:**
  - Wrote `WIP Docs/Outline/Outline 4C v0.1.md`: 38 paragraph bullets across six sections,
    ~2,550 words. An earlier write reached ~3,190 words and was tightened before saving.
  - Redesigned the opening pair (AI-originated) and saved the design note to
    `Scrap/opening-pair-design-note.md`.
    - *Smoke:* the neighbour's body props the trapdoor harmlessly, and the released smoke kills
      him.
    - *Wedge:* his body is wedged, and the trapdoor crushes him.
    - Both are killings, with the same use of his body. Only whether his death is the cost of what
      his body supplies varies. This removes the doing/allowing confound in Plan v0.4's candidate.
- **Compliance flags:** none. No custodian input.
- **Approx. cost/time:** Human: 0. Machine: ~35 min.

## [2026-09-22] Session 1 (cont.) — Stage 4C Round 1 (completeness): Coverage Map; outline v0.2
- **Models/agents:** Claude (Claude Code remote session).
- **AI actions:**
  - Built `WIP Docs/Outline/Coverage Map v0.1.md`. It maps 20 arguments and 19 objections from
    4B, Plan v0.4 and Crux Memo v0.2 to the v0.1 bullets.
    - Gaps: O5 (harmless use), O10 (consent), O13 (the "just another counterfactual" reply), O19
      (compulsion accounts cannot reach omissions).
    - Partials: A4, A5, A15, O3, O8, O9.
  - Wrote `Outline 4C v0.2.md` (v0.1 moved to `Old versions/`), closing all of them.
    - Eight bullets revised across five sections: ¶1.5, ¶2.2, ¶2.4, ¶2.5, ¶3.4, ¶3.5, ¶4.2, ¶5.4.
    - About 2,850 words, including inline line references.
  - Sources re-checked for the new material:
    - Ramakrishnan L107–117 (compulsion does not reach omissions), L109 (the drowning case) and
      L227–233 (the cave-exit case: dislodging someone is not making her serve);
    - Liao & Barry L291 ("sound very much like the MP");
    - Kahn L9 (argues against consent accounts).
- **New AI-originated content:**
  - why letting someone suffer the cost of supply is spending, answering the limit of the
    compulsion account;
  - the generalization to anyone merely "in the way".
- **Compliance flags:** none.
- **Approx. cost/time:** Machine: ~25 min.

## [2026-09-22] Session 1 (cont.) — Stage 4C Round 2 (engagement): outline v0.3
- **Models/agents:** Claude (Claude Code remote session).
- **AI actions:** wrote `Outline 4C v0.3.md` (v0.2 moved to `Old versions/`). Every interlocutor
  ranked in Literature Map v0.2 §4 was checked for real engagement; the table is at the end of v0.3.
  Changes:
  - Choo's reply to the "mere means" diagnosis (file 28 L193) is engaged in ¶5.3. The reply
    (AI-originated): those who judge *Loop* permissible see the use, but use is not what makes
    the footbridge wrong (*Smoke*). What matters is spending.
  - Quong's own rationale (rights "block" usefulness as a reason, file 09 L135–137) is credited for
    its structure and corrected for its object, in ¶3.4.
  - Kamm's contrast between substitution and subordination is footnoted at ¶2.1.
  - Lazar is added to the ¶3.2 credit note.
  - Walen is consolidated to three notes (§2, §4, §5), and Øverland is merged into the §2 note.
  - Sources checked: Choo L183–195; Quong L135–137; Lazar L9; Kamm file 20 (substitution and
    subordination).
- **Length note:** about 3,030 words including inline references, about 2,860 without, which is
  above the ~2,400 guide. A compression pass is planned when the clinic and referee items are folded
  in.
- **Compliance flags:** none.
- **Approx. cost/time:** Machine: ~20 min.

## [2026-09-22] Session 1 (cont.) — Stage 4C argument-clinic pass; outline v0.4
- **Models/agents:** Claude, running the `argument-clinic` skill (all five modes) in the main
  session.
- **AI actions:**
  - Re-read Outline 4C v0.3 from the file.
  - Wrote the memo `Scrap/argument-clinic-4C.md`. It contains the reconstruction, three suppressed
    premises (S1–S3), the validity check, premise-by-premise tests, an equivocation table, the
    steelman and reply, 8 generated minimal-pair cases, and a dispositions table.
  - Accepted fixes landed in `Outline 4C v0.4.md` (v0.3 moved to `Old versions/`).
- **Most serious finding (clear gap):** P2 was false of harmless use, the pillow case, so the
  displayed argument was unsound. P1 and P2 are now restricted to treatment "at their own
  expense". This refines Display 2's wording and supersedes Plan v0.4 §4 on that wording only.
- **Other accepted fixes:**
  - F2: ¶1.3 is fairer to Quong, who does give a reason.
  - F3: the ¶5.6 intentions claim is narrowed and made conditional (a spiteful donor is the test
    case).
  - F4: the crux reply is now in the text: being *taken from* vs being *harmed*; giving as a
    structural notion.
  - F5: "for the sake of" is defined objectively.
  - F6: C is aligned with Display 1.
  - F7: the permission's point is given from inherited sources (Walen 2016 L301; Quong L135).
  - F8: support for the *Smoke* verdict.
  - F9: resistance to the omissions verdict (Alexander) is acknowledged.
  - F11: a loop-to-one footnote.
  - F12: the function-to-content premise is stated.
  - F10: drafting notes.
- **Sources checked:** Walen 2016 L301; Quong L135, L175.
- **Length note:** v0.4 is about 3,540 words including references, above the guide. Compression is
  planned in v0.5 alongside the referee items.
- **Compliance flags:** none. The clinic is AI self-sparring, which the rules explicitly permit.
- **Approx. cost/time:** Machine: ~45 min.

## [2026-09-22] Session 1 (cont.) — Stage 4C blind outline referee; outline v0.5
- **Models/agents:**
  - Claude (main).
  - One blind referee subagent (**sonnet tier**). It was given only the lens (harming and
    deontological constraints), the venue text, and a clean copy of Outline 4C v0.4 with the
    process notes stripped (`Scrap/outline-for-referee-4C.md`, committed). No claim summary, no
    leading questions. It ran ~14 min, ~232k tokens.
- **Referee's findings (full report in the session record; condensed in
  `WIP Docs/Referee Reports/Outline referee memo 4C.md` with dispositions):**
  - M1 [HIGH]: the *Loop* section does not engage Choo's robustness argument, and use and spending
    coincide in *Loop*.
  - M2: P2 is defended only by case-sorting.
  - M3: the *Smoke* verdict is contested by Quong.
  - M4: Quinn is never engaged directly.
  - M5: a tension with Christensen's *Streets*.
  - Minor: density, case load, budget arithmetic, "shown first" wording, the partial-justification
    note.
  - Strengths recorded: citation accuracy (~15 checks, all accurate); *Smoke*/*Wedge* "a genuine,
    original piece of case design"; near the bar of a good subfield journal. Finalist odds 20–30%
    as outlined, 45–55% after revisions.
- **AI dispositions** (all major items accepted; one factual claim of the referee's rejected):
  - M1: §5 is rebuilt. The "use, not spending" reply is dropped, Choo's findings are granted, and
    the theory-over-intuition trade is defended via Otsuka's chain of cases.
  - M1a: the AI's own claim "Choo does not engage this" is corrected. Choo answers Otsuka's
    general claim (L185–195); a grep of file 28 finds no discussion of the bridge-toppling loop or
    the ramp.
  - M2: a conceptual defence of P2, using Quinn L297 and Quong L135.
  - M3: *Smoke* is now diversion plus a harmless use, and the burden against Quong is stated.
  - M4: Quinn is quoted directly (file 12 L238–254, L297). The idea is credited to Quinn, and the
    test is presented as an improvement on his shelter test and its absence-form descendants,
    shown with Ramakrishnan's pill case (file 01 L125–129).
  - M5: Christensen's passer-by is spending by omission, so the view agrees with him. The spiteful
    donor spends no one.
  - Minor: all accepted. The referee's claim that the unprimed figures differ from the Loop-first
    figures is rejected (file 28 L153 reports no-prior-case studies; Group B was Standard-first),
    but the wording is changed to "unprimed".
- **Outline v0.5:** v0.4 moved to `Old versions/`. It adds a budget check projecting ~5,610 words
  of prose including notes and abstract: under the cap, with section trims planned at draft.
- **Originality note (AI):** engaging Quinn directly shows that the criterion's core idea
  ("usefully involved ... only at the cost of") is Quinn's. The essay's claim is recalibrated
  again: the idea is Quinn's; the new part is the test that makes it precise (replacement plus
  comparison with the alternatives) and its consequences.
- **Compliance flags:** none.
- **Approx. cost/time:** Machine: ~1 h (referee ~232k tokens).

## [2026-09-22] Session 1 (cont.) — Auditor gate 4C FINAL: APPROVE
- **Models/agents:** paper-auditor subagent, haiku tier.
- **AI actions before the gate:** wrote `WIP Docs/Outline/Coverage Map v0.2.md`, re-mapping every
  argument and objection, plus the clinic and referee items, onto the v0.5 bullets; v0.1 moved to
  `Old versions/`. Added a dated correction to Literature Map v0.2 §5: the criterion's core idea is
  Quinn's (file 12 L250–254), and claim (a) is narrowed to the test.
- **Gate result (verdict line, verbatim):** "VERDICT: APPROVE — Stage 4C's claimed work is genuinely
  done (files confirm it); the agent may proceed to Stage 5 (Draft v1.0)."
- **What the auditor verified:**
  - 38 bullets;
  - broad diffs at each of the four version steps;
  - Coverage Map v0.2, with 5 mappings spot-checked;
  - the engagement table;
  - the clinic dispositions (F1, F4, F5 spot-checked);
  - the referee dispositions (M1, M3, M4 spot-checked);
  - the clean referee input has no process notes.
- **Next:** Checkpoint 3 with the custodian (structure sign-off; generic feedback only).
- **Approx. cost/time:** Machine: ~3 min.

## [2026-09-22] Session 1 (cont.) — CHECKPOINT 3 presented: "Needs more support"
- **Models/agents:** Claude (Claude Code remote session).
- **AI actions:** summarized Outline 4C v0.5 in plain English in chat: the redesigned opening pair,
  the clinic's hole, the referee's main points. Then asked one menu question: "Can I lock the
  outline's structure and start writing the draft?"
  - "Approve (Recommended)";
  - "Parts are unclear";
  - "Too much for 6,000 words";
  - "Needs more support", described as "I'll strengthen the argument where it's thinnest before
    drafting".
- **Human message (verbatim):** selected "Needs more support". No free text.
- **Compliance assessment:** permitted, no flags. This is generic feedback of the kind the rules
  list ("premise N needs more support"), without naming a premise. The AI alone decides where the
  argument is thinnest and how to strengthen it. The custodian was not asked which part, to avoid
  inviting substantive input.
- **AI diagnosis (AI-originated):** the thinnest load-bearing points are:
  1. P3's claim that the permission not to give must be more than a permission to refuse,
     supported only by quotations;
  2. the case that only spending overrides what the permission protects (P4's "exactly");
  3. why letting someone suffer the cost of supply is spending;
  4. the *Loop* chain argument, stated only in summary.
- **Next:** Outline 4C v0.6 strengthening these four points, a deterministic self-check, then
  Checkpoint 3 re-presented.

## [2026-09-22] Session 1 (cont.) — Outline 4C v0.6 (response to "Needs more support")
- **Models/agents:** Claude (Claude Code remote session). No subagents.
- **AI actions (all AI-originated):** wrote `WIP Docs/Outline/Outline 4C v0.6.md` to strengthen the
  four points diagnosed in the previous entry. v0.5 (4C gate APPROVE) moved to `Old versions/`.
  1. ¶3.2 (P3): a self-written case, *the kidney rule* (a hospital may take a kidney from anyone
     whose kidney would save a life, while leaving everyone free to refuse to donate). It shows that
     a permission others could override by taking would be hollow. The two-step reason is spelled
     out (Walen 2016, file 14 L301; Quong, file 09 L135). A footnote comparison with Harris's
     "survival lottery" is tagged (verify) and added to `Background Readings/REQUESTS.md` as #22.
  2. ¶3.5 (P4's "exactly"): why a side-effect harm leaves the permission's object untouched. Its
     loss is not the cost of anything of hers serving: either nothing of hers serves, or the loss
     would fall on her all the same were what serves supplied from elsewhere (the smoke in *Smoke*).
  3. ¶4.2 (omissions): the sliding man is the kidney rule by omission.
  4. ¶5.3 (*Loop*): Otsuka's argument set out case by case, with two routes from *Loop* to his
     Bridge Case (file 27 L13, L107, L119, L125, L145–151, L159, L163 n. 25). The reply to Choo is
     sharpened: the chain sets the *Loop* verdict against a verdict on a case, not a principle, so
     his point that people trust the *Loop* verdict over the principles (file 28 L193–195) does not
     reach it.
  5. Budget: §3 1,300 (+100), §5 1,000 (−100); projected total ~5,710 of 6,000.
- **Deterministic self-check (stands in for the auditor on an incremental revision):**
  - The diff v0.5 → v0.6 has 12 hunks. Each maps to a changelog item: the header, the changelog,
    the §3 and §5 headings, ¶3.2, ¶3.5, ¶4.2, ¶5.3, and three budget rows. No other change.
  - Bullet numbers are unchanged, so Coverage Map v0.2 still maps every argument and objection.
  - Re-reading the new text against the outline's own test and the sources caught three errors in
    the first text of v0.6, fixed before commit:
    1. ¶3.5 explained side-effect harms by the victim's absence. §2 rejects absence tests, and the
       explanation misdescribed *Smoke*. Restated in the replacement test's terms.
    2. ¶5.3 called Otsuka's endpoint "the footbridge" and presented his cases as one four-link
       chain. In the source, the endpoint is his Bridge Case (a lever-operated pole topples the
       man, L13), reached by two routes. The claim that no principle separates the cases was stated
       as the essay's own; it is now Otsuka's stated doubt (L159, L163 n. 25).
    3. ¶4.2 said the sliding man's body "is taken", which misdescribes an omission. Now: it "serves
       the five at his cost all the same".
  - The self-check did not surprise in the gate sense (the diff matches the changelog), so no
    auditor escalation.
- **Searches:** none new. All line references are to files already on disk (09, 12, 14, 27, 28).
- **Human messages:** none since the Checkpoint 3 answer.
- **Compliance flags:** none.
- **Next:** Checkpoint 3 re-presented to the custodian.
- **Approx. cost/time:** Machine: ~25 min.

## [2026-09-22] Session 1 (cont.) — CHECKPOINT 3 re-presented: APPROVED
- **Models/agents:** Claude (Claude Code remote session).
- **AI actions:** summarized Outline 4C v0.6 in plain English in chat: the kidney rule, why
  side-effect harms differ, omissions as the kidney rule by omission, the *Loop* cases set out step
  by step, and the three self-check corrections. Reminded the custodian about OpenReview
  registration. Asked the same menu question as before: "Can I lock the outline's structure and
  start writing the draft?"
  - "Approve (Recommended)", described as "Lock the outline and start writing Draft 1 from it.";
  - "Parts are unclear";
  - "Too much for 6,000 words";
  - "Needs more support".
- **Human message (verbatim):** selected "Approve (Recommended)". No free text.
- **Compliance assessment:** permitted, no flags. A selection among the AI's options.
- **Result:** Outline 4C v0.6 is locked as the drafting contract for Draft v1.0.
- **Next:** Stage 5. Calibration reads, then Draft v1.0 in one full-density pass to the section
  budgets, then Lens Ac and the Draft v1.0 auditor gate.

## [2026-09-22] Session 1 (cont.) — Stage 5: Draft v1.0
- **Models/agents:** Claude (Claude Code remote session). No subagents.
- **Calibration reads (before the first sentence):**
  - `Playbook/Craft/model-paragraphs.md` in full;
  - the Style Guide (both budgets), `Craft/prose-principles.md`, `Craft/moves-catalog.md` Part 2,
    and the thesis and roadmap rules in `Craft/intro-playbook.md`;
  - register samples from Plan v0.4: Ramakrishnan 2016 (file 01, L1–40) and Parry 2023 (file 06,
    L1–75).
- **AI actions (all AI-originated):**
  - Pulled every planned quotation from the source files before drafting.
  - Wrote `WIP Docs/Drafts/Draft v1.0.md` in one full-density pass from Outline 4C v0.6. It has 44
    body paragraphs in six sections, 13 notes and a reference list; the abstract is left for
    Stage 10.
  - Closed two gaps against the outline within the pass:
    - ¶5.4 now cites Quinn's treatment of the driver case, as Liao and Barry report it.
    - Walen's forfeiture view is placed with the malicious diverter (file 22 L121).
  - Terminology fix: spending includes the bound, so the outline's "spent within the duty" became
    "does not spend her" (¶4.5, ¶5.7).
  - Deterministic checks, all recorded in `WIP Docs/Change Logs/Draft v1.0 — Lens Ac and
    self-check.md`:
    - a quotation script: 41 quotations, 40 verbatim on disk; Harris is not on disk and is tagged
      (verify);
    - Lens Ac: all 38 bullets landed;
    - prose_lint: 3 FLAGs, each dispositioned;
    - word count: 6,459 words before the abstract, about 1,000 over the budgets. Stage 6 Pass 1
      will be a cut pass.
  - Hygiene search: no mention of AI, the competition or prompts; nothing addressed to an AI reader.
  - Noted for Stage 6 but not added, to keep the pass faithful to the outline:
    - Quong's definition of use mentions "some relevantly similar body or property" (file 09 L49).
      A referee might compare this with the replacement test; a note could separate them.
    - Alexander's note 8 condemns turning the trolley in loop cases (file 25 L45), so he could join
      the company on *Loop*.
- **Searches:** none on the web. All lookups were in files already on disk.
- **Human messages:** none since the Checkpoint 3 approval.
- **Compliance flags:** none.
- **Next:** the Draft v1.0 auditor gate.
- **Approx. cost/time:** Machine: ~1.5 h.

## [2026-09-22] Session 1 (cont.) — Auditor gate, Draft v1.0: APPROVE
- **Models/agents:** paper-auditor subagent, haiku tier.
- **Gate result (verdict line, verbatim):** "VERDICT: APPROVE — Stage 5 (Draft v1.0)'s claimed work
  is genuinely done (files confirm it); all 38 outline bullets are unpacked into prose with clear
  mappings to draft paragraphs; quotations are verified against source files on disk; word count
  matches the self-check's ~1,000-word overage; calibration reads and drafting session are logged
  in full in the Process Log; the draft contains no mention of AI, the competition, or its own
  process; and the self-check's minor deviations are transparent and within budget allowances. The
  agent may proceed to Stage 6 (Quality passes)."
- **What the auditor reported verifying:**
  - the six-section structure against the outline;
  - two quotations against the source files (Quong, file 09 L47; Quinn, file 12 L249–255);
  - the word count (6,506 with the changelog line);
  - the Process Log's Stage 5 entry;
  - a hygiene search for AI, competition and prompt terms.
  It was asked for at least six bullet spot-checks and five quotation checks. Its report lists
  fewer, so this log records only what it reported.
- **Next:** Stage 6 Pass 1 (v1.1), a cut pass with quality work.
- **Approx. cost/time:** Machine: ~5 min.

## [2026-09-22] Session 1 (cont.) — Stage 6 Pass 1: Draft v1.1 (cut and tighten)
- **Models/agents:** Claude (Claude Code remote session). No subagents.
- **Calibration read:** `Playbook/Craft/model-paragraphs.md` in full, fresh, before the pass.
- **AI actions (all AI-originated):**
  - Cut 6,459 → 5,761 words before the abstract. Most of the cut is repeated points, credit lists
    and long notes.
  - Merged two paragraphs; folded the Steinhoff paragraph into the premise 4 paragraph; cut the
    note on the cave and parking cases.
  - Made two claims precise. The support for *Smoke* now claims only that a harmless use cannot be
    what makes the killing wrongful. Ramakrishnan's primitivism now attaches to his principle.
  - Added a note separating the replacement test from Quong's "relevantly similar body or
    property" clause (file 09 L49), and added Alexander to the company on *Loop* (file 25, n. 8).
  - Split the long *Loop* paragraph in two.
  - v1.0 moved to `Old versions/`.
- **Self-check (deterministic):** `WIP Docs/Change Logs/Draft v1.1 — self-check.md`.
  - The diff matches the changelog row by row.
  - Quotation script: 42 quotations, 41 verbatim on disk; Harris remains (verify).
  - Note references and definitions match.
  - Lint: 3 FLAGs (list triads, short sentences, one uniform-length run), deferred to 7b.
  - First attempt: the first version of this pass cut only about 170 words, so the pass was redone
    paragraph by paragraph until the word target was met.
- **Human messages:** none since the Checkpoint 3 approval.
- **Compliance flags:** none.
- **Next:** Stage 6 Pass 2 (dialectical balance; each argument once; additions).
- **Approx. cost/time:** Machine: ~45 min.

## [2026-09-22] Session 1 (cont.) — Stage 6 Pass 2: Draft v1.2; Stage 6 converged
- **Models/agents:** Claude (Claude Code remote session). No subagents.
- **Calibration read:** `Playbook/Craft/model-paragraphs.md` in full, fresh, before the pass.
- **AI actions (all AI-originated):**
  - Ruled out intention as the difference in the opening pair, with a note on the problem of
    closeness (Quong, file 09 L357; Choo, file 28 n. 11). This pre-empts the reply from the
    doctrine of double effect.
  - Ran the replacement test explicitly on the sliding man.
  - Named the permission not to give in its usual terms (an agent-relative prerogative).
  - Weakened an overclaim about coercion.
  - Cut a repeated point (¶5.7) and a redundant note sentence.
  - v1.1 moved to `Old versions/`.
- **Self-check (deterministic):** `WIP Docs/Change Logs/Draft v1.2 — self-check.md`.
  - With note numbers masked, the word-diff matches the changelog.
  - Notes are renumbered and matched.
  - Quotations: 40 of 41 verbatim; Harris remains (verify).
  - Words: 5,809 before the abstract, too close to the cap. The 7b condense pass must cut at least
    200 words.
- **Convergence:** no further argument-level change without outside review. Stage 6 is declared
  converged after two passes.
- **Human messages:** none since the Checkpoint 3 approval.
- **Compliance flags:** none.
- **Next:** Stage 7, the clarity chain (7a prose-rewriter; 7b condense and lint; 7c cold reader).
- **Approx. cost/time:** Machine: ~25 min.

## [2026-09-22/23] Session 1 (cont.) — Stage 7a: register rewrite in fresh contexts (Draft v1.3)
- **Models/agents:** prose-rewriter subagents, sonnet tier, run in parallel.
  - The first run used three rewriters (sections 1–2, 3, 4–6). The one for sections 1–2 stopped at
    the output-length limit and returned nothing.
  - The re-run used two rewriters (section 1; section 2), each told to write its text to a file and
    return a short memo.
  - That makes five subagent runs in all, four of them productive.
- **Inputs given to each rewriter:**
  - its section only, as a clean file in `Scrap/`;
  - the thesis in one sentence;
  - a glossary of terms from other sections;
  - the register-sample paths;
  - hard constraints: no growth in length; quotations, citations, placeholders and displays fixed;
    no new labels.
  - It was never given the outline or the plan.
- **AI actions:** dispositioned every change in each rewriter's table. The records are
  `Scrap/7a-changes-*.md`; the raw and applied texts are kept beside them.
  - 19 edits were rejected or corrected. Most important: "the good is what would justify the loss"
    (it contradicts the thesis, restored); "the duties the principle imposes" (the duties set the
    bound, so restored); a tu quoque reading of Ramakrishnan's arbitrariness worry (restored); the
    log's cost moved onto the burners (restored).
  - Also restored: the fixed term "the permission not to give"; bridging sentences; full first
    names; purpose clauses ("so that").
  - New labels ("criterion camp", "*Smoke*-structured") were rejected.
  - From the rewriters' flags: glossed Quong's rescue condition in his words (file 09 L249), and
    named the view's two features in the §3 reply.
  - Assembled `WIP Docs/Drafts/Draft v1.3.md`. v1.2 moved to `Old versions/`.
- **Self-check (deterministic):** `WIP Docs/Change Logs/Draft v1.3 — self-check.md`. Displays are
  byte-identical; notes matched; 42 quotations, 41 verbatim on disk (Harris remains);
  5,818 words before the abstract; per-section ledger started.
- **Human messages:** one from the environment, not the custodian: the stop hook asked for
  untracked files to be committed. Done; a stray Python cache folder was deleted, not committed.
- **Compliance flags:** none.
- **Next:** 7b, the condense and tell-strip pass (target ≤ 5,550 words before the abstract), with
  the lint report.
- **Approx. cost/time:** Machine: ~2 h wall-clock (subagents ~1.1M tokens in total).

## [2026-09-23] Session 1 (cont.) — Stage 7b: condense and tell-strip (Draft v1.4)
- **Models/agents:** Claude (Claude Code remote session). No subagents.
- **AI actions:** One whole-draft pass, walked §6 → §1, opposite to 7a.
  - About 40 phrase-level cuts and merges; six very short sentences merged.
  - The Steinhoff citations consolidated; Parry's externalities point compressed.
  - The note on Walen's "tightly connected" test cut; notes renumbered.
  - AI-tells sweep: nothing to fix beyond the merges.
  - The linter ran twice, and every FLAG is dispositioned in the self-check.
  - v1.3 moved to `Old versions/`.
- **Self-check:** `WIP Docs/Change Logs/Draft v1.4 — self-check.md`.
  - Displays byte-identical; notes matched; quotations as before.
  - 5,732 words before the abstract. The target of ≤ 5,550 was **not met**. A list of about 230
    words of reserve cuts is recorded for Stage 9–10.
  - The per-section ledger is updated, and §1's PASS has a stated reason.
- **Human messages:** none.
- **Compliance flags:** none.
- **Next:** 7c, a fresh cold-reader subagent on the full v1.4.
- **Approx. cost/time:** Machine: ~40 min.

## [2026-09-23] Session 1 (cont.) — Stage 7c round 1: cold read of v1.4; fixes in v1.5
- **Models/agents:** a cold-reader subagent (sonnet tier), fresh instance. It saw only the clean
  copy of v1.4 (`Scrap/7c-input-v1.4 (clean copy).md`).
- **Result (report saved as `Scrap/7c-report-round1.md`):**
  - The one-read test passed: the reader reconstructed the thesis and the central argument
    correctly, with no mismatch.
  - Friction score 14, which is in the "another round" band. The verdict was "followable with
    effort".
  - The items clustered in the literature-positioning sentences of §2–§3 and in the case-heavy
    stretch of §4–§5.
- **AI actions:** fixed all 14 items in `WIP Docs/Drafts/Draft v1.5.md`, with dispositions in
  `WIP Docs/Change Logs/Draft v1.5 — self-check.md`:
  - three terms glossed at first use;
  - the McMahan citation made explicit;
  - the Steinhoff step shown;
  - Otsuka's chain restructured by route;
  - the vase paragraph cut to reduce the case load;
  - the §1 closing triplet flattened.
  The displays are unchanged; 5,812 words before the abstract.
- **Next:** 7c round 2, with a fresh cold reader on v1.5.
- **Human messages:** none. **Compliance flags:** none.
- **Approx. cost/time:** Machine: ~40 min (cold reader ~66k tokens).

## [2026-09-23] Session 1 (cont.) — Stage 7c round 2: cold read of v1.5; fixes in v1.6
- **Models/agents:** a cold-reader subagent (sonnet tier), a fresh instance. It saw only the clean
  copy of v1.5.
- **Result:** the report is saved as `Scrap/7c-report-round2.md`.
  - The one-read test passed.
  - The friction score was 13, verdict "followable with effort". The items were mostly different
    from round 1 and concentrated in §2 and the Otsuka passage.
- **AI actions:** fixed or dispositioned all 13 items in `WIP Docs/Drafts/Draft v1.6.md`; the
  dispositions are in `WIP Docs/Change Logs/Draft v1.6 — self-check.md`.
  - Shown steps: Alexander's accounting and the three-track wrench case.
  - Structure: the Otsuka passage split, with a one-line map; the two readings in Quong's dilemma
    signposted.
  - Case load: Liao and Barry's log case moved to a note.
  - Glosses: "Fat Man" glossed; the case of shortage tied to the door case.
  - The *Loop* company list moved to a note.
  - Item 5, the definition of spending, was kept, with a stated reason.
  - Three reserve cuts were spent to stay under the cap with room for the abstract.
  - Lazar was removed from the references, since it is no longer cited.
  - Result: 5,775 words before the abstract.
- **Next:** 7c round 3, with a fresh cold reader on v1.6.
- **Human messages:** none. **Compliance flags:** none.
- **Approx. cost/time:** Machine: ~35 min (cold reader ~66k tokens).

## [2026-09-23] Session 1 (cont.) — Stage 7c round 3: cold read of v1.6; fixes in v1.7
- **Models/agents:** a cold-reader subagent (sonnet tier), fresh instance; it saw only the clean
  copy of v1.6.
- **Result:** report saved as `Scrap/7c-report-round3.md`. The one-read test passed. The friction
  score was 11, "followable with effort". The trend so far is 14 → 13 → 11.
- **AI actions:** fixed all 11 items in `WIP Docs/Drafts/Draft v1.7.md`; the dispositions are in
  `WIP Docs/Change Logs/Draft v1.7 — self-check.md`.
  - A structural fix for the spot every reader flagged: Otsuka's second route moved to a note, so
    the text runs one chain.
  - Two unearned steps now shown: why the *Loop* verdict should yield, and why the explanation is
    not circular.
  - The pill and flamethrower cases retold for easier tracking.
  - A repeated point cut; the Kamm note and other note material cut to pay for the additions.
  - Result: 5,754 words before the abstract.
- **Next:** 7c round 4, with a fresh cold reader on v1.7.
- **Human messages:** none. **Compliance flags:** none.
- **Approx. cost/time:** Machine: ~35 min (cold reader ~60k tokens).

## [2026-09-23] Session 1 (cont.) — Stage 7c round 4: cold read of v1.7; fixes in v1.8
- **Models/agents:** a cold-reader subagent (sonnet tier), fresh instance. It saw only the clean
  copy of v1.7.
- **Result:** report in `Scrap/7c-report-round4.md`. The one-read test passed. Friction score 10,
  "followable with effort", "at its gentle end". Trend: 14 → 13 → 11 → 10.
- **AI actions:** all 10 items fixed in `WIP Docs/Drafts/Draft v1.8.md`; dispositions in
  `WIP Docs/Change Logs/Draft v1.8 — self-check.md`.
  - The spots that recurred across readers were fixed at the root: the §1 two-tracks paragraph,
    the wording of P2, Quong's dilemma, and name density in the notes.
  - P2 was reworded for clarity. Its content is unchanged; this is the only change to the
    displayed argument since Checkpoint 3, and it is logged here for the methodology report.
  - The motive assumption now has stated support.
  - Costa 1987, Walen 2014 and Liao et al. 2012 were removed from the references because nothing
    cites them any more. REQUESTS #21 (Costa) is marked no longer needed.
  - The Steinhoff sentence in §3 was cut for length.
  - Result: 5,780 words before the abstract.
- **Next:** 7c round 5, with a fresh cold reader on v1.8.
- **Human messages:** none. **Compliance flags:** none.
- **Approx. cost/time:** Machine: ~30 min (cold reader ~61k tokens).
