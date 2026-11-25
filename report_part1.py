# -*- coding: utf-8 -*-
"""Nội dung báo cáo - phần 1: bìa, mục lục, giới thiệu, công nghệ."""

# ============================================================ BÌA
for _ in range(4):
    para("", indent=False)
para("BÁO CÁO ĐỒ ÁN", size=22, bold=True, color=BLUE,
     align=WD_ALIGN_PARAGRAPH.CENTER, indent=False, space_after=10)
para("XÂY DỰNG ỨNG DỤNG QUẢN LÝ KHO HÀNG", size=18, bold=True, color=DARK,
     align=WD_ALIGN_PARAGRAPH.CENTER, indent=False, space_after=6)
para("trên nền tảng Android", size=16, italic=True, color=GRAY,
     align=WD_ALIGN_PARAGRAPH.CENTER, indent=False, space_after=40)

table(
    ["Mục đồ án", "Xây dựng ứng dụng Quản lý Kho hàng (Android)"],
    [
        ["Ngành nghề", "Công nghệ thông tin"],
        ["Học phần", "Lập trình ứng dụng di động (Android)"],
        ["Nền tảng", "Android – Jetpack Compose (Kotlin)"],
        ["Cơ sở dữ liệu", "SQLite (Android SQLiteOpenHelper)"],
        ["Công cụ build", "Gradle 9.5.0 – Android Gradle Plugin 9.3.3"],
        ["Ngôn ngữ", "Kotlin 2.2.10"],
        ["Giao diện", "Jetpack Compose + Material 3 (Compose BOM 2026.02.01)"],
        ["Mã nguồn", "com.example.quan_ly_kho_hang"],
        ["Ngày nộp báo cáo", "........................................"],
    ],
    widths=[4.5, 11.0],
    font_size=12,
)

page_break()

# ============================================================ MỤC LỤC
heading("MỤC LỤC", 1)
toc = [
    "MỤC LỤC",
    "DANH MỤC HÌNH ẢNH",
    "DANH MỤC BẢNG BIỂU",
    "MỞ ĐẦU",
    "1. Giới thiệu chung về dự án",
    "1.1. Lý do chọn đề tài",
    "1.2. Mục tiêu và phạm vi dự án",
    "1.3. Đối tượng sử dụng",
    "2. Công nghệ và công cụ sử dụng",
    "2.1. Ngôn ngữ lập trình Kotlin",
    "2.2. Jetpack Compose và hệ thống Material 3",
    "2.3. Cơ sở dữ liệu SQLite cục bộ",
    "2.4. Hệ thống build Gradle và Android Gradle Plugin",
    "2.5. Kiến trúc MVVM và các thành phần kiến trúc Android",
    "2.6. Bảng tổng hợp công nghệ",
    "3. Phân tích và thiết kế hệ thống",
    "3.1. Phân tích yêu cầu chức năng",
    "3.2. Phân tích yêu cầu phi chức năng",
    "3.3. Sơ đồ Use Case",
    "3.4. Thiết kế cơ sở dữ liệu",
    "3.5. Thiết kế giao diện và hệ thống màu sắc",
    "4. Cài đặt và triển khai",
    "4.1. Cấu trúc thư mục mã nguồn",
    "4.2. Cấu hình dự án Gradle",
    "4.3. Cài đặt các lớp thành phần chính",
    "4.4. Xử lý lỗi đường dẫn không ASCII trên Windows",
    "5. Kiểm thử và kết quả thực thi",
    "5.1. Quy trình kiểm thử",
    "5.2. Kết quả kiểm thử chức năng",
    "5.3. Giao diện thực tế của ứng dụng",
    "6. Kết luận và hướng phát triển",
    "TÀI LIỆU THAM KHẢO",
]
for item in toc:
    p = para(item, size=12.5, indent=False, space_after=2, line=1.25,
             align=WD_ALIGN_PARAGRAPH.LEFT)

page_break()

# ============================================================ DANH MỤC HÌNH
heading("DANH MỤC HÌNH ẢNH", 1)
for i, t in enumerate([
    "Màn hình đăng nhập ứng dụng",
    "Màn hình danh sách sản phẩm kèm thống kê kho",
    "Màn hình chi tiết sản phẩm",
    "Màn hình thêm sản phẩm mới",
    "Trạng thái lỗi khi tên sản phẩm bị bỏ trống",
    "Trạng thái lỗi khi giá bán không hợp lệ",
    "Màn hình sản phẩm hết hàng",
], start=1):
    para("Hình %d: %s" % (i, t), size=12, indent=False, space_after=3, line=1.25,
         align=WD_ALIGN_PARAGRAPH.LEFT)

heading("DANH MỤC BẢNG BIỂU", 1)
for i, t in enumerate([
    "Bảng 1: Tổng hợp công nghệ sử dụng trong dự án",
    "Bảng 2: Danh sách các yêu cầu chức năng",
    "Bảng 3: Cấu trúc bảng CSDL products",
    "Bảng 4: Bảng màu giao diện",
    "Bảng 5: Cấu trúc thư mục mã nguồn",
    "Bảng 6: Kết quả kiểm thử chức năng",
], start=1):
    para("Bảng %d: %s" % (i, t), size=12, indent=False, space_after=3, line=1.25,
         align=WD_ALIGN_PARAGRAPH.LEFT)

page_break()
