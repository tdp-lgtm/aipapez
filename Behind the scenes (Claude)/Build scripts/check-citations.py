#!/usr/bin/env python3
"""Citation integrity helper for competition essays — handles citekey drafts
AND our real case: Markdown drafts with author-date narrative citations.

It always extracts BOTH kinds of evidence from the draft (a stray @token can
no longer hide the narrative citations, and vice versa):

1. CITEKEYS (@key / \\cite{}): verified against a .bib. Unresolved keys are a
   hard failure (exit 1) — the classic fabrication signature.

2. NARRATIVE CANDIDATES: author-year mentions (parenthesized or not), whole
   citation-ish footnotes (multi-line footnotes are read in full), and
   [CITE?] / [CITE] markers. A script cannot confirm these; each item must be
   verified against the real sources (the citation-auditor does this against
   Background Readings/ and the web).
   Their presence exits 3 so that "nothing automated could be confirmed" is
   NEVER mistaken for a pass.

Usage:
    python3 "Behind the scenes (Claude)/Build scripts/check-citations.py" DRAFT [BIB ...]
    (DRAFT: the essay's Markdown draft. Our essays use author-date in-text
    citations, so expect exit 3 + the numbered checklist: that list is the
    citation-auditor's work order, never a pass.)

Exit codes:
    0   citekeys only, and all keys resolve (clean pass)
    1   unresolved citekeys (likely fabricated/mistyped) — fix before anything
    2   nothing detected at all (NOT a pass — verify manually)
    3   verification required: narrative candidates and/or [CITE?] markers
        and/or citekeys with no .bib to resolve them against
    64  usage error
    65  input isn't readable text (e.g. you passed the .docx itself)

This checks existence only. Page numbers, quotations, and attributions always
need the source itself and judgement.
"""
import glob
import os
import re
import sys

LATEX_CITE = re.compile(r"\\[a-zA-Z]*cite[a-zA-Z]*\*?(?:\[[^\]]*\])*\{([^}]*)\}")
PANDOC_CITE = re.compile(r"(?<![\w@])@([A-Za-z0-9][\w:.\-]*)")
BIB_ENTRY = re.compile(r"@\w+\s*\{\s*([^,\s]+)\s*,")

# Narrative patterns.
NAME = r"[A-Z][A-Za-z'’\-]+"
YEAR = r"(?:1[89]|20)\d{2}[a-z]?"
# "Quong (2009)", "Frowe and Parry (2019):"
NARRATIVE = re.compile(rf"({NAME}(?:,? (?:and|&) {NAME})*)\s*\(\s*({YEAR})\s*[):,]")
# "(Frowe 2021: 44)", "(Tadros 2016)"
PAREN_CITE = re.compile(rf"\(\s*({NAME}(?:,? (?:and|&) {NAME})*)\s+({YEAR})")
# Bare author-year with NO parentheses: "See Tadros 2016, p. 34", "Hurd 1996".
# Cheap false positives are fine here (this is a verification checklist, not a
# validator); false negatives are what we can't afford.
BARE_CITE = re.compile(rf"\b({NAME}(?:,? (?:and|&) {NAME})*)\s+({YEAR})\b")
# Capitalized sentence-starters etc. that BARE_CITE would misread as surnames.
NOT_A_NAME = {
    "A", "After", "Around", "At", "Before", "Between", "By", "Circa", "During",
    "Early", "From", "In", "Late", "Mid", "Of", "On", "Since", "Spring",
    "Summer", "The", "Until", "Autumn", "Fall", "Winter", "When", "While",
    "Version", "Draft", "Section", "Chapter", "Part", "Footnote", "Note",
    "Punishment", "New",
}
# bare "(2017: 5)" style — author must be attributed from surrounding context
YEAR_PAGE = re.compile(rf"\(\s*({YEAR})\s*:\s*\d+")
# [CITE?] / [CITE] markers, with or without Markdown escaping (\[CITE?\])
CITE_MARKER = re.compile(r"\\?\[\s*CITE[^\]\\]*\\?\]", re.I)
FOOTNOTE_START = re.compile(r"^\[\^[^\]]+\]:")
HEADING = re.compile(r"^#{1,6}\s")
# citation-ish footnotes: a year, a cite-verb, or a "the <Name> paper" pointer —
# note-drafts hide fabrication risk in exactly these ("Cite Hurd", "Follow Vicky")
CITEISH = re.compile(
    rf"\b{YEAR}\b"
    r"|(?:^|[.;!?]\s+)(Cf\.|cf\.|See|see|Cite|cite|Follow|Compare)\b"
    r"|\bthe\s+[A-Z][A-Za-z'’\-]+\s+(paper|article|book|chapter)\b"
)


def keys_in_draft(text):
    found = set()
    for m in LATEX_CITE.finditer(text):
        found.update(k.strip() for k in m.group(1).split(",") if k.strip())
    for m in PANDOC_CITE.finditer(text):
        found.add(m.group(1).rstrip(".,;:"))
    return found


def keys_in_bib(paths):
    keys = set()
    for p in paths:
        try:
            with open(p, encoding="utf-8", errors="ignore") as fh:
                keys.update(m.group(1) for m in BIB_ENTRY.finditer(fh.read()))
        except OSError:
            continue
    return keys


def footnote_blocks(text):
    """Yield each footnote's FULL text, following continuation lines.

    A footnote runs from its `[^id]:` line until the next footnote def, a
    heading, or a blank line NOT followed by an indented continuation
    (pandoc's multi-paragraph-note convention). Hard-wrapped footnotes —
    which hid citations from the old first-line-only regex — are captured
    whole.
    """
    lines = text.splitlines()
    i, n = 0, len(lines)
    while i < n:
        if not FOOTNOTE_START.match(lines[i]):
            i += 1
            continue
        block = [lines[i]]
        i += 1
        while i < n:
            line = lines[i]
            if FOOTNOTE_START.match(line) or HEADING.match(line):
                break
            if line.strip() == "":
                # blank line ends the note unless the next line is indented
                if i + 1 < n and lines[i + 1].startswith(("    ", "\t")):
                    block.append(line)
                    i += 1
                    continue
                break
            block.append(line)
            i += 1
        yield " ".join(l.strip() for l in block if l.strip())


def narrative_candidates(text):
    """Collect (who, year) pairs, citation-ish footnotes, and [CITE?] markers."""
    pairs = set()
    for rx in (NARRATIVE, PAREN_CITE):
        for m in rx.finditer(text):
            pairs.add((m.group(1), m.group(2)))
    for m in BARE_CITE.finditer(text):
        first = m.group(1).split()[0]
        if first not in NOT_A_NAME:
            pairs.add((m.group(1), m.group(2)))
    for m in YEAR_PAGE.finditer(text):
        pairs.add(("[attribute from context]", m.group(1)))
    notes = []
    for note in footnote_blocks(text):
        body = note.split(":", 1)[1].strip() if ":" in note else note
        if CITEISH.search(body) or CITE_MARKER.search(body):
            notes.append(body[:160])
    markers = []
    for lineno, line in enumerate(text.splitlines(), 1):
        if CITE_MARKER.search(line):
            markers.append((lineno, line.strip()[:120]))
    return sorted(pairs), notes, markers


def looks_binary(path, text):
    if path.lower().endswith((".docx", ".doc", ".pdf", ".odt", ".zip")):
        return True
    return "\x00" in text[:4096]


def main():
    if len(sys.argv) < 2:
        print(__doc__, file=sys.stderr)
        sys.exit(64)
    draft = sys.argv[1]
    bibs = sys.argv[2:]
    if not bibs:
        d = os.path.dirname(os.path.abspath(draft))
        bibs = sorted(set(glob.glob(os.path.join(d, "*.bib")) + glob.glob("*.bib")))
    try:
        text = open(draft, encoding="utf-8", errors="ignore").read()
    except OSError as exc:
        print(f"cannot read draft: {exc}", file=sys.stderr)
        sys.exit(65)
    if looks_binary(draft, text):
        print(f"ERROR: {draft} is not Markdown/plain text.", file=sys.stderr)
        print('Convert it first:  bash scripts/docx-bridge.sh to-md "%s"' % draft,
              file=sys.stderr)
        sys.exit(65)

    used = keys_in_draft(text)
    pairs, notes, markers = narrative_candidates(text)

    print(f"draft: {draft}")
    verification_needed = False
    key_failure = False

    if used:
        defined = keys_in_bib(bibs)
        unresolved = sorted(k for k in used if k not in defined)
        print(f"citekeys: {len(used)} used  |  bib: "
              f"{', '.join(bibs) if bibs else '(none found)'}")
        if not bibs:
            print("  No .bib found — every citekey is unverified (check against real sources).")
            verification_needed = True
        elif unresolved:
            print(f"\n  UNRESOLVED ({len(unresolved)}) — verify before submitting:")
            for k in unresolved:
                print(f"    - {k}")
            key_failure = True
        else:
            print("  All citation keys resolve. (Pages/quotes still need the sources.)")

    if pairs:
        print(f"\nauthor-year candidates ({len(pairs)}) — VERIFY EACH AGAINST A REAL SOURCE:")
        for i, (who, yr) in enumerate(pairs, 1):
            print(f"  {i:2d}. {who} ({yr})")
        verification_needed = True
    if notes:
        print(f"\ncitation-like footnotes ({len(notes)}) to check:")
        for i, note in enumerate(notes, 1):
            print(f"  n{i:2d}. {note}")
        verification_needed = True
    if markers:
        print(f"\n[CITE?] markers ({len(markers)}) — each needs a real source:")
        for lineno, line in markers:
            print(f"  line {lineno}: {line}")
        verification_needed = True

    if key_failure:
        print("\nFAIL: unresolved citekeys — likely fabricated or mistyped.")
        sys.exit(1)
    if verification_needed:
        print("\nNOT A PASS: exit 3 = source-by-source verification required (citation-auditor).")
        sys.exit(3)
    if used:
        sys.exit(0)

    print("nothing detected — no citekeys, no narrative citations, no [CITE?] markers.")
    print("Either the draft is citation-free or the format wasn't recognised; "
          "verify manually.")
    sys.exit(2)


if __name__ == "__main__":
    main()
