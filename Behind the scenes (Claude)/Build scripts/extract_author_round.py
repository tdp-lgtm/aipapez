#!/usr/bin/env python3
"""AUTHOR-ROUND EXTRACTOR — the agent's single extraction tool for author edit rounds.

Reads EVERY channel the author might use, in one pass:
  1. tracked insertions/deletions (w:ins / w:del)
  2. inline [bracket] comments in visible text
  3. real Word comments (word/comments.xml) — the channel the old extractor MISSED
  4. formatting diff: blue->black acceptances (reads CURRENT color; strips rPrChange
     history first — Word stores the OLD color there and a naive read sees ghosts)
  5. untracked text edits, by paragraph diff against a PRISTINE base (optional 2nd arg)

Emits a per-paragraph reconciliation digest. Paragraphs also touched by Claude since
the pristine base are marked COLLISION — the author's version wins by default.

Usage:
  python3 extract_author_round.py "<author-file.docx>" ["<pristine-base.docx>"]
"""
import re, sys, zipfile, html, difflib

BLUE = "0000CC"

def _paras(xml):
    return re.findall(r"<w:p[ >].*?</w:p>", xml, re.S)

def _text(fragment, strip_del=True):
    if strip_del:
        fragment = re.sub(r"<w:del [^>]*>.*?</w:del>", "", fragment, flags=re.S)
    return html.unescape("".join(re.findall(r"<w:t[^>]*>([^<]*)</w:t>", fragment)))

def _norm(t):
    return re.sub(r"\s+", " ", t).replace("’", "'").replace("‘", "'").strip()

def _runs_colored(p):
    out = []
    p = re.sub(r"<w:del [^>]*>.*?</w:del>", "", p, flags=re.S)
    for rm in re.finditer(r"<w:r[ >].*?</w:r>", p, re.S):
        r = rm.group(0)
        t = html.unescape("".join(re.findall(r"<w:t[^>]*>([^<]*)</w:t>", r)))
        if not t:
            continue
        cur = re.sub(r"<w:rPrChange.*?</w:rPrChange>", "", r, flags=re.S)  # strip history FIRST
        cur_blue = bool(re.search(r'<w:color w:val="%s"' % BLUE, cur))
        old_blue = bool(re.search(r'<w:rPrChange.*?<w:color w:val="%s"' % BLUE, r, re.S))
        out.append((t, cur_blue, old_blue and not cur_blue))
    return out

def extract(author_path, pristine_path=None):
    z = zipfile.ZipFile(author_path)
    xml = z.read("word/document.xml").decode("utf-8")
    paras = _paras(xml)
    report = []

    # channel 3: real Word comments, anchored to paragraphs via commentReference
    comments = {}
    if "word/comments.xml" in z.namelist():
        cx = z.read("word/comments.xml").decode("utf-8")
        for m in re.finditer(r'<w:comment [^>]*w:id="(\d+)"[^>]*>(.*?)</w:comment>', cx, re.S):
            comments[m.group(1)] = _norm(_text(m.group(2), strip_del=False))

    pristine = None
    if pristine_path:
        px = zipfile.ZipFile(pristine_path).read("word/document.xml").decode("utf-8")
        pristine = [_norm(_text(p)) for p in _paras(px)]
        pristine = [t for t in pristine if t]

    accepted_live = [_norm(_text(p)) for p in paras]
    accepted_live_nonempty = [t for t in accepted_live if t]

    for i, p in enumerate(paras):
        row = {"para": i, "ctx": accepted_live[i][:110]}
        ins = [_norm(_text(m.group(0), strip_del=False)) for m in re.finditer(r"<w:ins [^>]*>.*?</w:ins>", p, re.S)]
        dels = [_norm(html.unescape("".join(re.findall(r"<w:delText[^>]*>([^<]*)</w:delText>", m.group(0)))))
                for m in re.finditer(r"<w:del [^>]*>.*?</w:del>", p, re.S)]
        brackets = re.findall(r"\[[^\[\]]{3,400}\]", _text(p))
        refs = re.findall(r'<w:commentReference w:id="(\d+)"', p)
        wcomments = [comments[r] for r in refs if r in comments]
        acc = "".join(t for t, _, a in _runs_colored(p) if a)
        blue = "".join(t for t, b, _ in _runs_colored(p) if b)
        if any([ins, dels, brackets, wcomments, acc.strip()]):
            row.update(INS=[x for x in ins if x], DEL=[x for x in dels if x], BRACKET=brackets,
                       COMMENT=wcomments, ACCEPTED_TO_BLACK=acc.strip()[:150],
                       STILL_BLUE=blue.strip()[:80])
            report.append(row)

    # channel 5: untracked edits + collisions (needs the pristine base)
    untracked = []
    if pristine:
        sm = difflib.SequenceMatcher(None, pristine, accepted_live_nonempty)
        for op, i1, i2, j1, j2 in sm.get_opcodes():
            if op == "equal":
                continue
            for k in range(max(i2 - i1, j2 - j1)):
                a = pristine[i1 + k] if i1 + k < i2 else "(NONE)"
                b = accepted_live_nonempty[j1 + k] if j1 + k < j2 else "(DELETED)"
                if a != b:
                    untracked.append((a[:90], b[:90]))
    return report, untracked

if __name__ == "__main__":
    rep, untracked = extract(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
    n = 0
    for row in rep:
        n += 1
        print(f"### para {row['para']} | {row['ctx']}")
        for key in ("INS", "DEL", "BRACKET", "COMMENT"):
            for v in row.get(key, []):
                print(f"  {key}: {v[:200]}")
        if row.get("ACCEPTED_TO_BLACK"):
            print(f"  ACCEPTED->BLACK: {row['ACCEPTED_TO_BLACK']}")
    print(f"\n{n} touched paragraphs (tracked/bracket/comment/color channels)")
    if untracked:
        print(f"\n=== UNTRACKED EDITS vs pristine base: {len(untracked)} ===")
        for a, b in untracked[:40]:
            print(f"  {a!r}\n    -> {b!r}")
