# -*- coding: utf-8 -*-
"""Tạo báo cáo Word QL_khohang.docx - điểm khởi chạy."""

import os
import runpy

ROOT = os.path.dirname(os.path.abspath(__file__))

# nạp helper (định nghĩa doc, heading, para, picture, table, ...)
ns = runpy.run_path(os.path.join(ROOT, "gen_report.py"))

doc = ns["doc"]
para = ns["para"]
heading = ns["heading"]
bullet = ns["bullet"]
picture = ns["picture"]
table = ns["table"]
code_block = ns["code_block"]
page_break = ns["page_break"]
WD_ALIGN_PARAGRAPH = ns["WD_ALIGN_PARAGRAPH"]
OUT_DOCX = ns["OUT_DOCX"]

for part in ["report_part1.py", "report_part2.py",
             "report_part3.py", "report_part4.py"]:
    path = os.path.join(ROOT, part)
    src = open(path, encoding="utf-8").read()
    exec(compile(src, path, "exec"), ns)
    print("  ->", part, "OK")

# thêm số trang ở chân trang
ns["add_footer_page_numbers"]()

doc.save(OUT_DOCX)
print("ĐÃ TẠO:", OUT_DOCX)
