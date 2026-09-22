#!/usr/bin/env python3
"""Scaffold a new competition essay: Essays/<slug>/ with the standard tree,
the Checklist (from Playbook/4. Essay Project Template.md), the Progress Log,
and the Process Log. Usage:

    python3 "Behind the scenes (Claude)/Build scripts/new_essay.py" "<Essay slug or working title>"
"""
import datetime
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

SUBDIRS = [
    "Brief",
    "Background Readings/Converted text",
    "WIP Docs/Candidates/Old versions",
    "WIP Docs/Literature Map/Old versions",
    "WIP Docs/Plan/Old versions",
    "WIP Docs/Outline/Old versions",
    "WIP Docs/Drafts/Old versions",
    "WIP Docs/Abstract/Old versions",
    "WIP Docs/Referee Reports",
    "WIP Docs/Change Logs",
    "Methodology",
    "Progress reports",
    "Scrap/Review artifacts",
    "Submission",
]


def extract_checklist(template_text: str, slug: str) -> str:
    """Pull the checklist code block out of the project template."""
    m = re.search(r"```markdown\n(# Checklist.*?)```", template_text, re.S)
    if not m:
        sys.exit("Could not find the checklist block in the project template.")
    return m.group(1).replace("<essay slug>", slug)


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit('Usage: new_essay.py "<Essay slug or working title>"')
    slug = sys.argv[1].strip()
    essay_dir = ROOT / "Essays" / slug
    if essay_dir.exists():
        sys.exit(f"Refusing to scaffold: {essay_dir} already exists.")

    template = (ROOT / "Playbook" / "4. Essay Project Template.md").read_text(encoding="utf-8")
    today = datetime.date.today().isoformat()

    for sub in SUBDIRS:
        (essay_dir / sub).mkdir(parents=True, exist_ok=True)

    reports = essay_dir / "Progress reports"
    (reports / "Checklist.md").write_text(extract_checklist(template, slug), encoding="utf-8")
    (reports / "Progress Log.md").write_text(
        f"# Progress Log — {slug}\n\n"
        "Append at each gate and after each substantive change: what was produced, what changed,\n"
        "decisions, open questions, auditor verdicts, and what is needed from the custodian.\n\n"
        f"## [{today}] Setup\n- Scaffolded by new_essay.py.\n",
        encoding="utf-8",
    )
    (essay_dir / "Methodology" / "Process Log.md").write_text(
        f"# Process Log — {slug}\n\n"
        "Append-only session log; see Playbook/3. Methodology Protocol.md for the entry template.\n"
        "Verbatim human messages; AI actions; models; candidate counts; selections; compliance\n"
        "flags; approximate cost. This log is the compliance evidence and the raw material for the\n"
        "methodology report.\n\n"
        f"## [{today}] Session 1 — Stage 0 Setup\n"
        "- **Models/agents:** \n- **Human messages (verbatim):**\n  > \n"
        "- **AI actions:** scaffolded the essay folder.\n- **Selections:** \n"
        "- **Tools/retrieval:** \n- **Compliance flags:** none\n- **Approx. cost/time:** \n",
        encoding="utf-8",
    )
    print(f"Scaffolded {essay_dir}")
    print("Created: Checklist.md, Progress Log.md, Methodology/Process Log.md")
    print("Next: record the intake in Brief/ and the Process Log, then Stage 1 (idea generation).")


if __name__ == "__main__":
    main()
