#!/usr/bin/env python3
"""Build '1a. Pipeline v1.0.docx' (General Guide to Academic Writing/) — the Shareable
Edition's core operating procedure, generalized from the original agent's Pipeline v0.15.
The Word master may be edited by the author after first generation — check mirrors/mtimes
before regenerating (versioning rules apply)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_docx import build

GG = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
                  "General Guide to Academic Writing")

B = []
B.append(("title", "Pipeline: How We Write a Paper"))
B.append(("subtitle", "The process Claude follows for every paper in the Deep Drafter. "
          "v1.0 — Shareable Edition, July 2026. Generalized from the original agent's pipeline after several "
          "complete papers; every standing rule below earned its place on a real draft."))
B.append(("note", "HOW TO USE THIS DOC. This is the operating procedure for drafting an academic paper with the "
          "author. Claude follows these stages in order. After producing each deliverable Claude runs its own "
          "lenses (A/E/S/I), invokes any specialist agents the stage calls for, then the AUDITOR gate at the "
          "RESERVED gates only (early stages, first draft, every author round, final) — elsewhere a deterministic "
          "self-check on the Change Log stands in for it — and stops at each gate until APPROVE (and, at the human "
          "checkpoints, until the author signs off). We work OUTLINE-FIRST: the outline is built in three layers "
          "and the paragraph layer is the DRAFTING CONTRACT — no prose until it is signed off. Drafting lands at "
          "FULL DENSITY (Stage 4), quality passes remove what is bad and add what is good (Stage 5), and the Style "
          "& Voice pass makes every sentence the author's (Stage 6) — only then does the author read (Stage 7, "
          "GATE 3); substantive quality comes from the referee panel (Stage 8). The accountability mechanism is "
          "the Project Checklist (created FIRST, never pre-filled) plus the independent auditor."))

B += [
    ("h1", "Guiding principles"),
    ("bullet", "Outline first, in layers; lock structure before prose. Restructuring an outline is cheap; "
     "restructuring prose is ~10× more expensive in time and author attention. Do the structural work where it "
     "is cheap."),
    ("bullet", "Build a FAT outline (~30–40% of final length). A useful outline for a 25k-word paper is ~8–10k "
     "words of structured bullets — roughly the information density of the final paper, in bullet form. A thin "
     "outline guarantees expensive restructuring later. Err toward more detail."),
    ("bullet", "The paragraph outline is the drafting contract. Once it is approved, drafting is mostly expansion "
     "into prose. Write no prose until it is signed off (Human Gate 2)."),
    ("bullet", "Separate mechanical drafting from quality work. One pass converts each bullet to its paragraph "
     "with NO polishing; quality is its own separate set of passes. Mixing them yields uneven sections."),
    ("bullet", "Quality passes improve the paper in both directions: remove stuff that is bad and add stuff that "
     "is good — where 'good' includes explanation, examples, stylistic material, and NEW ARGUMENTS. Cut "
     "editorializing, repetition, and decoration; add whatever makes the paper better. Length is an outcome of "
     "those two duties, not a pass constraint; the target length is managed at Stage 10, never by starving the "
     "paper."),
    ("bullet", "An independent auditor gates the RESERVED gates — integrity only. Its sole job is to verify, "
     "against the files, that the work a checklist row claims as done was genuinely done — reserved for the "
     "early stages, the first draft, every author round, and the final check. On the agent's own incremental "
     "revisions a deterministic self-check on the Change Log (isolation diff + verify scripts) stands in for it. "
     "It does NOT judge quality. You may not pass a reserved gate until it APPROVES. (It exists because agents "
     "otherwise record steps as done without doing them.)"),
    ("bullet", "Quality is enforced by specialist agents: the multi-persona REFEREE panel (simulated peer review, "
     "spawned BLIND — each referee gets only its lens, the manuscript, and the venue, never a claim-summary or "
     "leading questions), the CITATION-AUDITOR (no fabricated cites; verified pinpoints), and the COPY-CRITIC "
     "(mistakes + anti-LLM tics). Invoke them where the stages below say to."),
    ("bullet", "The author's edits set DIRECTION — they are not frozen text. Anyone may improve author-touched "
     "text further. What is FORBIDDEN is regression: never revert, in substance or wording, to a formulation the "
     "author already overruled — the author's deletions and replacements define the overruled set, recorded in "
     "the Change Logs and the returned '- edits' files. Before changing author-touched text, check the change "
     "against that record; improvements to the author's text are surfaced in the version's changelog so the "
     "trajectory is visible. The test is monotonic improvement: continuing to improve rather than going in "
     "circles."),
    ("bullet", "Word documents; never overwrite; version at gates. Every deliverable is a .docx (author-facing "
     "paper drafts with gen_paper_docx; structured working docs with gen_docx; edit prose docs in place). Each "
     "gated revision is a new numbered version; superseded versions move to Old versions/. Build .pdf/.tex only "
     "at submission and only when the type calls for it."),
    ("bullet", "Never fabricate — not work, not sources. Ground every claim about the literature in the real PDFs "
     "in Background Readings/, not training memory (unreliable on secondary literature and pinpoints). During "
     "drafting, citations are honest placeholders — '(Smith 2024)' — and every empirical claim gets a (verify) "
     "tag the citation-auditor later checks."),
    ("bullet", "Match the target venue's register. The Writing Guide is the shared core; the paper-type Style "
     "Module sets length, citation/footnote practice, structure, and register (a philosophy journal ≠ a law "
     "review ≠ a monograph ≠ an empirical venue)."),
    ("bullet", "Self-critique before showing the author, and surface judgment calls. Present your best work, not "
     "first drafts of your reasoning; when choosing between two defensible options (framing, terminology, "
     "emphasis), surface the choice rather than deciding silently. Prefer cutting or footnoting to hedging."),
    ("bullet", "Four human checkpoints — Argument Sketch, Plan, Paragraph Outline, the voiced Draft — plus the "
     "author-owned Finish gate, unless the author says 'run straight through' (fully autonomous, auditor-only). "
     "Tier the effort: the fat outline, the draft, and the referee rounds are HIGH tier and get the closest "
     "scrutiny."),
]

B += [
    ("h1", "Structural design principles (defaults for argumentative papers — confirmed or replaced at setup)"),
    ("body", "These emerged as load-bearing for strongly argumentative papers (philosophy, law, argumentative "
     "social science). They shape the outline and the draft. Empirical and narrative genres replace the "
     "section-structure defaults with their Style Module's conventions; the thesis-front-loading and "
     "concreteness principles survive almost everywhere."),
    ("bullet", "~3–5 arguments per section/subsection, each its own paragraph, explicitly numbered (\"First… "
     "Second… Third…\"). Depends on the argumentation — don't pad to hit a count."),
    ("bullet", "Named arguments with stable labels (1–3 words), reused verbatim across abstract, intro, body "
     "headings, cross-references, and conclusion."),
    ("bullet", "Interleaved objections, plus a dedicated section for the 1–3 largest cross-cutting ones. Local "
     "objections live with their argument; only whole-thesis objections get their own section. Brief steelman, "
     "then direct response. Don't over-compress objections into a one-sided polemic; don't pad them either."),
    ("bullet", "A concrete example, name, case, or number in every paragraph. Abstract claims need anchor points; "
     "historical precedents are powerful when the topic is novel."),
    ("bullet", "Front-loaded thesis — it appears in the abstract, the first paragraph of the introduction, and "
     "the first paragraph of the body. A reader who stops after page one knows exactly what the paper argues."),
    ("bullet", "Stable section numbers; resolve cross-references in one verified pass. No \"what we're not going "
     "to discuss\" bullets; no verbal disputes (pick a meaning, state it, move on)."),
]

B += [
    ("h1", "The agents"),
    ("h2", "The auditor — the integrity gate at the reserved gates"),
    ("body", "The paper-auditor subagent (.claude/agents/paper-auditor.md) is the honesty gate. Claude builds the "
     "paper; the auditor decides whether each stage's claimed work was actually done before Claude may move on. "
     "It is RESERVED for the high-value gates (early stages, first draft, every author round, final); on "
     "Claude's own incremental revisions, a deterministic self-check on the Change Log stands in for it."),
    ("bullet", "After producing a deliverable AND running your own lenses (and any specialist passes the stage "
     "calls for), spawn the paper-auditor (Agent tool, subagent_type: paper-auditor). Tell it the STAGE and the "
     "file path(s). Keep using the SAME auditor across stages (continue it) so it accrues context — but it must "
     "re-derive findings from the files each time, not from memory."),
    ("bullet", "If the verdict is REVISE, do every required fix, then re-audit. Only on VERDICT: APPROVE do you "
     "record the gate row (paste the verdict line) and proceed."),
    ("bullet", "The auditor judges ONLY whether the work happened (counts, diffs, artifact existence). Whether "
     "the argument is good, a citation correct, the prose clean — that is the specialists' job, below."),
    ("bullet", "Model tiering: procedural audits (file/count/diff/anchor checks, protocol verification, re-checks "
     "of specified fixes) run on a cheaper model so they never leave the author waiting; the stronger default "
     "model is reserved for judgment audits (did an intellectual round genuinely happen; is a reconciliation "
     "sound)."),
    ("h2", "The specialist quality agents — when to call them"),
    ("bullet", "referee (referee.md) — at Stage 8, spawn THREE in parallel (the paper type's fixed lens trio), "
     "each BLIND (lens + manuscript + venue only; no claim-summary, no leading questions — use the prompts in "
     "Referee Templates/), reading the manuscript INCLUDING footnotes; implement the consensus (≥2 referees) but "
     "read the TRAJECTORY and specific issues, not the accept/R&R label (AI referees almost never say 'accept'); "
     "add one 'case-for-acceptance' reader; cap at two substantive rounds plus a blind pre-submission read. Also "
     "spawn ONE referee as a 'review memo' on the paragraph outline at 3C before the drafting-contract sign-off."),
    ("bullet", "citation-auditor (citation-auditor.md) — at Stage 10: at least once before the first referee "
     "round and once before submission, and on any newly added or referee-suggested citation."),
    ("bullet", "copy-critic (copy-critic.md) — at Stage 10 for the anti-LLM prose pass and the pre-send review."),
    ("body", "All three specialists PROPOSE; Claude (or the author) disposes. They do not edit the paper; Claude "
     "applies the consensus/approved fixes, and the auditor then confirms the fixes were actually applied."),
]

B += [
    ("h1", "The review lenses (Claude's own self-review before each auditor gate)"),
    ("body", "When a stage says \"run the lenses,\" apply each named lens ONCE — a real read-critique-improve "
     "pass through a specific frame — and record its outcome on the Checklist with a verifiable artifact or a "
     "specific finding. \"No-change (checked)\" is fine; record what you checked. Then invoke specialists / the "
     "auditor."),
    ("bullet", "A — Argument. Is each claim developed and valid? Is every objection steelmanned then answered? "
     "Any logical gap, any overclaim the argument doesn't earn? (Evidence: the gap closed, or the specific fix.)"),
    ("bullet", "E — Engagement. Are the key interlocutors from the Literature Map engaged, the paper positioned "
     "in its open niche, no straw men, no must-cite work ignored, no conflict with the authors' prior positions? "
     "(Evidence: the engagement added, or the Coverage-Map line.)"),
    ("bullet", "S — Style. Does it obey the Writing Guide — one move per sentence, no editorializing, no verbal "
     "disputes, no point repeated across sections, named-argument labels consistent, model-prose register? "
     "(Evidence: the specific edit, or \"checked — conforms.\")"),
    ("bullet", "I — Integrity. Is every empirical claim cited or (verify)-tagged, no fabricated citation, do all "
     "cross-references resolve, do the claims match the body (\"we make four arguments\" ⇒ four arguments)? "
     "(Evidence: the mismatch found and fixed.)"),
    ("body", "The Plan uses A/E/S/I. The Literature Map uses E/I. 3A uses A/E; 3B and 3C and the Draft use all "
     "four. Length is NOT a per-round lens — it is one light pass in Stage 10."),
]

B += [
    ("h1", "Stage 0 — Setup (read everything first)"),
    ("bullet", "Argument Sketch first. The ideal starting input is the author's half-to-one-page Argument Sketch "
     "— the thesis plus the actual argumentative moves (premises, key steps, the intended payoff). It becomes "
     "the contract the Plan and outline must honor. When the author gives only a topic or a one-line thesis, the "
     "first deliverable is a PROPOSED sketch for sign-off BEFORE any outlining (correcting the architecture on "
     "one page is far cheaper than on a built outline — a real trial run had the plan's architecture wrong until "
     "a one-comment author correction fixed it; an up-front sketch makes that correction free). Save the "
     "signed-off sketch in Brief/. This is Human Checkpoint 0."),
    ("bullet", "Intake FIRST — ask the author up front (don't make them remember to specify). Before scaffolding, "
     "ask the setup questions and let the answers drive everything, LEADING WITH THE PAPER TYPE (it selects the "
     "Style Module — length, citations, structure, register): type; title + one-sentence thesis; target venue + "
     "limit; target length (offer the type default); coauthors + author order (per the field's convention in the "
     "Context doc); model-prose anchor; hard-nos; autonomy (four gates / run straight through / every gate); and "
     "where the brief, readings, and model paper are. Use the interactive picker for the menu choices; record "
     "the answers in the Progress Log and the per-paper profile (Context §5)."),
    ("bullet", "Scaffold the project: run new_paper.py (or copy the Project Template) — this creates the paper's "
     "DEDICATED folder Papers/<title>/, and EVERYTHING for the paper lives inside it (brief, readings, outlines, "
     "drafts, reviews, scratch, build outputs — nothing scattered to the agent root). Create the Project "
     "Checklist FIRST and start the running Progress Log; drive the whole project from the checklist (never "
     "pre-filled)."),
    ("bullet", "Capture the Setup Contract: paper TYPE; target venue; target length (default by type); the "
     "division of labor (how aggressively to cut; whether the author or Claude does the Stage-9 substantive "
     "rewrite); and the model-prose anchor."),
    ("bullet", "Read the core Writing Guide, the paper-type Style Module (and its field-register companion, if "
     "named), the Voice Profile, and the Context doc. Load the author's 1-page Brief (thesis; central arguments; "
     "target journal; word budget; 3–5 key sources) into Brief/, the real PDFs of the core interlocutors into "
     "Background Readings/ (convert to text), and a prior paper to imitate for voice into Model Prose/. Read the "
     "model prose carefully before starting."),
    ("bullet", "Auditor gate — Setup: the auditor confirms the structure, checklist, brief, and reads are "
     "genuinely in place before Stage 1."),

    ("h1", "Stage 1 — Literature Review & Positioning"),
    ("bullet", "Go find the literature — don't rely only on what's handed to you, and never on memory. Actively "
     "search out the relevant books and papers on the topic (WebSearch and scholarly sources): the key "
     "interlocutors, the canonical works, and the recent and opposing positions. Build a relevance-ranked "
     "reading list, then READ the most relevant for familiarization and to place the paper. When a needed source "
     "is paywalled or you cannot access it, FLAG it for the author to supply — never fabricate its contents or "
     "silently skip a load-bearing work."),
    ("bullet", "Read every Background Reading carefully and produce per-source notes. Also research the authors' "
     "OWN prior published work — it informs voice and surfaces positions in their prior work that may conflict "
     "with this paper's thesis."),
    ("bullet", "Produce the Literature Map: the existing critical/constructive landscape; who holds which live "
     "position; the OPEN NICHE this paper will occupy; the key interlocutors to engage; and candidate referees."),
    ("bullet", "Run the lenses (E, I). Auditor gate — Lit Review."),

    ("h1", "Stage 2 — Plan (thesis-sharpening)   [HUMAN GATE 1]"),
    ("bullet", "Produce a research plan / thesis-sharpening doc: the thesis in its sharpest form; the analytic "
     "MOVE that makes the argument work, spelled out explicitly; a reason it is the sharpest version of the "
     "argument rather than just a version; a section-by-section outline with approximate word budgets (scaled to "
     "the target length); the dialectical structure (objections interleaved, dedicated, or both); the "
     "named-argument vocabulary; and the planned formal/technical apparatus, if any."),
    ("bullet", "Run the lenses (A, E, S, I). Auditor gate — Plan."),
    ("bullet", "Human sign-off — Plan [GATE 1]. The author reviews the thesis, the move, the angle, and the "
     "structure before any outline detail. This is the moment to redirect if the angle is wrong — changes here "
     "cost minutes; after drafting they cost hours. (Skipped on 'run straight through'.)"),

    ("h1", "Stage 3 — Layered Outline (3A → 3B → 3C; the fat outline)   [HUMAN GATE 2 at 3C]"),
    ("body", "The outline is built in three layers, each more detailed than the last, each gated. This is the "
     "load-bearing stage — get the structure and the coverage right here, in bullets, where it is cheap to "
     "change. (For empirical papers the outline is organized around the analyses, figures, and tables — the "
     "results are the spine; see the Style Module.)"),
    ("h2", "3A — Skeleton outline"),
    ("bullet", "Lay out the top-level parts/chapters: what each covers, in what order. Run lenses (A, E). "
     "Auditor gate — 3A."),
    ("h2", "3B — Argument outline"),
    ("bullet", "Expand each section premise-by-premise: 3–5 sub-arguments per subsection, each as its own bullet, "
     "with the intended example/evidence attached and the relevant source named; place objections (interleaved "
     "vs dedicated per the Plan); flag cross-references to resolve later. Run lenses (A, E, S, I). Auditor gate "
     "— 3B."),
    ("h2", "3C — Paragraph outline (the FAT outline / drafting contract)   [HIGH tier]"),
    ("bullet", "v0.1 — first pass. Expand 3B into a paragraph-level outline: one bullet per planned paragraph "
     "(~30–40% of final length), each bullet ≈ a 100–150-word drafted paragraph, carrying its claim, its "
     "example, and any (verify)-tagged empirical claim; use named-argument labels and stable section numbers. "
     "Run lenses."),
    ("bullet", "v0.2 — round 1 (completeness / rigor). Map every central argument and every major objection to "
     "specific bullets; build the Argument & Objection Coverage Map (one row per argument/objection → where it "
     "is made/answered → Covered/Partial/Gap); close every gap with new bullets. Auditor gate — 3C round 1 (a "
     "genuine, broad expansion vs v0.1; coverage complete)."),
    ("bullet", "v0.3 — round 2 (literature engagement). Re-read the Literature Map; ensure every key interlocutor "
     "is engaged as bullets, the positioning vs the niche is solid, and any conflict with the authors' prior "
     "work is handled. Auditor gate — 3C round 2 (a genuine engagement expansion vs v0.2)."),
    ("bullet", "Confirm the outline is dense enough to draft from (fat, not padded) and run lenses (A, E, S, I). "
     "Iterate with the author: apply bracketed [initials:] inline comments VERBATIM; iterate to convergence "
     "(stop when the author's comments get shorter and more local — typo-level rather than structural)."),
    ("bullet", "Spawn ONE referee as a Review Memo on the paragraph outline: ranked vulnerabilities, the "
     "strongest missing objection, factual landmines, and the weakest lines — referee proposes, author disposes, "
     "accepted items folded in with a note of which were taken. Auditor gate — 3C FINAL (outline complete, "
     "coverage mapped, dense; the review memo was produced and its accepted dispositions applied)."),
    ("bullet", "Human sign-off — Paragraph Outline = the DRAFTING CONTRACT [GATE 2]. Hold drafting until the "
     "author signs off. (Skipped on 'run straight through'.)"),

    ("h1", "Stage 4 — First Prose Draft (full density)   [HIGH tier]"),
    ("bullet", "Convert the locked fat outline to full prose in a SINGLE pass, at FULL DENSITY: write each "
     "bullet's paragraph(s) to its Part's word budget — the draft lands at target length, not at outline length "
     "(mechanical 'expand each bullet a fixed ratio' rules under-produce at scale and were retired on a real "
     "run). Preserve structure exactly (do not restructure); match the model prose in voice and density; keep "
     "citations as placeholders. Do NO quality work in this pass — that is Stage 5. Save as Draft v1.0."),
    ("bullet", "Run lens I (every bullet covered; nothing skipped; cross-refs noted). Auditor gate — Draft v1.0 "
     "(full bullet-to-paragraph coverage; no section skipped)."),
    ("bullet", "NO author read at this stage: once the author has vector-corrected at the outline gate, they see "
     "only best work. The author's read is Stage 7 [GATE 3], after the quality passes (Stage 5) and the full "
     "Style & Voice pass (Stage 6)."),

    ("h1", "Stage 5 — Quality passes (against the Writing Guide)   [HIGH tier]"),
    ("bullet", "Do 2–3 whole-draft quality passes, each a new version: cut editorializing; tighten verbose "
     "constructions; break cross-paragraph repetition (same example, same connector, same point twice); check "
     "dialectical balance (each positive argument engages its objection without drowning); verify "
     "cross-references resolve; check terminology consistency. Stop when a pass makes only minor changes."),
    ("bullet", "Do NOT, in this stage, change the author's voice, restructure sections against the signed-off "
     "outline, or cut anything the Writing Guide marks load-bearing. ADDING good arguments IS allowed — surface "
     "substantive additions in the version's changelog line so the author sees what is new at their next read."),
    ("bullet", "Run lenses (A, E, S, I). Self-check — Quality (the passes genuinely happened across the whole "
     "draft; the diff is broad and each change traces to one of the two duties — removing what is bad or adding "
     "what is good. Word count may move either way; what it may not do is grow through editorializing, "
     "repetition, or decoration)."),

    ("h1", "Stage 6 — Style & Voice Pass (every sentence, every paragraph, in the author's voice)   [HIGH tier]"),
    ("bullet", "This stage has ONE job: make the prose the author's. It runs in ROUNDS. Each round: first re-read "
     "the author's example papers FRESH (the per-paper Model Prose anchor plus the Model Prose Library's closest "
     "pieces — reading them immediately before editing is the point; the patterns fade fast); then go through "
     "the ENTIRE draft paragraph by paragraph and sentence by sentence, pushing the prose toward the author's "
     "style using the calibration guides — the Voice Profile (the author's own sentence and paragraph patterns, "
     "with their signpost whitelist) and 'Prose Register — All Paper Types' (the two tests; explain-before-use; "
     "no metaphors doing argument work; plain referents; concrete before abstract). This is a separate pass: no "
     "argument or structure work."),
    ("bullet", "Include the anti-LLM sweep calibrated to the author's signpost whitelist (keep the phrases the "
     "author genuinely uses; cut generic AI throat-clearing, stacked hedges, dash-chains, paragraph-restating "
     "summaries). Each style pass is a NEW numbered version with a changelog line; the deterministic self-check "
     "applies (broad diff; every change traces to a Voice-Profile pattern, or removes something bad, or adds "
     "something good — length may move either way)."),
    ("bullet", "Rounds and sufficiency: run as many rounds as it takes — TWO is the minimum (a single-pass draft "
     "failed a real author read as 'not in my voice, quite AI generated'; the two-round floor has held since). "
     "Each round walks the ENTIRE draft asking of each sentence 'would this author write this sentence?' and of "
     "each paragraph 'is this how their paragraphs move?' — replacing whatever reads as AI-written or off-voice. "
     "Keep a per-paragraph pass ledger (PASS / TOUCHED / FIXED with reasons) so 'every sentence and every "
     "paragraph' is a checkable claim, not an assertion. Stop only when a fresh round finds nothing but minor "
     "touches (convergence), never at a fixed count. TAIL DILIGENCE: voice passes reliably lose steam in a "
     "draft's last quarter — alternate walking direction between rounds (round 2 goes back to front), and report "
     "per-quartile touch rates in the ledger; a collapsed final-quartile rate without a stated reason fails the "
     "round's self-check."),
    ("bullet", "Later rounds catch different failure classes: round one catches drafting-register failures "
     "(meta-scaffolding, stacked intensifiers, coined labels, jargon openers); later rounds catch what earlier "
     "rewrites introduced, register leaks (internal drafting vocabulary surfacing in the prose), and "
     "over-correction (e.g. too many punchy landings — most authors' paragraphs mostly end on ordinary "
     "workmanlike sentences; check the Voice Profile). Every round runs the no-regression sweep against the "
     "overruled set (the author's deleted formulations, recorded in the Change Logs and edit files) — a voice "
     "rewrite must never resurrect overruled text."),
    ("bullet", "Each round is a NEW numbered version with a changelog line; self-check discipline applies (the "
     "builder diff must match the ledger's touched rows one-for-one). The author reads only after the stage "
     "completes — that read is Stage 7. And the rule is STANDING, not stage-local: after Gate 3, any substantial "
     "prose added or rewritten in later stages gets the same fresh-model-read + voice walk over the changed "
     "regions before the author's next read — the author never reads unvoiced prose, so they never have to "
     "leave style comments a pass should have caught."),

    ("h1", "Stage 7 — Author read of the draft   [HUMAN GATE 3]"),
    ("bullet", "Human sign-off — the quality-passed, style-and-voice-passed draft [GATE 3]. The author reads "
     "their best-work draft — voice, framing, substance. (Skipped on 'run straight through'.)"),
    ("bullet", "Apply the author's round under the author-round protocol: run the AUTHOR-ROUND EXTRACTOR (agent "
     "Build scripts/extract_author_round.py) against the author file AND the pristine base: it reads all five "
     "channels in one pass (tracked changes, inline brackets, Word comments, marking-color-to-black acceptances "
     "with rPrChange history stripped, and untracked text edits), and flags COLLISIONS where both parties "
     "touched a paragraph — the author's version wins by default. The author accepts marked additions by "
     "turning them black, so a color diff is part of every extraction (skipping it once nearly dropped 17 "
     "acceptances). Apply every instruction, produce the Change Log, run verify_author_round, and pass the "
     "mandatory author-round auditor gate. If the author's edits add or demand substantial new prose, that "
     "prose gets a voice walk (Stage 6 discipline) before the next stage. Render Claude's bigger changes in the "
     "MARKING COLOR (new ¶s, new arguments, wholesale rewrites); the author's incorporated edits and all "
     "footnote bodies stay black. Verify extraction against the raw XML when the author's file merges or splits "
     "paragraphs: Word stores ¶-mark deletions as self-closing w:del tags, and naive stripping swallows "
     "¶-initial insertions."),

    ("h1", "Stage 8 — Referee panel (simulated peer review)   [HIGH tier]"),
    ("bullet", "Once the paper is internally coherent, spawn THREE referee subagents in parallel (the paper "
     "type's fixed lens trio), each BLIND — given only its lens, the manuscript, and the venue, with NO summary "
     "of the paper's claims and NO leading questions (leading prompts make the panel converge on whatever you "
     "point at; use the Referee Templates). Each reads the manuscript INCLUDING footnotes, independently, and "
     "files a severity-ranked report that also gives acceptance-odds and an above/below-the-venue-bar signal."),
    ("bullet", "Consolidate consensus: concerns flagged by two or more referees are the consensus set; "
     "single-referee concerns are held in reserve. THEN STOP: present the author a disposition PLAN in chat — "
     "each consensus item, the proposed fix, the proposed skips — and implement only after the author signs "
     "off. Implement the approved set in one pass (a new version) — and the pass is not done until a VOICE "
     "ROUND has run over every region the implementation touched (fresh model-prose read first, walk each new "
     "or rewritten passage against 'would this author write this sentence?', keep the per-passage ledger). "
     "Referee-driven prose arrives in the referees' register by default; the voice round is what converts it to "
     "the author's before they read it."),
    ("bullet", "Run a second round with FRESH referees reading the revised paper clean. Read the TRAJECTORY and "
     "the specific convergent issues, NOT the accept/R&R/reject label — AI referees almost never say 'accept as "
     "is', so the label cannot flip and must not be chased. Add one 'case-for-acceptance' reader to counter the "
     "critique lean. CAP: two substantive rounds (first complete draft; post-author-revision) plus one blind "
     "pre-submission read. STOP when scholarship is clean (citation-auditor pass) and issues have converged; "
     "never action a referee's CITATION complaint without reconciling it against the citation-auditor."),
    ("bullet", "Auditor gate — Referee (each round's reports are real and the consensus fixes were actually "
     "applied; fixed point reached)."),

    ("h1", "Stage 9 — Author rewrite + targeted changes (author-led)"),
    ("bullet", "The author takes the keyboard for the parts where their judgment, voice, or expertise is "
     "irreplaceable (intro/hook/thesis, load-bearing arguments, contemporary illustrations). The author's edits "
     "to a section set its direction: later versions may improve further, but may never regress to formulations "
     "the author overruled (check the Change Logs), and improvements to the author's text are flagged in the "
     "changelog."),
    ("bullet", "Apply the author's targeted change requests VERBATIM; produce a Change Log (section / before / "
     "after / why) so the author can spot-check rather than re-read; DIFF against the prior version to confirm "
     "only the intended changes happened and no prior author edit was reverted."),
    ("bullet", "Auditor gate — Author changes (the Change Log matches the actual diff; prior author edits "
     "preserved)."),

    ("h1", "Stage 10 — Finishing"),
    ("bullet", "Integration pass. Re-read the entire paper front to back for stale cross-references, "
     "notation/terminology drift, places where earlier edits no longer match later ones, dangling references to "
     "cut material, and small prose polish. This catches what no single-read referee would. Voice discipline "
     "holds here too: regions substantially rewritten since the last voice round (referee fixes, integration "
     "rewrites) get a voice walk before the author's pre-submission read."),
    ("bullet", "Abstract — written LAST. Never write it early (it pulls the framing subtly wrong). Produce 2–3 "
     "candidates in different registers; have a fresh pass critique them and recommend a synthesis; verify it "
     "matches the paper's ACTUAL framing; insert at the top."),
    ("bullet", "Anti-LLM prose pass. Invoke the copy-critic to flag AI tells (hedging-redundancy, three-part "
     "lists where two suffice, adverbial throat-clearing, metaphor-chaining, paragraph-restating summaries), "
     "calibrated to the Voice Profile's whitelist; revise them; then a fresh pass rewrites anything still "
     "mechanical."),
    ("bullet", "Citation audit. Invoke the citation-auditor to verify author/year/title and EVERY page pinpoint "
     "against the real source (≥1 pass before the first referee round and 1 before submission); resolve every "
     "placeholder and (verify) tag. No fabricated citations."),
    ("bullet", "Build the citation apparatus to TYPE (per the Style Module: author-date + reference list; "
     "Bluebook footnotes carrying nearly every proposition; numbered citations; whatever the venue requires — "
     "for footnote-heavy types this is a heavy pass turning placeholders into full notes)."),
    ("bullet", "Length pass (light, here only). Now — and only now — scope up a thin paper or trim a bloated one "
     "toward the target length. Argument quality is already settled; this is sizing, not arguing."),
    ("bullet", "Pre-send review. Invoke the copy-critic for a must-fix vs can-wait checklist (typos; claims that "
     "don't match the body; duplicated cross-refs; undefined acronyms; terminology/format inconsistency; weak "
     "sections; style drift). Present the must-fix list to the author; apply approved fixes."),
    ("bullet", "Auditor gate — Final (every finishing step has a backing artifact; the package is complete) plus "
     "the 'knowing when to stop' check: the last referee round produced only polish; the integration pass found "
     "only cosmetics; abstract/intro/conclusion frame the paper the same way; you can read it end to end "
     "without wincing. THE FINISH DECISION IS AUTHOR-OWNED: because AI referees never say 'accept as is', no "
     "referee verdict releases the paper — the finish signal is citation-auditor clean + referee issues "
     "converged + the author judging the remaining objections answerable or acceptable as stated limitations."),

    ("h1", "Stage 11 — Revise & Resubmit (only if a journal sends referee reports)"),
    ("bullet", "Create a Revise and Resubmit/ folder. Reproduce the journal's referee reports VERBATIM; write a "
     "Response-to-Referees letter with responses inline, each quoting the point it answers; use a prior example "
     "letter to calibrate tone. Follow 'Revise & Resubmit Module.docx' (General Guide) for the full procedure."),
    ("bullet", "Make MODULAR changes — a small new subsection or an end-of-section paragraph, never a big "
     "restructure — so each change is easy for a referee to verify; mark all changes for the author's review. "
     "WebSearch-verify any referee-suggested citation before adding it. Keep Revised and Clean manuscript "
     "versions."),

    ("h1", "Stage 12 — Improvement retrospective (after each paper)"),
    ("bullet", "Write a 1–2 page retrospective (a Word doc in Progress reports): what worked, what slowed us "
     "down, the auditor's most common REVISE reasons, recurring author feedback, and concrete suggested changes "
     "to the playbook docs and the agents. This is how the agent improves — the original agent's every "
     "standing rule came from one of these."),
]

B += [
    ("h1", "Versioning rules"),
    ("bullet", "FREEZE RULE: the moment a draft version is handed to the author, that FILENAME is frozen. No "
     "build script may write it again, however trivial the fix; post-handoff builds bump the version number "
     "FIRST. Applies to every generated document the author reviews. (Added after a rebuild overwrote an "
     "author's in-progress edits.)"),
    ("bullet", "Version at gates. By design the paragraph outline goes 3C v0.1 → v0.2 → v0.3, and the Draft goes "
     "v1.0 → quality versions (v1.1, v1.2…) → voice versions → referee versions → author versions. Use "
     "integer/decimal naming: \"<Paper> - Draft v1.4.docx\". Save a new numbered file when a deliverable goes "
     "to or returns from a gate."),
    ("bullet", "Never overwrite a gated version. Superseded versions move to Old versions/. The author's "
     "returned markup is saved as a parallel '- author edits' file and treated as intentional."),
    ("bullet", "Each new version opens with a short changelog line noting what changed and which "
     "comments/lenses/referee items/auditor fixes it addresses. (The changelog line lives in the Change Log or "
     "the Progress Log for author-facing paper drafts — the draft itself stays clean.)"),
    ("bullet", "The .docx the author edits is the single source of truth. After any author edit, re-extract from "
     "the docx rather than relying on a prior build script — build scripts go stale fast."),
    ("bullet", "Fresh base for every build. A delivered file is author-editable the moment it lands in the "
     "shared folder — including between two of Claude's own builds in one session. Every build re-unpacks the "
     "current live file; never reuse a working directory, unpacked tree, or in-memory state from an earlier "
     "build. Record a hash at every delivery and check it before every rebuild (check_live_base.py, Build "
     "scripts; log .delivered_hashes.jsonl hidden next to the paper). On MISMATCH or NO RECORD: convert both "
     "states to text, diff, and reconcile every difference as an author edit — authors edit untracked as well "
     "as tracked, so zero w:ins/w:del marks prove nothing. (Added after a stale-base rebuild dropped six "
     "untracked author edits.)"),
]

B += [
    ("h1", "Progress reports (kept clean and author-facing)"),
    ("body", "Progress reports/ holds ONLY: the Project Checklist; the running Progress Log (appended at each "
     "gate and after each substantive change — what was produced, what changed, decisions, open questions, the "
     "auditor's verdicts, and what is needed from the author); the Argument & Objection Coverage Map; and the "
     "Stage 12 Retrospective. Working/review artifacts — the Claims-to-Verify register, the Citation Audit, the "
     "Setup Brief, and working referee notes — live in Scrap/Review artifacts/ (referee reports themselves in "
     "WIP Docs/Referee Reports/)."),
    ("h1", "Project folder structure (reference)"),
    ("bullet", "General Guide to Academic Writing/ — the shared playbook (this Pipeline, Style Modules, Context, "
     "Voice Profile, Prose Register, Model Prose Library, Project Template, Referee Templates). The root "
     "Writing Guide is the style core. Subagents live in .claude/agents/."),
    ("bullet", "Brief/ — the author's 1-page project description + notes/fragments. Background Readings/ — real "
     "PDFs of the core interlocutors (+ Converted text/). Model Prose/ — a prior paper, for voice only."),
    ("bullet", "WIP Docs/ — Literature Map, Plan, Outline, Draft, Abstract, Referee Reports, Change Logs (each "
     "main type with Old versions/). Progress reports/ — Checklist, Progress Log, Coverage Map, Retrospective. "
     "Scrap/Review artifacts/ — Claims-to-Verify, Citation Audit, Setup Brief. Submission/ — only what is "
     "literally submitted. Behind the scenes (Claude)/Build scripts/ — this paper's own build scripts."),
    ("h1", "Appendix — gate & lens quick reference"),
    ("table", [
        ["Stage", "Lenses", "Specialist", "Auditor gate", "Human gate"],
        ["0 Setup", "—", "—", "Setup", "Argument Sketch"],
        ["1 Lit Review", "E, I", "—", "Lit Review", "—"],
        ["2 Plan", "A,E,S,I", "—", "Plan", "GATE 1"],
        ["3A Skeleton", "A, E", "—", "3A", "—"],
        ["3B Argument", "A,E,S,I", "—", "3B", "—"],
        ["3C Paragraph (v0.1→v0.3)", "A,E,S,I", "referee (review memo)", "3C×3 + FINAL", "GATE 2"],
        ["4 Draft v1.0 (full density)", "I", "—", "Draft v1.0", "—"],
        ["5 Quality passes", "A,E,S,I", "—", "self-check", "—"],
        ["6 Style & Voice (rounds until converged; fresh model reads; per-¶ ledger)", "S",
         "copy-critic (whitelist)", "self-check", "—"],
        ["7 Author read + round applied", "—", "—", "Author changes", "GATE 3"],
        ["8 Referee panel", "—", "referee ×3 BLIND (capped) + case-for-acceptance", "self-check", "—"],
        ["9 Author rewrite + changes", "—", "—", "Author changes", "—"],
        ["10 Finishing", "A,E,S,I", "citation-auditor; copy-critic", "Final", "Finish (author-owned)"],
        ["11 Revise & Resubmit (opt.)", "—", "citation-auditor", "—", "author-led"],
        ["12 Retrospective", "—", "—", "—", "—"],
    ], [2.9, 0.9, 2.3, 1.4, 1.4]),
]

if __name__ == "__main__":
    build(os.path.join(GG, "1a. Pipeline v1.0.docx"), B,
          header_lines=["Deep Drafter"],
          footer_text="Deep Drafter   |   Pipeline v1.0")
    print("pipeline built")
