# TH03 - Phát triển ứng dụng di động

## Ứng dụng Quản lý Kho hàng (Android)

Ứng dụng quản lý kho hàng chạy trên nền tảng Android, xây dựng bằng **Kotlin** và **Jetpack Compose**, lưu trữ dữ liệu cục bộ bằng **SQLite**.

### Tính năng

| STT | Nhóm chức năng | Mô tả |
|-----|----------------|-------|
| 1 | Đăng nhập | Xác thực tên đăng nhập và mật khẩu (tài khoản mẫu: `admin` / `123456`) |
| 2 | Thống kê kho | Tổng số sản phẩm, tổng giá trị kho, số sản phẩm sắp hết hàng và hết hàng |
| 3 | Danh sách sản phẩm | Cuộn danh sách, hiển thị tên, số lượng, giá, loại và chip trạng thái tồn kho |
| 4 | Thêm sản phẩm | Kiểm tra dữ liệu đầu vào, báo lỗi tại ô nhập và Toast |
| 5 | Chi tiết sản phẩm | Xem đầy đủ thông tin, giá trị tồn kho, mô tả |
| 6 | Cập nhật tồn kho | Nhập thêm 1 / bán bớt 1, nút bán tự vô hiệu hóa khi hết hàng |
| 7 | Xóa sản phẩm | Xóa khỏi cơ sở dữ liệu |

### Công nghệ sử dụng

- **Kotlin** 2.2.10
- **Jetpack Compose** (Compose BOM 2026.02.01) + **Material 3**
- **SQLite** thông qua `SQLiteOpenHelper`
- **Gradle** 9.5.0 · **Android Gradle Plugin** 9.3.3 · **Version Catalog**
- `compileSdk` / `targetSdk` 37, `minSdk` 24

### Cấu trúc mã nguồn

```
app/src/main/java/com/example/quan_ly_kho_hang/
├── MainActivity.kt            # Danh sách sản phẩm + thống kê kho
├── LoginActivity.kt           # Đăng nhập
├── AddProductActivity.kt      # Thêm sản phẩm (có validate dữ liệu)
├── ProductDetailActivity.kt   # Chi tiết + cập nhật tồn kho
├── model/Product.kt           # Data class Product
├── database/DatabaseHelper.kt # Quản lý SQLite
├── ui/theme/                  # Color, Theme, Type, AppIcons
└── utils/CurrencyUtils.kt     # Định dạng tiền tệ VND
```

### Chạy dự án

1. Mở bằng **Android Studio** (Jellyfish trở lên).
2. Đồng bộ Gradle và chờ quá trình build hoàn tất.
3. Chọn emulator hoặc thiết bị thật, nhấn **Run**.

> **Lưu ý về đường dẫn:** nếu thư mục dự án chứa ký tự không thuộc bảng ASCII
> (ví dụ `D:\Phát triển Android\...`), Android Gradle Plugin sẽ báo lỗi
> *"Your project path contains non-ASCII characters"*. Khi đó hãy chuyển dự án
> sang đường dẫn thuần ASCII, hoặc thêm `android.overridePathCheck=true`
> vào `gradle.properties`.

### Báo cáo

Báo cáo đồ án chi tiết nằm trong file [`QL_khohang.docx`](QL_khohang.docx), gồm 6 chương với phần tổng quan công nghệ, phân tích thiết kế, cài đặt, kết quả kiểm thử và hình ảnh giao diện thực tế.

Các ảnh chụp màn hình trong báo cáo được lưu tại thư mục [`.report_images/`](.report_images).

### Giấy phép

MIT License.
