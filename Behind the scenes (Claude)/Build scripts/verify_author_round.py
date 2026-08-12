#!/usr/bin/env python3
"""MANDATORY author-round verifier. After applying an author's edit round, run:

    python3 verify_author_round.py "<author file.docx>" "<new draft.docx>"

For EVERY tracked insertion and every bracketed comment in the author file it
reports one of:
    FOUND      — the inserted text appears in the new draft (verbatim, after
                 whitespace/quote normalization)
    PARTIAL    — a long insertion appears only in part (shows the missing part)
    ABSENT     — not in the new draft: MUST be explained line-by-line in the
                 Change Log (superseded by a later author edit, a comment that
                 was actioned rather than copied, or a logged consolidation) —
                 'substance preserved' with no location is NOT an explanation
Deletions are checked the other way: text the author deleted that still appears
in the new draft is reported as STILL-PRESENT.

Exit code 0 only if every item is FOUND or is a bracket (brackets are
instructions; they must be actioned, which this tool cannot judge — it lists
them for the reconciliation). Built after a real incident in which a
contaminated diff base silently cancelled 41 author insertions and a
'substance preserved' judgment waved them through."""
import re
import sys
import html
import zipfile


def norm(t):
    t = t.replace('’', "'").replace('‘', "'")
    t = t.replace('“', '"').replace('”', '"')
    t = t.replace('ﬁ', 'fi').replace('ﬂ', 'fl')
    t = t.replace('—', '-').replace('–', '-').replace('­', '')
    return re.sub(r'\s+', ' ', t).strip()


def doc_xmls(path):
    z = zipfile.ZipFile(path)
    xmls = [z.read('word/document.xml').decode('utf-8')]
    if 'word/footnotes.xml' in z.namelist():
        xmls.append(z.read('word/footnotes.xml').decode('utf-8'))
    return xmls


def visible_text(path):
    out = []
    for xml in doc_xmls(path):
        out.append(html.unescape(''.join(
            re.findall(r'<w:t[^>]*>([^<]*)</w:t>', xml))))
    return norm(' '.join(out))


def author_items(path):
    xml = doc_xmls(path)[0]
    ins, dels, brackets = [], [], []
    for p in re.findall(r'<w:p\b.*?</w:p>', xml, re.S):
        for i in re.findall(r'<w:ins\b.*?</w:ins>', p, re.S):
            t = norm(html.unescape(''.join(
                re.findall(r'<w:t[^>]*>([^<]*)</w:t>', i))))
            if t:
                ins.append(t)
        for d in re.findall(r'<w:del\b.*?</w:del>', p, re.S):
            t = norm(html.unescape(''.join(
                re.findall(r'<w:delText[^>]*>([^<]*)</w:delText>', d))))
            if t:
                dels.append(t)
        vis = html.unescape(''.join(re.findall(r'<w:t[^>]*>([^<]*)</w:t>', p)))
        brackets += [norm(b) for b in re.findall(r'\[[^\[\]]{6,500}?\]', vis)]
    return ins, dels, brackets


def main(author_path, draft_path):
    draft = visible_text(draft_path)
    ins, dels, brackets = author_items(author_path)
    # merge consecutive tiny insertions is not attempted; tiny fragments (<4
    # words) are only checked when they carry alphanumerics and length > 12
    absent, partial, found = [], [], 0
    for t in ins:
        if t in draft:
            found += 1
            continue
        if len(t) < 13 or not re.search(r'[A-Za-z]{3}', t):
            found += 1  # fragment too small to check meaningfully
            continue
        words = t.split()
        if len(words) >= 12:
            head = ' '.join(words[:8])
            tail = ' '.join(words[-8:])
            if head in draft or tail in draft:
                partial.append(t)
                continue
        absent.append(t)
    still = [t for t in dels
             if len(t) >= 13 and re.search(r'[A-Za-z]{3}', t) and t in draft]

    print(f'insertions: {len(ins)}  FOUND(or tiny): {found}  '
          f'PARTIAL: {len(partial)}  ABSENT: {len(absent)}')
    for t in partial:
        print(f'\nPARTIAL: {t[:220]}')
    for t in absent:
        print(f'\nABSENT : {t[:220]}')
    print(f'\ndeletions still present in draft: {len(still)}')
    for t in still:
        print(f'\nSTILL-PRESENT: {t[:220]}')
    print(f'\nbrackets (author instructions — each must be actioned and '
          f'reconciled): {len(brackets)}')
    for b in brackets:
        print(f'  BRACKET: {b[:200]}')
    ok = not absent and not partial and not still
    print(f'\nVERDICT: {"CLEAN" if ok else "ITEMS REQUIRE RECONCILIATION"}')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1], sys.argv[2]))
