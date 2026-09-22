#!/usr/bin/env python3
"""Competition word count for a Markdown essay: counts everything except the
bibliography (a final section headed 'Bibliography' or 'References') and
Markdown mechanics. The competition limit is 6,000 words. Usage:

    python3 "Behind the scenes (Claude)/Build scripts/word_count.py" "<essay.md>"
"""
import re
import sys
from pathlib import Path

BIB_HEADING = re.compile(r"^#{1,3}\s*(bibliography|references)\b", re.I)
LIMIT = 6000


def countable_text(md: str) -> tuple[str, str]:
    """Split into (body, bibliography) at the bibliography heading, if any."""
    lines = md.splitlines()
    for i, line in enumerate(lines):
        if BIB_HEADING.match(line.strip()):
            return "\n".join(lines[:i]), "\n".join(lines[i:])
    return md, ""


def n_words(text: str) -> int:
    # Strip markdown mechanics that aren't words: headings markers, emphasis,
    # blockquote markers, list markers, links kept as their text.
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"[#>*_`|-]+", " ", text)
    return len(text.split())


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit('Usage: word_count.py "<essay.md>"')
    md = Path(sys.argv[1]).read_text(encoding="utf-8")
    body, bib = countable_text(md)
    n = n_words(body)
    print(f"Countable words (everything except bibliography): {n}")
    if bib:
        print(f"Bibliography (excluded): {n_words(bib)} words")
    else:
        print("No 'Bibliography'/'References' heading found — nothing excluded.")
    status = "WITHIN" if n <= LIMIT else "OVER"
    print(f"Limit {LIMIT}: {status} ({n - LIMIT:+d})")


if __name__ == "__main__":
    main()
