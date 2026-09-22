#!/usr/bin/env python3
"""Build the General Guide docs of the Shareable Edition: Context (template), Prose Register,
Voice Profile (template), Revise & Resubmit Module, Model Prose Library Catalog (template),
Project Setup & Folder Structure, and the Project Checklist TEMPLATE (generated from
new_paper.py so script and template can never drift). Check mirrors/mtimes before
regenerating over a possibly-edited Word master (versioning rules apply)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_docx import build
from new_paper import checklist_blocks

GG = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
                  "General Guide to Academic Writing")
HDR = ["Deep Drafter"]

# ---------------------------------------------------------------- 1b. Context (TEMPLATE)
context = [
    ("title", "Context: Authors, Venues, and Standing Preferences"),
    ("subtitle", "Shared reference read at the start of every paper. v1.0 — Shareable Edition; filled in at "
                 "setup (see 'SETUP — Personalize the Agent')."),
    ("note", "HOW TO USE THIS DOC. Part 1 (authors, preferences, venues) is stable background, filled in ONCE at "
             "setup and updated as facts change. Part 2 (§5) is filled in PER PAPER. Anything marked [TODO] must "
             "be asked, not assumed — and Claude should verify affiliations and titles with the author rather "
             "than trusting training memory."),
    ("h1", "1. The author(s)"),
    ("bullet", "[TODO] Name — field and subfield; affiliation; role. Anything a venue's author line needs."),
    ("bullet", "[TODO] Notable prior work (books, known papers) — used for voice calibration and for checking "
               "that a new paper doesn't silently contradict the author's published positions."),
    ("bullet", "[TODO] Author-order convention in this field (alphabetical / contribution / seniority) — the "
               "default for every coauthored paper unless a paper's profile says otherwise."),
    ("h1", "2. Frequent coauthors"),
    ("bullet", "[TODO] Name — field; affiliation; what they typically bring to a joint paper. (One bullet per "
               "coauthor. Confirm the coauthors and the author order for EACH paper in §5 — they vary by "
               "project.)"),
    ("h1", "3. Standing voice & content preferences"),
    ("bullet", "[TODO] Substantive commitments the agent should respect across papers — positions the author "
               "builds on, framings to avoid, sources or literatures the author considers unreliable."),
    ("bullet", "Strong, direct arguments (see the Writing Guide). No editorializing, no verbal disputes, one "
               "move per sentence; each argument appears in exactly one place. [Confirm or adjust at setup.]"),
    ("bullet", "Prefer cutting or footnoting to hedging. When a claim is uncertain, cut it or footnote it rather "
               "than softening the prose. [Confirm or adjust at setup.]"),
    ("bullet", "[TODO] Formal-work conventions, if any (notation preferences, plain-English vs symbolic variable "
               "names, where proofs live)."),
    ("bullet", "[TODO] Bracket-comment initials the author will use in documents (e.g. '[ab: tighten this]')."),
    ("bullet", "[TODO] Marking color for Claude's reviewable additions in author rounds (default blue; final "
               "drafts always clean black)."),
    ("bullet", "[TODO] Paper-draft appearance (default: Arial, black text only, real Word footnotes, page "
               "numbers in the footer, no page header, no heading rules — implemented by gen_paper_docx.py). "
               "Record any deviation here."),
    ("bullet", "[TODO] AI-use disclosure stance: what the author discloses, where, in what words — re-confirmed "
               "per venue at each paper's Intake. Nothing is submitted until this is settled for that venue."),
    ("h1", "4. Venues (typical)"),
    ("bullet", "[TODO] The venues the author actually targets, per paper type, with length limits and register "
               "notes (each journal has its own — confirm per paper). One bullet per venue or venue family."),
    ("h1", "5. Per-paper profile (copy this block into each paper's Brief / Setup Brief and fill it)"),
    ("bullet", "Paper title: [TODO]"),
    ("bullet", "Paper type (per the Style Modules on hand): [TODO]"),
    ("bullet", "Target venue + its length limit: [TODO]"),
    ("bullet", "Coauthors on THIS paper + confirmed author order: [TODO]"),
    ("bullet", "Model-prose anchor (the prior paper to imitate for voice): [TODO]"),
    ("bullet", "Hard-nos for THIS paper (topical exclusions, positions to avoid): [TODO]"),
    ("bullet", "Division of labor (how aggressively to cut; who writes the Stage-9 substantive rewrite): [TODO]"),
    ("bullet", "AI-disclosure decision for THIS venue: [TODO]"),
]

# ---------------------------------------------------------------- Prose Register
register = [
    ("title", "Prose Register — All Paper Types"),
    ("subtitle", "The register layer for EVERY paper the agent drafts, whatever the field. v1.0 — Shareable "
                 "Edition. Distilled from a heavily-commented author correction round on the original agent's "
                 "first trial paper (38 register comments on one gate), then confirmed general across types."),
    ("h1", "Where this sits, and when to read it"),
    ("body", "The root 'Writing Guide — House Style' is house law (argument discipline, no editorializing, no "
             "verbal disputes, sentence hygiene). This guide adds the register layer beneath it: how sentences "
             "and paragraphs should sound, whatever the paper type. The paper type's Style Module then adds its "
             "own conventions on top, and the Voice Profile calibrates everything to THIS author. Read this "
             "guide before drafting Stage-4 prose and again before any register pass. Two tests govern every "
             "sentence:"),
    ("bullet", "Would the author write this sentence? Calibrate on the model-prose paper chosen at Setup and on "
               "the Voice Profile. Read the model paper for sentence shapes before drafting — never for content."),
    ("bullet", "Does the reader already have everything needed to parse it? If a term, case, device, or allusion "
               "appears before it has been introduced, the sentence is broken no matter how good it is."),
    ("h1", "1. The target register"),
    ("body", "The default target — confirmed by working authors across fields — is simple, clear, even boring "
             "academic prose: invisible prose, where the reader notices the argument and never the writing."),
    ("bullet", "Plain declarative sentences. One point per sentence. Short sentences dominate; a longer one is "
               "fine when its spine stays simple."),
    ("bullet", "The whole transition kit: 'First / Second / Third', 'But', 'So', 'Yet', 'Now', 'Consider', "
               "'Take X first', 'Why? Because…', and an occasional question as a pivot. Nothing fancier."),
    ("bullet", "Plain verbs of assertion: says, holds, argues, requires, forbids, implies, shows. If a verb is "
               "doing style work ('the theory goes quiet'), replace it."),
    ("bullet", "No rhetorical fragments. No drama adjectives ('extraordinary', 'striking', 'remarkable') — "
               "authors strike them on sight."),
    ("bullet", "If a sentence would sound clever read aloud, flatten it. Wit lives in the examples, never in the "
               "diction."),
    ("h1", "2. Explain before use"),
    ("body", "The single largest source of author register comments on real runs ('premature — you haven't "
             "explained what X is'; an allusion 'is not contributing')."),
    ("bullet", "Nothing appears in an argument before the reader has it: no term, formal device, named case, "
               "doctrine, or literature allusion is used first and explained later."),
    ("bullet", "Assume a smart reader with zero background in any imported apparatus — game theory in a "
               "philosophy paper, economics in a law review, doctrine in a policy piece, statistics beyond the "
               "venue's norm in an empirical paper. Define it from scratch, in the body, in a sentence or two."),
    ("bullet", "An allusion the reader may not share is either developed properly or cut. There is no middle "
               "setting where a knowing reference does the work."),
    ("bullet", "Machinery is introduced at the point of use, not previewed. Roadmaps name what each section "
               "shows, not the tools it will use."),
    ("h1", "3. No metaphors doing argument work"),
    ("body", "A metaphor may restate a point the prose has already made plainly; it may never carry the point. "
             "The test: delete the metaphor. If the argument loses a step, that step was never argued — write it "
             "as a mechanism, in plain words, and only then decide whether any image is still worth having (it "
             "usually is not)."),
    ("h1", "4. Referents and coinages"),
    ("bullet", "Repeat the plain noun. 'The proportionality condition' is 'the proportionality condition' every "
               "time — never 'the test', 'this instrument', 'that machinery'. Elegant variation makes the reader "
               "re-derive reference."),
    ("bullet", "Coin a term only when it is defined at first use, reused throughout, and load-bearing. A label "
               "that the next sentence does not cash out, or that the paper never leans on again, becomes a "
               "plain description."),
    ("bullet", "One name per thing, one thing per name, for the whole paper."),
    ("h1", "5. Structure: roadmaps and limits"),
    ("bullet", "Roadmap: one plain sentence per section. No tool preview, no promises of significance."),
    ("bullet", "No up-front limits paragraph. Concessions and scope restrictions appear where they arise, stated "
               "once, without apology."),
    ("h1", "6. The body and the notes"),
    ("body", "The body carries only what the argument needs. Demote to the paper's aside apparatus (footnotes, "
             "endnotes, or parentheticals — the type's Style Module governs the vehicle): terminology and "
             "priority credits, technical refinements the argument survives without, secondary qualifications. "
             "And if a precision does no work even there — an exact fraction nobody uses — cut it entirely."),
    ("h1", "7. Quoting the opposition"),
    ("bullet", "State the views you target in their authors' own words, with pinpoints — short verbatim quotes "
               "where the target is stated, so the disagreement is on the surface, not asserted."),
    ("bullet", "Quotes are for opponents and evidence; paraphrase is for your own moves."),
    ("bullet", "Every quote comes from the sources on disk, verified at write time — never from memory (house "
               "law; the citation-auditor checks)."),
    ("h1", "8. Concrete before abstract"),
    ("body", "Open the paper with a real case told plainly — dates, places, named people, real numbers — before "
             "any theory appears. Prefer the same order inside sections: example, then machinery."),
    ("h1", "Before and after — real edits from a trial run"),
    ("body", "All pairs are verbatim from a rejected Draft v1.0 and the approved Draft v1.2 of the original "
             "agent's first trial paper (a philosophy paper). Every pair illustrates a general rule."),
    ("table", [
        ["Draft v1.0 (rejected at the author gate)", "Draft v1.2 (approved register)", "The rule"],
        ["'Honesty about what the tournaments do not show.'",
         "'The tournament results have limits, and I want to state them plainly.'",
         "No rhetorical fragments. Announce a turn in a full plain sentence."],
        ["'The unsophisticated reciprocator's response runs through the past, and the past cannot be jammed.'",
         "'The unsophisticated reciprocator acts on the fact of the provocation, and the aggressor cannot "
         "change that fact.'",
         "No metaphors doing argument work. Delete the image; say the mechanism."],
        ["'…under the orthodox tests, the switch that turns the victim's response on and off sits in the "
         "aggressor's hands, because the aggressor controls the signals the forecast runs on; under the "
         "reciprocity norm, the switch sits in the provocation itself, and nothing the aggressor says can "
         "reach it.'",
         "'Under the standard theory, A's own signals turn B's response off. Under the reciprocity norm, "
         "nothing A says can do that.'",
         "Two short plain sentences beat one clever one. Unpack compressed contrasts."],
        ["'The distinction sounds small. The next three cases show that it is the whole game — and they share "
         "a shape worth naming in advance.'",
         "'The difference looks small. It is not, because it determines who controls the defender's response. "
         "… Three cases develop this difference.'",
         "No drama ('the whole game'), no forecasting flourishes. Say why it matters, then move."],
        ["'In Axelrod's two computer tournaments, game theorists submitted strategies for the iterated "
         "prisoner's dilemma and the strategies played round-robin.'",
         "'The prisoner's dilemma is the standard model of a situation in which each party does better by "
         "defecting whatever the other does, yet both do worse under mutual defection than under mutual "
         "cooperation. In the iterated version, the same two parties play repeatedly…'",
         "Explain before use. Imported formalism is defined from zero, in the body, before it appears in an "
         "argument."],
    ], [3.2, 3.2, 2.4]),
    ("h1", "Document appearance (author-facing paper drafts)"),
    ("body", "Default appearance for paper drafts the author reads (confirm or adjust at setup; the Context doc "
             "records deviations): Arial, black text ONLY — no accent colors, which read as an AI tell — no "
             "horizontal rules under headings, no page header, page numbers in the footer, REAL Word footnotes "
             "(not inline boxes), an abstract under the title once one exists, and no build/version log inside "
             "the document (provenance lives in the Change Log). Build with gen_paper_docx.py (agent Build "
             "scripts), which implements all of this including a proper footnotes part; author-facing WORKING "
             "docs (checklists, logs, memos) may keep the gen_docx house style."),
    ("h1", "Running a register pass"),
    ("body", "When a draft needs the register applied (or a gate returns prose comments): first re-read the "
             "model-prose paper for voice; then go paragraph by paragraph and sentence by sentence, asking of "
             "each sentence the two tests at the top of this guide; apply the author's comments verbatim where "
             "given, and apply the same corrections proactively to sections the author has not read — so the "
             "author never has to make the same comment twice. A good register pass usually shortens the flashy "
             "sentences and lengthens the technical ones — cleverness compresses, explanation expands."),
    ("body", "Quick checklist before returning a draft: no sentence the reader lacks the pieces to parse; no "
             "metaphor carrying an argument; no fragment, no drama adjective, no elegant variation; roadmap one "
             "sentence per section; limits where they arise; asides demoted; opposition quoted verbatim; "
             "concrete before abstract; and the whole thing sounds like the model-prose paper, not like an essay "
             "that wants to be admired. Then check the paper type's Style Module for its own register additions."),
    ("bullet", "Dash discipline (default). Chained dashes are a leading AI tell, and several working authors ban "
               "prose dashes outright. The shipped default: in the Style & Voice stage, remove dash-chains and "
               "dash asides that don't earn their place — use a colon, a comma, parentheses, or a new sentence "
               "instead. (Hyphenated compound words and page-range hyphens are not dashes and stay.) Record THIS "
               "author's dash policy in the Voice Profile at setup and follow it."),
]

# ---------------------------------------------------------------- Voice Profile (TEMPLATE)
voice = [
    ("title", "Voice Profile — Sentence & Paragraph Craft"),
    ("subtitle", "What to match when drafting for THIS author, at the level authors care about most: the "
                 "sentence, then the paragraph — not the architecture. TEMPLATE — built from the author's own "
                 "papers at setup (see 'SETUP — Personalize the Agent', Step 4)."),
    ("note", "STATUS: TEMPLATE — this profile has not been personalized yet. Claude: do not draft a paper "
             "against this template; run the setup procedure first. To build the profile: read 3–6 of the "
             "author's papers IN FULL (the Model Prose Library), fill every pattern below with the author's "
             "actual pattern plus 1–2 VERBATIM example sentences from their papers, build the signpost "
             "whitelist, record the personal rules, then review the finished profile with the author. Rebuild "
             "this document (new version) with the findings; delete this status note in the personalized "
             "version."),
    ("h1", "The single instruction"),
    ("body", "Write the sentences this author would write. [TODO after mining: a 3–4 sentence portrait of the "
             "author's prose — its default length and rhythm, what it never does, what it reaches for, and the "
             "when-in-doubt rule. Example shape: 'Plain, short, and concrete, with a deliberate rhythm — a "
             "longer sentence sets up, a short one lands. Never hedges in stacks, never decorates. When in "
             "doubt, shorten the sentence and make it concrete.']"),
    ("h1", "The patterns (fill each with the author's pattern + verbatim examples)"),
    ("body", "1. Rhythm and sentence length. How long do sentences run? Is variation deliberate (long setup, "
             "short landing)? Are fragments ever used, and for what? [TODO: pattern + verbatim examples.]"),
    ("body", "2. Openings. How do sentences and paragraphs start — with the subject? with plain connectives "
             "(But, So, Then)? with scene-setting? Does the author open with throat-clearing, or never? "
             "[TODO: pattern + verbatim examples.]"),
    ("body", "3. Questions. Does the author pose questions? Answered how — bluntly, at length, rhetorically? "
             "How often? [TODO: pattern + verbatim examples.]"),
    ("body", "4. Anchoring abstractions. When an abstract claim appears, what follows — a concrete case, a "
             "number, a named example, a present-tense picture? How fast? [TODO: pattern + verbatim examples.]"),
    ("body", "5. Labels and coinages. Does the author coin compact labels for ideas? How are they cashed out "
             "('That is,…')? How sparingly? [TODO: pattern + verbatim examples.]"),
    ("body", "6. Hedging. How does the author qualify claims — single precise qualifiers or stacked ones? How "
             "are honest limits stated? [TODO: pattern + verbatim examples.]"),
    ("body", "7. Concessions. How does the author grant a point before answering it (concede-then-affirm, or "
             "another move)? [TODO: pattern + verbatim examples.]"),
    ("body", "8. Punctuation. Colons, semicolons, dashes, parentheses — which does the author actually reach "
             "for, and for what work? What never appears? [TODO: pattern + verbatim examples.]"),
    ("body", "9. Verbs, voice, tense, person. Active or passive? Plain or fancy verbs? 'I' or 'we' (and does "
             "the field fix this)? Present or past tense for claims? Nominalizations? [TODO: pattern + verbatim "
             "examples.]"),
    ("body", "10. Paragraph shape. Where does the paragraph's claim sit (topic sentence first?)? Typical length "
             "in sentences? How do paragraphs end — on a beat, or on ordinary workmanlike sentences? [TODO: "
             "pattern + verbatim examples.]"),
    ("h1", "Signposts the author actually uses (and the anti-AI calibration rule)"),
    ("body", "[TODO: the WHITELIST — transition and framing phrases mined from the author's papers, verbatim. "
             "These are in the author's voice; the anti-LLM pass must never strip them.] The calibration rule is "
             "fixed: if a phrase appears in the model prose, it stays; if it is generic AI throat-clearing that "
             "never appears in the author's papers, it goes. Typical offenders to cut when they are NOT in the "
             "whitelist: 'Ultimately,' 'Crucially, however,' 'The upshot is that,' 'it is worth pausing to "
             "reflect,' stacked hedges, three-part lists where two suffice, dash-chains, and "
             "paragraph-restating summary sentences."),
    ("h1", "Personal rules"),
    ("body", "[TODO: the author's hard rules, mined or stated at setup — e.g. a dash policy; banned words or "
             "phrases; fragment tolerance; anything the author strikes on sight. One line each, stated as "
             "rules.]"),
    ("h1", "How to use this when drafting"),
    ("body", "(1) Before Stage-4 drafting, read the single closest paper in the Model Prose Library in full — "
             "the sentences set the register better than any rule. (2) Draft to the patterns above, sentence by "
             "sentence. (3) In Stage 6, run the dedicated sentence-level rounds (separate from argument and "
             "structure work): read each sentence and ask — would this author write it? is the abstraction "
             "anchored the way they anchor? is the hedge theirs? does the paragraph open and close the way "
             "theirs do? Then run the anti-AI pass calibrated to the whitelist above."),
]

# ---------------------------------------------------------------- Revise & Resubmit Module
rr = [
    ("title", "Revise & Resubmit Module"),
    ("subtitle", "Pipeline Stage 11 — when a journal returns referee reports. v1.0 — Shareable Edition (drafted "
                 "from one real case in the original agent; refine it after this author's first real R&R)."),
    ("h1", "When this module fires"),
    ("body", "Referee reports arrive on a submitted paper (R&R, conditional accept, or a reject-with-reports "
             "worth answering at a new venue). The module produces two deliverables: the revised manuscript "
             "(built under the agent's normal change-log discipline) and the response letter. The response "
             "letter is a first-class document — referees judge the revision through it."),
    ("h1", "The process"),
    ("body", "R1 — Inventory. Read the reports cold and build a Point Inventory: every distinct referee point "
             "gets a number, the referee's text (verbatim or tightly quoted), and its location in the "
             "manuscript. Completeness is the gate — run a count check against the raw reports; a missed point "
             "is a desk-reject risk. Points include praise (it calibrates what not to break) and editor "
             "instructions."),
    ("body", "R2 — Response plan. For each point, propose a disposition: accept-and-revise / accept-in-part / "
             "decline-with-reason / correct-a-misreading. Flag which points are load-bearing (touch the thesis "
             "or architecture) versus local. Estimate what each accepted revision costs (a sentence, a "
             "paragraph, a section, new analysis). AUTHOR GATE: the author approves the dispositions before any "
             "prose changes. Don't relitigate the author's calls later."),
    ("body", "R3 — Revise. Implement the accepted revisions with the agent's usual discipline: every change "
             "logged and tied to its point number; the author-round protocol applies if the author has touched "
             "the manuscript meanwhile; the deterministic self-check (isolation diff + change log) verifies "
             "nothing else moved. New or changed citations go through the citation-auditor. New or rewritten "
             "prose gets a voice walk before the author reads it."),
    ("body", "R4 — Response letter. Write the response letter in the author's register (defaults below): "
             "referee text in full, responses inline after each point. Every 'we have revised' names the "
             "location and QUOTES the added or changed text — an unanchored 'we address this' is a defect. "
             "Declines give a real reason."),
    ("body", "R5 — Final check. Verify every inventory point has a response; citation-auditor clean on new "
             "material; render both documents to PDF and eyeball; the author reads letter + revision before "
             "anything is submitted."),
    ("h1", "The response-letter register (defaults — calibrate to the author's own prior letters when they exist)"),
    ("body", "Format. Open with brief thanks to the referees and editor, then reproduce each referee point with "
             "the response after it. Set responses off visibly — a distinct color is the common convention (and "
             "unlike paper drafts, a response letter is a place where colored text is expected; confirm the "
             "author's preference)."),
    ("body", "Candor. Candid when wrong: name the error, give the fix, move on. No defensiveness, no "
             "over-apology."),
    ("body", "Quote the fix. Concessions are specific and quoted: 'I've added the following clarification above "
             "the table: \"…\"' — the referee sees exactly what changed without opening the manuscript."),
    ("body", "Declining. Declines are graceful and reasoned, usually on the paper's economy: the discussion "
             "would distract from the central argument; the suggestion belongs to a different paper. It is fine "
             "to note that a cut discussion existed in an earlier version. Never decline by ignoring."),
    ("body", "History. Be transparent about the paper's history where it bears on the reports (predecessor "
             "versions, title changes, what will be updated where)."),
    ("body", "Spine. Keep the thesis's shape. Referees get real engagement, not capitulation: accept what "
             "improves the paper, bound each concession precisely, and answer the strongest version of a "
             "criticism rather than its wording."),
    ("h1", "What not to do"),
    ("body", "No groveling or flattery beyond the standard thanks. No restating the whole paper. No response "
             "that just says 'addressed' without location + quoted text. No new claims that bypass the "
             "citation-auditor. No touching points the author declined at R2. No submitting anything the author "
             "hasn't read."),
]

# ---------------------------------------------------------------- Model Prose Library — Catalog (TEMPLATE)
catalog = [
    ("title", "Model Prose Library — Catalog"),
    ("subtitle", "Full-text examples of the AUTHOR's own prose, for Claude to match in voice, density, and "
                 "structure. TEMPLATE — populated at setup (see 'SETUP — Personalize the Agent', Step 3)."),
    ("note", "STATUS: EMPTY — no examples yet. Claude: populate this library at setup before drafting any "
             "paper. This catalog is the index; the PDFs (and extracted-text .txt files) beside it are the "
             "prose. Read the actual example(s) closest to the paper's type and target venue IN FULL before "
             "Stage-4 drafting — they set the register far better than any rule."),
    ("h1", "How to populate (and grow) the library"),
    ("bullet", "At setup: 3–6 of the author's best or most representative papers, ideally spanning the types "
               "they write. Published versions preferred. For each: the PDF, a ' — extracted text.txt' "
               "extraction beside it, and a catalog row below."),
    ("bullet", "The row's load-bearing column is WHAT TO IMITATE — named precisely (the argument shape, the "
               "way formalism is introduced, the objection-handling, the opening move), never just 'good "
               "prose'. Write it after actually analyzing the paper (setup Step 4)."),
    ("bullet", "Growing collection: add every new example the author likes — including, over time, papers the "
               "agent helped write once the author judges them representative. Keep coverage by type in the "
               "closing paragraph current."),
    ("bullet", "Early-career authors with few papers: use what exists, and add 1–2 admired papers by OTHERS in "
               "the field as register models — mark them clearly as register models (structure, conventions), "
               "with the author's own prose remaining the voice authority."),
    ("bullet", "The per-paper Model Prose/ folder still holds the single closest anchor for each paper; this "
               "shared library is the cross-paper collection referenced from CLAUDE.md and each Style Module."),
    ("h1", "Catalog"),
    ("table", [
        ["Example (file in this folder)", "Type · length · venue", "What to imitate in it"],
        ["[TODO — e.g. Author — 'Title' ('file.pdf')]", "[TODO — e.g. journal article; ~8,000 words; Venue]",
         "[TODO — the precise things this paper exemplifies: its opening move, its argument-naming, how it "
         "introduces machinery, its objection handling…]"],
        ["[TODO]", "[TODO]", "[TODO]"],
    ], [2.6, 2.0, 4.2]),
    ("body", "Coverage by type: [TODO — one line mapping each paper type the author writes to its closest "
             "example, so the Stage-0 'model-prose anchor' question has a default answer.]"),
]

# ---------------------------------------------------------------- 0. Project Setup & Folder Structure
proj_setup = [
    ("title", "Project Template — Setup & Folder Structure"),
    ("subtitle", "How to start a new paper in the correct structure — shared playbook. v1.0 — Shareable "
                 "Edition."),
    ("body", "Use this every time a new paper starts. The full process is in the Pipeline; this is just the "
             "start-up template and the standard folder structure (so every paper looks the same)."),
    ("h1", "Start here — the first steps of a new paper"),
    ("num", "Intake first — ask the author up front. Ask the paper TYPE (this picks the Style Module) and the "
            "rest of the Setup Contract — title, one-sentence thesis (or the Argument Sketch), target venue + "
            "length (offer the type default), coauthors + author order (per the Context doc's convention), "
            "model-prose anchor, hard-nos, and autonomy (four gates / run straight through / every gate). Lead "
            "with type; use the interactive picker for the menu choices. Don't make the author remember to "
            "specify these."),
    ("num", "Scaffold the project: python3 \"Behind the scenes (Claude)/Build scripts/new_paper.py\" "
            "\"<Title>\" \"<type>\" [\"<length>\"]. This creates the folder tree below, the Project Checklist "
            "(FIRST), and a Progress Log stub. (Or copy this Project Template by hand.)"),
    ("num", "Load the inputs: the author's 1-page brief into Brief/; the real PDFs of the core interlocutors "
            "into Background Readings/ (convert to text); and a prior paper to imitate for voice into "
            "Model Prose/."),
    ("num", "Open the Project Checklist and drive everything from it — top to bottom, a row filled only when "
            "its step is genuinely done, evidence written from the finished artifact, never pre-filled."),
    ("num", "Read the General docs (the Pipeline, the paper-type Style Module, Context, the Voice Profile) and "
            "the root Writing Guide; then build the Literature Map and the Plan."),
    ("num", "At every stage, run the lenses; pass the AUDITOR gate at the reserved gates (its only job: "
            "confirm the claimed work was actually done) or attach the deterministic self-check; and invoke "
            "the specialist agents where the Pipeline says (referee panel; citation-auditor; copy-critic). "
            "Pause for the author at the four human gates (Argument Sketch, Plan, Paragraph Outline, voiced "
            "draft) unless told 'run straight through'."),
    ("body", "Why checklist-first + auditor matters: if the checklist is created late or pre-filled, the "
             "layered outline, the revision rounds, the referee passes, and the citation audit tend to get "
             "recorded as 'done' without being done. Creating and honestly working the checklist from minute "
             "one — and letting the independent auditor gate the reserved stages — keeps every step real."),
    ("h1", "The standard folder structure (the same for every paper)"),
    ("table", [
        ["Folder", "What it holds"],
        ["Brief/", "The author's 1-page project description (thesis; central arguments; target journal; word "
         "budget; 3–5 key sources) + any notes or draft fragments. The source of truth for intent."],
        ["Background Readings/", "Real PDFs of the core interlocutors (read these, not training memory) + "
         "Converted text/."],
        ["Model Prose/", "A prior paper by the author, read for VOICE/register only (never for content)."],
        ["WIP Docs/", "Every working doc, by type: Literature Map, Plan, Outline (3A/3B/3C), Draft, Abstract, "
         "Referee Reports, Change Logs — each main type with its own Old versions/."],
        ["Progress reports/", "Clean & author-facing: the Project Checklist (created FIRST), the running "
         "Progress Log, the Argument & Objection Coverage Map, and the Stage-12 Retrospective."],
        ["Scrap/", "Working/review material: the Claims-to-Verify register, the Citation Audit, the Setup "
         "Brief (in Review artifacts/), and converted source text."],
        ["Submission/", "ONLY the file(s) literally submitted (final .docx, and .pdf/.tex where the type "
         "calls for it)."],
        ["Behind the scenes (Claude)/", "This paper's own build scripts (they import the shared gen_docx / "
         "gen_paper_docx)."],
    ], [1.7, 7.1]),
    ("h2", "WIP Docs subfolders (one per document type)"),
    ("bullet", "Literature Map  •  Plan  •  Outline (3A Skeleton / 3B Argument / 3C Paragraph, as named "
               "versions)  •  Draft  •  Abstract  •  Referee Reports  •  Change Logs — each main type with its "
               "own Old versions/."),
    ("h1", "Created at setup, before any deliverable"),
    ("bullet", "The standard folder tree (above)."),
    ("bullet", "The Project Checklist — created FIRST, worked top-to-bottom (from Project Checklist TEMPLATE "
               "or the scaffolder)."),
    ("bullet", "The running Project Progress Log (a stub, appended at each gate)."),
]

if __name__ == "__main__":
    build(os.path.join(GG, "1b. Context — Authors, Venues, Preferences.docx"), context,
          header_lines=HDR, footer_text="Deep Drafter   |   Context")
    build(os.path.join(GG, "Prose Register — All Paper Types.docx"), register,
          header_lines=HDR, footer_text="Deep Drafter   |   Prose Register")
    build(os.path.join(GG, "Voice Profile — Sentence & Paragraph Craft.docx"), voice,
          header_lines=HDR, footer_text="Deep Drafter   |   Voice Profile")
    build(os.path.join(GG, "Revise & Resubmit Module.docx"), rr,
          header_lines=HDR, footer_text="Deep Drafter   |   Revise & Resubmit")
    build(os.path.join(GG, "Model Prose Library", "Model Prose Library — Catalog.docx"), catalog,
          header_lines=HDR, footer_text="Deep Drafter   |   Model Prose Library")
    build(os.path.join(GG, "Project Template", "0. Project Setup & Folder Structure.docx"), proj_setup,
          header_lines=HDR, footer_text="Deep Drafter   |   Project Template")
    # Checklist TEMPLATE — generated from new_paper.py so the script and template never drift.
    blocks = checklist_blocks("[Paper Title]", "philosophy", None)
    blocks[0] = ("title", "[Paper Title] — Project Checklist (TEMPLATE)")
    build(os.path.join(GG, "Project Template", "Project Checklist TEMPLATE.docx"), blocks,
          header_lines=HDR, footer_text="Deep Drafter   |   Project Checklist TEMPLATE")
    print("general guide built")
