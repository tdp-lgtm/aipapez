#!/usr/bin/env python3
"""Author-round FORMATTING diff: report blue->black acceptances in a tracked-changes docx.
CRITICAL: Word stores the PRE-CHANGE run properties inside <w:rPrChange>; the current color
must be read from the run's rPr AFTER stripping rPrChange, or accepted (blackened) text will
be misread as still blue. This exact bug once silently dropped a full round of acceptances.
Usage: python3 color_census.py "<file.docx>"  -> per-paragraph accepted-to-black + still-blue report."""
import re, sys, zipfile, html

def runs(path):
    xml = zipfile.ZipFile(path).read("word/document.xml").decode("utf-8")
    for i, pm in enumerate(re.finditer(r"<w:p[ >].*?</w:p>", xml, re.S)):
        live = re.sub(r"<w:del [^>]*>.*?</w:del>", "", pm.group(0), flags=re.S)
        for rm in re.finditer(r"<w:r[ >].*?</w:r>", live, re.S):
            r = rm.group(0)
            t = html.unescape("".join(re.findall(r"<w:t[^>]*>([^<]*)</w:t>", r)))
            if not t:
                continue
            cur = re.sub(r"<w:rPrChange.*?</w:rPrChange>", "", r, flags=re.S)  # strip history FIRST
            cur_blue = bool(re.search(r'<w:color w:val="0000CC"', cur))
            old_blue = bool(re.search(r'<w:rPrChange.*?<w:color w:val="0000CC"', r, re.S))
            yield i, t, cur_blue, (old_blue and not cur_blue)

if __name__ == "__main__":
    acc, blue = {}, {}
    for i, t, cur_blue, accepted in runs(sys.argv[1]):
        if accepted: acc.setdefault(i, []).append(t)
        if cur_blue: blue.setdefault(i, []).append(t)
    print(f"ACCEPTED to black: {len(acc)} paragraphs")
    for i, ts in sorted(acc.items()): print(f"  P{i}: {''.join(ts)[:110]!r}")
    print(f"STILL BLUE: {len(blue)} paragraphs")
    for i, ts in sorted(blue.items()): print(f"  P{i}: {''.join(ts)[:110]!r}")
