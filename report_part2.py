# -*- coding: utf-8 -*-
"""Nội dung báo cáo - phần 2: mở đầu, giới thiệu, công nghệ."""

# ============================================================ MỞ ĐẦU
heading("MỞ ĐẦU", 1)

heading("1. Lý do chọn đề tài", 2)
para(
    "Trong bối cảnh hoạt động kinh doanh ngày càng phát triển, việc quản lý kho hàng "
    "thủ công bằng sổ tay hoặc bảng tính Excel thường dẫn đến nhiều hạn chế: dữ liệu bị "
    "phân mảnh, cập nhật chậm, dễ xảy ra sai sót khi đối chiếu tồn kho và thường khó "
    "theo dõi kịp thời các chỉ số quan trọng như giá trị tồn kho hay cảnh báo sắp hết hàng. "
    "Đặc biệt với các cửa hàng nhỏ và vừa, nhu cầu truy xuất tồn kho tức thời trên điện "
    "thoại là một nhu cầu thực tế và cấp thiết.",
)
para(
    "Bên cạnh đó, sự phổ biến của hệ điều hành Android và tính ưu việt của các ứng dụng "
    "di động trong việc hỗ trợ công tác quản lý tại hiện trường đã mở ra cơ hội để xây dựng "
    "một ứng dụng quản lý kho hàng hoạt động hoàn toàn trên thiết bị, không cần máy tính, "
    "không cần kết nối Internet và không tốn chi phí cấp phép. Xu hướng hiện nay trong lĩnh "
    "vực phát triển phần mềm cũng chuyển dịch mạnh sang nền tảng Android với Jetpack "
    "Compose – công nghệ khai báo giao diện hiện đại, giúp đẩy nhanh tốc độ phát triển và "
    "tăng khả năng bảo trì.",
)
para(
    "Xuất phát từ những nhận thức trên, em lựa chọn xây dựng ứng dụng Quản lý Kho hàng "
    "chạy trên nền tảng Android sử dụng ngôn ngữ Kotlin và thư viện Jetpack Compose. "
    "Ứng dụng tập trung vào các chức năng cốt lõi: đăng nhập, xem danh sách và thống kê kho, "
    "thêm mới, xem chi tiết, cập nhật tồn kho (nhập thêm/bán) và xóa sản phẩm.",
)

heading("2. Mục tiêu của đồ án", 2)
para(
    "Mục tiêu tổng quát của đồ án là xây dựng một ứng dụng quản lý kho hàng hoàn chỉnh, "
    "hoạt động ổn định, giao diện thẩm mỹ và dễ sử dụng trên các thiết bị chạy Android.",
)
para("Các mục tiêu cụ thể bao gồm:", indent=False)
for b in [
    "Xây dựng cơ chế đăng nhập đơn giản để bảo vệ dữ liệu kho hàng.",
    "Hiển thị danh sách sản phẩm kèm thống kê tổng quan: tổng số sản phẩm, tổng giá trị kho, "
    "số sản phẩm sắp hết hàng và số sản phẩm hết hàng.",
    "Cung cấp chức năng thêm sản phẩm mới với cơ chế kiểm tra dữ liệu đầu vào chặt chẽ, "
    "ngăn chặn việc lưu các giá trị không hợp lệ.",
    "Cung cấp màn hình chi tiết sản phẩm với các thao tác nhập thêm tồn kho, bán bớt và xóa.",
    "Hiển thị trạng thái tồn kho rõ ràng qua các nhãn màu: Sắp hết hàng (cam) và Hết hàng (đỏ).",
    "Áp dụng các nguyên tắc kiểm thử phần mềm trong quá trình hoàn thiện và kiểm chứng ứng dụng.",
]:
    bullet(b)

heading("3. Phạm vi và hạn chế của dự án", 2)
para(
    "Phạm vi thực hiện của đồ án được giới hạn trong một ứng dụng quản lý kho hàng chạy "
    "hoàn toàn cục bộ trên một thiết bị Android, sử dụng cơ sở dữ liệu SQLite nhúng sẵn. "
    "Ứng dụng hỗ trợ thiết bị từ Android 7.0 (API 24) trở lên và được build với "
    "compileSdk/targetSdk 37.",
)
para(
    "Một số hạn chế đáng lưu ý: ứng dụng chưa có tính năng đồng bộ dữ liệu giữa nhiều thiết bị, "
    "chưa hỗ trợ đa người dùng cùng lúc trên cùng một kho, chưa có chức năng xuất báo cáo "
    "thống kê ra tệp và chưa có cơ chế sao lưu dữ liệu tự động. Mật khẩu đăng nhập hiện được "
    "kiểm tra trực tiếp trong mã nguồn, phù hợp với đối tượng bài tập nhưng chưa đủ an toàn "
    "cho môi trường sản xuất thực tế.",
)

heading("4. Phương pháp thực hiện", 2)
para(
    "Quá trình thực hiện đồ án được chia thành các giai đoạn: khảo sát và phân tích yêu cầu, "
    "thiết kế cơ sở dữ liệu và giao diện, cài đặt từng màn hình theo mô hình MVVM, xây dựng "
    "bộ kiểm thử và kiểm chứng kết quả. Mỗi giai đoạn đều được kiểm tra bằng cách biên dịch "
    "mã nguồn và chạy ứng dụng trên thiết bị thật hoặc trình giả lập.",
)

page_break()

# ============================================================ CHƯƠNG 1
heading("1. GIỚI THIỆU CHUNG VỀ DỰ ÁN", 1)

heading("1.1. Tổng quan", 2)
para(
    "Quản lý Kho hàng là ứng dụng Android hỗ trợ người dùng theo dõi và cập nhật tồn kho "
    "của các sản phẩm đang kinh doanh. Ứng dụng được xây dựng hoàn toàn bằng ngôn ngữ "
    "Kotlin kết hợp bộ công cụ Jetpack Compose của JetBrains và Google cho phần giao diện, "
    "sử dụng SQLite làm hệ quản trị cơ sở dữ liệu cục bộ.",
)
para(
    "Điểm nổi bật của ứng dụng nằm ở trải nghiệm người dùng: toàn bộ quy trình từ đăng nhập, "
    "xem thống kê, thêm sản phẩm đến cập nhật tồn kho đều được thực hiện trên một màn hình "
    "trực quan với phản hồi tức thời. Thống kê kho được tính toán trực tiếp từ dữ liệu trong "
    "cơ sở dữ liệu, nhờ vậy số liệu luôn luôn khớp với thực tế kho hàng.",
)

heading("1.2. Cấu trúc ứng dụng", 2)
para(
    "Ứng dụng gồm bốn màn hình chính được liên kết với nhau theo luồng nghiệp vụ tự nhiên:",
)
for b in [
    "Màn hình đăng nhập (LoginActivity): xác thực người dùng trước khi truy cập hệ thống.",
    "Màn hình danh sách (MainActivity): hiển thị thống kê kho tổng quan và danh sách sản phẩm.",
    "Màn hình thêm sản phẩm (AddProductActivity): nhập và kiểm tra thông tin sản phẩm mới.",
    "Màn hình chi tiết (ProductDetailActivity): xem đầy đủ thông tin và thao tác cập nhật tồn kho.",
]:
    bullet(b)

heading("1.3. Đối tượng sử dụng", 2)
para(
    "Ứng dụng hướng đến các chủ cửa hàng, nhân viên bán hàng và quản lý kho tại cửa hàng vừa và "
    "nhỏ, cũng như sinh viên thực tập muốn tìm hiểu cách xây dựng ứng dụng Android hiện đại. "
    "Giao diện được thiết kế đơn giản, dùng tiếng Việt, phù hợp với người dùng phổ thông.",
)

page_break()

# ============================================================ CHƯƠNG 2
heading("2. CÔNG NGHỆ VÀ CÔNG CỤ SỬ DỤNG", 1)

heading("2.1. Ngôn ngữ lập trình Kotlin", 2)
para(
    "Kotlin là ngôn ngữ lập trình chính thức được Google khuyến nghị cho việc phát triển ứng "
    "dụng Android. Ngôn ngữ này chạy trên JVM, hoàn toàn tương thích với Java, đồng thời bổ "
    "sung nhiều tính năng hiện đại giúp giảm thiểu lỗi và tăng năng suất lập trình.",
)
para(
    "Trong dự án này, Kotlin được sử dụng ở phiên bản 2.2.10 với các đặc điểm nổi bật sau:",
)
for b in [
    "Null safety: hệ thống kiểu dữ liệu loại bỏ null, giúp loại bỏ phần lớn lỗi NullPointerException "
    "thường gặp trong lập trình Android.",
    "Type safety: hỗ trợ sealed class, data class và pattern matching, giúp mô hình hóa trạng "
    "thái và dữ liệu rõ ràng.",
    "Extension functions: mở rộng chức năng của lớp có sẵn mà không cần kế thừa (ví dụ hàm "
    "formatVND mở rộng kiểu Double).",
    "Coroutines và StateFlow: hỗ trợ lập trình bất đồng bộ, tránh block giao diện người dùng.",
    "Scope functions (let, apply, apply): viết code gọn gàng cho các thao tác khởi tạo đối tượng.",
]:
    bullet(b)
para(
    "Dự án cũng áp dụng các khuyến nghị chính thức về Kotlin Coding Conventions, sử dụng "
    "định dạng chuẩn với 4 khoảng thụt đầu dòng, khai báo biến bất biến khi có thể và "
    "ưu tiên biểu thức vị ngữ.",
)

heading("2.2. Jetpack Compose – hệ thống giao diện khai báo", 2)
para(
    "Jetpack Compose là bộ công cụ xây dựng giao diện người dùng hiện đại của Android, được "
    "xem là thế hệ tiếp theo so với hệ thống View truyền thống. Triết lý cốt lõi của Compose "
    "là mô tả giao diện bằng cách khai báo các hàm @Composable trả về cây giao diện, thay vì "
    "thao tác trực tiếp lên đối tượng View.",
)
para("Các điểm nổi bật được ứng dụng trong dự án:", indent=False)
for b in [
    "Khai báo theo cấu trúc: dùng Column, Row, Box và các hàm bố trục để mô tả bố cục.",
    "Modifier: chuỗi chỉnh sửa được gắn vào từng thành phần (padding, background, clip, "
    "clickable), giúp mã nguồn gọn và linh hoạt hơn so với XML.",
    "Tái sử dụng với State: khi dữ liệu thay đổi, Compose tự động tính lại và vẽ lại những "
    "phần giao diện bị ảnh hưởng.",
    "Animation và tương tác: hỗ trợ chuyển động mượt mà, hiệu ứng nhấn và xử lý cảm ứng.",
]:
    bullet(b)
para(
    "Dự án sử dụng Material 3 (Material 3 Components) làm hệ thống thiết kế, kết hợp thư viện "
    "Compose BOM phiên bản 2026.02.01 để quản lý thống nhất các phiên bản thư viện Compose. "
    "Các thành phần chủ đạo được dùng gồm Scaffold, Card, OutlinedTextField, Button, "
    "ExposedDropdownMenuBox, Switch, IconButton và HorizontalDivider.",
)
para(
    "Để hạn chế phụ thuộc vào thư viện biểu tượng bên ngoài, hai vector biểu tượng được sử dụng "
    "nhiều nhất (mũi tên quay lại và mũi tên thả xuống) được tự định nghĩa thủ công bằng "
    "ImageVector.Builder trong tệp AppIcons.kt, kèm theo cơ chế cache để tránh dựng lại vector "
    "mỗi lần vẽ.",
)

heading("2.3. Cơ sở dữ liệu SQLite cục bộ", 2)
para(
    "SQLite là hệ quản trị cơ sở dữ liệu quan hệ nhúng, được tích hợp sẵn trong mọi thiết bị "
    "Android. Dữ liệu được lưu trữ trực tiếp trên thiết bị, không cần máy chủ, không cần kết "
    "nối Internet và hoạt động hoàn toàn offline.",
)
para(
    "Dự án sử dụng lớp SQLiteOpenHelper thông qua lớp DatabaseHelper, tuân theo mô hình quản lý "
    "vòng đời cơ sở dữ liệu chuẩn của Android:",
)
for b in [
    "onCreate(): được gọi lần đầu khi tạo cơ sở dữ liệu, thực hiện câu lệnh CREATE TABLE và "
    "chèn dữ liệu mẫu khởi tạo.",
    "onUpgrade(): được gọi khi cần nâng cấp phiên bản cơ sở dữ liệu, hiện thực hiện DROP TABLE "
    "rồi tạo lại để đảm bảo tính nhất quán.",
    "getAllProducts(), getProductById(), insertProduct(), updateProduct(), updateQuantity(), "
    "deleteProduct(): các phương thức truy vấn và thao tác dữ liệu, đều sử dụng đối tượng "
    "Cursor trong khối try-with-resources để bảo đảm giải phóng tài nguyên.",
]:
    bullet(b)
para(
    "Các truy vấn được viết bằng tham số hóa (selection và selectionArgs) thay vì nối chuỗi, "
    "giúp loại bỏ nguy cơ SQL Injection và tận dụng được cơ chế cache của SQLite.",
)

heading("2.4. Hệ thống build Gradle và Android Gradle Plugin", 2)
para(
    "Gradle là hệ thống build mặc định của Android, hỗ trợ quản lý dependency, biên dịch mã "
    "nguồn, đóng gói APK và tối ưu hóa. Dự án sử dụng Gradle 9.5.0 với Android Gradle Plugin "
    "phiên bản 9.3.3, cấu hình thông qua ngôn ngữ Kotlin DSL (build.gradle.kts).",
)
para(
    "Việc khai báo phiên bản thư viện được tập trung hóa trong Gradle Version Catalog "
    "(gradle/libs.versions.toml), cho phép thay đổi phiên bản ở một vị trí duy nhất và tránh "
    "xung đột khi nhiều thư viện phụ thuộc vào cùng một thư viện trung gian.",
)

heading("2.5. Kiến trúc MVVM và các thành phần kiến trúc Android", 2)
para(
    "Ứng dụng tổ chức mã nguồn theo kiến trúc MVVM (Model – ViewModel – View) được rút gọn "
    "cho phạm vi ứng dụng cục bộ:",
)
for b in [
    "Model: lớp Product đóng vai trò dữ liệu, cùng lớp DatabaseHelper đóng vai trò kho "
    "dữ liệu (Repository) truy cập SQLite.",
    "View: các hàm @Composable (MainScreenContent, AddProductScreen, ProductDetailContent, "
    "LoginScreen) chịu trách nhiệm dựng giao diện, hoàn toàn không chứa logic nghiệp vụ.",
    "State: dữ liệu được nắm giữ bởi mutableStateOf và được quan sát bằng by trong "
    "setContent, khiến giao diện tự động cập nhật khi dữ liệu thay đổi.",
]:
    bullet(b)
para(
    "Dự án tận dụng Activity Result API hiện đại (registerForActivityResult với "
    "ActivityResultContracts.StartActivityForResult) để truyền dữ liệu hai chiều giữa các "
    "màn hình. Cụ thể, khi thêm sản phẩm thành công, AddProductActivity trả về mã sản phẩm "
    "mới thông qua setResult(), và MainActivity nhận mã này để nạp lại danh sách, đồng thời "
    "đánh dấu sản phẩm vừa thêm để người dùng dễ nhận biết.",
)
para(
    "Ngoài ra, ứng dụng sử dụng các thành phần hỗ trợ từ thư viện androidx.activity và "
    "androidx.lifecycle, trong đó hàm enableEdgeToEdge() cho phép nội dung hiển thị trải rộng "
    "dưới thanh trạng thái và thanh điều hướng của thiết bị, đồng thời các modifier "
    "statusBarsPadding() và navigationBarsPadding() giữ nội dung không bị che khuất.",
)

heading("2.6. Bảng tổng hợp công nghệ", 2)
table(
    ["Hạng mục", "Công nghệ / Thư viện", "Phiên bản", "Mục đích sử dụng"],
    [
        ["Ngôn ngữ", "Kotlin", "2.2.10", "Ngôn ngữ lập trình chính cho Android"],
        ["Giao diện", "Jetpack Compose (BOM)", "2026.02.01", "Xây dựng giao diện khai báo"],
        ["Thiết kế", "Material 3 Components", "Theo BOM", "Bộ component giao diện chuẩn"],
        ["Nền tảng", "Android SDK", "compileSdk/targetSdk 37", "Nền tảng chạy ứng dụng"],
        ["Tối thiểu", "Android SDK", "minSdk 24", "Hỗ trợ Android 7.0 trở lên"],
        ["CSDL", "SQLite (SQLiteOpenHelper)", "Bản nhúng trong SDK", "Lưu trữ dữ liệu cục bộ"],
        ["Build", "Gradle", "9.5.0", "Hệ thống build và quản lý dependency"],
        ["Build plugin", "Android Gradle Plugin", "9.3.3", "Plugin build chính thức của Android"],
        ["Dependency", "Gradle Version Catalog", "libs.versions.toml", "Quản lý tập trung phiên bản"],
        ["Activity", "androidx.activity:activity-compose", "1.13.0", "ComposeActivity, Activity Result API"],
        ["Lifecycle", "androidx.lifecycle:lifecycle-runtime-ktx", "2.11.0", "Hỗ trợ vòng đời Activity"],
        ["Lõi", "androidx.core:core-ktx", "1.19.1", "Các tiện ích mở rộng của AndroidX"],
        ["Kiểm thử", "JUnit 4.13.2 / Espresso 3.7.0", "-", "Kiểm thử đơn vị và kiểm thử giao diện"],
    ],
    widths=[2.8, 5.6, 3.0, 4.6],
    font_size=10.5,
)

page_break()
