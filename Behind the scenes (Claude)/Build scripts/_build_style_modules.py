#!/usr/bin/env python3
"""Build the Style Modules of the Shareable Edition: Philosophy Paper, Law Review, Cambridge
Element, Empirical Social Science Paper, the Analytic Philosophy field-register EXAMPLE, and
the _Template for new types. Check mirrors/mtimes before regenerating over a possibly-edited
Word master (versioning rules apply)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_docx import build

SM = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
                  "General Guide to Academic Writing", "Style Modules")
HDR = ["Deep Drafter"]

LAYER_NOTE = ("This is the PER-TYPE layer. The root 'Writing Guide — House Style' is the shared core and "
              "applies IN FULL to every type (strong direct arguments; no editorializing; no verbal disputes; "
              "one move per sentence; cut filler; each argument in exactly one place). This module only adds "
              "what is specific to this paper type: length, citation/footnote practice, structure, and "
              "register. Defaults below are starting points — confirm them against the author's real venues "
              "at setup.")

philosophy = [
    ("title", "Philosophy Paper — Style Module"),
    ("subtitle", "Journal article in philosophy. v1.0 — Shareable Edition."),
    ("note", LAYER_NOTE),
    ("h1", "Register — read the companion guide (REQUIRED)"),
    ("body", "For sentence- and paragraph-level register, this module is paired with 'Analytic Philosophy "
             "Prose — Style Guide' (same folder) — the field-register companion (displays; premise-form "
             "central argument; named-vignette cases). Read it before drafting Stage-4 prose and again before "
             "any register pass, after the general 'Prose Register — All Paper Types'."),
    ("h1", "Target length"),
    ("body", "Default ~7,000–8,000 words (some journals allow ~10–12k; confirm the target journal's limit in "
             "the Setup Contract). Abstract ~150–250 words."),
    ("body", "Tight. Compress aggressively; nail one thing and generalize rather than surveying every variant. "
             "Demote secondary material to footnotes rather than padding the body."),
    ("h1", "Citations & footnotes"),
    ("body", "Author-date in-text ('Smith 2024', 'Smith 2024, 12') with a reference list at the end."),
    ("body", "Footnotes sparingly — only for genuinely substantive asides (a qualification, a secondary "
             "objection, a pointer), NOT as the main citation vehicle. If a point matters, put it in the main "
             "text; if it doesn't, cut it or footnote it (prefer footnoting to hedging)."),
    ("body", "Strip jargon, even from footnotes; plain English over heavy formalism. Push any heavy formal "
             "apparatus to an appendix and keep the main text readable."),
    ("h1", "Structure conventions"),
    ("body", "5–7 numbered sections (1, 2, 3 …) plus an optional appendix. Front-loaded thesis (abstract + "
             "first ¶ of the intro + first ¶ of the body)."),
    ("body", "Displays: named principles, the paper's own view (stated in full), named cases (as "
             "self-contained vignettes), and the central argument in premise form are all set as indented "
             "bold-label displays — the ('display', 'Label.', 'text') block in gen_docx / gen_paper_docx. "
             "Details and examples in the field-register companion."),
    ("body", "Interleaved objections per argument, plus a dedicated objections section for the 1–3 largest "
             "cross-cutting ones — the dual structure that reads rigorous without reading defensive."),
    ("body", "3–5 affirmative arguments per section, each a numbered paragraph; brief steelman then direct "
             "response to objections."),
    ("h1", "Register & voice (on top of the Writing Guide)"),
    ("body", "Argument-directive journal register: philosophical rather than survey-style; footnote-tolerant; "
             "moderate formality. Hold the reader's hand in the main text; keep density in the appendix."),
    ("body", "Match the SPECIFIC target journal — different philosophy journals differ in length, formality, "
             "and section style; confirm the house conventions in the Setup Contract."),
    ("h1", "Model prose"),
    ("body", "A prior philosophy paper by the author in the same register (chosen at setup — see the Model "
             "Prose Library catalog's coverage-by-type line). Put the chosen one in the paper's Model Prose/ "
             "folder and read it for voice before drafting — sentence shapes, not content. Also read the "
             "closest example in the shared Model Prose Library in full before Stage-4 drafting."),
    ("h1", "Referee lenses (Stage 8 — spawned BLIND)"),
    ("body", "The fixed trio for a philosophy paper: (1) a specialist in the paper's own sub-field / the "
             "tradition it targets (the hostile expert); (2) a broad philosophy GENERALIST — the venue's "
             "typical gatekeeper, who judges whether it is a genuine, publishable contribution; (3) a "
             "foundations/adjacent specialist who can pressure-test the deepest formal or metaethical "
             "commitments. Fresh personas each round, same three lenses. Each is spawned BLIND (only its lens "
             "+ the manuscript + the venue; no summary of the paper's claims, no leading questions) and reads "
             "the footnotes. Add one standing 'case-for-acceptance' reader to offset the built-in "
             "revise-and-resubmit lean. See referee.md and the Pipeline for the full standard (read the "
             "trajectory not the label; cap the rounds; author-owned Finish)."),
    ("h1", "Special passes / notes"),
    ("body", "Pinpoint citations are the most error-prone element — the citation-auditor checks every 'X "
             "argues Y on p. Z'."),
    ("body", "For a formal paper, verify any .tex build recompiles to an identical PDF before shipping "
             "(pdftotext diff)."),
]

law = [
    ("title", "Law Review — Style Module"),
    ("subtitle", "Student-edited law-review article. v1.0 — Shareable Edition."),
    ("note", LAYER_NOTE),
    ("h1", "Target length"),
    ("bullet", "Default ~25,000 words INCLUDING footnotes (full articles often run 25,000–35,000; the "
               "footnotes are a large fraction of the total). Confirm the target review's preferred length in "
               "the Setup Contract."),
    ("bullet", "A practical band from real runs: ~20,000 words including footnotes is the SUBMISSION FLOOR for "
               "top general law reviews; ~23,000–25,000 is the OPTIMUM. Drafting targets aim inside the band, "
               "not at the floor."),
    ("bullet", "Length is real here, but it still follows from the argument and the apparatus — build the fat "
               "outline and let the footnotes carry weight; do not pad the body."),
    ("h1", "Citations & footnotes"),
    ("bullet", "Bluebook footnotes — the defining feature. Nearly every sentence/proposition carries a "
               "footnote; string citations with signals (see, see also, cf., but see); short forms (id., "
               "supra, infra); pincites throughout."),
    ("bullet", "Substantive footnotes are common and can be long (qualifications, counterarguments, parallel "
               "authority)."),
    ("bullet", "Draft with placeholder cites and (verify) tags; a heavy end-stage footnote-build pass (Stage "
               "10) turns placeholders into full Bluebook footnotes. No in-text author-date."),
    ("bullet", "The first footnote conventionally carries the author line/acknowledgments; the thesis is often "
               "previewed there too."),
    ("h1", "Structure conventions"),
    ("bullet", "Introduction that does heavy lifting: states the problem, the contribution/novelty, and an "
               "explicit ROADMAP of the Parts."),
    ("bullet", "Roman-numeral Parts (I, II, III …), sections (A, B, C), subsections (1, 2, 3), sub-subsections "
               "(a, b, c). Typically a descriptive Part (the problem / the doctrine) before the normative Part "
               "(the proposal)."),
    ("bullet", "Conclusion. Named-argument labels reused across intro, Part headings, and conclusion."),
    ("h1", "Register & voice (on top of the Writing Guide)"),
    ("bullet", "Law-review register: exposition-heavy and heavily sign-posted; authority-driven (the footnotes "
               "carry the proof); accessible to a generalist legal reader; the contribution stated explicitly."),
    ("bullet", "The Writing Guide still governs the prose — direct arguments, no editorializing — but expect "
               "more scaffolding and roadmapping than a philosophy paper."),
    ("h1", "Model prose"),
    ("bullet", "A prior law-review article by the author (or, if none exists, a well-placed recent article in "
               "the target review, marked as a register model). Put it in Model Prose/ and read for structure "
               "(Parts, roadmap, footnote density) and voice."),
    ("h1", "Referee lenses (Stage 8 — spawned BLIND)"),
    ("bullet", "The fixed trio: one DOCTRINAL reader, one THEORY/NORMATIVE reader, one PRACTICAL/INSTITUTIONAL "
               "reader. Student-edited selection also rewards a crisp novelty claim — the case-for-acceptance "
               "reader doubles as the articles-editor check."),
    ("h1", "Special passes / notes"),
    ("bullet", "The footnote-build pass is the biggest type-specific effort — budget for it; the "
               "citation-auditor verifies pincites against real sources."),
    ("bullet", "Student-edited: claims of novelty and a crisp contribution statement matter; the referee panel "
               "should include a doctrinal reader."),
]

element = [
    ("title", "Cambridge Element — Style Module"),
    ("subtitle", "Short monograph (Cambridge Elements series or similar) or book chapter. v1.0 — Shareable "
                 "Edition."),
    ("note", LAYER_NOTE),
    ("h1", "Target length"),
    ("bullet", "Default ~30,000 words (Elements run ~20,000–35,000). Set the exact target in the Setup "
               "Contract; the press gives a word ceiling per series — treat it as a hard cap."),
    ("bullet", "It is a short MONOGRAPH — longer and more self-contained than a journal article, shorter than "
               "a book. Budget several substantive sections plus a real introduction and conclusion."),
    ("h1", "Citations & footnotes"),
    ("bullet", "Author-date in-text ('Smith 2024', 'Smith 2024, 145') with a reference list at the end."),
    ("bullet", "Footnotes are substantive, used moderately — genuine asides, qualifications, and pointers — "
               "not a citation apparatus (citations go in-text)."),
    ("bullet", "Drafting placeholders '(Author Year)' resolve in the Stage-10 citation audit against the real "
               "sources."),
    ("h1", "Structure conventions"),
    ("bullet", "A motivating Introduction that frames the whole topic for an interested but non-specialist "
               "reader, states the thesis up front, and roadmaps the sections."),
    ("bullet", "Several substantive sections/chapters, each opening with its numbered arguments listed at the "
               "top (e.g., 'three economic arguments'); each argument then develops in its own subsection with "
               "a clean topic sentence, sustained development, and concrete examples."),
    ("bullet", "Numbered sub-arguments within subsections; named-argument labels reused across the whole "
               "Element."),
    ("bullet", "A forward-looking Conclusion (not a recap). Optional brief 'state of the field' early, since "
               "readers may be newcomers to the topic."),
    ("h1", "Register & voice (on top of the Writing Guide)"),
    ("bullet", "Monograph register: accessible and pedagogically clear; define terms; assume an interested "
               "reader, not a sub-field specialist. Still fully argument-driven — the Writing Guide's "
               "directness applies."),
    ("bullet", "Broader framing than a single journal article: the Element makes a sustained case across "
               "chapters, so motivate the topic and connect the chapters, without re-arguing a point made "
               "elsewhere (cross-reference instead)."),
    ("bullet", "Short emphatic sentences mixed with longer accumulating ones; specific figures, named actors, "
               "dated events embedded inline."),
    ("h1", "Model prose"),
    ("bullet", "The author's own long-form work where it exists (chosen at setup); otherwise an admired "
               "Element in the target series, read for STYLE and chapter architecture, not content."),
    ("h1", "Referee lenses (Stage 8 — spawned BLIND)"),
    ("bullet", "Elements are peer-reviewed — the trio should include a generalist in the series' field, a "
               "sub-field specialist, and one adjacent-field reader for the chapters that import machinery."),
    ("h1", "Special passes / notes"),
    ("bullet", "Chapters can stand somewhat alone; ensure the named-argument labels and cross-references are "
               "consistent across the whole work in the Stage-10 integration pass."),
]

empirical = [
    ("title", "Empirical Social Science Paper — Style Module"),
    ("subtitle", "Quantitative or mixed-methods empirical article (economics, psychology, political science, "
                 "sociology, management, …). v1.0 — Shareable Edition. STARTER MODULE — empirical venues vary "
                 "widely; confirm every default against the target venue at setup."),
    ("note", LAYER_NOTE),
    ("h1", "How the Pipeline adapts for empirical work"),
    ("bullet", "The results are the paper's spine. Stage 3's layered outline is organized around the ANALYSES: "
               "which tables and figures will exist, what each shows, and what claim each supports — one "
               "outline bullet per planned result, with its (verify) tag. The 'arguments' of the argumentative "
               "default become the paper's claims-from-evidence."),
    ("bullet", "The agent drafts around the author's results; it never invents them. Numbers, tables, and "
               "figures come from the author's analysis outputs, loaded like Background Readings. Every number "
               "in the prose carries a (verify) tag until checked against the source output."),
    ("bullet", "The Literature Map doubles as the positioning for the contribution statement: what is known, "
               "what this design adds, which prior estimates this one speaks to."),
    ("h1", "Target length"),
    ("bullet", "Default ~8,000–12,000 words plus tables/figures and appendices — but venue norms differ by "
               "an order of magnitude across fields (an economics job-market paper is not a psychology brief "
               "report). Set the target from the venue at Intake."),
    ("h1", "Citations & footnotes"),
    ("bullet", "Per the venue: author-date (APA/Chicago-style) in most social sciences; numbered in some. "
               "Footnotes sparse; methods details go to the appendix or supplement, not to footnotes."),
    ("h1", "Structure conventions"),
    ("bullet", "The standard arc: Introduction (motivation, question, preview of findings and contribution) → "
               "Literature/Background → Data & Methods → Results → Discussion (interpretation, limitations, "
               "implications) → Conclusion. Field variants exist (economics folds literature into the intro; "
               "psychology may run multiple studies each with methods/results) — follow the venue's exemplars."),
    ("bullet", "The introduction states the finding, not just the question — the reader should know the "
               "headline result and the contribution by the end of page one."),
    ("bullet", "Methods written for reproducibility: design, sample, measures, estimation strategy, "
               "pre-registration status, data availability — at the venue's customary depth."),
    ("bullet", "Results follow the analysis plan; every claim in the text matches its table or figure exactly. "
               "Limitations stated plainly in the Discussion, where they arise — not as apology."),
    ("h1", "Register & voice (on top of the Writing Guide)"),
    ("bullet", "Precise and unadorned; no drama adjectives around effect sizes; hedges are statistical, not "
               "rhetorical (confidence and uncertainty stated once, in the accepted vocabulary)."),
    ("bullet", "Tense conventions per field (commonly: past tense for what was done and found; present for "
               "what the results show/mean). Confirm against the venue's exemplars and the author's own "
               "papers."),
    ("h1", "Model prose"),
    ("bullet", "The author's own empirical papers (chosen at setup); supplement with 1–2 well-regarded recent "
               "articles in the target venue as structure models."),
    ("h1", "Referee lenses (Stage 8 — spawned BLIND)"),
    ("bullet", "The fixed trio: one METHODS/STATISTICS reader (design validity, estimation, inference, "
               "robustness), one SUBSTANTIVE-FIELD expert (does this speak to the literature; are the "
               "mechanisms plausible), one venue GENERALIST (contribution and clarity)."),
    ("h1", "Special passes / notes"),
    ("bullet", "Numbers-consistency pass (Stage 10, before the citation audit): every statistic in the text, "
               "abstract, and tables agrees; N's add up; percentages match counts; the abstract's numbers "
               "appear in the body. This is the empirical sibling of the cross-reference check."),
    ("bullet", "Verify the required statements exist per venue: data availability, pre-registration, ethics/"
               "IRB, conflicts, funding."),
    ("bullet", "The citation-auditor also checks that empirical claims about PRIOR work state the right "
               "direction and magnitude — misquoted effect sizes are this genre's fabricated pinpoint."),
]

analytic = [
    ("title", "Analytic Philosophy Prose — Style Guide"),
    ("subtitle", "EXAMPLE field-register companion (analytic philosophy) — paired with the Philosophy Paper "
                 "module, and a model for writing your own field's register companion. v1.0 — Shareable "
                 "Edition."),
    ("note", "WHAT THIS IS. Some fields have register conventions beyond what a Style Module's mechanics "
             "capture — recurring formatting and argument-presentation moves that mark competent work in the "
             "field. This document is the analytic-philosophy example, distilled from a real author-correction "
             "round in the original agent. If your field has its own such conventions (proof environments, "
             "case-report structure, ethnographic voice), write the analogous companion at setup and name it "
             "from your Style Module."),
    ("h1", "Where this sits"),
    ("body", "Three layers apply to a philosophy paper's prose, in order: the root 'Writing Guide — House "
             "Style' (house law), 'Prose Register — All Paper Types' (the general register: explain before "
             "use, no metaphors doing argument work, plain referents, concrete before abstract, roadmap and "
             "limits discipline, quoting the opposition), and then this guide. The Philosophy Paper style "
             "module governs mechanics (length, citations, structure)."),
    ("h1", "1. Displays: principles, views, cases, premises"),
    ("body", "This module's standing convention: the main views, principles, and examples under discussion get "
             "indented bold-label formatting. In gen_docx / gen_paper_docx this is the ('display', 'Label.', "
             "'text') block — indented, bold label, body text."),
    ("bullet", "Every named principle under discussion gets a display: the principle stated in one or two "
               "plain sentences under its bold name."),
    ("bullet", "The paper's own view gets a display, stated IN FULL, early — the reader should be able to "
               "quote the thesis from the display alone."),
    ("bullet", "Auxiliary principles the paper relies on get displays too, introduced only after their "
               "ingredients are explained (general guide: 'explain before use')."),
    ("h1", "2. Cases as named vignettes"),
    ("body", "Every named case is a displayed vignette: bold name, a 2–4 sentence self-contained story in the "
             "display, and the analysis in the following paragraphs — never interleaved with the story. The "
             "vignette contains everything the analysis will use: if the analysis needs a stipulation, it goes "
             "in the story, not in a later aside."),
    ("h1", "3. The central argument in premise form"),
    ("body", "The paper's central argument appears once, as displayed premises (Premise One, Premise Two, …, "
             "Conclusion): simple premises that VISIBLY imply the conclusion — no enthymemes at the paper's "
             "load-bearing joint. The surrounding text says where each premise is defended ('Premise one was "
             "defended in sections 3 and 4. This section defends premise two.')."),
    ("h1", "4. Philosophy-register notes"),
    ("bullet", "Solo papers use 'I' throughout ('I will argue', 'I defend'); no authorial 'we'. Coauthored "
               "papers use 'we'."),
    ("bullet", "Objections: only the strongest few (3–4 for a journal paper). Steelman briefly in the "
               "objector's voice, then reply plainly."),
    ("bullet", "Defending a view from inside several ethical or theoretical frameworks in turn is a standard "
               "and welcome structure — one framework per stretch, plainly labeled — because different readers "
               "want different routes to the conclusion."),
    ("bullet", "Terminology credits and formal refinements go to footnotes — the general guide's demotion "
               "rule, with footnotes as philosophy's vehicle."),
    ("body", "Philosophy additions to the pre-return checklist (run the general guide's checklist first): "
             "every principle / the view / every case / the central argument displayed; each display "
             "self-contained; premises visibly valid with their defense locations named; objections capped and "
             "steelmanned; 'I' not 'we' when solo; asides in footnotes."),
]

template = [
    ("title", "[New paper type] — Style Module"),
    ("subtitle", "Copy this file, rename it to the type, and fill every section. v1.0 — Shareable Edition."),
    ("note", LAYER_NOTE),
    ("body", "After writing the module: (1) add the type to TYPE_PRESETS in new_paper.py (default length + "
             "one-line posture) so the scaffolder recognizes it; (2) if the field has distinctive register "
             "conventions beyond mechanics, write a field-register companion too (see 'Analytic Philosophy "
             "Prose — Style Guide' for the shape) and name it from this module. Examples already built: "
             "Philosophy Paper, Law Review, Cambridge Element, Empirical Social Science Paper."),
    ("h1", "Target length"),
    ("bullet", "[Default word count + range; where the venue sets a hard cap; abstract length.]"),
    ("h1", "Citations & footnotes"),
    ("bullet", "[In-text author-date vs footnotes vs numbered? Reference list? Footnote role — substantive vs "
               "citation apparatus? How placeholders resolve.]"),
    ("h1", "Structure conventions"),
    ("bullet", "[Section numbering scheme; intro/roadmap expectations; objection or limitations placement; "
               "standard parts; what is the paper's spine.]"),
    ("h1", "Register & voice (on top of the Writing Guide)"),
    ("bullet", "[What this type adds to the shared house style — formality, scaffolding, audience "
               "assumptions, tense/person conventions.]"),
    ("h1", "Model prose"),
    ("bullet", "[The author's prior paper(s) to imitate for voice — put the chosen one in the paper's "
               "Model Prose/ folder; name the Library's closest example.]"),
    ("h1", "Referee lenses (Stage 8 — spawned BLIND)"),
    ("bullet", "[The fixed trio of reading lenses for this type — e.g. one hostile specialist, one venue "
               "generalist, one methods/foundations reader.]"),
    ("h1", "Special passes / notes"),
    ("bullet", "[Any type-specific pass — e.g., a heavy apparatus build, a numbers-consistency check, a "
               "build-format step.]"),
]

if __name__ == "__main__":
    build(os.path.join(SM, "Philosophy Paper.docx"), philosophy,
          header_lines=HDR, footer_text="Deep Drafter   |   Style Module — Philosophy Paper")
    build(os.path.join(SM, "Law Review.docx"), law,
          header_lines=HDR, footer_text="Deep Drafter   |   Style Module — Law Review")
    build(os.path.join(SM, "Cambridge Element.docx"), element,
          header_lines=HDR, footer_text="Deep Drafter   |   Style Module — Cambridge Element")
    build(os.path.join(SM, "Empirical Social Science Paper.docx"), empirical,
          header_lines=HDR, footer_text="Deep Drafter   |   Style Module — Empirical Social Science")
    build(os.path.join(SM, "Analytic Philosophy Prose — Style Guide.docx"), analytic,
          header_lines=HDR, footer_text="Deep Drafter   |   Field Register — Analytic Philosophy (example)")
    build(os.path.join(SM, "_Template (new paper type).docx"), template,
          header_lines=HDR, footer_text="Deep Drafter   |   Style Module Template")
    print("style modules built")
