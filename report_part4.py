# -*- coding: utf-8 -*-
"""Nội dung báo cáo - phần 4: kiểm thử, hình ảnh, kết luận."""

# ============================================================ CHƯƠNG 5
heading("5. KIỂM THỬ VÀ KẾT QUẢ THỰC THI", 1)

heading("5.1. Quy trình kiểm thử", 2)
para(
    "Quá trình kiểm thử được thực hiện theo ba bước: biên dịch mã nguồn để phát hiện lỗi cú pháp "
    "và lỗi kiểu dữ liệu, đóng gói APK thông qua tác vụ assembleDebug, và kiểm tra thủ công "
    "từng chức năng trên thiết bị. Toàn bộ quá trình đều được thực hiện với phiên bản Gradle "
    "9.5.0 và Android Gradle Plugin 9.3.3.",
)

heading("5.2. Kết quả kiểm thử chức năng", 2)
table(
    ["STT", "Hạng mục kiểm thử", "Kết quả", "Ghi chú"],
    [
        ["1", "Biên dịch mã nguồn Kotlin (compileDebugKotlin)", "Đạt", "Không có lỗi cú pháp hoặc lỗi kiểu"],
        ["2", "Đóng gói APK (assembleDebug)", "Đạt", "BUILD SUCCESSFUL, tạo ra tệp APK"],
        ["3", "Đăng nhập với thông tin đúng", "Đạt", "Chuyển sang màn hình danh sách"],
        ["4", "Đăng nhập với thông tin sai", "Đạt", "Hiển thị thông báo lỗi, không chuyển màn hình"],
        ["5", "Hiển thị danh sách và thống kê", "Đạt", "Số liệu khớp với dữ liệu thực tế"],
        ["6", "Thêm sản phẩm hợp lệ", "Đạt", "Lưu thành công, quay lại danh sách, sản phẩm mới được đánh dấu"],
        ["7", "Thêm sản phẩm thiếu tên", "Đạt", "Hiển thị lỗi dưới ô nhập, không lưu"],
        ["8", "Thêm sản phẩm với giá rỗng", "Đạt", "Hiển thị lỗi dưới ô nhập, không lưu"],
        ["9", "Thêm sản phẩm với giá bằng 0 hoặc âm", "Đạt", "Hiển thị lỗi dưới ô nhập, không lưu"],
        ["10", "Thêm sản phẩm với số lượng không hợp lệ", "Đạt", "Hiển thị lỗi dưới ô nhập, không lưu"],
        ["11", "Xem chi tiết sản phẩm", "Đạt", "Hiển thị đầy đủ thông tin và giá trị tồn kho"],
        ["12", "Nhập thêm 1 đơn vị", "Đạt", "Số lượng tăng, thống kê cập nhật"],
        ["13", "Bán 1 đơn vị", "Đạt", "Số lượng giảm, nút bán bị vô hiệu hóa khi hết hàng"],
        ["14", "Xóa sản phẩm", "Đạt", "Xóa khỏi CSDL, quay lại danh sách"],
        ["15", "Hiển thị trạng thái hết hàng", "Đạt", "Chip đỏ Hết hàng, cảnh báo trong màn chi tiết"],
    ],
    widths=[1.2, 6.4, 2.0, 6.4],
    font_size=10.5,
)
para(
    "Kết luận: toàn bộ 15 hạng mục kiểm thử đều đạt. Ứng dụng biên dịch không lỗi, đóng gói "
    "thành công và đáp ứng đầy đủ các yêu cầu chức năng đã đề ra.",
)

heading("5.3. Giao diện thực tế của ứng dụng", 2)
para(
    "Phần này trình bày các ảnh chụp màn hình từ ứng dụng đã cài đặt trên thiết bị thật, thể hiện "
    "giao diện và các chức năng chính.",
)

heading("5.3.1. Màn hình đăng nhập", 3)
para(
    "Màn hình đăng nhập gồm biểu trưng vòng tròn, tiêu đề ứng dụng, hai ô nhập tên đăng nhập và "
    "mật khẩu (mật khẩu hiển thị dưới dạng ký tự đại diện), nút đăng nhập bo tròn và gợi ý tài "
    "khoản mẫu. Khi thông tin không đúng, thông báo lỗi hiển thị ngay dưới ô mật khẩu.",
)
picture("image1.png", 1, "Màn hình đăng nhập ứng dụng", width_cm=7.8)

heading("5.3.2. Màn hình danh sách sản phẩm và thống kê kho", 3)
para(
    "Màn hình chính của ứng dụng. Phần trên là Card thống kê kho gồm hai hàng: hàng đầu hiển thị "
    "tổng số sản phẩm và tổng giá trị kho, hàng dưới hiển thị số sản phẩm sắp hết hàng và số "
    "sản phẩm hết hàng, với các nhãn nằm thẳng hàng theo cột. Bên dưới là danh sách sản phẩm "
    "mỗi mục hiển thị tên, số lượng, giá bán, chip loại sản phẩm và chip trạng thái tồn kho.",
)
picture("image2.png", 2, "Màn hình danh sách sản phẩm kèm thống kê kho", width_cm=7.8)

heading("5.3.3. Màn hình chi tiết sản phẩm", 3)
para(
    "Màn hình chi tiết hiển thị tên sản phẩm lớn, chip loại sản phẩm, giá bán, thẻ thống kê tồn "
    "kho (số lượng tồn kho kèm nhãn trạng thái và giá trị tồn kho), thẻ mô tả, cùng các nút hành "
    "động nhập thêm, bán, quay lại và xóa.",
)
picture("image3.png", 3, "Màn hình chi tiết sản phẩm", width_cm=7.8)

heading("5.3.4. Màn hình thêm sản phẩm", 3)
para(
    "Màn hình thêm sản phẩm gồm các ô nhập tên, giá bán, số lượng, danh sách loại sản phẩm "
    "dạng thả xuống, công tắc trạng thái đang kinh doanh, ô mô tả nhiều dòng và nút lưu sản phẩm.",
)
picture("image4.png", 4, "Màn hình thêm sản phẩm mới", width_cm=7.8)

heading("5.3.5. Kiểm tra dữ liệu đầu vào", 3)
para(
    "Hình 5 minh họa trường hợp tên sản phẩm bị bỏ trống: ô nhập được viền đỏ và thông điệp lỗi "
    "hiển thị ngay bên dưới, đồng thời một thông báo Toast báo người dùng nhập đầy đủ thông tin.",
)
picture("image5.png", 5, "Trạng thái lỗi khi tên sản phẩm bị bỏ trống", width_cm=7.8)
para(
    "Hình 6 minh họa trường hợp giá bán không hợp lệ (bằng 0): cơ chế kiểm tra chặn không cho lưu "
    "sản phẩm và hiển thị thông báo lỗi tương ứng.",
)
picture("image6.png", 6, "Trạng thái lỗi khi giá bán không hợp lệ", width_cm=7.8)

heading("5.3.6. Trạng thái hết hàng", 3)
para(
    "Hình 7 minh họa trường hợp sản phẩm đã bán hết. Trong danh sách, sản phẩm hiển thị chip đỏ "
    "Hết hàng thay cho chip cam Sắp hết hàng, số lượng được tô đậm màu đỏ. Trong màn hình chi tiết, "
    "xuất hiện hộp cảnh báo nền đỏ nhắc người dùng bổ sung tồn kho và nút Bán 1 bị vô hiệu hóa.",
)
picture("image7.png", 7, "Màn hình sản phẩm hết hàng", width_cm=7.8)

page_break()

# ============================================================ CHƯƠNG 6
heading("6. KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN", 1)

heading("6.1. Kết luận", 2)
para(
    "Đồ án đã hoàn thành các mục tiêu đề ra. Ứng dụng Quản lý Kho hàng chạy trên nền tảng "
    "Android với Kotlin và Jetpack Compose, cung cấp đầy đủ chu trình quản lý kho hàng từ đăng "
    "nhập, theo dõi thống kê, thêm mới, xem chi tiết, cập nhật tồn kho đến xóa sản phẩm.",
)
para(
    "Điểm đáng chú ý nhất của sản phẩm là tính đúng đắn về mặt nghiệp vụ: mọi đầu vào đều được "
    "kiểm tra chặt chẽ trước khi lưu, thống kê được tính toán trực tiếp từ cơ sở dữ liệu nên "
    "luôn khớp với thực tế, và người dùng luôn biết chính xác sản phẩm nào đang sắp hết hàng, "
    "sản phẩm nào đã hết hàng.",
)
para(
    "Về mặt kỹ thuật, dự án cũng đạt được các yêu cầu về chất lượng mã nguồn: mã nguồn biên "
    "dịch không lỗi, cấu trúc package được tổ chức rõ ràng theo tầng, các truy vấn cơ sở dữ liệu "
    "đều được tham số hóa, tài nguyên được giải phóng đúng cách, và các thành phần giao diện "
    "được tách bạch khỏi logic nghiệp vụ.",
)

heading("6.2. Hạn chế còn tồn tại", 2)
for b in [
    "Xác thực người dùng hiện đơn giản, mật khẩu nằm trực tiếp trong mã nguồn.",
    "Dữ liệu chỉ tồn tại trên một thiết bị, chưa có đồng bộ hoặc sao lưu.",
    "Chưa hỗ trợ nhiều kho hàng, nhiều người dùng cùng lúc truy cập.",
    "Chưa có chức năng xuất báo cáo, thống kê theo khoảng thời gian hoặc biểu đồ.",
    "Chưa có tìm kiếm và sắp xếp danh sách sản phẩm theo tiêu chí.",
]:
    bullet(b)

heading("6.3. Hướng phát triển trong tương lai", 2)
for b in [
    "Nâng cấp cơ chế xác thực: lưu mật khẩu dạng băm, thêm đăng nhập bằng vân tay và hỗ trợ đổi mật khẩu.",
    "Bổ sung đồng bộ dữ liệu qua dịch vụ đám mây để người dùng truy cập trên nhiều thiết bị.",
    "Thêm tính năng nhập và xuất dữ liệu theo định dạng CSV hoặc Excel.",
    "Bổ sung biểu đồ thống kê theo thời gian, theo loại sản phẩm và đường biểu diễn giá trị tồn kho.",
    "Thêm tìm kiếm, lọc và sắp xếp danh sách sản phẩm.",
    "Hỗ trợ quét mã vạch để nhập nhanh thông tin sản phẩm.",
    "Bổ sung chức năng nhập kê hàng và ghi chú giao dịch theo lịch sử.",
]:
    bullet(b)

page_break()

# ============================================================ TLTK
heading("TÀI LIỆU THAM KHẢO", 1)
for i, ref in enumerate([
    "Google. (2024). Jetpack Compose Documentation. Android Developers. "
    "https://developer.android.com/develop/ui/compose",
    "Google. (2024). Material Design 3 - Compose. Android Developers. "
    "https://developer.android.com/develop/ui/compose/designsystems/material3",
    "Google. (2024). Save data in a local database using Room. Android Developers. "
    "https://developer.android.com/training/data-storage/room",
    "Google. (2024). SQLite and Android. Android Developers. "
    "https://developer.android.com/training/data-storage/sqlite",
    "Google. (2024). Activity Result APIs. Android Developers. "
    "https://developer.android.com/training/activity-result",
    "JetBrains. (2024). Kotlin Documentation. https://kotlinlang.org/docs/home.html",
    "JetBrains. (2024). Kotlin Coding Conventions. "
    "https://kotlinlang.org/docs/coding-conventions.html",
    "Google. (2024). Gradle Version Catalogs. Android Developers. "
    "https://developer.android.com/build/dependencies/version-catalogs",
    "Google. (2024). Android Gradle Plugin Release Notes. Android Developers. "
    "https://developer.android.com/build/releases/gradle-plugin",
]):
    p = para("[%d] %s" % (i + 1, ref), size=12.5, indent=False, space_after=6, line=1.4)

doc.save(OUT_DOCX)
print("Đã tạo báo cáo:", OUT_DOCX)
