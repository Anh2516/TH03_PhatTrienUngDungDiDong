# -*- coding: utf-8 -*-
"""Sinh báo cáo Word cho dự án Quản lý Kho hàng (Android)."""

import os
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

ROOT = r"D:\Phát triển Android\QuanLyKhoHang2"
IMG_DIR = os.path.join(ROOT, ".report_images")
OUT_DOCX = os.path.join(ROOT, "QL_khohang.docx")

FONT = "Times New Roman"
BLUE = RGBColor(0x0D, 0x47, 0xA1)
DARK = RGBColor(0x1E, 0x29, 0x3B)
GRAY = RGBColor(0x64, 0x74, 0x8B)

doc = Document()

# ---------------------------------------------------------------- page setup
sec = doc.sections[0]
sec.top_margin = Cm(2.0)
sec.bottom_margin = Cm(2.0)
sec.left_margin = Cm(3.0)
sec.right_margin = Cm(2.0)

# ---------------------------------------------------------------- base style
st = doc.styles["Normal"]
st.font.name = FONT
st.font.size = Pt(13)
st.element.rPr.rFonts.set(qn("w:eastAsia"), FONT)
st.paragraph_format.line_spacing = 1.5
st.paragraph_format.space_after = Pt(6)
st.paragraph_format.first_line_indent = Cm(1.25)


def set_font(run, size=13, bold=False, italic=False, color=None, font=FONT):
    run.font.name = font
    run.font.size = Pt(size)
    run.bold = bold
    run.italic = italic
    if color is not None:
        run.font.color.rgb = color
    run._element.rPr.rFonts.set(qn("w:eastAsia"), font)


def para(text="", size=13, bold=False, italic=False, color=None,
         align=WD_ALIGN_PARAGRAPH.JUSTIFY, indent=True, space_before=0,
         space_after=6, line=1.5, keep_with_next=False):
    p = doc.add_paragraph()
    p.alignment = align
    pf = p.paragraph_format
    pf.first_line_indent = Cm(1.25) if indent else Cm(0)
    pf.space_before = Pt(space_before)
    pf.space_after = Pt(space_after)
    pf.line_spacing = line
    pf.keep_with_next = keep_with_next
    if text:
        set_font(p.add_run(text), size, bold, italic, color)
    return p


def heading(text, level=1):
    sizes = {0: 18, 1: 15, 2: 13.5}
    p = doc.add_paragraph()
    pf = p.paragraph_format
    pf.first_line_indent = Cm(0)
    pf.space_before = Pt(14 if level == 1 else 10)
    pf.space_after = Pt(8)
    pf.line_spacing = 1.3
    pf.keep_with_next = True
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    set_font(p.add_run(text), sizes.get(level, 13.5), True, color=BLUE if level <= 1 else DARK)
    return p


def bullet(text, size=13, indent_cm=0.75, bold_prefix=None):
    p = doc.add_paragraph(style="List Bullet")
    pf = p.paragraph_format
    pf.first_line_indent = Cm(-0.5)
    pf.left_indent = Cm(indent_cm + 0.5)
    pf.space_after = Pt(3)
    pf.line_spacing = 1.4
    if bold_prefix:
        set_font(p.add_run(bold_prefix), size, True)
    set_font(p.add_run(text), size)
    return p


def caption(text, idx):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    pf = p.paragraph_format
    pf.first_line_indent = Cm(0)
    pf.space_before = Pt(4)
    pf.space_after = Pt(12)
    pf.line_spacing = 1.2
    set_font(p.add_run("Hình %d: %s" % (idx, text)), 11, italic=True, color=GRAY)
    return p


def picture(filename, idx, caption_text, width_cm=7.8):
    path = os.path.join(IMG_DIR, filename)
    if not os.path.exists(path):
        print("MISSING", filename)
        return
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.first_line_indent = Cm(0)
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.keep_with_next = True
    p.add_run().add_picture(path, width=Cm(width_cm))
    caption(caption_text, idx)


def table(headers, rows, widths=None, font_size=11.5):
    t = doc.add_table(rows=1, cols=len(headers))
    t.style = "Table Grid"
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr = t.rows[0].cells
    for i, h in enumerate(headers):
        hdr[i].text = ""
        p = hdr[i].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.first_line_indent = Cm(0)
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.line_spacing = 1.15
        set_font(p.add_run(h), font_size, True, color=RGBColor(0xFF, 0xFF, 0xFF))
        shd = OxmlElement("w:shd")
        shd.set(qn("w:val"), "clear")
        shd.set(qn("w:fill"), "0D47A1")
        hdr[i]._tc.get_or_add_tcPr().append(shd)
    for row in rows:
        cells = t.add_row().cells
        for i, val in enumerate(row):
            cells[i].text = ""
            p = cells[i].paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            p.paragraph_format.first_line_indent = Cm(0)
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.line_spacing = 1.15
            set_font(p.add_run(str(val)), font_size)
    if widths:
        for r in t.rows:
            for i, w in enumerate(widths):
                r.cells[i].width = Cm(w)
    doc.add_paragraph().paragraph_format.space_after = Pt(0)
    return t


def code_block(lines, size=10.5):
    for ln in lines:
        p = doc.add_paragraph()
        pf = p.paragraph_format
        pf.first_line_indent = Cm(0)
        pf.left_indent = Cm(0.6)
        pf.space_after = Pt(0)
        pf.space_before = Pt(0)
        pf.line_spacing = 1.15
        set_font(p.add_run(ln), size, font="Consolas")
    doc.add_paragraph().paragraph_format.space_after = Pt(0)


def page_break():
    doc.add_page_break()


def add_footer_page_numbers():
    """Thêm số trang ở chân trang, định dạng 'Trang X / Y'."""
    footer = doc.sections[0].footer
    p = footer.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.first_line_indent = Cm(0)

    def field(instr):
        r = p.add_run()
        fc = OxmlElement("w:fldChar")
        fc.set(qn("w:fldCharType"), "begin")
        r._r.append(fc)
        r2 = p.add_run()
        it = OxmlElement("w:instrText")
        it.set(qn("xml:space"), "preserve")
        it.text = instr
        r2._r.append(it)
        r3 = p.add_run()
        fc2 = OxmlElement("w:fldChar")
        fc2.set(qn("w:fldCharType"), "end")
        r3._r.append(fc2)
        for rr in (r, r2, r3):
            set_font(rr, 11, color=GRAY)

    set_font(p.add_run("Trang "), 11, color=GRAY)
    field("PAGE")
    set_font(p.add_run(" / "), 11, color=GRAY)
    field("NUMPAGES")
