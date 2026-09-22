#!/usr/bin/env python3
"""Prose linter for competition essays: countable register checks with budgets.
Approximate by design — it flags for a human/agent pass to judge, it does not
auto-fix. Budgets implement the Style Guide's apparatus and snap budgets and
ai-tells.md's cadence checks. Usage:

    python3 "Behind the scenes (Claude)/Build scripts/prose_lint.py" "<essay.md>"

Exit codes: 0 = all within budget, 2 = one or more FLAGs (paste the report into
the pass's self-check either way).
"""
import re
import sys
from pathlib import Path

BIB_HEADING = re.compile(r"^#{1,3}\s*(bibliography|references)\b", re.I)

BANNED_PHRASES = [
    "it is important to note", "it is worth noting", "it should be emphasized",
    "delve", "rich tapestry", "nuanced interplay", "complex landscape",
    "plays a crucial", "plays a pivotal", "plays a vital", "navigate the complexities",
    "in today's", "multifaceted", "myriad", "plethora", "testament to",
    "in conclusion", "broadly speaking", "as we shall see", "in the first instance",
    "the upshot is", "at bottom", "at a more fundamental level", "stands as",
    "serves as a", "boasts", "underscores", "ultimately,",
]

def body_text(md: str) -> str:
    lines = md.splitlines()
    out = []
    for ln in lines:
        if BIB_HEADING.match(ln.strip()):
            break
        if ln.startswith("Changelog:") or ln.startswith("#"):
            continue
        out.append(ln)
    return "\n".join(out)

def sentences(text: str):
    plain = re.sub(r"\[\^?\d+\]|\(verify[^)]*\)", "", text)
    plain = re.sub(r"\*\*?|__|>", "", plain)
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z\"'“*])", plain)
    return [s.strip() for s in parts if len(s.strip()) > 1]

def paragraphs(text: str):
    return [p.strip() for p in re.split(r"\n\s*\n", text) if len(p.split()) > 5]

def main() -> None:
    if len(sys.argv) < 2:
        sys.exit('Usage: prose_lint.py "<essay.md>"')
    md = Path(sys.argv[1]).read_text(encoding="utf-8")
    text = body_text(md)
    words = len(text.split())
    per300 = max(words / 300.0, 1.0)
    sents = sentences(text)
    paras = paragraphs(text)
    lens = [len(s.split()) for s in sents]

    rows = []  # (metric, value, budget-desc, ok)

    def row(name, value, budget, ok):
        rows.append((name, value, budget, ok))

    # --- tells & phrases
    low = text.lower()
    hits = {p: low.count(p) for p in BANNED_PHRASES if low.count(p)}
    row("banned phrases (ai-tells)", sum(hits.values()) or 0, "0", not hits)

    em = text.count("—") + text.count(" -- ")
    row("em dashes", f"{em} ({em/per300:.1f}/300w)", "<= 0.7 per 300w", em / per300 <= 0.7)

    notonly = len(re.findall(r"\bnot only\b", low))
    row('"not only … but also"', notonly, "<= 1", notonly <= 1)

    antith = len(re.findall(r"\bnot\b[^.;:\n]{2,45}\bbut\b", low))
    row('"not X but Y" frames', f"{antith} ({antith/per300:.1f}/300w)", "<= 0.5 per 300w", antith / per300 <= 0.5)

    triads = len(re.findall(r", [^,\n]{2,40}, and ", text))
    row("list triads", f"{triads} ({triads/per300:.1f}/300w)", "<= 0.8 per 300w", triads / per300 <= 0.8)

    # --- cadence
    frags = [s for s in sents if len(s.split()) <= 4]
    row("fragments (<=4 words)", len(frags), "<= 3 per essay", len(frags) <= 3)

    runs, run = [], 0
    for L in lens:
        if 17 <= L <= 23:
            run += 1
        else:
            if run:
                runs.append(run)
            run = 0
    if run:
        runs.append(run)
    maxrun = max(runs, default=0)
    row("uniform-length run (17-23w)", maxrun, "<= 3 consecutive", maxrun <= 3)

    openers = sum(1 for s in sents if re.match(r"(The|This|It|In)\b", s))
    share = openers / max(len(sents), 1)
    row("The/This/It/In openers", f"{share:.0%}", "<= 45%", share <= 0.45)

    punchy = 0
    for p in paras:
        last = sentences(p)[-1:] or [""]
        if len(last[0].split()) <= 8:
            punchy += 1
    pshare = punchy / max(len(paras), 1)
    row("paragraphs ending punchy (<=8w)", f"{punchy}/{len(paras)} ({pshare:.0%})", "<= 25%", pshare <= 0.25)

    # --- apparatus budget
    named = set(re.findall(
        r"\bthe ([A-Z][a-z]+(?: [A-Z][a-z]+)?) (?:View|Condition|Principle|Account|Thesis|Problem|Model|Challenge|Test|Argument)\b",
        text))
    row("named views/principles", f"{len(named)}: {sorted(named)}", "<= 3 distinct", len(named) <= 3)

    cases = set(re.findall(r"(?<!\w)\*([A-Z][A-Za-z]+(?: [A-Z][a-z]+){0,3})\*(?!\w)", text))
    row("italic case names", f"{len(cases)}: {sorted(cases)}", "<= 3 distinct", len(cases) <= 3)

    coin = len(re.findall(r"\bCall (?:this|it)\b|\bIn a slogan\b|\bSay that\b", text))
    row("coinage/slogan moves", coin, "<= 2", coin <= 2)

    displays = len(re.findall(r"^> \*\*", text, re.M))
    row("displays (blockquotes)", displays, "<= 2", displays <= 2)

    # --- report
    print(f"prose_lint: {Path(sys.argv[1]).name} — {words} countable words, "
          f"{len(sents)} sentences, {len(paras)} paragraphs\n")
    width = max(len(r[0]) for r in rows)
    flags = 0
    for name, value, budget, ok in rows:
        mark = "OK  " if ok else "FLAG"
        if not ok:
            flags += 1
        print(f"  {mark}  {name.ljust(width)}  {value}   [budget: {budget}]")
    if hits:
        print("\n  banned-phrase hits:")
        for p, n in sorted(hits.items(), key=lambda x: -x[1]):
            print(f"    {n}x  \"{p}\"")
    print(f"\n{flags} FLAG(s). Budgets are working defaults from the Style Guide; a FLAG is a "
          f"prompt to look, not an automatic defect — but every FLAG needs a disposition in the "
          f"pass's self-check.")
    sys.exit(0 if flags == 0 else 2)

if __name__ == "__main__":
    main()
