#!/usr/bin/env python3
"""
Block-based .docx generator for the Deep Drafter (academic paper pipeline).
The block vocabulary is generic: the same toolkit builds plans, outlines, coverage maps,
checklists, and review reports. (Author-facing PAPER drafts use gen_paper_docx.py instead.)

Block types (tuples):
  ('title', text)
  ('subtitle', text)
  ('h1', text) ('h2', text) ('h3', text)
  ('instr', text)            -> verbatim instruction quote: shaded, bordered, italic; label "Instruction — "
  ('instr', label, text)     -> same, with a custom bold label (e.g. "Venue requirement:")
  ('note', text)             -> shaded, bordered, italic box with NO label (changelog / internal note)
  ('body', text)             -> normal paragraph; **bold** inline supported
  ('lead', label, text)      -> bold run 'label' then normal text (e.g. "Response: ...")
  ('bullet', text) ('bullet2', text)
  ('num', text)
  ('caption', text)          -> table caption (bold, small)
  ('table', rows)            -> rows = list of list[str]; first row = header (bold + shaded)
  ('table', rows, widths)    -> optional col widths in inches
  ('spacer',)
  ('pagebreak',)
Inline **bold** is honored in body/lead/bullet/caption/table cells.
"""
import sys
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

INSTR_SHADE = "EFEFEF"
HEADER_TEXT = RGBColor(0xFF, 0xFF, 0xFF)
# Accent color (headings, table-header fills) for WORKING docs. Neutral by default;
# pass accent=... to build() to restyle. Author-facing paper drafts never use accents
# (gen_paper_docx.py builds those: black text only).
NEUTRAL_ACCENT  = "44546A"   # neutral dark blue-gray

def _set_cell_shade(cell, hexfill):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear'); shd.set(qn('w:color'), 'auto'); shd.set(qn('w:fill'), hexfill)
    tcPr.append(shd)

def _para_shade(p, hexfill):
    pPr = p._p.get_or_add_pPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear'); shd.set(qn('w:color'), 'auto'); shd.set(qn('w:fill'), hexfill)
    pPr.append(shd)

def _para_border(p, color="9A9A9A", sz="6", space="6"):
    pPr = p._p.get_or_add_pPr()
    pbdr = OxmlElement('w:pBdr')
    for edge in ('top','left','bottom','right'):
        e = OxmlElement('w:'+edge)
        e.set(qn('w:val'),'single'); e.set(qn('w:sz'),sz); e.set(qn('w:space'),space); e.set(qn('w:color'),color)
        pbdr.append(e)
    pPr.append(pbdr)

def _add_runs(p, text, base_italic=False, base_bold=False):
    """Honor **bold** segments."""
    parts = text.split("**")
    for i, seg in enumerate(parts):
        if seg == "": continue
        r = p.add_run(seg)
        r.italic = base_italic
        r.bold = base_bold or (i % 2 == 1)

def _shade_row(row, hexfill):
    for c in row.cells:
        _set_cell_shade(c, hexfill)

GRAY = RGBColor(0x70, 0x70, 0x70)

def _runfmt(run, size, color=None, bold=False, italic=False, font="Calibri"):
    run.font.name = font; run.font.size = Pt(size); run.bold = bold; run.italic = italic
    if color is not None: run.font.color.rgb = color

def _add_page_field(p):
    """Append a live PAGE number field to paragraph p."""
    for kind, val in (("begin", None), (None, "PAGE"), ("end", None)):
        r = OxmlElement('w:r')
        if kind:
            fld = OxmlElement('w:fldChar'); fld.set(qn('w:fldCharType'), kind); r.append(fld)
        else:
            it = OxmlElement('w:instrText'); it.set(qn('xml:space'), 'preserve'); it.text = " PAGE "; r.append(it)
        p._p.append(r)
    for r in p.runs:
        _runfmt(r, 8.5, GRAY)

def _para_topborder(p, color="808080", sz="6"):
    pPr = p._p.get_or_add_pPr(); pbdr = OxmlElement('w:pBdr')
    e = OxmlElement('w:top'); e.set(qn('w:val'),'single'); e.set(qn('w:sz'),sz); e.set(qn('w:space'),'4'); e.set(qn('w:color'),color)
    pbdr.append(e); pPr.append(pbdr)

def _para_botborder(p, color="808080", sz="6"):
    pPr = p._p.get_or_add_pPr(); pbdr = OxmlElement('w:pBdr')
    e = OxmlElement('w:bottom'); e.set(qn('w:val'),'single'); e.set(qn('w:sz'),sz); e.set(qn('w:space'),'4'); e.set(qn('w:color'),color)
    pbdr.append(e); pPr.append(pbdr)

# Default running header/footer. Pass header_lines / footer_text to build() to override.
DEFAULT_HEADER = ["Deep Drafter"]
DEFAULT_FOOTER = "Deep Drafter"

def _setup_running(section, header_lines, footer_text):
    section.different_first_page_header_footer = True   # clean title page
    section.header_distance = Inches(0.35); section.footer_distance = Inches(0.35)
    # Header: right-aligned running lines
    hdr = section.header; hdr.is_linked_to_previous = False
    hdr.paragraphs[0].clear()
    first = True
    for line in header_lines:
        p = hdr.paragraphs[0] if first else hdr.add_paragraph()
        first = False
        p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        p.paragraph_format.space_after = Pt(0); p.paragraph_format.space_before = Pt(0)
        _runfmt(p.add_run(line), 8.5, GRAY)
    _para_botborder(hdr.paragraphs[-1], "C9D6DC", "4")
    # Footer: title (left) + page number (right) via a tab stop
    ftr = section.footer; ftr.is_linked_to_previous = False
    fp = ftr.paragraphs[0]; fp.clear()
    _para_topborder(fp, "C9D6DC", "4")
    from docx.enum.text import WD_TAB_ALIGNMENT
    fp.paragraph_format.tab_stops.add_tab_stop(Inches(7.3), WD_TAB_ALIGNMENT.RIGHT)
    _runfmt(fp.add_run(footer_text + "\t"), 8.5, GRAY)
    _runfmt(fp.add_run("Page "), 8.5, GRAY)
    _add_page_field(fp)

def build(out_path, blocks, body_font="Calibri", body_size=11.0,
          accent=NEUTRAL_ACCENT, header_lines=None, footer_text=None):
    accent_hex = accent.lstrip("#")
    accent_rgb = RGBColor.from_string(accent_hex)
    doc = Document()
    # base style — Calibri 11pt, single spacing
    normal = doc.styles['Normal']
    normal.font.name = body_font
    normal.font.size = Pt(body_size)
    pf = normal.paragraph_format
    pf.space_after = Pt(6); pf.line_spacing = 1.0   # single line spacing (Word "1.0")
    # margins — narrow sides for content density, room for header/footer
    for s in doc.sections:
        s.top_margin = Inches(0.8); s.bottom_margin = Inches(0.8)
        s.left_margin = Inches(0.6); s.right_margin = Inches(0.6)
        _setup_running(s, header_lines or DEFAULT_HEADER, footer_text or DEFAULT_FOOTER)
    # heading colors/sizes (Calibri Bold; accent color)
    for hname, sz in (('Heading 1',16),('Heading 2',13),('Heading 3',11.5)):
        st = doc.styles[hname]; st.font.color.rgb = accent_rgb; st.font.name = body_font
        st.font.size = Pt(sz); st.font.bold = True

    for blk in blocks:
        kind = blk[0]
        if kind == 'title':
            p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r = p.add_run(blk[1]); r.bold = True; r.font.size = Pt(21); r.font.name = body_font; r.font.color.rgb = accent_rgb
        elif kind == 'subtitle':
            p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r = p.add_run(blk[1]); r.italic = True; r.font.size = Pt(10.5); r.font.name = body_font; r.font.color.rgb = RGBColor(0x55,0x55,0x55)
        elif kind == 'h1':
            h = doc.add_heading(blk[1], level=1)
            _para_botborder(h, accent_hex, "8")   # thin accent rule under each major section
        elif kind == 'h2':
            doc.add_heading(blk[1], level=2)
        elif kind == 'h3':
            doc.add_heading(blk[1], level=3)
        elif kind in ('instr', 'note'):
            if kind == 'instr':
                label = blk[1] if len(blk) > 2 else "Instruction — "
                text = blk[2] if len(blk) > 2 else blk[1]
            else:
                label = None; text = blk[1]
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Inches(0.05); p.paragraph_format.right_indent = Inches(0.05)
            p.paragraph_format.space_before = Pt(4); p.paragraph_format.space_after = Pt(8)
            _para_shade(p, INSTR_SHADE); _para_border(p)
            if label:
                lab = p.add_run(label); lab.bold = True; lab.italic = True; lab.font.size = Pt(9.5); lab.font.color.rgb = RGBColor(0x40,0x40,0x40)
            _add_runs(p, text, base_italic=True)
            for r in p.runs:
                r.font.size = Pt(9.5)
                if not r.bold: r.font.color.rgb = RGBColor(0x33,0x33,0x33)
        elif kind == 'body':
            p = doc.add_paragraph(); _add_runs(p, blk[1])
        elif kind == 'lead':
            p = doc.add_paragraph()
            r = p.add_run(blk[1]); r.bold = True
            p.add_run(" ")
            _add_runs(p, blk[2])
        elif kind == 'display':
            # ('display', 'Label.', 'text') -> indented block with bold label; the analytic-
            # philosophy convention for named principles, views, and cases.
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Inches(0.45)
            p.paragraph_format.right_indent = Inches(0.2)
            p.paragraph_format.space_before = Pt(6); p.paragraph_format.space_after = Pt(8)
            if blk[1]:
                lab = p.add_run(blk[1] + '  '); lab.bold = True
            _add_runs(p, blk[2])
        elif kind == 'bullet':
            p = doc.add_paragraph(style='List Bullet'); _add_runs(p, blk[1])
        elif kind == 'bullet2':
            p = doc.add_paragraph(style='List Bullet 2'); _add_runs(p, blk[1])
        elif kind == 'num':
            p = doc.add_paragraph(style='List Number'); _add_runs(p, blk[1])
        elif kind == 'caption':
            p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(6); p.paragraph_format.space_after = Pt(2)
            r = p.add_run(blk[1]); r.bold = True; r.font.size = Pt(9.5); r.font.color.rgb = accent_rgb
        elif kind == 'spacer':
            doc.add_paragraph()
        elif kind == 'pagebreak':
            doc.add_page_break()
        elif kind == 'table':
            rows = blk[1]; widths = blk[2] if len(blk) > 2 else None
            ncol = max(len(r) for r in rows)
            t = doc.add_table(rows=0, cols=ncol)
            t.style = 'Table Grid'; t.alignment = WD_TABLE_ALIGNMENT.CENTER
            for ri, rowvals in enumerate(rows):
                cells = t.add_row().cells
                for ci in range(ncol):
                    val = rowvals[ci] if ci < len(rowvals) else ""
                    cell = cells[ci]
                    cell.paragraphs[0].text = ""
                    pp = cell.paragraphs[0]
                    _add_runs(pp, val, base_bold=(ri == 0))
                    pp.paragraph_format.space_after = Pt(2); pp.paragraph_format.space_before = Pt(2)
                    for r in pp.runs:
                        r.font.size = Pt(9.5); r.font.name = "Calibri"
                        if ri == 0: r.font.color.rgb = HEADER_TEXT
                if ri == 0:
                    _shade_row(t.rows[0], accent_hex)
                elif ri % 2 == 0:                       # subtle alternating shading (light teal tint)
                    _shade_row(t.rows[ri], "EEF3F5")
            if widths:
                for ci, w in enumerate(widths):
                    for r in t.rows:
                        r.cells[ci].width = Inches(w)
            doc.add_paragraph().paragraph_format.space_after = Pt(2)
        elif kind == 'image':
            # ('image', path) | ('image', path, width_in) | ('image', path, width_in, caption)
            p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            w = blk[2] if len(blk) > 2 and blk[2] else 6.8
            p.add_run().add_picture(blk[1], width=Inches(w))
            if len(blk) > 3 and blk[3]:
                cap = doc.add_paragraph(); cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
                cap.paragraph_format.space_before = Pt(2); cap.paragraph_format.space_after = Pt(6)
                r = cap.add_run(blk[3]); r.bold = True; r.font.size = Pt(9.5); r.font.color.rgb = accent_rgb
        else:
            raise ValueError(f"unknown block: {kind}")

    doc.save(out_path)
    # stats
    words = 0
    for p in doc.paragraphs: words += len(p.text.split())
    for t in doc.tables:
        for row in t.rows:
            for c in row.cells: words += len(c.text.split())
    sys.stderr.write(f"[built] {out_path}\n[stats] paras={len(doc.paragraphs)} tables={len(doc.tables)} words={words}\n")
    return words
