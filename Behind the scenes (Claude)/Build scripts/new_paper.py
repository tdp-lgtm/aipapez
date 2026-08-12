#!/usr/bin/env python3
"""Scaffold a new academic paper project in the Deep Drafter — in the correct, standard
structure — and create the Project Checklist FIRST so the work is driven by it from step one.

Single source of truth for: the standard per-paper FOLDER TREE, the staged CHECKLIST ROWS, and
the starter Progress Log. The Project Checklist TEMPLATE .docx (General Guide to Academic
Writing/Project Template/) is GENERATED from this script — when the Pipeline revises the stages,
update CHECKLIST_ROWS and regenerate the template in the same change.

Usage:
    python3 new_paper.py "<Paper title>" "<paper type>" ["<target length>"] ["<papers root>"]
e.g.
    python3 new_paper.py "Distributive Justice in Triage" philosophy
    python3 new_paper.py "Platform Liability Reconsidered" law-review "25k words"
    python3 new_paper.py "The Ethics of Attention" cambridge-element

Paper types (set length/citation/structure/register defaults; modules live in
General Guide to Academic Writing/Style Modules/): cambridge-element | philosophy | law-review
| policy-report  (any other string is accepted and treated generically — add a module for it).

It creates Papers/<title>/ with the full folder tree, a starter "<title> - Project Checklist.docx"
(all rows blank) and a "<title> - Project Progress Log.docx" stub, then prints the next steps.
It never overwrites: if the project folder already exists it stops (use --adopt to fill in a
pre-seeded folder without touching existing files).
"""
import os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_docx import build, NEUTRAL_ACCENT

# Agent root = two levels up from this script's dir (.../Paper writing agent/Behind the scenes (Claude)/Build scripts)
_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ENGINE_ROOT = os.path.dirname(os.path.dirname(_SCRIPT_DIR))
DEFAULT_ROOT = os.path.join(ENGINE_ROOT, "Papers")

# --- Paper-type presets: default length + the one-line citation/structure posture. The full module
#     lives in General Guide to Academic Writing/Style Modules/. Unknown types fall back to generic. ---
TYPE_PRESETS = {
    "cambridge-element": ("~30,000 words", "Author-date in-text + reference list; substantive footnotes; chapter-level numbered arguments; monograph register."),
    "philosophy":        ("~8,000 words",  "Author-date in-text + reference list; footnotes sparingly; 5-7 numbered sections; argument-directive journal register."),
    "law-review":        ("~25,000 words", "Bluebook footnotes carrying nearly every proposition; Roman-numeral Parts; roadmapping introduction; heavy end-stage footnote build."),
    "policy-report":     ("~5,000 words",  "Light citation; public-facing register; executive summary; minimal footnotes."),
    "empirical":         ("~10,000 words", "Intro/lit/methods/results/discussion structure; citation style per venue; results conventions govern; precise unadorned register."),
}

# --- The standard per-paper folder tree (leaf dirs; parents created automatically) ---
FOLDER_DIRS = [
    "Brief",                                  # the author's 1-page project description + any notes/draft fragments (the source of truth)
    "Background Readings/Converted text",     # real PDFs of the core interlocutors (read these, not training memory) + extracted text
    "Model Prose",                            # a prior paper by the author, read for VOICE/register only
    "WIP Docs/Literature Map/Old versions",
    "WIP Docs/Plan/Old versions",
    "WIP Docs/Outline/Old versions",          # the three layers (3A Skeleton -> 3B Argument -> 3C Paragraph "fat outline") live here as named versions
    "WIP Docs/Draft/Old versions",
    "WIP Docs/Abstract/Old versions",
    "WIP Docs/Referee Reports",               # the simulated-referee reports, per round
    "WIP Docs/Change Logs",                   # section/before/after/why logs at each author-facing version bump
    "Progress reports/Old versions",          # clean & author-facing: Checklist, Progress Log, Coverage Map, Retrospective
    "Scrap/Review artifacts",                  # Claims-to-Verify register, Citation Audit, Setup Brief, working referee notes
    "Submission",                             # ONLY the file(s) literally submitted (final .docx, and .pdf/.tex for formal/law work)
    "Behind the scenes (Claude)/Build scripts",  # this paper's own build scripts (import the shared gen_docx)
]
# Created on demand, not at setup: "Revise and Resubmit/" — holds the journal's referee reports, the
# Response-to-Referees letter, and Revised/Clean manuscripts when a real R&R arrives (see the Pipeline).

# --- The Project Checklist rows (created FIRST, worked top-to-bottom). [step/lens, outcome, evidence] ---
# Lens keys (the drafting agent's own self-review before each gate):
#   A = Argument (each claim developed & valid; objections steelmanned then answered; no gaps)
#   E = Engagement (key literature/interlocutors engaged; positioned in the niche; no straw men)
#   S = Style (the Writing Guide: one move per sentence; no editorializing; no verbal disputes; no
#       cross-section repetition; model-prose register; named-argument labels consistent)
#   I = Integrity (every empirical claim cited or (verify)-tagged; NO fabricated citations; cross-refs
#       resolve; claims match the body, e.g. "we make four arguments" => four arguments)
# The AUDITOR's sole job is to verify — against the files, not the agent's claims — that the work a row
# claims as done was genuinely done. It does NOT judge quality; the referee panel, citation-auditor,
# and copy-critic do that. You may NOT pass a gate until the auditor returns APPROVE.
CHECKLIST_ROWS = [
    ["Step / review lens", "Outcome", "Evidence / auditor verdict (from the finished artifact; NEVER pre-filled)"],

    ["Setup — standard project folder structure created", "", ""],
    ["Setup — Project Checklist created FIRST; project driven from it", "", ""],
    ["Setup — running Progress Log started", "", ""],
    ["Setup — Setup Contract captured (paper TYPE; target venue; target length; division of labor — how aggressively to cut, who does the substantive rewrite; the model-prose anchor)", "", ""],
    ["Setup — read the core Writing Guide + the paper-type Style Module + the Context doc", "", ""],
    ["Setup — author's 1-page project description loaded to Brief/ (thesis; central arguments; target journal; word budget; 3-5 key sources)", "", ""],
    ["Setup — Background Readings (real PDFs of the core interlocutors) loaded & converted; Model Prose loaded", "", ""],
    ["AUDITOR GATE — Setup (auditor confirms setup genuinely complete before Lit Review)", "", ""],

    ["1. Lit Review — literature actively searched out (WebSearch/scholarly): a relevance-ranked reading list of the key books & papers built; the most relevant read; inaccessible sources flagged for the author to supply (never fabricated or silently skipped)", "", ""],
    ["1. Lit Review — every Background Reading read; per-source notes produced", "", ""],
    ["1. Lit Review — authors' OWN prior work checked for positions that conflict with this paper's thesis", "", ""],
    ["1. Lit Review — Literature Map produced (the critical/constructive landscape; who holds which live position; the OPEN NICHE this paper fills; interlocutors to engage; candidate referees)", "", ""],
    ["1. Lit Review — lenses E/I applied (each: a logged change OR checked-no-change)", "", ""],
    ["AUDITOR GATE — Lit Review", "", ""],

    ["2. Plan — thesis in its sharpest form; the analytic MOVE that makes it work spelled out; why this is the sharpest line, not just a line", "", ""],
    ["2. Plan — section-by-section structure with word budgets (scaled to target length); dialectical structure decided (objections interleaved vs dedicated section vs both); named-argument vocabulary; planned formal apparatus", "", ""],
    ["2. Plan — lenses A/E/S/I applied (each logged)", "", ""],
    ["AUDITOR GATE — Plan", "", ""],
    ["HUMAN SIGN-OFF — Plan [GATE 1] (author confirms thesis/angle/structure before any outline detail; skipped on 'run straight through')", "", ""],

    ["3A. Skeleton outline — top-level parts/chapters, what each covers, in order", "", ""],
    ["3A — lenses A/E applied (each logged)", "", ""],
    ["AUDITOR GATE — 3A Skeleton", "", ""],
    ["3B. Argument outline — premise-by-premise; 3-5 sub-arguments per subsection; intended example/evidence per bullet; objections placed; sources attached; cross-refs flagged", "", ""],
    ["3B — lenses A/E/S/I applied (each logged)", "", ""],
    ["AUDITOR GATE — 3B Argument outline", "", ""],
    ["3C. Paragraph outline (the FAT outline / drafting contract) v0.1 — one bullet per planned paragraph (~30-40% of final length); (verify) tags on empirical claims; named-argument labels; stable section numbers", "", ""],
    ["3C v0.2 — round 1 (completeness/rigor): every central argument + major objection mapped to specific bullets; Argument & Objection Coverage Map built; gaps closed", "", ""],
    ["AUDITOR GATE — 3C round 1 (auditor confirms a GENUINE coverage expansion vs v0.1; every argument & objection mapped)", "", ""],
    ["3C v0.3 — round 2 (literature engagement): every key interlocutor from the Lit Map engaged as bullets; positioning vs the niche solid; authors'-prior-work conflicts handled", "", ""],
    ["AUDITOR GATE — 3C round 2 (auditor confirms a GENUINE engagement expansion vs v0.2)", "", ""],
    ["3C — lenses A/E/S/I applied; outline is dense enough to draft from (FAT, not padded)", "", ""],
    ["3C — outline iteration with the author: bracketed [initials: ...] comments applied VERBATIM; iterate to convergence (comments getting shorter/more local)", "", ""],
    ["3C — REFEREE REVIEW MEMO on the paragraph outline (ranked vulnerabilities; missing-objection hunt; factual landmines; weakest lines) — referee proposes, author disposes; accepted items folded in", "", ""],
    ["AUDITOR GATE — 3C FINAL (auditor confirms outline complete, coverage mapped, dense; the referee memo was produced and its accepted dispositions applied)", "", ""],
    ["HUMAN SIGN-OFF — Paragraph Outline = the DRAFTING CONTRACT [GATE 2] ('hold drafting until sign-off'; skipped on 'run straight through')", "", ""],

    ["4. Draft v1.0 — every outline bullet converted to its paragraph in ONE full-density pass, written to the Part word budgets so the draft lands at target length (not outline length); structure preserved exactly; citations as placeholders; NO quality work in this pass", "", ""],
    ["4. Draft v1.0 — lens I (every bullet covered; nothing skipped; cross-refs noted)", "", ""],
    ["AUDITOR GATE — Draft v1.0 (auditor confirms full bullet-to-paragraph coverage; no section skipped)", "", ""],

    ["5. Quality passes (2-3) against the Writing Guide — cut editorializing; remove what is bad and ADD what is good (explanation, examples, new arguments — surfaced in the changelog); break cross-paragraph repetition; check dialectical balance; resolve cross-refs; terminology consistency. Length may move either way, but never grows through editorializing, repetition, or decoration. Each pass = a new version; stop when changes are minor", "", ""],
    ["5. Quality — lenses A/E/S/I applied (each logged)", "", ""],
    ["SELF-CHECK — Quality (deterministic: broad diff across the whole draft; every change removes bad or adds good; changelog line per version)", "", ""],

    ["6. Style & Voice pass — ROUNDS until converged (two minimum): each round = FRESH read of the author's example papers first, then EVERY sentence and EVERY paragraph walked ('would this author write this sentence?' / 'is this how their paragraphs move?'), replacing whatever reads as AI-written or off-voice; per-paragraph pass ledger (PASS/TOUCHED/FIXED) kept so coverage is checkable; no-regression sweep vs the author's overruled set every round", "", ""],
    ["SELF-CHECK — Style & Voice (builder diff matches the ledger's touched rows one-for-one; a final round finds only minor touches — convergence, never a fixed count)", "", ""],
    ["HUMAN SIGN-OFF — the voiced draft [GATE 3] (author reads the quality-passed, style-and-voice-passed draft: voice, framing, substance — the author never reads unvoiced prose)", "", ""],

    ["7. Author round applied — extract-first protocol (pristine-base isolation); every instruction applied or dispositioned; Change Log; verify_author_round run; substantial new prose from the author's edits gets a voice walk before the next stage", "", ""],
    ["AUDITOR GATE — Author round (MANDATORY: Change Log matches the actual diff; every author edit present or superseded-with-trace; no overruled formulation resurrected)", "", ""],

    ["8. Referee panel round 1 — 3 personas (lenses matched to the paper's mix + the venue's tradition) each file a severity-ranked report; consensus (flagged by >=2) implemented in one pass; single-referee concerns held in reserve", "", ""],
    ["AUDITOR GATE — Referee round 1 (auditor confirms 3 real reports exist AND the consensus fixes were actually applied)", "", ""],
    ["8. Referee panel round 2 — FRESH personas read the revised paper clean; implement new consensus; run round 3 only if substantially new items (4+ rounds => rethink the thesis, flag to author). Stop at the fixed point (only polish items remain)", "", ""],
    ["AUDITOR GATE — Referee (fixed point reached; all rounds' reports & applied fixes are real)", "", ""],

    ["9. Author substantive rewrite (author-led) — intro/thesis/load-bearing parts. The author's edits set each section's DIRECTION: improve further if you can, but never revert to a formulation the author overruled (check the Change Logs)", "", ""],
    ["9. Targeted change requests applied VERBATIM; Change Log produced (section / before / after / why); diffed against the prior version to confirm NO prior author edits were reverted", "", ""],
    ["AUDITOR GATE — Author changes (post-referee rewrite round) (auditor confirms the Change Log matches the actual diff AND prior author edits are preserved)", "", ""],

    ["10. Integration pass — full front-to-back read: stale cross-refs, notation/terminology drift, dangling references to cut sections, prose polish", "", ""],
    ["10. Abstract written LAST (2-3 candidates -> critique -> synthesis); matches the paper's ACTUAL framing", "", ""],
    ["10. Anti-LLM prose pass — copy-critic flags AI tics (hedging-redundancy, three-part lists, adverbial throat-clearing, metaphor-chaining, paragraph-restating summaries); revised", "", ""],
    ["10. Citation audit — citation-auditor verifies author/year/title and EVERY page pinpoint against the real source (WebSearch where needed); NO fabricated citations. (>=1 audit before referees; 1 before submission)", "", ""],
    ["10. Citation apparatus built to TYPE (Bluebook footnotes for law review; author-date + reference list for philosophy/Element); placeholders resolved", "", ""],
    ["10. Length pass (LIGHT, here only) — scope up a thin paper / trim a bloated one toward the target; argument quality already settled", "", ""],
    ["10. Pre-send critic pass — copy-critic must-fix vs can-wait checklist; author approves the must-fix list; fixes applied", "", ""],
    ["AUDITOR GATE — Final (auditor confirms every finishing step is genuinely done and the package is complete) + 'knowing when to stop' checklist met", "", ""],

    ["11. (Optional) Revise & Resubmit — journal referee reports reproduced verbatim; Response-to-Referees letter (responses in blue inline); MODULAR changes (small new subsections/paragraphs, not big restructures); referee-suggested cites WebSearch-verified; example letter used to calibrate", "", ""],

    ["12. Retrospective written — what worked, what slowed us down, recurring auditor REVISE reasons, and concrete suggested changes to the playbook docs and the agents", "", ""],
]

# Outcome vocabulary for the middle column (use these, not a bare "Yes").
# Work rows: Done | No-change (checked) | Deferred (why+owner) | —.
# Auditor-gate rows: APPROVE | REVISE.   Human-gate rows: SIGN-OFF | CHANGES-REQUESTED.
OUTCOMES = ("Done | No-change (checked) | Deferred (why+owner) | APPROVE / REVISE (auditor gates) | "
            "SIGN-OFF / CHANGES-REQUESTED (human gates) | —")


def checklist_blocks(paper, paper_type, target_length, intro_note=None):
    preset = TYPE_PRESETS.get(paper_type)
    type_line = f"Paper type: {paper_type}"
    if preset:
        type_line += f"  •  default length {preset[0]}  •  {preset[1]}"
    if target_length:
        type_line += f"   (target for THIS paper: {target_length})"
    note = intro_note or (
        "Created FIRST, at project setup, and worked top-to-bottom. The mechanisms that keep this honest: "
        "(1) An INDEPENDENT AUDITOR gates the RESERVED stages — the early stages, the first full draft, every "
        "author round, and the Final check. Its SOLE job is to verify — against the actual files, not the "
        "drafting agent's claims — that the work a row claims as done was genuinely done; it keeps the other "
        "agents from recording steps as done without doing them. It does NOT judge quality. You may NOT advance "
        "past a reserved gate until the auditor returns APPROVE; paste its verdict in the gate row. On the "
        "agent's own incremental revisions (quality passes; Style & Voice rounds) a deterministic SELF-CHECK on "
        "the Change Log — isolation diff + verify scripts — stands in for it. "
        "(2) Quality is enforced by SEPARATE specialist agents — the multi-persona REFEREE panel (simulated peer "
        "review; consensus of >=2 referees implemented, iterate to a fixed point), the CITATION-AUDITOR (no "
        "fabricated citations; every pinpoint verified against the real source), and the COPY-CRITIC (mistakes, "
        "consistency, anti-LLM tics). "
        "(3) NEVER pre-fill the checklist. A row stays blank until its step is genuinely done; then its Evidence "
        "cell is written FROM the finished artifact (a version+section, a named artifact, a measured count, a "
        "quoted line) — never an adjective, never restating the step, never ahead of the work. "
        "(4) The OUTLINE is layered and gated (3A Skeleton -> 3B Argument -> 3C Paragraph 'fat outline'); the "
        "paragraph outline is the DRAFTING CONTRACT — no prose until it is signed off. Build a FAT outline "
        "(~30-40% of final length) so structure is settled before prose, where it costs ~10x more to change. "
        "(5) DRAFTING is mechanical (bullets->paragraphs, no quality work) THEN separate quality passes that "
        "improve in BOTH directions — remove what is bad, add what is good (explanation, examples, new arguments, "
        "surfaced in the changelog); length is an outcome, never a per-pass constraint. Argument quality comes "
        "first; the target length is one LIGHT pass near the end. "
        "(6) The AUTHOR's edits set DIRECTION — later versions may improve author-touched text further, but may "
        "NEVER revert, in substance or wording, to a formulation the author overruled; surface improvements to "
        "author-touched text in the changelog; diff before saving; a returned '- author edits' file is "
        "intentional. "
        "Lens keys — A=Argument, E=Engagement(literature), S=Style(Writing Guide), I=Integrity(citations/cross-refs/"
        "claims-match-body). Human sign-offs: the Argument Sketch at Setup, then Plan [GATE 1], Paragraph "
        "Outline [GATE 2], and the author's read of the VOICED draft [GATE 3] — after the Quality and Style & "
        "Voice passes; the author never reads unvoiced prose — plus the author-owned Finish gate; all unless the author "
        "says 'run straight through'. Outcome vocabulary: " + OUTCOMES + ".")
    return [
        ("title", f"{paper} — Project Checklist"),
        ("subtitle", "Accountability record per the Pipeline — Deep Drafter"),
        ("note", type_line),
        ("note", note),
        ("table", CHECKLIST_ROWS, [4.7, 1.2, 3.1]),
    ]


def progresslog_blocks(paper, paper_type, target_length):
    preset = TYPE_PRESETS.get(paper_type)
    tl = target_length or (preset[0] if preset else "[set target length]")
    return [
        ("title", f"{paper} — Project Progress Log"),
        ("subtitle", "Single running record — Deep Drafter"),
        ("note", "One running record for the whole paper (newest entry at the bottom). Each entry notes what was "
                 "produced, what changed, decisions, open questions, the auditor's verdicts, and what is needed "
                 "from the author."),
        ("h1", "[date] — Project setup"),
        ("bullet", f"Paper type: **{paper_type}**.  Target length: **{tl}**."),
        ("bullet", "Created the standard folder structure and this Progress Log; created the Project Checklist first."),
        ("bullet", "Next: capture the Setup Contract; load the 1-page Brief, Background Readings, and Model Prose; "
                   "read the Writing Guide + Style Module + Context; then build the Literature Map."),
    ]


def _ensure_writable(path):
    """If a directory exists but isn't user-writable, add owner write (user-created folders are sometimes read-only)."""
    import stat
    if os.path.isdir(path) and not os.access(path, os.W_OK):
        try:
            os.chmod(path, os.stat(path).st_mode | stat.S_IWUSR)
        except OSError:
            pass


def _safe_name(name):
    """Filesystem-safe folder/file name — academic titles often contain ':' (subtitles) and '/'."""
    safe = re.sub(r'[\\/:*?"<>|]+', ' - ', name)
    safe = re.sub(r'\s+', ' ', safe).strip(' .')
    return safe or "Untitled Paper"


def scaffold(paper, paper_type="philosophy", target_length=None, root=DEFAULT_ROOT, adopt=False):
    """Create the standard paper project. By default STOPS if the folder exists. With adopt=True it
    ADOPTS a pre-seeded folder: adds only the missing standard structure and creates the Checklist/
    Progress Log only if absent — never overwriting files."""
    safe = _safe_name(paper)
    proj = os.path.join(root, safe)
    exists = os.path.exists(proj)
    if exists and not adopt:
        print(f"STOP: {proj} already exists — not overwriting. Re-run with --adopt to add the missing standard "
              "structure to an existing (pre-seeded) project without touching existing files.")
        return proj
    _ensure_writable(proj)
    for d in FOLDER_DIRS:
        os.makedirs(os.path.join(proj, d), exist_ok=True)
    if exists:
        for name in os.listdir(proj):
            _ensure_writable(os.path.join(proj, name))
    hdr = ["Deep Drafter", f"Working document — {paper}"]
    cl = os.path.join(proj, "Progress reports", f"{safe} - Project Checklist.docx")
    pl = os.path.join(proj, "Progress reports", f"{safe} - Project Progress Log.docx")
    if not (adopt and os.path.exists(cl)):
        build(cl, checklist_blocks(paper, paper_type, target_length), accent=NEUTRAL_ACCENT, header_lines=hdr,
              footer_text=f"Deep Drafter   |   {paper} — Project Checklist")
    if not (adopt and os.path.exists(pl)):
        build(pl, progresslog_blocks(paper, paper_type, target_length), accent=NEUTRAL_ACCENT, header_lines=hdr,
              footer_text=f"Deep Drafter   |   {paper} — Project Progress Log")
    print(f"[{'adopted' if exists else 'scaffolded'}] {proj}")
    print("  - standard folder tree ensured (Brief, Background Readings, Model Prose, WIP Docs/<type>, "
          "Progress reports, Scrap, Submission, Behind the scenes); existing files untouched")
    print(f"  - {safe} - Project Checklist.docx  (created FIRST — drive the work from it)")
    print(f"  - {safe} - Project Progress Log.docx")
    if paper_type not in TYPE_PRESETS:
        print(f"  NOTE: '{paper_type}' has no preset Style Module yet — add one in "
              "General Guide to Academic Writing/Style Modules/ (copy _Template), or use a known type: "
              + ", ".join(TYPE_PRESETS))
    print("  NEXT: put the 1-page Brief in Brief/, the interlocutor PDFs in Background Readings/, and a prior "
          "paper in Model Prose/; then work the checklist top-to-bottom.")
    return proj


if __name__ == "__main__":
    argv = [a for a in sys.argv[1:] if a != "--adopt"]
    adopt = "--adopt" in sys.argv[1:]
    if len(argv) < 1:
        print(__doc__)
        sys.exit(1)
    title = argv[0]
    ptype = argv[1] if len(argv) > 1 else "philosophy"
    tlen  = argv[2] if len(argv) > 2 else None
    root  = argv[3] if len(argv) > 3 else DEFAULT_ROOT
    scaffold(title, ptype, tlen, root, adopt=adopt)
