# DIGEST — the always-on core

The compressed synthesis of the whole playbook. **Load this every session; pull the deep files only
when the task needs them** (table in §10). Hard cap: 2,000 words — to add here, demote something.
Precedence on any conflict: root `CLAUDE.md` → §8 Adjudications here → the owning deep file →
the Moves Catalog (§11).

## 0. The venue and the two hard constraints

- **Venue:** the AI Philosophy Competition — ≤ 6,000 words excluding bibliography (everything else
  counts); deadline Oct 31, 2026; graded on **Clarity, Argumentation, Significance, Originality,
  Engagement, Accuracy**; anonymized; prompt injection = disqualification. Full brief:
  `Competition/Competition Brief.md`.
- **Compliance:** every substantive philosophical contribution originates with the AI. The custodian
  chooses topics, selects among outputs, gives generic feedback; a custodian message carrying
  philosophical substance is flagged, quarantined, logged, never used
  (`Competition/Rules — Human Involvement.md`).
- **Logging:** every session appends to the essay's `Methodology/Process Log.md` — verbatim human
  messages, AI actions, models, candidate counts, selections, flags. Unlogged work didn't happen
  (`Playbook/3. Methodology Protocol.md`).

## 1. The contribution test (before anything else)

- One sentence: *"I argue that **P**, against the view that **Q**, on the grounds that **R**."*
  Can't fill it in → a topic, not a thesis.
- **One spine.** One decisive contribution — new argument, new distinction, counterexample,
  reframing, or diagnosis — beats three adequate ones. Name which type this essay makes.
- **Narrow and complete** beats grand and gestured. State what you are *not* claiming, in its own
  sentence, right after the positive claim.
- The contribution must be legible by the end of page one — and **checked for originality against
  the literature**, not assumed (Stages 1, 2, 10).
- Find **the crux** — the sub-problem that makes or breaks the thesis — and solve it before
  building anything else on top.

## 2. Structure (the field conventions, at 6k scale)

- **Open on a concrete hook**: a named case, a sharp puzzle, or a real event abstracted within a
  page. A gap-framed first line only when the gap itself is the hook. Never "much has been written
  about X"; never a lit review before the thesis.
- **Thesis early (by p.2), stated twice** (compressed + fully scoped), **named**, distinguished from
  its two nearest rivals *in the paragraph that introduces it*. Prefer "can/often" over
  "must/always" when the weaker modality still makes the contribution.
- **Cases are machinery**: minimal (3–6 sentences), built in pairs varying **one feature at a
  time**, verdict sentence immediately after; at most three carry names, told inline, not displayed.
- **THE APPARATUS BUDGET (hard, per essay)**: 1 named view + ≤1 named rival + ≤1 further coined term
  + ≤3 named cases + exactly 2 displays (the view; the premise-form central argument) + 1 metaphor
  that may illustrate, never argue and never become an essay-wide vocabulary. Everything else is
  plain description. `prose_lint.py` counts; over budget needs a changelog justification.
- **Objections in three layers**: preemptive caveats up front; mid-argument micro-objections; one
  dedicated section for the strongest objection or best rival. Steelman; concede what you can;
  close each objection with a flat verdict.
- **Literature selectively and asymmetrically**: at 6k, ONE closely engaged rival (two at most);
  everyone else in footnotes. No survey.
- **Signpost**: roadmap paragraph ends the intro; each section opens by recalling the dialectical
  position; each paragraph opens with a topic sentence naming its job.
- **Conclusion restates the result**, re-marks scope, adds nothing new.
- 5–7 numbered sections; the central argument once, in premise form, defense locations named
  (`Playbook/2. Essay Style Guide.md` has the display mechanics and both budgets).

## 3. Prose: the self-edit sequence

(1) one statable claim per paragraph, up front → (2) given→new flow across sentences → (3) concrete
subjects, active verbs; de-nominalize → (4) repeat key terms, never elegant variation → (5) keep
hedges that narrow content, cut hedges that only lower confidence (exception: intuitive case
verdicts keep one light hedge — §8) → (6) cut 10–20% → (7) strip AI-tells (`Craft/ai-tells.md`) →
(8) read aloud; vary rhythm.

## 4. The register — and the calibration duty

Simple, clear, even boring academic prose — invisible prose; the reader notices the argument, never
the writing. Tie-breaker on every sentence: **invisible beats clever** (the essay earns 2–3 pointed
landings, total; each snap move from the Moves Catalog at most twice; most paragraphs end
workmanlike). Short anchoring sentences at the pivots; thesis, definitions, and objection-closers
flat; explain before use; reasoning unpacked, never compressed — cleverness compresses, explanation
expands; no metaphor doing argument work; concrete before abstract; plain referents repeated; "I"
throughout; em dashes minimal. **Calibrate before every prose session**: read
`Craft/model-paragraphs.md` in full, fresh (the patterns fade fast), plus 5–10 pages of the essay's
chosen register samples from `Background Readings/`; log both reads. Full rules:
`Playbook/2. Essay Style Guide.md`; craft depth: `Craft/prose-principles.md`.

## 5. The Moves Catalog — and the anonymity rule

`Craft/moves-catalog.md` is the bank of transferable techniques: Part 1 argument architectures
(pick 2–3 at Plan/Outline time by contribution type), Part 2 prose moves (drafting and clarity
passes). Two standing rules (canonical in `Craft/README.md`): **the playbook names no real authors
or papers** — craft lessons are kept as anonymous, abstract rules (essays, by contrast, cite the
real literature by name, verified); and **techniques are executed in the essay's own material** —
no pastiche, no imported cases, coinages, or sentences.

## 6. Top AI-tells

"delve", "it is important to note", "crucial/vital" as reflexes, "not only X but also Y" on repeat,
stacked triads, listicle-ified arguments, hollow recaps, confident vagueness, uniform sentence
length, participial tack-ons, fake-profound kickers. Full list + cadence checks: `Craft/ai-tells.md`.
The aim is prose quality, never disguise.

## 7. The pass pipeline (per essay, in order)

Setup → Idea Generation & Selection (P/Q/R candidates, originality pre-screen, crux) → Lit Review →
Plan → Outline 4A/4B/4C (fat = ~30–40% of 6k) + argument-clinic pass → Draft v1.0 (full density =
full information, unpacked at reading speed) → Quality passes → **Clarity chain** (7a prose-rewriter
per section in fresh contexts → 7b condense/tell-strip + `prose_lint.py` → 7c cold-reader friction
report; repeat until clean) → Custodian read (generic only; style feedback invited — it is
compliance-free) → **Iterative referee loop** (blind panels; revise; prose-rewriter over rewritten
passages; repeat to convergence) → Finishing (abstract last; citation audit; length; lint;
anonymity + injection sweep; final cold read) → Methodology report → Ship → Retrospective (add
moves to the catalog, update this playbook). Full procedure:
`Playbook/1. Pipeline — Competition Edition.md`.

## 8. Adjudications (canonical here on any conflict)

- **Hedging by function**: intuitive case verdicts get one light hedge ("It seems plausible that…");
  definitions, inferences, the thesis, and objection-closers stay flat.
- **Footnotes**: qualifications, literature, scope-limits below the line; **no substantive argument
  in footnotes** — if a footnote argues, promote it or cut it.
- **Closings**: plain restatement + scope; one crisp final sentence permitted if the body earned it;
  an explicitly flagged open question is fine; future-work filler is not.
- **Paragraph endings**: a "Thus/Hence…" closer that *completes an inferential step* is field
  register; a closer that merely repeats the paragraph is the recap-tell. Close on the inference
  earned; never echo.
- **Openings**: concrete hook first is the default; a sharp gap opening is legitimate when the gap
  is the surprise and carries the motivation; limp gap-framing stays banned.
- **Em-dashes**: not a field tell, but the house preference is minimal — commas, colons, parentheses
  first; a gloss-dash only where clearly the best tool.
- **Premise-form arguments**: the central argument appears once as displayed premises (house rule,
  from the Style Guide); everywhere else, prose with displayed principles and named cases —
  numbered-premise format as the *primary* expository mode reads as a student exercise
  (`Craft/journal-craft.md` §5).
- **Referee labels**: never chase accept/reject labels; read trajectory and convergent issues. The
  loop stops on convergence, not on a verdict.
- **Register lock-in**: prose that reads AI-written, over-compressed, or over-clever goes to the
  **prose-rewriter** in a fresh context (never the drafting context); comprehension is measured by
  the **cold-reader**'s friction score, and the clarity stage exits only on a clean read.

## 9. Anti-fabrication (non-negotiable)

Never invent a reference, page number, quotation, or attribution. Ground literature claims in real
texts (`Background Readings/` or verified web sources) — training memory is not a source. Mark
reconstructions ("roughly," "in effect"); `(verify)` tags and honest placeholders beat guesses; the
citation-auditor discharges them before anything ships. A needed source we can't access goes on the
**request list** for the custodian (`Playbook/5. Literature Access Protocol.md`) — never faked,
never silently skipped.

## 10. What to load, when

| Task | Pull these deep files |
|---|---|
| Any session's start | This DIGEST + the essay's Checklist + Process Log |
| Idea generation / thesis testing | §1 here + `Craft/journal-craft.md` §1–2 + Pipeline Stage 1 |
| Structure / intro / outline work | `Craft/journal-craft.md` + `Craft/intro-playbook.md` + `Craft/moves-catalog.md` Part 1 |
| Argument pressure-testing | `.claude/skills/argument-clinic` procedure |
| Any prose session (first!) | `Craft/model-paragraphs.md` (in full, fresh) + the essay's register samples |
| Drafting prose / quality passes | `2. Essay Style Guide.md` (incl. both budgets) + `Craft/prose-principles.md` + `Craft/moves-catalog.md` Part 2 |
| Clarity chain | 7a: prose-rewriter agent · 7b: `Craft/ai-tells.md` + self-edit sequence + `prose_lint.py` · 7c: cold-reader agent |
| Referee loop | Pipeline Stage 9 + `Playbook/Referee Templates/` |
| Abstract & title | `Craft/abstracts-and-titles.md` |
| Citation verification | citation-auditor agent + `check-citations.py` (Build scripts) |
| Sources we lack | `5. Literature Access Protocol.md` |
| Compliance question | `Competition/Rules — Human Involvement.md` |

## 11. Rule ownership

One canonical home per judgment; fix drift at the owner, point from everywhere else:

- Compliance → `Competition/Rules — Human Involvement.md`. Process → the Pipeline. Logging →
  `3. Methodology Protocol.md`.
- Register/style adjudications → **§8 here** (canonical). Essay mechanics (length, displays,
  citations) → `2. Essay Style Guide.md`.
- Structure craft → `Craft/journal-craft.md`; sentence craft → `Craft/prose-principles.md`;
  AI-tells → `Craft/ai-tells.md`; abstracts/titles → `Craft/abstracts-and-titles.md`; the move
  bank → `Craft/moves-catalog.md`; the anonymity rule → `Craft/README.md`.
