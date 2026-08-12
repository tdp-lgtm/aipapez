#!/usr/bin/env python3
"""Author-facing PAPER builder. Default paper appearance (adjust to the author's own
preferences, recorded in the Context doc): Arial, black text only (accent-colored text in
a draft reads as an AI tell), no horizontal rules under headings, no page header, page
numbers in the footer, REAL Word footnotes.

Blocks:
  ('title', text)          — Arial 16 bold, centered
  ('abstract', text)       — 'Abstract' heading + indented body
  ('h1', text)             — Arial 13 bold, black, no border
  ('body', text)           — Arial 11; inline **bold** honored; inline {{FN: ...}}
                             becomes a real footnote anchored at that point
  ('display', label, text) — indented, bold label (analytic-philosophy display)

Footnotes are injected as a proper footnotes part (separator + continuation stubs,
then notes id 2..N), related from the document part; anchors are superscript
footnoteReference runs."""
import re

from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import parse_xml
from docx.oxml.ns import qn, nsmap
from docx.opc.part import Part
from docx.opc.packuri import PackURI

FONT = 'Arial'
NS = 'xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"'
FOOTNOTES_RELTYPE = ('http://schemas.openxmlformats.org/officeDocument/2006/'
                     'relationships/footnotes')
FOOTNOTES_CTYPE = ('application/vnd.openxmlformats-officedocument.'
                   'wordprocessingml.footnotes+xml')


def _set_font(run, size=11, bold=False, italic=False):
    run.font.name = FONT
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.italic = italic
    rPr = run._element.get_or_add_rPr()
    rFonts = rPr.find(qn('w:rFonts'))
    if rFonts is None:
        rFonts = parse_xml(f'<w:rFonts {NS} w:ascii="{FONT}" w:hAnsi="{FONT}"/>')
        rPr.append(rFonts)
    else:
        rFonts.set(qn('w:ascii'), FONT)
        rFonts.set(qn('w:hAnsi'), FONT)


BLUE = '0000CC'


def _set_color(run, hexval):
    rPr = run._element.get_or_add_rPr()
    rPr.append(parse_xml(f'<w:color {NS} w:val="{hexval}"/>'))


def _add_text_runs(par, text, notes, size=11):
    """Add runs honoring **bold**, {{FN: ...}} footnotes, and [[blue]]...[[/blue]]
    revision-marking spans (blue text; may span bold and footnote anchors)."""
    blue = False
    # NB: the bold alternative must precede the italic one, or the italic pattern
    # matches the inside of '**bold**' and mangles any later {{FN: ...}} in the piece.
    pieces = re.split(r'(\{\{FN:.*?\}\}|\[\[blue\]\]|\[\[/blue\]\]|\*\*[^*\n]+\*\*|\*[^*\n]+\*)', text,
                      flags=re.S)
    for piece in pieces:
        if piece == '[[blue]]':
            blue = True
            continue
        if piece == '[[/blue]]':
            blue = False
            continue
        if piece.startswith('{{FN:'):
            note = piece[5:-2].strip()
            # footnote bodies stay black even inside [[blue]] prose spans:
            # blue marks new/reviewable PROSE; carried citations are not new.
            # A note renders blue only if the builder wraps it explicitly.
            notes.append(note)
            fn_id = len(notes) + 1  # ids 0,1 are separators; real notes from 2
            run = par.add_run()
            _set_font(run, size=size)
            rPr = run._element.get_or_add_rPr()
            rPr.append(parse_xml(f'<w:vertAlign {NS} w:val="superscript"/>'))
            if blue:
                _set_color(run, BLUE)
            run._element.append(parse_xml(
                f'<w:footnoteReference {NS} w:id="{fn_id}"/>'))
            continue
        for seg in re.split(r'(\*\*.*?\*\*)', piece, flags=re.S):
            if not seg:
                continue
            if seg.startswith('*') and seg.endswith('*') and not seg.startswith('**'):
                run = par.add_run(seg[1:-1])
                _set_font(run, size=size, italic=True)
                if blue:
                    _set_color(run, BLUE)
                continue
            if seg.startswith('**') and seg.endswith('**'):
                run = par.add_run(seg[2:-2])
                _set_font(run, size=size, bold=True)
            else:
                run = par.add_run(seg)
                _set_font(run, size=size)
            if blue:
                _set_color(run, BLUE)


def _footnotes_xml(notes):
    def esc(t):
        return (t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
                 .replace('"', '&quot;'))
    parts = [
        f'<w:footnote w:type="separator" w:id="0"><w:p><w:pPr><w:spacing w:after="0"'
        f'/></w:pPr><w:r><w:separator/></w:r></w:p></w:footnote>',
        f'<w:footnote w:type="continuationSeparator" w:id="1"><w:p><w:pPr>'
        f'<w:spacing w:after="0"/></w:pPr><w:r><w:continuationSeparator/></w:r>'
        f'</w:p></w:footnote>',
    ]
    for i, note in enumerate(notes, start=2):
        runs = []
        blue = False
        for seg in re.split(r'(\*\*.*?\*\*|\*[^*\n]+\*|\[\[blue\]\]|\[\[/blue\]\])', note,
                            flags=re.S):
            if seg == '[[blue]]':
                blue = True
                continue
            if seg == '[[/blue]]':
                blue = False
                continue
            if not seg:
                continue
            color = f'<w:color w:val="0000CC"/>' if blue else ''
            if seg.startswith('*') and seg.endswith('*') and not seg.startswith('**'):
                runs.append(f'<w:r><w:rPr><w:rFonts w:ascii="{FONT}" w:hAnsi='
                            f'"{FONT}"/><w:sz w:val="18"/><w:i/>{color}</w:rPr><w:t '
                            f'xml:space="preserve">{esc(seg[1:-1])}</w:t></w:r>')
                continue
            if seg.startswith('**') and seg.endswith('**'):
                runs.append(f'<w:r><w:rPr><w:rFonts w:ascii="{FONT}" w:hAnsi='
                            f'"{FONT}"/><w:sz w:val="18"/><w:b/>{color}</w:rPr><w:t '
                            f'xml:space="preserve">{esc(seg[2:-2])}</w:t></w:r>')
            else:
                runs.append(f'<w:r><w:rPr><w:rFonts w:ascii="{FONT}" w:hAnsi='
                            f'"{FONT}"/><w:sz w:val="18"/>{color}</w:rPr><w:t '
                            f'xml:space="preserve">{esc(seg)}</w:t></w:r>')
        parts.append(
            f'<w:footnote w:id="{i}"><w:p><w:pPr><w:spacing w:after="60"/></w:pPr>'
            f'<w:r><w:rPr><w:rFonts w:ascii="{FONT}" w:hAnsi="{FONT}"/><w:sz '
            f'w:val="18"/><w:vertAlign w:val="superscript"/></w:rPr>'
            f'<w:footnoteRef/></w:r><w:r><w:rPr><w:rFonts w:ascii="{FONT}" '
            f'w:hAnsi="{FONT}"/><w:sz w:val="18"/></w:rPr><w:t '
            f'xml:space="preserve"> </w:t></w:r>{"".join(runs)}</w:p></w:footnote>')
    return ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
            f'<w:footnotes {NS}>' + ''.join(parts) + '</w:footnotes>').encode()


def build_paper(path, blocks):
    doc = Document()
    for section in doc.sections:
        section.left_margin = Inches(1)
        section.right_margin = Inches(1)
        # footer: centered page number, no header content
        footer_p = section.footer.paragraphs[0]
        footer_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        fld = parse_xml(f'<w:fldSimple {NS} w:instr="PAGE"><w:r><w:rPr><w:rFonts '
                        f'w:ascii="{FONT}" w:hAnsi="{FONT}"/><w:sz w:val="20"/>'
                        f'</w:rPr></w:r></w:fldSimple>')
        footer_p._p.append(fld)

    notes = []
    words = 0
    for blk in blocks:
        kind = blk[0]
        if kind == 'title':
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_after = Pt(18)
            r = p.add_run(blk[1])
            _set_font(r, size=16, bold=True)
            words += len(blk[1].split())
        elif kind == 'abstract':
            ph = doc.add_paragraph()
            ph.paragraph_format.space_after = Pt(4)
            rh = ph.add_run('Abstract')
            _set_font(rh, size=11, bold=True)
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Inches(0.4)
            p.paragraph_format.right_indent = Inches(0.4)
            p.paragraph_format.space_after = Pt(14)
            _add_text_runs(p, blk[1], notes, size=10)
            words += len(blk[1].split())
        elif kind == 'h1':
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(14)
            p.paragraph_format.space_after = Pt(6)
            r = p.add_run(blk[1])
            _set_font(r, size=13, bold=True)
            words += len(blk[1].split())
        elif kind == 'h2':
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(10)
            p.paragraph_format.space_after = Pt(4)
            r = p.add_run(blk[1])
            _set_font(r, size=12, bold=True)
            words += len(blk[1].split())
        elif kind == 'h3':
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(8)
            p.paragraph_format.space_after = Pt(3)
            r = p.add_run(blk[1])
            _set_font(r, size=11, bold=True, italic=True)
            words += len(blk[1].split())
        elif kind == 'body':
            p = doc.add_paragraph()
            p.paragraph_format.space_after = Pt(8)
            _add_text_runs(p, blk[1], notes)
            words += len(re.sub(r'\{\{FN:.*?\}\}|\[\[/?blue\]\]', ' ', blk[1], flags=re.S).split())
        elif kind == 'display':
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Inches(0.45)
            p.paragraph_format.right_indent = Inches(0.2)
            p.paragraph_format.space_before = Pt(6)
            p.paragraph_format.space_after = Pt(8)
            if blk[1]:
                lab = p.add_run(blk[1] + '  ')
                _set_font(lab, bold=True)
            _add_text_runs(p, blk[2], notes)
            words += len((blk[1] + ' ' + blk[2]).split())
        else:
            raise ValueError(f'unknown block kind: {kind}')

    if notes:
        fn_words = sum(len(re.sub(r'\*\*', '', n).split()) for n in notes)
        part = Part(PackURI('/word/footnotes.xml'), FOOTNOTES_CTYPE,
                    _footnotes_xml(notes), doc.part.package)
        doc.part.relate_to(part, FOOTNOTES_RELTYPE)
    else:
        fn_words = 0

    doc.save(path)
    # post-build hygiene: never hand the author a quarantined file (macOS only)
    import sys as _sys
    if _sys.platform == "darwin":
        import subprocess as _sp
        _sp.run(["xattr", "-d", "com.apple.quarantine", path], capture_output=True)
    # render checks: quote parity + glued punctuation + doubled pincites
    import re as _re
    _txt = "\n".join(p.text for p in doc.paragraphs)
    _odd = sum(1 for _p in doc.paragraphs if _p.text.count('"') % 2)
    _glue = _re.findall(r"[a-z]'[A-Za-z]{2,}", _txt)
    _glue = [g for g in _glue if not _re.match(r"[a-z]'(s|t|ll|re|ve|d|m)\b", g)]
    if _odd or _glue:
        print(f"[render-check WARNING] odd-quote paragraphs={_odd}, glued-quote candidates={_glue[:5]}")
    print(f'[paper] {path}')
    print(f'[stats] body words={words} footnotes={len(notes)} '
          f'(fn words={fn_words})')
    return words
