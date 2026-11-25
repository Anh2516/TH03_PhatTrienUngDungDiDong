# -*- coding: utf-8 -*-
"""Nội dung báo cáo - phần 3: thiết kế, cài đặt, kiểm thử, kết luận."""

# ============================================================ CHƯƠNG 3
heading("3. PHÂN TÍCH VÀ THIẾT KẾ HỆ THỐNG", 1)

heading("3.1. Phân tích yêu cầu chức năng", 2)
para(
    "Từ phân tích mô tả bài toán và khảo sát nhu cầu người dùng, hệ thống được chia thành các "
    "nhóm chức năng chính sau:",
)
table(
    ["STT", "Nhóm chức năng", "Mô tả chi tiết"],
    [
        ["1", "Đăng nhập", "Xác thực tên đăng nhập và mật khẩu, hiển thị thông báo lỗi khi sai"],
        ["2", "Xem thống kê kho", "Tổng số sản phẩm, tổng giá trị kho, số sản phẩm sắp hết hàng, số sản phẩm hết hàng"],
        ["3", "Danh sách sản phẩm", "Hiển thị danh sách dạng cuộn, kèm tên, số lượng, giá, loại và nhãn trạng thái"],
        ["4", "Thêm sản phẩm", "Nhập tên, giá, số lượng, loại, trạng thái kinh doanh và mô tả; kiểm tra dữ liệu đầu vào"],
        ["5", "Xem chi tiết sản phẩm", "Hiển thị đầy đủ thông tin, giá trị tồn kho và mô tả sản phẩm"],
        ["6", "Cập nhật tồn kho", "Nút nhập thêm 1 và bán bớt 1, tự động làm mới dữ liệu hiển thị"],
        ["7", "Xóa sản phẩm", "Xóa khỏi cơ sở dữ liệu và trở về màn hình danh sách"],
        ["8", "Định dạng tiền tệ", "Hiển thị giá theo định dạng Việt Nam, dấu chấm phân tách nghìn và ký hiệu đ"],
    ],
    widths=[1.4, 4.2, 10.4],
    font_size=11,
)

heading("3.2. Phân tích yêu cầu phi chức năng", 2)
for b in [
    "Hiệu năng: ứng dụng phải khởi động và phản hồi thao tác trong thời gian ngắn, truy vấn cơ sở dữ liệu không được làm nghẽn giao diện.",
    "Dễ sử dụng: giao diện tiếng Việt, phân cấp rõ ràng, thao tác bằng một tay trên điện thoại, phản hồi lỗi tức thời tại ô nhập.",
    "Khả năng mở rộng: mã nguồn được tổ chức theo package (model, database, ui/theme, utils) để dễ bổ sung tính năng.",
    "Tính ổn định: dữ liệu phải được lưu trữ bền vững, không mất khi đóng ứng dụng; các thao tác cập nhật phải an toàn về mặt dữ liệu.",
    "Khả năng kiểm thử: tách biệt rõ ràng giữa tầng dữ liệu và tầng giao diện để có thể kiểm thử độc lập.",
    "Tương thích: hỗ trợ Android 7.0 trở lên, hoạt động được cả trên máy thật lẫn trình giả lập.",
]:
    bullet(b)

heading("3.3. Sơ đồ Use Case", 2)
para(
    "Xét về phía người dùng (chủ kho), các trường hợp sử dụng chính của hệ thống được tổng "
    "kết như sau:",
)
for b in [
    "UC01 – Đăng nhập: người dùng nhập tên đăng nhập và mật khẩu; hệ thống kiểm tra và cho phép hoặc từ chối truy cập.",
    "UC02 – Xem danh sách và thống kê: người dùng mở ứng dụng và xem tổng quan kho hàng.",
    "UC03 – Thêm sản phẩm: người dùng nhập thông tin sản phẩm mới; hệ thống kiểm tra tính hợp lệ rồi lưu và thông báo kết quả.",
    "UC04 – Xem chi tiết: người dùng chọn một sản phẩm trong danh sách để xem thông tin đầy đủ.",
    "UC05 – Nhập thêm tồn kho: người dùng tăng số lượng tồn kho của một sản phẩm.",
    "UC06 – Bán sản phẩm: người dùng giảm số lượng tồn kho; hệ thống chặn thao tác khi đã hết hàng.",
    "UC07 – Xóa sản phẩm: người dùng xóa một sản phẩm không còn kinh doanh.",
]:
    bullet(b)
para(
    "Ràng buộc nghiệp vụ quan trọng: tên sản phẩm không được để trống; giá bán phải là số lớn hơn 0; "
    "số lượng phải là số nguyên không âm; số lượng tồn kho không được nhỏ hơn 0; không thể bán khi "
    "số lượng đã bằng 0.",
)

heading("3.4. Thiết kế cơ sở dữ liệu", 2)
para(
    "Cơ sở dữ liệu SQLite với tên quan_ly_kho_hang.db, phiên bản 1, gồm một bảng duy nhất "
    "lưu trữ thông tin sản phẩm:",
)
table(
    ["Tên cột", "Kiểu dữ liệu", "Ràng buộc", "Mô tả"],
    [
        ["id", "INTEGER", "PRIMARY KEY AUTOINCREMENT", "Mã định danh duy nhất, tự tăng"],
        ["name", "TEXT", "NOT NULL", "Tên sản phẩm"],
        ["price", "REAL", "NOT NULL", "Giá bán đơn vị đồng Việt Nam"],
        ["quantity", "INTEGER", "NOT NULL", "Số lượng tồn kho hiện tại"],
        ["category", "TEXT", "NOT NULL", "Loại sản phẩm"],
        ["is_selling", "INTEGER", "NOT NULL DEFAULT 1", "Trạng thái đang kinh doanh (1/0)"],
        ["description", "TEXT", "Cho phép null", "Mô tả chi tiết sản phẩm"],
    ],
    widths=[3.2, 3.4, 5.2, 4.2],
    font_size=11,
)
para(
    "Kiểu dữ liệu REAL được chọn cho cột price nhằm thuận tiện cho phép tính toán giá trị tồn "
    "kho (price × quantity) trong mã nguồn. Cột is_selling sử dụng kiểu INTEGER làm cờ nhị phân "
    "đơn giản, tương thích với cơ chế put trong ContentValues.",
)
para(
    "Ngay khi tạo bảng, lớp DatabaseHelper chèn sẵn ba bản ghi dữ liệu mẫu (chuột không dây, "
    "bàn phím cơ và sổ tay A5) nhằm giúp người dùng làm quen với giao diện ngay từ lần chạy đầu tiên.",
)

heading("3.5. Thiết kế giao diện và hệ thống màu sắc", 2)
para(
    "Giao diện được xây dựng theo nguyên tắc thiết kế phẳng (flat design), ưu tiên sự rõ ràng "
    "về mặt thị giác và tính nhất quán trên toàn bộ ứng dụng. Hệ thống màu được định nghĩa tập "
    "trung trong tệp Color.kt nhằm dễ bảo trì và thay đổi:",
)
table(
    ["Tên hằng số", "Mã màu", "Ý nghĩa sử dụng"],
    [
        ["BluePrimary", "#1565C0", "Màu nhấn chính: nền nút, thành phần chủ đạo"],
        ["BluePrimaryDark", "#0D47A1", "Màu nền thanh tiêu đề, chữ tiêu đề"],
        ["BlueLightContainer", "#E3F2FD", "Nền thẻ thống kê, nền chip loại sản phẩm"],
        ["OrangeSell", "#F57C00", "Nút bán, chỉ số sắp hết hàng"],
        ["OrangeSellBg", "#FFF3E0", "Nền chip sắp hết hàng"],
        ["RedDelete", "#D32F2F", "Nút xóa sản phẩm"],
        ["RedBadgeText", "#C62828", "Chữ cảnh báo hết hàng"],
        ["RedBadgeBg", "#FFEBEE", "Nền chip hết hàng, nền hộp cảnh báo"],
        ["SurfaceBackground", "#F8FAFC", "Màu nền chung của màn hình"],
        ["TextDark", "#1E293B", "Màu chữ tiêu đề nội dung"],
        ["TextGray", "#64748B", "Màu chữ phụ, chữ ghi chú"],
    ],
    widths=[4.6, 3.4, 8.0],
    font_size=11,
)
para(
    "Quy ước về nhãn trạng thái tồn kho được thống nhất trên cả hai màn hình danh sách và chi tiết:",
)
for b in [
    "Số lượng từ 1 đến 5: hiển thị chip nền cam với nhãn Sắp hết hàng.",
    "Số lượng bằng 0: hiển thị chip nền đỏ với nhãn Hết hàng, đồng thời số lượng và cảnh báo "
    "trong màn hình chi tiết chuyển sang màu đỏ để thu hút sự chú ý.",
]:
    bullet(b)

page_break()

# ============================================================ CHƯƠNG 4
heading("4. CÀI ĐẶT VÀ TRIỂN KHAI", 1)

heading("4.1. Cấu trúc thư mục mã nguồn", 2)
table(
    ["Đường dẫn", "Nội dung"],
    [
        ["app/src/main/java/com/example/quan_ly_kho_hang/", "Gốc mã nguồn Kotlin của ứng dụng"],
        ["  ├─ MainActivity.kt", "Màn hình danh sách sản phẩm và thống kê kho"],
        ["  ├─ LoginActivity.kt", "Màn hình đăng nhập"],
        ["  ├─ AddProductActivity.kt", "Màn hình thêm sản phẩm mới"],
        ["  ├─ ProductDetailActivity.kt", "Màn hình chi tiết sản phẩm"],
        ["  ├─ model/Product.kt", "Lớp dữ liệu Product (data class)"],
        ["  ├─ database/DatabaseHelper.kt", "Lớp truy cập SQLite và quản lý vòng đời CSDL"],
        ["  ├─ ui/theme/", "Color.kt, Theme.kt, Type.kt, AppIcons.kt"],
        ["  ├─ utils/CurrencyUtils.kt", "Hàm định dạng tiền tệ Việt Nam"],
        ["app/src/main/res/", "Tài nguyên: hình ảnh, giá trị, giao diện XML"],
        ["app/src/main/AndroidManifest.xml", "Khai báo Activity, quyền và cấu hình ứng dụng"],
        ["app/build.gradle.kts", "Cấu hình build của module app"],
        ["gradle/libs.versions.toml", "Gradle Version Catalog khai báo phiên bản thư viện"],
    ],
    widths=[8.0, 8.0],
    font_size=10.5,
)

heading("4.2. Cấu hình dự án Gradle", 2)
para(
    "Tệp app/build.gradle.kts khai báo plugin Android Application và Kotlin Compose, đồng thời "
    "cấu hình các thông số build quan trọng:",
)
code_block([
    "plugins {",
    "    alias(libs.plugins.android.application)",
    "    alias(libs.plugins.kotlin.compose)",
    "}",
    "",
    "android {",
    "    namespace = \"com.example.quan_ly_kho_hang\"",
    "    compileSdk { version = release(37) }",
    "",
    "    defaultConfig {",
    "        applicationId = \"com.example.quan_ly_kho_hang\"",
    "        minSdk = 24",
    "        targetSdk = 37",
    "        versionCode = 1",
    "        versionName = \"1.0\"",
    "    }",
    "",
    "    buildTypes {",
    "        release { optimization { enable = false } }",
    "    }",
    "    compileOptions {",
    "        sourceCompatibility = JavaVersion.VERSION_11",
    "        targetCompatibility = JavaVersion.VERSION_11",
    "    }",
    "    buildFeatures { compose = true }",
    "}",
])
para(
    "Cấu hình trong gradle.properties tối ưu cho quá trình phát triển:",
)
code_block([
    "org.gradle.jvmargs=-Xmx2048m -Dfile.encoding=UTF-8",
    "org.gradle.configuration-cache=true",
    "kotlin.code.style=official",
    "android.overridePathCheck=true",
    "android.sync.suppressAgpWarnings=UNSUPPORTED_PROJECT_OPTION_USE",
])

heading("4.3. Cài đặt các lớp thành phần chính", 2)

heading("4.3.1. Lớp dữ liệu Product", 3)
para(
    "Lớp Product được thiết kế dưới dạng data class của Kotlin, tự động sinh ra các hàm equals, "
    "hashCode, toString và copy. Việc này giúp việc so sánh và truyền tải đối tượng trong Compose "
    "trở nên thuận tiện:",
)
code_block([
    "data class Product(",
    "    val id: Int = 0,",
    "    val name: String,",
    "    val price: Double,",
    "    val quantity: Int,",
    "    val category: String,",
    "    val isSelling: Boolean = true,",
    "    val description: String = \"\"",
    ")",
])

heading("4.3.2. Lớp DatabaseHelper", 3)
para(
    "Lớp DatabaseHelper kế thừa SQLiteOpenHelper, chịu trách nhiệm toàn bộ thao tác với cơ sở "
    "dữ liệu. Điểm đáng chú ý là phương thức updateQuantity() thực hiện việc đọc giá trị hiện "
    "tại, cộng thêm độ biến rồi giới hạn kết quả không nhỏ hơn 0 bằng hàm coerceAtLeast(), "
    "đảm bảo tính toàn vẹn dữ liệu ngay cả khi có thao tác cạnh tranh:",
)
code_block([
    "fun updateQuantity(id: Int, delta: Int): Boolean {",
    "    val product = getProductById(id) ?: return false",
    "    val newQuantity = (product.quantity + delta).coerceAtLeast(0)",
    "    val values = ContentValues().apply { put(COLUMN_QUANTITY, newQuantity) }",
    "    val rows = db.update(TABLE_PRODUCTS, values, \"$COLUMN_ID = ?\", arrayOf(id.toString()))",
    "    return rows > 0",
    "}",
])

heading("4.3.3. Màn hình đăng nhập", 3)
para(
    "Màn hình đăng nhập được xây dựng theo mẫu trang trí (decorative pattern) của Compose. Trạng "
    "thái lỗi isError được quản lý bằng mutableStateOf và được xóa ngay khi người dùng bắt đầu "
    "nhập lại, tạo cảm giác phản hồi tức thì. Mật khẩu được hiển thị dưới dạng ký tự đại diện "
    "nhờ PasswordVisualTransformation.",
)

heading("4.3.4. Màn hình danh sách và thống kê kho", 3)
para(
    "Màn hình danh sách sử dụng Scaffold với thanh tiêu đề trên cùng và thanh nút hành động ở "
    "dưới. Các chỉ số thống kê được đặt trong một Card nền xanh nhạt và chia thành hai hàng, "
    "mỗi hàng hai cột có cùng tỷ lệ chiều rộng để các nhãn nằm thẳng hàng dọc:",
)
code_block([
    "val totalProducts  = products.size",
    "val totalValue     = products.sumOf { it.price * it.quantity }",
    "val lowStockCount  = products.count { it.quantity in 1..5 }",
    "val outOfStockCount = products.count { it.quantity == 0 }",
])
para(
    "Danh sách sản phẩm hiển thị bằng LazyColumn, một thành phần chỉ dựng các mục đang nhìn "
    "thấy, giúp ứng dụng xử lý tốt với danh sách dài mà không tốn nhiều bộ nhớ. Sản phẩm vừa được "
    "thêm được đánh dấu bằng nền xanh nhạt và đường viền xanh để người dùng nhận biết ngay.",
)

heading("4.3.5. Màn hình thêm sản phẩm và cơ chế kiểm tra dữ liệu", 3)
para(
    "Đây là phần xử lý quan trọng nhất về mặt nghiệp vụ. Hàm validate() kiểm tra đồng thời ba "
    "trường bắt buộc và gán thông điệp lỗi tương ứng vào từng biến trạng thái. Các ô nhập sử "
    "dụng thuộc tính isError kết hợp supportingText để hiển thị lỗi ngay dưới ô nhập, đồng thời "
    "một thông báo Toast tổng quát giúp người dùng nhận biết ngay khi thao tác lưu thất bại:",
)
code_block([
    "fun validate(): Boolean {",
    "    var isValid = true",
    "    if (name.isBlank()) {",
    "        nameError = \"Vui lòng nhập tên sản phẩm\"",
    "        isValid = false",
    "    } else nameError = null",
    "",
    "    val price = priceText.trim().toDoubleOrNull()",
    "    when {",
    "        priceText.isBlank() -> { priceError = \"Vui lòng nhập giá bán\"; isValid = false }",
    "        price == null       -> { priceError = \"Giá bán không hợp lệ, chỉ nhập số\"; isValid = false }",
    "        price.isNaN() || price.isInfinite() -> { priceError = \"Giá bán không hợp lệ...\"; isValid = false }",
    "        price <= 0.0       -> { priceError = \"Giá bán phải lớn hơn 0\"; isValid = false }",
    "        else -> priceError = null",
    "    }",
    "    // ... kiểm tra tương tự cho quantity (số nguyên, không âm)",
    "    return isValid",
    "}",
])
para(
    "Sau khi vượt qua kiểm tra, sản phẩm được lưu vào cơ sở dữ liệu. Nếu thành công, "
    "AddProductActivity trả mã sản phẩm mới về MainActivity qua setResult(), MainActivity nạp lại "
    "danh sách và thống kê, đồng thời đánh dấu sản phẩm vừa thêm.",
)

heading("4.3.6. Màn hình chi tiết sản phẩm", 3)
para(
    "Màn hình chi tiết cung cấp bốn nhóm thao tác: nhập thêm 1, bán 1, quay lại và xóa sản phẩm. "
    "Nút Bán 1 được cấu hình enabled = product.quantity > 0 nên không thể bán khi đã hết hàng. "
    "Mỗi lần thao tác, phương thức loadProduct() được gọi lại trong onResume() để dữ liệu hiển thị "
    "luôn khớp với cơ sở dữ liệu.",
)

heading("4.4. Xử lý lỗi đường dẫn không ASCII trên Windows", 3)
para(
    "Trong quá trình cài đặt và build dự án đã gặp một lỗi đặc thù đáng lưu ý: thư mục dự án "
    "được đặt tại đường dẫn chứa ký tự tiếng Việt không thuộc bảng ASCII, ví dụ "
    "D:\\Phát triển Android\\QuanLyKhoHang2. Android Gradle Plugin kiểm tra điều này và báo lỗi:",
)
code_block([
    "Your project path contains non-ASCII characters. This will most likely cause",
    "the build to fail on Windows. Please move your project to a different directory.",
])
para(
    "Biểu hiện cụ thể là tác vụ mergeDebugResources thất bại với thông báo Resource compilation "
    "failed và ResourceCompilerRunnable không thể tìm thấy đường dẫn, trong khi tác vụ biên dịch "
    "Kotlin vẫn chạy bình thường. Có hai hướng xử lý:",
)
for b in [
    "Khuyến nghị: chuyển dự án sang đường dẫn thuần ASCII, ví dụ D:\\Projects\\QuanLyKhoHang2. "
    "Cách này giải quyết triệt để và tránh mọi rắc rối phát sinh về sau.",
    "Tạm thời: bổ sung thuộc tính android.overridePathCheck=true trong gradle.properties để vô "
    "hiệu hóa cơ chế kiểm tra của AGP. Khi build qua dòng lệnh, có thể dùng lệnh subst trên "
    "Windows để ánh xạ thư mục dự án sang một ổ đĩa có tên chỉ chứa ký tự ASCII.",
]:
    bullet(b)

page_break()
