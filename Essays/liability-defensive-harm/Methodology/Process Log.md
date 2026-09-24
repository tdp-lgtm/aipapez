# Process Log — liability-defensive-harm

Append-only session log; see Playbook/3. Methodology Protocol.md for the entry template.
Verbatim human messages; AI actions; models; candidate counts; selections; compliance
flags; approximate cost. This log is the compliance evidence and the raw material for the
methodology report.

## [2026-09-24] Session 1 — Stage 0 Setup
- **Surface:** Claude Code remote session (claude.ai/code), branch `claude/serene-cori-umse3p`.
- **Models/agents:** Claude (Claude Code remote session; drafting agent). No subagents yet
  (paper-auditor to be spawned for the Setup gate, small model tier).
- **Human messages (verbatim):**
  > @"/root/.claude/uploads/96c4f606-f3b2-59ca-8b87-e315bdc6c975/913481ee-Liability_for_AI.md" New Paper 3!
  > I want you to write a paper on the topic of "liability to defensive harming". It's an important
  > notion that plays a ton of important roles in moral philosophy. However, it's a notoriously difficult
  > notion to pin down. As you'll see from the attached readings, plenty of candidates have been put
  > forward for when an agent should count as "liable" to harm. Your task is to come up with a new, novel
  > account of liability which is both plausible (not ad hoc) and avoids (again, in a non-ad hoc) the kinds
  > of objections and counterexamples faced by existing accounts. I'm attaching several important paper,
  > but you can also ask for more resources if you want.

  Intake answers (given via the interactive question menu, custodian's selections):
  > Autonomy: "Default checkpoints (Recommended)"
  > Runway: "Quality first, use all time"
  > Paper 2: "Yes, in another session"
  > OpenReview: "Not yet"
- **AI actions:** Read CLAUDE.md, Competition Brief, Rules — Human Involvement, DIGEST, full Pipeline,
  Methodology Protocol, Essay Project Template, Literature Access Protocol; read essay 1's Intake and
  Process Log for the house format. Ran the bounded intake (topic already supplied; asked autonomy,
  runway, whether essay 2 is underway, and OpenReview status; did not ask for a thesis or arguments).
  Scaffolded `Essays/liability-defensive-harm/` with new_essay.py. Preserved the custodian's upload
  verbatim in `Background Readings/` and split it by line range into 19 per-paper files in
  `Converted text/` (script-checked: all 6,123 lines covered, no edits inside texts). Identified each
  paper's author and venue from the text and from reference lists inside the upload; wrote
  `Converted text/README.md` (bibliographic key with confirmed/(verify) status per record and a note
  that `{n}` markers are combined-PDF indices, not journal pages). Wrote `Brief/Intake.md`.
- **Selections:** Custodian chose the topic and task (permitted) and the four intake options above.
  No philosophical content selected or supplied.
- **Tools/retrieval:** Local file reads; new_essay.py; a Python split script; WebSearch ×5 to confirm
  bibliographic records: (1) Tadros "Two grounds of liability" → *Philosophical Studies* 178 (2021):
  3503–3522; (2) Clark "Mistaken Defense and the Unbundling of Rights" → *Ethics* 135(3) (2025):
  428–457; (3)–(5) Clark "'As If'" (venue not found; flagged for the custodian) — these searches also
  surfaced Burri 2025's venue (*Ethical Theory and Moral Practice*) and further candidate literature
  (Frowe 2021 "Risk Imposition and Liability to Defensive Harm"; Lang on the Moral Status Account;
  Bolinger 2021; Christie 2022 "Mortal Mistakes"; Clark 2023 "Refusing Protection").
- **Compliance flags:** none. The topic message specifies a topic, a task type (a new account of
  liability), and generic desiderata (plausible, not ad hoc, avoids existing counterexamples) — all
  permitted direction. It contains no thesis, candidate account, argument, distinction, or
  counterexample. The reading list is broad (every major family of account plus critics), so it does
  not curate toward an answer; the AI will widen the search regardless.
- **Approx. cost/time:** Human: ~3 minutes (topic message + upload + 4 menu clicks). Machine: ~25 min
  wall clock for setup.
- **Gate:** paper-auditor ×1 (haiku tier) for the Setup gate — "VERDICT: APPROVE" (verified tree,
  intake, verbatim messages, the 19-file split against the upload by line count, and the compliance
  judgment). Pasted into the Checklist.

## [2026-09-24] Session 1 (cont.) — Stage 1 Idea Generation (pre-checkpoint)
- **Models/agents:** Claude (Claude Code remote session; drafting agent). No subagents this segment.
- **Human messages (verbatim):** none this segment.
- **AI actions:** Close reading of the supplied texts in full: Quong 2012, McMahan 2005a, Burri 2025,
  Burri 2022, Clark "As If", Clark 2025, Tadros 2012, Tadros 2021, Thomson 1991, Ferzan 2012, Frowe
  2010; McMahan 2011 §§2–4; targeted reading of Quong 2009 (principle and means principle). Skimmed:
  McMahan 2005b, McMahan 1994, Frowe 2008a/b, Tadros 2014. Wrote `WIP Docs/Literature Map/Reading
  Notes — Round 1.md` (accounts, rationales, cases, objections, with `{n}` page markers for later
  pinpoints). Built a case/objection inventory (22 recurring verdicts, 14 recurring objections) in
  working notes. Generated **14 thesis candidates** in P/Q/R form with contribution type and
  originality hypothesis (`WIP Docs/Candidates/Thesis Candidates v0.1.md`). Pre-screen result:
  4 advance (C1 Conferral, C2 Knowledge-Norm, C9 Risk-Pool, C11 Present-Duty), 5 merged into C1
  (C3, C6, C10, C12, C13), 5 killed (C4 duress counterexample; C5 already Tadros's view; C7 yields
  symmetric permissions only; C8 anticipated by Frowe 2010/Chehtman 2017/Clark 2025; C14 misses the
  brief). Wrote 4 ranked half-page Argument Sketches with premises, payoff, main objection, and crux
  (`Argument Sketches v0.1.md`). Recommendation: Sketch A (Conferral Account).
- **Selections:** none yet (CHECKPOINT 1 pending).
- **Tools/retrieval:** WebSearch ×18 this segment (count corrected from an erroneous "×21" after the Idea Selection audit; the 3 further searches were run in the next segment and are logged there). Originality and landscape queries: (1) Hohfeld/
  power/conferral + mistaken attacker; (2) Kantian "hindering a hindrance" + liability; (3) "knowledge
  norm" + self-defense; (4) Quong 2020 ch. 2 MSA formulation (found: "(a) the evidence-relative
  permissibility of Φ-ing depends on the assumption that at least one person, B, lacks a [moral
  right]..."); (5) jurisdiction + defensive harm; (6) Ripstein 1996 "Self Defense and Equal
  Protection" (U. Pitt. L. Rev. 57: 685–724; risk-allocation view of reasonable mistakes);
  (7) Chehtman 2017 Utilitas 29(3): 321–343; (8) Christie 2020 JAP 37: 378–392 (causation not
  necessary); (9) Burri 2020 L&P 39(4): 381–408; (10) Frowe 2022 Crim L & Phil 16: 511–524 (token vs
  type justification of incidental risk; critique of Quong); (11) Gordon-Solmon 2018 PPR 97(3):
  543–567; (12) Lang, "Defensive Liability and the Moral Status Account" (argues the Driver/Mistaken
  Attacker distinction cannot be sustained); (13) Frowe 2022 detail; (14) Renzo 2017 JPP 25(3):
  324–342 (forfeiture incomplete/redundant); (15) Christie 2022 "Mortal Mistakes" JMP (MSA vs
  culpability); (16) strict liability for intentional harming vs risk; (17) Fletcher reciprocity +
  defensive harm (no development found); (18) consent analogy for mistaken attackers. WebFetch
  attempted on plato.stanford.edu and d-nb.info: both **egress-blocked** (as in essay 1); only
  search snippets and abstracts are reachable, so these sources are logged for request, not cited.
- **Compliance flags:** none (no custodian input this segment).
- **Approx. cost/time:** Human: 0. Machine: ~2.5 hours wall clock (reading ~120k words of source
  text plus generation).

## [2026-09-24] Session 1 (cont.) — CHECKPOINT 1 (thesis selection)
- **Models/agents:** Claude (Claude Code remote session).
- **Human messages (verbatim):**
  > (CHECKPOINT 1 selection, via interactive menu) "A: Conferral (Recommended)"
- **AI actions:** Presented the four ranked sketches in plain English with a recommendation (A),
  and reminded the custodian to register on OpenReview today. Saved the selected sketch to
  `Brief/Argument Sketch.md` (text unchanged from v0.1).
- **Selections:** Custodian selected Sketch A (Conferral Account) from 4 AI-generated, AI-ranked
  options; A was the AI's top-ranked recommendation. A menu pick; no philosophical content added.
- **Tools/retrieval:** none.
- **Compliance flags:** none.
- **Approx. cost/time:** Human: <1 minute (one menu click). Machine: negligible.

## [2026-09-24] Session 1 (cont.) — Stage 2 start: source request ping
- **Models/agents:** Claude (Claude Code remote session).
- **Human messages (verbatim):** none this segment.
- **AI actions:** Verified three further bibliographic records by search (Lang 2022, *Washington
  University Review of Philosophy* 2: 150–169; Clark 2023, *PPA* 51(1): 33–59; Ferzan 2017, *Legal
  Theory* 23(3): 168–202). Wrote `Background Readings/REQUESTS.md` (17 source rows + 1 citation
  query: 5 MUST, 4 HIGH, 5 MED, 3 LOW; free links given where found) and pinged the custodian in
  chat with the prioritized list, stating that work continues meanwhile on the crux and the
  Literature Map (dependent claims to be tagged `(verify — awaiting source #N)`).
- **Selections:** none. (The request list is AI-composed; the custodian only fetches.)
- **Tools/retrieval:** WebSearch ×3 (record verification).
- **Compliance flags:** none.
- **Approx. cost/time:** Human: 0 so far. Machine: ~10 min.

## [2026-09-24] Session 1 (cont.) — Idea Selection gate; Stage 2 Literature Map
- **Models/agents:** Claude (drafting agent). Subagents: paper-auditor ×1 (haiku tier), resumed once.
- **Human messages (verbatim):** none this segment.
- **AI actions:** Idea Selection gate: first verdict REVISE. The defect was real: the Stage 1 log
  said "WebSearch ×21" but only 18 searches ran in that segment. Corrected the log and Checklist
  (explicit correction note); the resumed auditor re-verified and returned APPROVE. Wrote
  `Scrap/crux-memo-v0.1.md`, a five-step proposed solution to the sketch's crux: the conferral
  principle; acting upon vs imposing risk; the independence argument; "whose act changes whose
  position"; a contractualist comparison answering Bolinger/Ripstein. It also lists residual issues
  (unknowing justification; selective liability; Lang; Frowe 2022; knowing side-effect harm). Wrote
  `WIP Docs/Literature Map/Literature Map v0.1.md`: landscape table (5 families × verdicts on 4 test
  cases), where the field is stuck, the open niche, 6 nearest neighbours distinguished, originality
  verdict OPEN (moderate confidence) with a risk register, engagement plan, lenses E and Ac.
- **Selections:** none.
- **Tools/retrieval:** none new (built from Round 1 reading and the logged searches).
- **Compliance flags:** none.
- **Approx. cost/time:** Human: 0. Machine: ~40 min.

## [2026-09-24] Session 1 (cont.) — Stage 3 Plan
- **Models/agents:** Claude (drafting agent). Subagent: paper-auditor ×1 (haiku) running the Lit
  Review gate in the background.
- **Human messages (verbatim):** none this segment.
- **AI actions:** Read the Essay Style Guide in full, Moves Catalog Part 1, and journal-craft
  headings and red flags. Selected the structural moves: a three-case puzzle opening (variant of the
  paired-cases opening), the reverse-engineering arc for the account, pre-emptive defence against
  the deflationary reading ("Quong restated"), and reply-layering for the fair-allocation objection.
  Chose register samples: Quong 2012 and Thomson 1991. Wrote `WIP Docs/Plan/Plan v0.1.md`: sharpest
  thesis (Display 1 draft), the three-step move, 7 sections budgeted to 5,950 words (arithmetic
  checked), dialectical structure with 4 planned concessions, apparatus within budget (1 view,
  1 rival, 1 coined term, 3 named cases, 2 displays), central argument draft (8 steps, defence
  locations named), evidence discipline, and six-lens review (one fix applied: a second coined term
  dropped to stay within budget).
- **Selections:** none.
- **Tools/retrieval:** local file reads only.
- **Compliance flags:** none.
- **Approx. cost/time:** Human: 0. Machine: ~35 min.

## [2026-09-24] Session 1 (cont.) — Lit Review gate; Plan v0.2
- **Models/agents:** Claude (drafting agent); paper-auditor ×1 (haiku), resumed once.
- **Human messages (verbatim):** none this segment.
- **AI actions:** Lit Review gate: first verdict REVISE. The defect was real: Ferzan 2005 was tagged
  [T] but is not on disk; retagged [A]. A parallel mis-tag (Otsuka 1994) was found and fixed
  unprompted. Re-verification APPROVE. Revised the Plan to v0.2 (v0.1 archived): a 5-step central
  argument whose enforcement premise carries an explicit standing clause (without it, the displayed
  argument would be false in bluff cases), and a matching estoppel clause in the statement of the
  view. Computed marker-to-page mappings for 11 of the 14 main texts and recorded them in
  `Converted text/README.md`; Frowe 2010's marker count does not match its printed range, so it
  is flagged, not computed.
- **Selections:** none.
- **Tools/retrieval:** local scripts (marker counts).
- **Compliance flags:** none.
- **Approx. cost/time:** Human: 0. Machine: ~30 min.

## [2026-09-24] Session 1 (cont.) — Plan gate
- **Models/agents:** paper-auditor ×1 (haiku tier).
- **Human messages (verbatim):** none this segment.
- **AI actions:** Plan gate returned APPROVE on the first pass (budget arithmetic, versioning diff,
  apparatus count, and view–argument consistency all verified). Appended a pre-outline stress test
  to the crux memo (agent-relative prerogatives handled modularly; mutual mistake; authority scoped
  to those within an authority's jurisdiction; omissions out of scope; careless appearance flagged
  for 4B).
- **Selections:** none.
- **Compliance flags:** none.
- **Approx. cost/time:** Human: 0. Machine: ~10 min.

## [2026-09-24] Session 1 (cont.) — CHECKPOINT 2 (Plan read)
- **Models/agents:** Claude (drafting agent).
- **Human messages (verbatim):**
  > (CHECKPOINT 2, via interactive menu) "Approve (Recommended)"
- **AI actions:** Presented Plan v0.2 in plain English (claim, seven sections, 5,950-word budget),
  with an explicit reminder that feedback must stay generic under the competition rules. Offered
  four responses: approve / something unclear / too ambitious / pause to read.
- **Selections:** Custodian approved the Plan (generic approval; no content supplied).
- **Compliance flags:** none.
- **Approx. cost/time:** Human: ~1 minute. Machine: negligible.

## [2026-09-24] Session 1 (cont.) — Stage 4A skeleton
- **Models/agents:** Claude (drafting agent).
- **Human messages (verbatim):** none this segment.
- **AI actions:** Read essay 1's 4A file for the house format. Wrote `WIP Docs/Outline/Outline 4A
  Skeleton v0.1.md`: 7 sections with budgets (sum 5,950), numbered jobs, exit states, and lenses
  A and E (one fix applied: the enforcement premise moved from §3 to §2.4, so §2 ends by setting the
  question §3 answers). Submitted to the 4A auditor gate.
- **Selections:** none.
- **Compliance flags:** none.
- **Approx. cost/time:** Human: 0. Machine: ~20 min.

## [2026-09-24] Session 1 (cont.) — 4A gate; Stage 4B argument outline
- **Models/agents:** Claude (drafting agent); paper-auditor ×1 (haiku) for the 4A gate.
- **Human messages (verbatim):** none this segment.
- **AI actions:** 4A gate APPROVE (first pass). Read essay 1's 4B for the house format. Wrote
  `WIP Docs/Outline/Outline 4B Argument v0.1.md`: every section expanded into 2–4 sub-arguments
  with examples and named sources, and journal page numbers from the marker mapping. Two mappings
  were confirmed independently against page numbers other authors cite: Ferzan 2012, p. 675 (as
  cited in Clark "As If") and McMahan 2011, pp. 555–56 (as cited in Clark 2025). After drafting,
  every page number was checked against the marker map; three were wrong and were corrected
  (Quong 2012, 51 n. 11; 64–67; Clark 2025, 453–54). Six-lens review in file (one gap fixed: the
  duress case added to §4.2). Eight `(verify — #N)` tags across seven awaited sources.
- **Selections:** none.
- **Tools/retrieval:** local reads and scripts only.
- **Compliance flags:** none.
- **Approx. cost/time:** Human: 0. Machine: ~45 min.

## [2026-09-24] Session 1 (cont.) — 4B gate; Stage 4C fat outline v0.1
- **Models/agents:** Claude (drafting agent); paper-auditor ×1 (sonnet) for the 4B gate.
- **Human messages (verbatim):** none this segment.
- **AI actions:** 4B gate APPROVE (first pass; the auditor spot-checked 8 page citations against
  the source texts, 7 exact). Its one non-blocking note, that the Quong 2012 definition is on p. 67
  and not "67–68", was checked against the text: the definition is on p. 67 (its tail displaced by a
  footnote in the conversion) and restated in full on p. 72; 4C cites "67, 72". While the gate ran,
  drafted `WIP Docs/Outline/Outline 4C Fat v0.1.md` from 4B v0.1: 44 paragraph bullets with planned
  lengths (2,461 words of bullets). The draft is a working file only; the 4C rounds, argument-clinic
  pass, referee memo and gate follow. A direct download of an open-access copy of source #3
  (Bolinger 2021, PhilArchive) was refused by this session's permission settings; it stays on the
  custodian request list, with the link added for convenience.
- **Selections:** none.
- **Tools/retrieval:** WebSearch ×3 (Ripstein's tort theory and the good-faith-mistake rule in
  trespass; mistaken self-defence in tort; Ripstein 1996 and Bolinger 2021 records).
- **Compliance flags:** none.
- **Approx. cost/time:** Human: 0. Machine: ~40 min.

## [2026-09-24] Session 1 (cont.) — Stage 4C rounds 1–2 and the argument clinic
- **Models/agents:** Claude (drafting agent); referee ×1 (sonnet) launched for the blind outline
  memo.
- **Human messages (verbatim):** none this segment.
- **AI actions:** Built `WIP Docs/Outline/4C Coverage Map v0.1.md`, mapping 38 items (the central
  argument's premises, the crux arguments and planned micro-objections, 13 cases, the planned
  objections and concessions, and the Literature Map's originality risks) to bullets: 21 covered, 10
  partial, 5 gaps, 2 deferred. Re-read the sources to close them: Clark "As If" §III (the trolley
  pair had been misdescribed as differing in a hidden real justification; in fact only the agent's
  evidence differs, and the account's verdict still holds); Quong 2012 n. 30 (his own institutional
  example, the prison guard and the lawfully convicted innocent); Ferzan 2012, 690–91 and n. 72 (her
  refusal of liability for negligently created appearances); Frowe 2010 §II and §VI (her verdict that
  the unaware actor may defend himself); Burri 2022, 540, 545–46 (against the distributive framing);
  Clark 2025, 442 (the distributive-justice quotations). AI decision on the open careless-appearance
  question: estoppel extends to careless conduct ("knowingly or carelessly behaved like an
  attacker"). Round 2 placed every interlocutor in the Literature Map's engagement plan. Wrote
  `Outline 4C Fat v0.2.md`. Then ran the argument-clinic pass (`Scrap/argument-clinic-4C.md`) on
  v0.2: 8 findings. The most serious: the definition of "acting upon" ("singles her out to bear a
  risk") misclassified a known risk to a particular person (a sniper's risk to a hostage). It was
  redefined as aiming to harm, restrain or use a person, or knowingly harming her, with the line at
  practical certainty credited to tort law's definition of intent. Others: the displayed argument
  lacked its standing premise (now six steps); "claims are against conduct" stated; the parity
  objection answered where the independence argument is made; prerogatives placed in the balance of
  claims; the source of authority's entitlement stated; the careless-estoppel standard derived from
  the risk standard; "standing" defined. All fixed in `Outline 4C Fat v0.3.md`, with the body plan
  re-set to 5,630 words because the abstract counts toward the limit. v0.1 and v0.2 moved to `Old
  versions/`. Added source request #19 (Ripstein 2016, *Private Wrongs*). Made a blind copy of v0.3
  without the process header (`Scrap/outline-for-referee-4C.md`) and launched one blind referee on
  it with the standard template (lens: ethics of self-defence; no summary and no leading questions).
- **Plan-level changes to flag at CHECKPOINT 3:** the coined term "acting upon" is redefined; the
  estoppel clause now covers careless conduct; the central argument has six steps.
- **Selections:** none.
- **Tools/retrieval:** WebSearch ×2 (*Ranson v. Kitner* record; Restatement (Second) of Torts §8A
  wording).
- **Compliance flags:** none.
- **Approx. cost/time:** Human: 0. Machine: ~90 min.

## [2026-09-24] Session 1 (cont.) — 4C blind referee memo folded in (v0.4)
- **Models/agents:** Claude (drafting agent); referee ×1 (sonnet), blind.
- **Human messages (verbatim):** none this segment.
- **AI actions:** The blind referee read the v0.3 displays and bullets (no process header, no
  summary, no leading questions). It reported four major concerns (HIGH: the fact/evidence asymmetry
  at the crux was asserted rather than derived; MED: the account's three statuses were hidden in
  Display 1; MED: the budget was tight where the crux needs room; LOW-MED: contractualist vocabulary
  in the reply to the fair-allocation objection). It also named one missing objection (private law's
  strict standards rest on cheap, reversible remedies, while defensive harm is lethal) and four minor
  points. Its odds: about 20% finalist as planned, 45–50% after revision. Dispositions recorded in
  `WIP Docs/Referee Reports/4C outline memo (blind referee) and dispositions.md`: all majors, the
  missing objection and two minors accepted. The central change is a new first argument for the
  crux, from authority, originated by the AI in response to the HIGH concern. Evidence gives a
  permission, not a power over another; no private person's judgment binds another. So only the
  person's own acts, the balance of claims and legitimate authority can permit acting upon him. The
  careful driver passes no judgment on what the pedestrian may be subjected to. The difference
  between the twin and the pedestrian is subjection, not luck. Kant's innate right (6:237) is
  credited; its wording was confirmed by web search, while a second Kant passage (6:312) could not be
  confirmed and is not quoted. Wrote `Outline 4C Fat v0.4.md` (45 paragraphs, 5,560-word body); v0.3
  moved to `Old versions/`. Added source requests #20 (Kant, *Metaphysics of Morals*) and #21
  (Ripstein 2009, *Force and Freedom*). One further repair made unprompted: 3.1 now says that
  "violation" is fact-relative and "permission" evidence-relative, which blocks a Hohfeldian
  objection (a liberty to attack would otherwise imply the twin has no claim).
- **Selections:** none.
- **Tools/retrieval:** WebSearch ×4 (two Kant passages; the venue of Clark's "As If", unresolved,
  query #18 stays open).
- **Compliance flags:** none.
- **Approx. cost/time:** Human: 0. Machine: ~60 min (referee ~15 min).

## [2026-09-24] Session 1 (cont.) — 4C gate
- **Models/agents:** paper-auditor ×1 (haiku).
- **Human messages (verbatim):** none this segment.
- **AI actions:** Before the gate, a deterministic self-check: a bullet-by-bullet diff of v0.3
  against v0.4. It found two small consistency edits (5.4, 6.5) missing from the v0.4 changelog;
  they were added. 4C gate APPROVE on the first pass. The auditor verified the Coverage Map rounds
  (5 dispositions spot-checked in v0.2), the argument-clinic fixes (4 of 8 in v0.3), the referee
  dispositions (4 in v0.4) and the blindness of the referee's input file. It also checked four
  accuracy fixes against the source texts: Clark's trolley pair, Quong's note 30, Ferzan's note 72,
  and Burri 2022's "localised affair". Next: CHECKPOINT 3.
- **Selections:** none.
- **Compliance flags:** none.
- **Approx. cost/time:** Human: 0. Machine: ~15 min.

## [2026-09-24] Session 1 (cont.) — CHECKPOINT 3 (structure)
- **Models/agents:** Claude (drafting agent).
- **Human messages (verbatim):**
  > (CHECKPOINT 3, via interactive menu) "Approve (Recommended)"
- **AI actions:** Presented the outline in plain English: the claim, a seven-section table with
  budgets, and the five changes since CHECKPOINT 2. All five were AI-originated (the new authority
  argument, the refined definition of "acting upon", the careless-bluffer extension, the six-step
  argument, the budget reset for the abstract). Included the reminder that feedback must stay
  generic. Offered four responses: approve / something unclear / too ambitious / pause to read.
- **Selections:** Custodian approved the structure (generic approval; no content supplied). The
  outline `Outline 4C Fat v0.4.md` is locked as the drafting contract.
- **Compliance flags:** none.
- **Approx. cost/time:** Human: ~1 minute. Machine: negligible.

## [2026-09-24] Session 1 (cont.) — Stage 5: Draft v1.0
- **Models/agents:** Claude (drafting agent).
- **Human messages (verbatim):** none this segment.
- **Calibration reads (before the first sentence):** `Playbook/Craft/model-paragraphs.md` in full;
  register samples Quong 2012, pp. 45–50, and Thomson 1991, pp. 283–286 (read for how the
  sentences move); `Playbook/Craft/prose-principles.md`; the Style Guide's apparatus and snap
  budgets; `Playbook/Craft/moves-catalog.md` Part 2.
- **AI actions:** Before drafting, re-checked against the source texts every case description and
  quotation the prose would retell. Confirmed: the case wordings (Quong 2012, 53, 57, 61–62; McMahan
  2005a, 387, 393, 397, 399, 403; Clark 2025, 430–33; Burri 2025 §4, §6.1), Thomson 1991, 301
  ("agency is no more required …"), Ferzan 2012, 682 n. 49 ("all that morality can fairly ask of
  them"), and McMahan 2005a, 394 (the driver's "couple of tons of steel", "it is fair that he should
  suffer"; the difference is "of comparatively slight moral significance"). Found and corrected two
  errors that had survived into the locked outline. (1) Burri's account does not clear the
  resident: she holds him liable by finding an earlier fault (warned of a killer, he should not
  have opened his door, 2025 §4), and she accepts non-liability only in her amended duped-soldiers
  case (§6.1). §1 and §2 were written accordingly. (2) Clark's third problem for treating apparent
  attackers as liable concerns an informed bystander's incentive to stay silent (2025, 438–39), not
  "rewarding convincing threats". The coerced-attacker case is now credited to its source (Burri
  2025 §4, "Duress"). Wrote `WIP Docs/Drafts/Draft v1.0.md` in one pass from `Outline 4C Fat v0.4.md`
  (45 paragraphs, two displays, one paragraph per line). §6 first came out about 300 words short
  and was unpacked to budget in the same pass (no new content). Body 5,737 words against a 5,560
  plan. Ran `prose_lint.py`: apparatus within budget; the one banned phrase ("the upshot is") was
  replaced; triads and fragments are carried to Stage 6. Items noticed but deliberately left for the
  quality passes are in `Scrap/stage6-notes.md` (one precursor credit found: McMahan 2005a, 402).
- **Selections:** none.
- **Compliance flags:** none. The essay text does not mention its authorship, the competition or
  its process.
- **Approx. cost/time:** Human: 0. Machine: ~75 min.

## [2026-09-24] Session 1 (cont.) — Draft v1.0 gate
- **Models/agents:** paper-auditor ×1 (haiku).
- **Human messages (verbatim):** none this segment.
- **AI actions:** Draft v1.0 gate APPROVE (first pass). The auditor matched the draft to the locked
  outline (7 sections, 45 paragraphs, 2 displays), confirmed the calibration log and the (verify)
  tags, and verified the three source corrections against the texts (Burri 2025 §4 and §6.1; Clark
  2025, 438–39; Burri 2025 §4, "Duress"). Its word count (5,952) includes the title and changelog
  lines; the essay body is 5,737.
- **Selections:** none.
- **Compliance flags:** none.
- **Approx. cost/time:** Human: 0. Machine: ~10 min.

## [2026-09-24] Session 1 (cont.) — Stage 6 pass 1 (v1.1)
- **Models/agents:** Claude (drafting agent).
- **Human messages (verbatim):** none this segment.
- **Calibration:** `Craft/model-paragraphs.md` (already read in full this session; re-scanned);
  register sample, a fresh stretch: Quong 2012, pp. 55–57.
- **AI actions:** Content pass on Draft v1.0, saved as `Draft v1.1.md`.
  - Added, each checked against the source texts before use:
    - McMahan's remark anticipating the knowing/unknowing line (2005a, 402);
    - a police-marksman illustration of a known risk to a particular person;
    - the source for Quong's treatment of bluffers as liable (2009, 519);
    - Ferzan's point that the resident gambles either way (2012, 682 n. 49), accepted and redirected;
    - McMahan's second argument for the driver's liability (as reconstructed by Quong 2012, 57), answered by modularity;
    - McMahan's premise that the driver "will therefore violate" the pedestrian's right (2005a, 403), named and denied.
  - Corrected after a full re-read: the private-law parallel had overstated the law. The law does
    excuse reasonable mistakes in self-defence (Restatement (Second) of Torts §63, wording confirmed
    by web search). The paragraph now claims only the property case (*Ranson*) and names the
    self-defence privilege as the fair-allocation view answered in §6.
  - Removed a duplicate, a false gloss, and an overclaim about the resident's avoidable burden.
  - Self-check: a paragraph-level diff shows 12 changed paragraphs, all listed in the changelog.
    v1.0 moved to `Old versions/`.
- **Selections:** none.
- **Tools/retrieval:** WebSearch ×1 (Restatement (Second) of Torts §63).
- **Compliance flags:** none.
- **Approx. cost/time:** Human: 0. Machine: ~45 min.

## [2026-09-24] Session 1 (cont.) — Stage 6 pass 2 (v1.2)
- **Models/agents:** Claude (drafting agent).
- **Human messages (verbatim):** none this segment.
- **Calibration:** `Craft/model-paragraphs.md` re-scanned (in context from this session's full
  read), with its negative specimen in view.
- **AI actions:** Cut pass on v1.1, saved as `Draft v1.2.md`. The body went from 5,989 to 5,632
  words, which leaves room for a ~150-word abstract under the 6,000 limit. No argument, case or
  citation was removed, except one duplicated McMahan quotation. Five sentence fragments were
  rewritten.
  - Self-check (scripted): every citation in v1.1 is present in v1.2, and all 14 (verify) tags
    survive.
  - `prose_lint.py`: apparatus within budget. Fragments and triads dispositioned in the changelog;
    triads are left for Stage 7b.
  - Pass 2 changed no content, so Stage 6 is judged converged. v1.1 moved to `Old versions/`.
- **Selections:** none.
- **Compliance flags:** none.
- **Approx. cost/time:** Human: 0. Machine: ~40 min.

## [2026-09-24] Session 1 (cont.) — Stage 7a and 7b (v1.3, v1.4)
- **Models/agents:** Claude (drafting agent); prose-rewriter ×4 (sonnet), one each for sections
  1–2, 3, 4–5 and 6–7. Four rather than seven (one per section) to use subagents sparingly.
- **Human messages (verbatim):** none this segment.
- **7a, register rewrite in fresh contexts.**
  - Each rewriter received only its section text (extracted to `Scrap/7a/`), the one-sentence
    thesis and the register-sample line ranges. Each calibrated on the model paragraphs and the
    Style Guide and returned a memo (rewrite, change table, flags). All four stayed within +5%.
  - The drafting agent applied the memos selectively (`Scrap/7a/*_applied.md`), assembled as
    `Draft v1.3.md`.
  - Accepted: splitting compressed sentences, flattening colon-reveals, the key term "confer" over
    "supply", "the Conferral Account" over "the account" in §4, the ordinal list of Clark's four
    problems, one paragraph split in §6, and two added one-line conclusions in §3.
  - Rejected or corrected:
    - (§4–5) a pronoun error introduced in the trolley verdict ("he is liable" for the female agent);
    - (§6–7) a change of meaning ("the objection fails even on its own terms" for "the first reply
      is in the account's own terms");
    - (§3) the marksman sentence rewritten back into one plain sentence;
    - (§1–2 and §4) splits that re-created sentence fragments.
  - Flags acted on:
    - the fact-/evidence-relative senses now defined before first use (§2, Quong 2012, 48);
    - Burri's own reason for finding fault in the resident (duties "can stretch out over time",
      Burri 2025 §4; checked in the text);
    - "the driver" disambiguated;
    - both versions of Clark's trolley case stated (five people versus two, checked against Clark
      "As If" §III);
    - the labels "argument from appearance" and "parity objection" introduced in §3;
    - McMahan's first premise made explicit about killing;
    - the contrast of the third objection with the first two named.
  - Flags noted without change: that "the manager" is introduced in §1, and that the dense §3
    paragraphs could not be thinned without cutting content.
- **7b, condense and strip** (`Draft v1.4.md`): the self-edit sequence and ai-tells sweep; about 25
  targeted edits merging over-split sentences, removing two redundant sentences in §6, and trimming
  elsewhere. Body 5,860 → 5,771. No citation lost; 14 (verify) tags kept. `prose_lint.py` flags
  dispositioned in the changelog. v1.2 and v1.3 moved to `Old versions/`.
- **Next:** 7c cold read on a clean copy (`Scrap/7c/essay-v1.4-clean.md`, title and body only).
- **Selections:** none.
- **Compliance flags:** none.
- **Approx. cost/time:** Human: 0. Machine: ~2.5 h (rewriters ran in parallel, 18–37 min each).

## [2026-09-24] Session 1 (cont.) — Stage 7c round 1 (cold read of v1.4) and fixes (v1.5)
- **Models/agents:** cold-reader ×1 (sonnet, fresh), given only `Scrap/7c/essay-v1.4-clean.md`.
- **Human messages (verbatim):** none this segment.
- **Cold read result:** one-read test passed. The reader restated the thesis and argument with no
  mismatch. Friction score 11 ("needs another round"), counted per pattern:
  - 3 re-read sentences (Quong's quoted test; Display 1's exception clause; a trolley ellipsis);
  - 2 definition hunts (Clark's "two background theories"; the short title "As If");
  - 1 apparatus-overload point (several dated works per author, plus legal citations);
  - 2 unearned steps and 1 soft one (why the balance of claims does not undercut the second
    argument; why a surviving claim keeps necessity in force; the prerogative step);
  - 2 register patterns: the 14 unresolved (verify) tags, the main drag; and four aphoristic
    lines.
- **AI actions (v1.5):** all items fixed except the verify tags, which are placeholders to be
  discharged at Stage 10. From now on, reading copies for readers (cold reader, custodian,
  referees) strip them, while the working draft keeps them. Display 1's exception reworded for
  clarity with the same content. Both unearned steps walked through. Clark's two theories named
  (checked: Clark 2025, sections V.A–B, pp. 442–50). Clark's "As If" now cited author-date as
  "Clark n.d.". Two aphoristic lines flattened. "See Ripstein 2009" dropped. §4's premise map
  shortened. Body 5,807 words. Made `Scrap/7c/essay-v1.5-reading-copy.md` (tags stripped; one
  empty-parentheses artifact fixed by hand).
- **Next:** 7c round 2 with a fresh cold reader on the v1.5 reading copy.
- **Selections:** none. **Compliance flags:** none.
- **Approx. cost/time:** Human: 0. Machine: ~40 min.

## [2026-09-24] Session 1 (cont.) — Stage 7c round 2 (cold read of v1.5) and fixes (v1.6)
- **Models/agents:** cold-reader ×1 (sonnet, fresh), given only the v1.5 reading copy.
- **Human messages (verbatim):** none this segment.
- **Cold read result:** one-read test passed with no mismatch. Friction 11, all new items; the
  round-1 fixes held. Items:
  - 4 re-read sentences;
  - 2 definition hunts (Renzo unintroduced; Clark's "further worry" against "two objections");
  - 1 apparatus-overload point (the trolley cases relied on in §2 before being described);
  - 2 unearned steps (the blurred line; the burden reply redescribing rather than justifying);
  - 1 register pattern (aphoristic paragraph closers).
- **AI actions (v1.6):** all 11 items fixed. The burden reply now gives its reason: only one party
  made a choice that put the stakes in play. The borderline-cases sentence is completed with an
  explicit concession. Offsetting cuts:
  - the ambulance-driver example;
  - a second McMahan concession quote;
  - one closing line.

  Body 5,831. Wrote `Scrap/make_reading_copy.py`, a reusable script that strips the placeholder
  tags for reading copies and fails on any leftover artifact. Made the v1.6 reading copy with it.
- **Length note:** 5,831 + abstract (~120) + title and headings (~25) ≈ 5,976. The Stage 10 length
  pass must find about 100 words. Rule for the referee loop: every addition must be offset.
- **Selections:** none. **Compliance flags:** none.
- **Approx. cost/time:** Human: 0. Machine: ~35 min.

## [2026-09-24] Session 1 (cont.) — Stage 7c round 3 (cold read of v1.6) and fixes (v1.7)
- **Models/agents:** cold-reader ×1 (sonnet, fresh), given only the v1.6 reading copy.
- **Human messages (verbatim):** none this segment.
- **Cold read result:** one-read test passed with no mismatch. Friction 13, clustered around one hot
  spot: Clark's case apparatus (warehouse, hiker, the paired trolley cases) in §2 and its payoff in
  §4. Quong's long quoted test was flagged by all three readers so far.
- **AI actions (v1.7):**
  - Structural fix: the paired trolley cases are no longer retold. The arbitrariness objection is
    stated, and answered, in principle: whether an entitlement exists does not depend on what else
    the agent's evidence would have supported, so the agent is liable in both cases.
  - Dropped: Clark's third worry (an unintroduced aside); the repeated triad in §3; a tricolon
    closer in §5.
  - Quong's quotation shortened with an ellipsis.
  - Restructured: two knotted sentences; the prerogative paragraph, which now separates the
    pedestrian's question from the driver's liability.
  - The necessity problem is now answered on its own terms.
  - Body 5,787, with no citation lost.
- **Selections:** none. **Compliance flags:** none.
- **Approx. cost/time:** Human: 0. Machine: ~30 min.

## [2026-09-24] Session 1 (cont.) — Stage 7c round 4 (cold read of v1.7) and fixes (v1.8)
- **Models/agents:** cold-reader ×1 (sonnet, fresh), given only the v1.7 reading copy.
- **Human messages (verbatim):** none this segment.
- **Cold read result:** one-read test passed with no mismatch. Friction 11. Items:
  - Display 1's pronouns;
  - a double-negative sentence;
  - the abstract paired cases, which were hard to picture after the round-3 simplification;
  - a fact-/evidence-relative reuse;
  - the fair-allocation view possibly confused with the distributive view;
  - apparatus density at §2's Clark paragraph;
  - an unearned dismissal of Lang;
  - an abstract fourth problem;
  - a rhetorical-question tic;
  - unparallel numbering of the four replies.
- **AI actions (v1.8):** all items fixed. Integrity point: the old reply to Lang characterised what
  Lang's arguments target, but Lang 2022 is not on disk, so the claim could not be verified. It was
  replaced by a reply on the merits. The Quong 2020 sentence was also removed until the book is in
  hand. Offsets:
  - the §1 rival sentence;
  - the §6 response and its reply;
  - the Burri 2020 and Frowe 2022 sentences in §3 (sources not yet received; to be re-added on
    receipt if space allows);
  - a concession clause;
  - a duplicated conclusion sentence.

  Body 5,754; 10 (verify) tags remain.
- **Observation for the methodology report:** four fresh cold readers each logged 11–13 items, and
  each passed the one-read test. The items were largely different each round, and fixes held. One
  structural hot spot (Clark's case apparatus) recurred and was fixed structurally in v1.7–v1.8.
- **Selections:** none. **Compliance flags:** none.
- **Approx. cost/time:** Human: 0. Machine: ~30 min.
