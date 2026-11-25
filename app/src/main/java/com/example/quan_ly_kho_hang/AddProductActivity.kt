package com.example.quan_ly_kho_hang

import android.content.Intent
import android.os.Bundle
import android.widget.Toast
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.foundation.verticalScroll
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.input.KeyboardType
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.example.quan_ly_kho_hang.database.DatabaseHelper
import com.example.quan_ly_kho_hang.model.Product
import com.example.quan_ly_kho_hang.ui.theme.*

class AddProductActivity : ComponentActivity() {
    private lateinit var dbHelper: DatabaseHelper

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        dbHelper = DatabaseHelper(this)
        enableEdgeToEdge()

        setContent {
            QuanLyKhoHangTheme {
                Scaffold(
                    modifier = Modifier.fillMaxSize(),
                    topBar = {
                        Row(
                            modifier = Modifier
                                .fillMaxWidth()
                                .background(BluePrimaryDark)
                                .statusBarsPadding()
                                .padding(vertical = 12.dp, horizontal = 12.dp),
                            verticalAlignment = Alignment.CenterVertically
                        ) {
                            IconButton(onClick = { finish() }) {
                                Icon(
                                    imageVector = ArrowBackIcon,
                                    contentDescription = "Back",
                                    tint = Color.White
                                )
                            }
                            Text(
                                text = "Thêm sản phẩm",
                                color = Color.White,
                                fontSize = 18.sp,
                                fontWeight = FontWeight.Bold
                            )
                        }
                    }
                ) { innerPadding ->
                    AddProductScreen(
                        modifier = Modifier.padding(innerPadding),
                        onSaveProduct = { newProduct ->
                            val result = dbHelper.insertProduct(newProduct)
                            if (result > 0) {
                                // Trả id sản phẩm vừa tạo về màn hình danh sách
                                setResult(
                                    RESULT_OK,
                                    Intent().putExtra(EXTRA_PRODUCT_ID, result.toInt())
                                )
                                Toast.makeText(this, "Thêm sản phẩm thành công!", Toast.LENGTH_SHORT).show()
                                finish()
                            } else {
                                Toast.makeText(this, "Thêm sản phẩm thất bại!", Toast.LENGTH_SHORT).show()
                            }
                        }
                    )
                }
            }
        }
    }

    companion object {
        const val EXTRA_PRODUCT_ID = "EXTRA_PRODUCT_ID"
    }
}

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun AddProductScreen(
    modifier: Modifier = Modifier,
    onSaveProduct: (Product) -> Unit
) {
    var name by remember { mutableStateOf("") }
    var priceText by remember { mutableStateOf("") }
    var quantityText by remember { mutableStateOf("") }
    var category by remember { mutableStateOf("Điện tử") }
    var isSelling by remember { mutableStateOf(true) }
    var description by remember { mutableStateOf("") }

    // Lỗi hiển thị dưới từng ô nhập
    var nameError by remember { mutableStateOf<String?>(null) }
    var priceError by remember { mutableStateOf<String?>(null) }
    var quantityError by remember { mutableStateOf<String?>(null) }

    val categories = listOf("Điện tử", "Văn phòng phẩm", "Gia dụng", "Thời trang", "Khác")
    var dropdownExpanded by remember { mutableStateOf(false) }

    val context = LocalContext.current

    fun validate(): Boolean {
        var isValid = true

        if (name.isBlank()) {
            nameError = "Vui lòng nhập tên sản phẩm"
            isValid = false
        } else {
            nameError = null
        }

        val price = priceText.trim().toDoubleOrNull()
        when {
            priceText.isBlank() -> {
                priceError = "Vui lòng nhập giá bán"
                isValid = false
            }
            price == null -> {
                priceError = "Giá bán không hợp lệ, chỉ nhập số"
                isValid = false
            }
            price.isNaN() || price.isInfinite() -> {
                priceError = "Giá bán không hợp lệ, chỉ nhập số"
                isValid = false
            }
            price <= 0.0 -> {
                priceError = "Giá bán phải lớn hơn 0"
                isValid = false
            }
            else -> priceError = null
        }

        val quantity = quantityText.trim().toIntOrNull()
        when {
            quantityText.isBlank() -> {
                quantityError = "Vui lòng nhập số lượng"
                isValid = false
            }
            quantity == null -> {
                quantityError = "Số lượng không hợp lệ, chỉ nhập số nguyên"
                isValid = false
            }
            quantity <= 0 -> {
                quantityError = "Số lượng không thể âm hoặc bằng 0"
                isValid = false
            }
            else -> quantityError = null
        }

        return isValid
    }

    Column(
        modifier = modifier
            .fillMaxSize()
            .background(SurfaceBackground)
            .verticalScroll(rememberScrollState())
            .padding(16.dp),
        verticalArrangement = Arrangement.spacedBy(16.dp)
    ) {
        // Tên sản phẩm
        Column {
            Text(text = "Tên sản phẩm", fontSize = 14.sp, fontWeight = FontWeight.Bold, color = TextDark)
            Spacer(modifier = Modifier.height(6.dp))
            OutlinedTextField(
                value = name,
                onValueChange = {
                    name = it
                    nameError = null
                },
                placeholder = { Text("Ví dụ: Tai nghe Bluetooth", color = TextGray) },
                singleLine = true,
                isError = nameError != null,
                supportingText = nameError?.let { { Text(it, color = RedBadgeText) } },
                modifier = Modifier.fillMaxWidth(),
                shape = RoundedCornerShape(10.dp)
            )
        }

        // Giá bán (VND)
        Column {
            Text(text = "Giá bán (VND)", fontSize = 14.sp, fontWeight = FontWeight.Bold, color = TextDark)
            Spacer(modifier = Modifier.height(6.dp))
            OutlinedTextField(
                value = priceText,
                onValueChange = {
                    priceText = it
                    priceError = null
                },
                placeholder = { Text("Chỉ nhập số, ví dụ: 250000", color = TextGray) },
                keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Number),
                singleLine = true,
                isError = priceError != null,
                supportingText = priceError?.let { { Text(it, color = RedBadgeText) } },
                modifier = Modifier.fillMaxWidth(),
                shape = RoundedCornerShape(10.dp)
            )
        }

        // Số lượng
        Column {
            Text(text = "Số lượng", fontSize = 14.sp, fontWeight = FontWeight.Bold, color = TextDark)
            Spacer(modifier = Modifier.height(6.dp))
            OutlinedTextField(
                value = quantityText,
                onValueChange = {
                    quantityText = it
                    quantityError = null
                },
                placeholder = { Text("Chỉ nhập số nguyên, ví dụ: 10", color = TextGray) },
                keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Number),
                singleLine = true,
                isError = quantityError != null,
                supportingText = quantityError?.let { { Text(it, color = RedBadgeText) } },
                modifier = Modifier.fillMaxWidth(),
                shape = RoundedCornerShape(10.dp)
            )
        }

        // Loại sản phẩm
        Column {
            Text(text = "Loại sản phẩm", fontSize = 14.sp, fontWeight = FontWeight.Bold, color = TextDark)
            Spacer(modifier = Modifier.height(6.dp))
            ExposedDropdownMenuBox(
                expanded = dropdownExpanded,
                onExpandedChange = { dropdownExpanded = !dropdownExpanded }
            ) {
                OutlinedTextField(
                    value = category,
                    onValueChange = {},
                    readOnly = true,
                    trailingIcon = {
                        Icon(
                            imageVector = ArrowDropDownIcon,
                            contentDescription = "Dropdown"
                        )
                    },
                    modifier = Modifier
                        .fillMaxWidth()
                        .menuAnchor(ExposedDropdownMenuAnchorType.PrimaryNotEditable),
                    shape = RoundedCornerShape(10.dp)
                )

                ExposedDropdownMenu(
                    expanded = dropdownExpanded,
                    onDismissRequest = { dropdownExpanded = false }
                ) {
                    categories.forEach { item ->
                        DropdownMenuItem(
                            text = { Text(item) },
                            onClick = {
                                category = item
                                dropdownExpanded = false
                            }
                        )
                    }
                }
            }
        }

        // Đang kinh doanh Switch
        Row(
            modifier = Modifier
                .fillMaxWidth()
                .padding(vertical = 4.dp),
            horizontalArrangement = Arrangement.SpaceBetween,
            verticalAlignment = Alignment.CenterVertically
        ) {
            Text(text = "Đang kinh doanh", fontSize = 14.sp, fontWeight = FontWeight.Bold, color = TextDark)
            Switch(
                checked = isSelling,
                onCheckedChange = { isSelling = it },
                colors = SwitchDefaults.colors(
                    checkedThumbColor = Color.White,
                    checkedTrackColor = BluePrimary
                )
            )
        }

        // Mô tả
        Column {
            Text(text = "Mô tả", fontSize = 14.sp, fontWeight = FontWeight.Bold, color = TextDark)
            Spacer(modifier = Modifier.height(6.dp))
            OutlinedTextField(
                value = description,
                onValueChange = { description = it },
                placeholder = { Text("Nhập mô tả (nhiều dòng)...", color = TextGray) },
                modifier = Modifier
                    .fillMaxWidth()
                    .height(110.dp),
                shape = RoundedCornerShape(10.dp)
            )
        }

        Spacer(modifier = Modifier.height(8.dp))

        // Button Lưu sản phẩm
        Button(
            onClick = {
                if (!validate()) {
                    Toast.makeText(
                        context,
                        "Vui lòng nhập đầy đủ và đúng thông tin!",
                        Toast.LENGTH_SHORT
                    ).show()
                    return@Button
                }

                val newProduct = Product(
                    name = name.trim(),
                    price = priceText.trim().toDouble(),
                    quantity = quantityText.trim().toInt(),
                    category = category,
                    isSelling = isSelling,
                    description = description.trim()
                )
                onSaveProduct(newProduct)
            },
            modifier = Modifier
                .fillMaxWidth()
                .height(50.dp),
            shape = RoundedCornerShape(12.dp),
            colors = ButtonDefaults.buttonColors(containerColor = BluePrimary)
        ) {
            Text(
                text = "Lưu sản phẩm",
                fontSize = 16.sp,
                fontWeight = FontWeight.Bold,
                color = Color.White
            )
        }
    }
}
