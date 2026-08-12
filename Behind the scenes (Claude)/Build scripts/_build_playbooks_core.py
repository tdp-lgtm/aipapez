#!/usr/bin/env python3
"""Build the root playbook docs of the Shareable Edition: START HERE, SETUP — Personalize
the Agent, and Writing Guide — House Style. Word masters may be edited by the author after
first generation — check the mirrors/mtimes before regenerating over a possibly-edited master
(versioning rules apply: new version, old to Old versions/)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_docx import build

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# ---------------------------------------------------------------- START HERE
start_here = [
    ("title", "START HERE — The Deep Drafter"),
    ("subtitle", "For the author. How to write a paper with this workspace. v1.0 — Shareable Edition, July 2026."),
    ("body", "This workspace turns a one-page brief into a finished, referee-tested draft through a documented "
             "pipeline. You supply the thesis, the central arguments, and the judgment calls; Claude does the "
             "execution. You don't need to run anything yourself — just talk to Claude in plain language."),
    ("note", "Provenance: the agent was developed by Simon Goldstein (philosophy, University of Hong Kong) with "
             "Claude, over a series of real papers in philosophy and law. This shareable edition is generalized: "
             "it works for any field once it has been personalized to you. Share and adapt freely."),
    ("h1", "First: personalize the agent (one session, once)"),
    ("body", "The agent ships generic. Before the first paper, tell Claude: **\"set up the paper writing agent "
             "for me.\"** Claude will interview you (your field, the kinds of papers you write, your venues, your "
             "coauthors, your standing preferences), ask you for 3–6 of your best papers as PDFs, and mine them to "
             "build your **Voice Profile** — the sentence- and paragraph-level patterns it will imitate whenever "
             "it drafts for you. This single step is what makes drafts come out sounding like you rather than like "
             "an AI. The full procedure is in 'SETUP — Personalize the Agent' (this folder); Claude follows it "
             "on its own."),
    ("h1", "What to do to start a paper"),
    ("body", "You don't have to specify everything yourself — Claude asks you. Just say you want to start a new "
             "paper (or hand over a rough one-pager), and Claude runs a short intake up front — beginning with "
             "what kind of paper it is (the type sets length, citations, structure, and register), then the "
             "target venue and length, coauthors, whose voice to match, any topics to avoid, and how much to "
             "check in with you. Answer the menu and it's off."),
    ("num", "Make a one-page brief: the thesis (one sharp paragraph), the central arguments, the target venue, a "
            "rough word budget, and 3–5 key sources. Rough is fine — Claude sharpens it with you."),
    ("num", "Gather the inputs: the PDFs of the few works you most want engaged, and one prior paper of yours (or "
            "a model paper) whose voice you want matched."),
    ("num", "Tell Claude: the paper's working title, its type, and the target length — then hand it the brief, "
            "the readings, and the model paper. Claude files them and starts."),
    ("h1", "How the work goes"),
    ("bullet", "Outline first. Claude builds the argument in layers — a skeleton, then an argument outline, then "
               "a detailed paragraph-by-paragraph outline — before writing any prose. Structure is settled where "
               "it's cheap to change."),
    ("bullet", "Then drafting, then voice, then review. Claude writes the draft, tightens it against your Writing "
               "Guide, rewrites every sentence into your voice (calibrated on your own papers), then runs a panel "
               "of simulated referees — each reading blind, the way real referees do — and a citation check that "
               "verifies every reference against the real sources. Quality comes from those reviewers; a separate "
               "auditor just keeps everyone honest about actually doing the work."),
    ("bullet", "You sign off at four points: the Argument Sketch (is this the argument?), the Plan (is the angle "
               "right?), the detailed outline (the drafting contract — nothing is drafted until you approve it), "
               "and the first full draft — which you only ever see AFTER it has been rewritten into your voice. "
               "Everywhere else it runs on its own."),
    ("h1", "Working with the drafts"),
    ("bullet", "Edit any document directly in Word. Track changes or don't — Claude detects both. Save it (a name "
               "like '… - your-name edits' is perfect, but saving over the file also works). Claude treats your "
               "edits as setting the direction and builds on them — it will never quietly revert them."),
    ("bullet", "Leave comments in the text as you read — a bracketed note like '[ab: cut this; tighten the third "
               "argument]' (your initials), or a real Word comment. Claude applies them as written."),
    ("bullet", "Every version is kept. Nothing is overwritten; older versions move to an 'Old versions' folder."),
    ("bullet", "In review rounds, Claude marks its own substantial additions in a marking color (blue by default) "
               "so you can spot what's new fast; your own incorporated edits stay black. Final drafts are always "
               "clean black text."),
    ("h1", "Two things you can say any time"),
    ("bullet", "'Run straight through' — go fully autonomous from the brief to a finished draft, no check-ins; you "
               "review at the end."),
    ("bullet", "'Check with me at every gate' — the opposite: pause for you at every stage."),
    ("h1", "One thing to settle before you submit anywhere"),
    ("body", "Journals and fields differ on disclosure of AI assistance, and policies are changing fast. The "
             "agent records your standing stance during setup and asks again per venue — but the decision is "
             "yours, and nothing is submitted until you've settled it."),
    ("h1", "Where things are"),
    ("bullet", "Your papers live in Papers/. The shared playbook (Pipeline, Style Modules, Context, the Writing "
               "Guide, your Voice Profile, the Model Prose Library) is in General Guide to Academic Writing/ and "
               "at the workspace root. Each paper's status is in its Progress reports/ (the Checklist and the "
               "Progress Log) — open those to see exactly where a paper stands."),
]

# ------------------------------------------------- SETUP — Personalize the Agent
setup = [
    ("title", "SETUP — Personalize the Agent"),
    ("subtitle", "The first-run procedure: calibrate the agent to this author before any paper is drafted. "
                 "v1.0 — Shareable Edition, July 2026. Claude runs this; the author just answers questions and "
                 "supplies PDFs."),
    ("note", "TRIGGER — Claude: run this procedure whenever the Context doc still contains [TODO] markers or the "
             "Model Prose Library is empty, before starting any paper. It takes one conversation. Record progress "
             "as you go; each personalized document is a new version (the versioning rules apply from the first "
             "edit)."),
    ("h1", "Why this step exists"),
    ("body", "The agent's biggest quality lever is not the pipeline — it is calibration. A draft succeeds when "
             "every sentence reads as the author's, when the structure matches the field's conventions, and when "
             "the review agents test against the right venue. All three require knowing the author. The shipped "
             "documents are strong field-neutral defaults with clearly marked slots; this procedure fills the "
             "slots."),
    ("h1", "Step 1 — Toolchain check (Claude does this silently)"),
    ("bullet", "Confirm python3 and the python-docx package are available (every builder and reader script needs "
               "them). If python-docx is missing, install it (pip3 install python-docx) or ask the author's "
               "permission to, per the machine's norms."),
    ("bullet", "Optional but recommended: a .docx→PDF renderer (LibreOffice headless, or Word itself) so built "
               "documents can be rendered and eyeballed before handoff, and pandoc for text-diffing Word files in "
               "the author-round protocol (a plain-text extraction fallback exists in read_docx.py, but pandoc "
               "diffs are cleaner)."),
    ("bullet", "Run: python3 \"Behind the scenes (Claude)/Build scripts/sync_playbooks.py\" — confirms the "
               "mirror system works and gives you fast text access to every playbook doc."),
    ("h1", "Step 2 — The interview (bundle the questions; don't drip them)"),
    ("body", "Ask the author, in one or two bundled rounds, and record every answer in the Context doc "
             "(replacing its [TODO] markers):"),
    ("num", "**Who you are.** Name, field and subfield, affiliation, and anything a venue would list (books, "
            "notable prior work). Used for author lines and for checking prior-work consistency in Stage 1."),
    ("num", "**What you write.** The paper types you actually produce (journal article, law review, monograph, "
            "empirical article, policy report, book chapter, …). For each: does a shipped Style Module fit, or "
            "should one be built? (Step 5.)"),
    ("num", "**Where you publish.** Typical venues per type, with any known length limits and house registers."),
    ("num", "**Who you write with.** Frequent coauthors (name, field); the author-order convention in your field "
            "(alphabetical? contribution? seniority?)."),
    ("num", "**Standing content preferences.** Substantive commitments the agent should respect across papers "
            "(positions you build on; framings you avoid); how you like objections handled; anything you never "
            "want in a draft."),
    ("num", "**Mechanics.** Your bracket-comment initials (e.g. '[ab: …]'); the marking color for Claude's "
            "reviewable additions in author rounds (default blue); paper-draft appearance (default: Arial, black "
            "text only, real Word footnotes, page numbers in the footer, no heading rules) — confirm or adjust; "
            "any hard formatting rules (e.g. some authors ban prose dashes outright — the shipped default treats "
            "dash-chains as an AI tell and removes them in the voice pass)."),
    ("num", "**AI-use disclosure stance.** What the author wants disclosed, where, and in what words — knowing "
            "that venue policies differ and change; re-confirm per venue at each paper's Intake. The agent never "
            "submits anything the author hasn't settled."),
    ("num", "**Autonomy default.** The standard gate set (Argument Sketch, Plan, Paragraph Outline, voiced "
            "draft), 'run straight through', or 'every gate' — per paper this can always be overridden."),
    ("h1", "Step 3 — Collect the model prose (3–6 of the author's own papers)"),
    ("bullet", "Ask for the author's best or most representative papers as PDFs — ideally spanning the types they "
               "write (e.g. one tight journal article, one long-form piece, one coauthored paper). Published "
               "versions preferred; final drafts fine."),
    ("bullet", "File each in General Guide to Academic Writing/Model Prose Library/ with a clean name; extract "
               "text alongside (a ' — extracted text.txt' file) so agents can read it fast."),
    ("bullet", "Add a catalog row per paper (the Catalog doc in that folder): type, length, venue, and — the "
               "important column — WHAT to imitate in it, named precisely (not 'good prose'). Write those notes "
               "AFTER Step 4's analysis, when you know what each paper exemplifies."),
    ("bullet", "If the author is early-career with few papers, use what exists and add 1–2 admired papers by "
               "OTHERS in the field, clearly marked as register models rather than the author's own voice; the "
               "Voice Profile then leans on the author's real prose for sentence patterns and on the register "
               "models for structure."),
    ("h1", "Step 4 — Mine the papers; build the Voice Profile"),
    ("body", "Read the collected papers IN FULL, then rebuild 'General Guide to Academic Writing/Voice Profile — "
             "Sentence & Paragraph Craft.docx' from its template: for each of its ten pattern categories, state "
             "the author's actual pattern and paste 1–2 VERBATIM example sentences from their papers. Then build "
             "the signpost whitelist (transition and framing phrases the author genuinely uses — with the rule "
             "that whatever appears in the model prose is never flagged as an AI tell) and record the author's "
             "personal rules (dash policy, banned words, fragment tolerance, hedging style). Show the finished "
             "profile to the author and adjust on their feedback — this document is the single most-consulted "
             "calibration asset in the pipeline."),
    ("h1", "Step 5 — Confirm or build the Style Modules"),
    ("bullet", "For each paper type from Step 2: if a shipped module fits (Philosophy Paper, Law Review, "
               "Cambridge Element, Empirical Social Science Paper), read it WITH the author's answers in hand and "
               "adjust its defaults (length, citation practice, venue register) to their field's reality."),
    ("bullet", "For a type with no module, copy '_Template (new paper type).docx', fill every section with the "
               "author (or from analysis of venue exemplars), and add the type to TYPE_PRESETS in new_paper.py so "
               "the scaffolder recognizes it."),
    ("bullet", "If the field has a distinctive register (the way analytic philosophy has displays and premise-form "
               "arguments — see the shipped example 'Analytic Philosophy Prose — Style Guide'), write a short "
               "field-register companion and name it from the module."),
    ("h1", "Step 6 — Personalize the Writing Guide"),
    ("body", "Walk the author through 'Writing Guide — House Style' section by section: keep, adjust, or replace "
             "each default. The shipped guide encodes a strongly argumentative house style (direct arguments, no "
             "editorializing, numbered argument structure); authors in narrative or empirical traditions will "
             "want different section-structure defaults — the sentence-level discipline usually survives across "
             "fields. Save as a new version."),
    ("h1", "Step 7 — Close out"),
    ("bullet", "Confirm the Context doc has no [TODO] left in Part 1; the Model Prose Library has its catalog "
               "rows; the Voice Profile is author-approved; the needed Style Modules exist."),
    ("bullet", "Offer a shakedown run: a short piece (a 1,500-word commentary or review) through the full "
               "pipeline is the fastest way to surface calibration misses cheaply before a real paper."),
    ("bullet", "Refresh the mirrors (sync_playbooks.py). From here, CLAUDE.md's normal orientation applies."),
]

# ------------------------------------------------- Writing Guide — House Style
writing_guide = [
    ("title", "Writing Guide — House Style"),
    ("subtitle", "The stylistic core for every paper this agent drafts. Personalized at setup; the defaults "
                 "below are field-neutral and battle-tested. v1.0 — Shareable Edition, July 2026."),
    ("note", "PERSONALIZE ME — these defaults were distilled from heavy real use on argumentative papers "
             "(philosophy, law) and most of them transfer to any field. At setup (see 'SETUP — Personalize the "
             "Agent'), the author confirms, adjusts, or replaces each section — especially 'Structure within "
             "sections', which is genre-specific. The author's own additions belong here too: this document is "
             "house law for every draft."),
    ("h1", "Core principle"),
    ("body", "Strong, clear, direct arguments. No verbal disputes. No editorializing. Claude's default draft "
             "style tends to over-hedge, over-qualify, and over-frame. Each argument should be stated forcefully "
             "and defended on substance, not buried in framing."),
    ("h1", "Structure within sections (default for argumentative papers — confirm at setup)"),
    ("body", "Often, but not always, each substantive section or subsection has 3–5 affirmative arguments, each "
             "one paragraph. Use explicit numbering: \"First, … Second, … Third, …\" within the relevant level."),
    ("body", "Often, but not always, after the affirmative arguments, engage 3–5 objections, one paragraph each. "
             "\"The first objection is X. … The second objection is Y. …\" Brief steelman, then direct response."),
    ("body", "Big-picture objections to the whole proposal can get their own section. But local objections — "
             "objections to a specific argument — live in the section or subsection with that argument, not in a "
             "separate objections chapter."),
    ("body", "Don't pad. If a section has only one or two real objections, engage those and move on. Canvas the "
             "important objections; don't add filler to round out the count."),
    ("h1", "What dialectical engagement should look like"),
    ("body", "The kind to produce: state the opposing view briefly and faithfully, then explain why it fails. "
             "\"It is true that X. Nonetheless, Y.\" Done in a paragraph; move on. (That said, don't overuse any "
             "one literal pattern.)"),
    ("body", "The kind to avoid: \"Some have argued X, but what they really mean is X′, which differs from X in "
             "that it relies on assumption A. If A is interpreted strictly, then… but if A is interpreted "
             "broadly, then…\" This is a verbal dispute. The reader doesn't care."),
    ("body", "If an opponent's position is unclear, take the strongest natural reading and respond to that. If "
             "multiple readings matter, footnote them."),
    ("h1", "Sentence-level discipline"),
    ("bullet", "One move per sentence. Multiple subordinate clauses pile up fast. Pick the main move and make it."),
    ("bullet", "Em-dash asides need to earn their place. \"The firm's decisionmakers — board members, executives, "
               "shareholders — make release decisions\" should become \"Firm decisionmakers make release "
               "decisions.\" If the aside does real work, keep it; usually it doesn't."),
    ("bullet", "Cut filler. \"In the first instance,\" \"it is worth noting,\" \"as we shall see,\" \"we "
               "acknowledge,\" \"broadly speaking\" — these signal hedging without adding information."),
    ("bullet", "Cut bloat. \"X supplies the most useful overview\" / \"Y provides a helpful framework\" — "
               "introductions that don't say anything. Engage the substance directly."),
    ("h1", "Editorializing — what to cut"),
    ("bullet", "Meta-statements about which argument is harder or stronger. \"The strongest objection is…\" \"The "
               "hardest version of the worry is…\" Let arguments stand on their own; the reader will form a view."),
    ("bullet", "Pacing sentences. \"We have shown X. We now turn to Y.\" Section structure already does this work."),
    ("bullet", "Self-referential commentary. \"We are arguing here that…\" \"The point of this section is to…\" "
               "Just make the argument."),
    ("bullet", "Reassuring the reader. \"We take seriously the concern that…\" Engage the concern directly; don't "
               "preface the engagement."),
    ("body", "Instead of this stuff, use simple idea-based signposting at the start of sections, saying very "
             "quickly what will happen."),
    ("h1", "Common Claude failure modes to watch for"),
    ("body", "These show up across projects and across drafts. Catch them on your own review passes."),
    ("bullet", "Repetition of main claims — the #1 failure mode. The same point made in three sections under "
               "three framings. Each argument should appear in exactly one place; downstream sections "
               "cross-reference rather than re-argue."),
    ("bullet", "Over-editorializing rather than direct arguing. Commenting on the argumentation rather than "
               "making it."),
    ("bullet", "Long-winded sentences. Em-dashes and parentheticals stacking up; one sentence doing the work of "
               "three."),
    ("bullet", "Bloated, padded prose. Sentences that introduce or frame without saying anything substantive."),
    ("h1", "At draft stage"),
    ("bullet", "Focus on argument quality, not length targets. Word counts come later (one light pass near the "
               "end — see the Pipeline)."),
    ("bullet", "Citations can be parenthetical placeholders (\"Smith 2024\"); the proper apparatus comes in a "
               "later pass, verified against real sources."),
    ("bullet", "Build up in layers: short outline → detailed outline → paragraph-by-paragraph long-form outline → "
               "prose. The intermediate layers catch structural redundancy before it gets baked into prose."),
    ("bullet", "When the author edits a document and sends it back, those edits set the direction. Never revert "
               "to a formulation the author overruled. If you see differences from what you produced, that is "
               "because the author made them on purpose."),
    ("h1", "Model prose"),
    ("body", "Before drafting, read the closest example in the Model Prose Library (General Guide to Academic "
             "Writing/Model Prose Library/) IN FULL — the author's own papers, cataloged with what to imitate in "
             "each. Read for register and sentence shapes, never for content: don't import material from the "
             "model paper into the draft. The Voice Profile distills the sentence-level patterns; the model "
             "papers show them live."),
    ("h1", "Quick self-review checklist"),
    ("body", "Before sending a draft, ask:"),
    ("bullet", "Does each argument appear in exactly one place?"),
    ("bullet", "Does each paragraph make one argument?"),
    ("bullet", "Does each sentence make one move?"),
    ("bullet", "Am I editorializing about the argumentation, or just making it?"),
    ("bullet", "Am I getting bogged down in verbal disputes, or engaging the substance?"),
    ("bullet", "Have I cut every \"it is worth noting,\" \"in the first instance,\" \"as we shall see,\" and "
               "similar filler?"),
]

if __name__ == "__main__":
    hdr = ["Deep Drafter"]
    build(os.path.join(ROOT, "START HERE.docx"), start_here,
          header_lines=hdr, footer_text="Deep Drafter   |   START HERE")
    build(os.path.join(ROOT, "SETUP — Personalize the Agent.docx"), setup,
          header_lines=hdr, footer_text="Deep Drafter   |   Setup & Personalization")
    build(os.path.join(ROOT, "Writing Guide — House Style.docx"), writing_guide,
          header_lines=hdr, footer_text="Deep Drafter   |   Writing Guide — House Style")
    print("core playbooks built")
