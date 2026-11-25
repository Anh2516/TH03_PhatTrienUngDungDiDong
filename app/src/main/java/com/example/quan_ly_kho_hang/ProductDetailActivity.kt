package com.example.quan_ly_kho_hang

import android.os.Bundle
import android.widget.Toast
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.foundation.verticalScroll
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.example.quan_ly_kho_hang.database.DatabaseHelper
import com.example.quan_ly_kho_hang.model.Product
import com.example.quan_ly_kho_hang.ui.theme.*
import com.example.quan_ly_kho_hang.utils.formatVND

class ProductDetailActivity : ComponentActivity() {
    private lateinit var dbHelper: DatabaseHelper
    private val productState = mutableStateOf<Product?>(null)

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        dbHelper = DatabaseHelper(this)
        val productId = intent.getIntExtra("PRODUCT_ID", -1)

        enableEdgeToEdge()

        setContent {
            QuanLyKhoHangTheme {
                val product by productState

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
                                text = "Chi tiết sản phẩm",
                                color = Color.White,
                                fontSize = 18.sp,
                                fontWeight = FontWeight.Bold
                            )
                        }
                    }
                ) { innerPadding ->
                    if (product != null) {
                        ProductDetailContent(
                            product = product!!,
                            modifier = Modifier.padding(innerPadding),
                            onAddStock = {
                                dbHelper.updateQuantity(product!!.id, 1)
                                loadProduct(productId)
                            },
                            onSellOne = {
                                if (product!!.quantity > 0) {
                                    dbHelper.updateQuantity(product!!.id, -1)
                                    loadProduct(productId)
                                } else {
                                    Toast.makeText(this, "Số lượng đã bằng 0!", Toast.LENGTH_SHORT).show()
                                }
                            },
                            onBack = { finish() },
                            onDelete = {
                                dbHelper.deleteProduct(product!!.id)
                                Toast.makeText(this, "Đã xóa sản phẩm!", Toast.LENGTH_SHORT).show()
                                finish()
                            }
                        )
                    } else {
                        Box(
                            modifier = Modifier
                                .fillMaxSize()
                                .padding(innerPadding),
                            contentAlignment = Alignment.Center
                        ) {
                            Text("Không tìm thấy sản phẩm", color = TextGray)
                        }
                    }
                }
            }
        }
    }

    override fun onResume() {
        super.onResume()
        val productId = intent.getIntExtra("PRODUCT_ID", -1)
        loadProduct(productId)
    }

    private fun loadProduct(productId: Int) {
        if (productId != -1) {
            productState.value = dbHelper.getProductById(productId)
        }
    }
}

@Composable
fun ProductDetailContent(
    product: Product,
    modifier: Modifier = Modifier,
    onAddStock: () -> Unit,
    onSellOne: () -> Unit,
    onBack: () -> Unit,
    onDelete: () -> Unit
) {
    val totalValue = product.price * product.quantity

    Column(
        modifier = modifier
            .fillMaxSize()
            .background(SurfaceBackground)
            .verticalScroll(rememberScrollState())
            .padding(16.dp),
        verticalArrangement = Arrangement.spacedBy(16.dp)
    ) {
        // Product Name & Category
        Column {
            Text(
                text = product.name,
                fontSize = 24.sp,
                fontWeight = FontWeight.Bold,
                color = Color(0xFF212121)
            )
            Spacer(modifier = Modifier.height(6.dp))
            Box(
                modifier = Modifier
                    .clip(RoundedCornerShape(6.dp))
                    .background(BlueLightContainer)
                    .padding(horizontal = 10.dp, vertical = 4.dp)
            ) {
                Text(
                    text = product.category,
                    fontSize = 12.sp,
                    fontWeight = FontWeight.Medium,
                    color = BluePrimaryDark
                )
            }
        }

        // Price formatted in Red/Orange
        Text(
            text = formatVND(product.price),
            fontSize = 22.sp,
            fontWeight = FontWeight.Bold,
            color = RedBadgeText
        )

        // Cảnh báo hết hàng
        if (product.quantity == 0) {
            Box(
                modifier = Modifier
                    .fillMaxWidth()
                    .clip(RoundedCornerShape(8.dp))
                    .background(RedBadgeBg)
                    .padding(horizontal = 12.dp, vertical = 10.dp)
            ) {
                Text(
                    text = "Sản phẩm này đã HẾT HÀNG. Hãy nhấn \"+ Nhập thêm 1\" để bổ sung tồn kho.",
                    fontSize = 13.sp,
                    fontWeight = FontWeight.Medium,
                    color = RedBadgeText
                )
            }
        }

        // Inventory Detail Stats Card
        Card(
            modifier = Modifier.fillMaxWidth(),
            shape = RoundedCornerShape(12.dp),
            colors = CardDefaults.cardColors(containerColor = Color.White),
            elevation = CardDefaults.cardElevation(defaultElevation = 2.dp)
        ) {
            Column(modifier = Modifier.padding(16.dp)) {
                // Stock quantity & low stock badge
                Row(
                    modifier = Modifier.fillMaxWidth(),
                    horizontalArrangement = Arrangement.SpaceBetween,
                    verticalAlignment = Alignment.CenterVertically
                ) {
                    Row(verticalAlignment = Alignment.CenterVertically) {
                        Text(
                            text = "Số lượng tồn kho",
                            fontSize = 14.sp,
                            color = TextGray
                        )
                        Spacer(modifier = Modifier.width(16.dp))
                        Text(
                            text = "${product.quantity}",
                            fontSize = 18.sp,
                            fontWeight = FontWeight.Bold,
                            color = if (product.quantity == 0) RedBadgeText else Color(0xFF212121)
                        )
                    }

                    if (product.quantity == 0) {
                        Box(
                            modifier = Modifier
                                .clip(RoundedCornerShape(6.dp))
                                .background(RedBadgeBg)
                                .padding(horizontal = 8.dp, vertical = 4.dp)
                        ) {
                            Text(
                                text = "Hết hàng",
                                fontSize = 12.sp,
                                fontWeight = FontWeight.Medium,
                                color = RedBadgeText
                            )
                        }
                    } else if (product.quantity <= 5) {
                        Box(
                            modifier = Modifier
                                .clip(RoundedCornerShape(6.dp))
                                .background(OrangeSellBg)
                                .padding(horizontal = 8.dp, vertical = 4.dp)
                        ) {
                            Text(
                                text = "Sắp hết hàng",
                                fontSize = 12.sp,
                                fontWeight = FontWeight.Medium,
                                color = OrangeSell
                            )
                        }
                    }
                }

                Spacer(modifier = Modifier.height(12.dp))
                HorizontalDivider(color = Color(0xFFEEEEEE))
                Spacer(modifier = Modifier.height(12.dp))

                // Inventory Total Value
                Row(
                    modifier = Modifier.fillMaxWidth(),
                    horizontalArrangement = Arrangement.SpaceBetween,
                    verticalAlignment = Alignment.CenterVertically
                ) {
                    Text(
                        text = "Giá trị tồn kho",
                        fontSize = 14.sp,
                        color = TextGray
                    )
                    Text(
                        text = formatVND(totalValue),
                        fontSize = 16.sp,
                        fontWeight = FontWeight.Bold,
                        color = Color(0xFF212121)
                    )
                }
            }
        }

        // Description Card
        Card(
            modifier = Modifier.fillMaxWidth(),
            shape = RoundedCornerShape(12.dp),
            colors = CardDefaults.cardColors(containerColor = Color.White),
            elevation = CardDefaults.cardElevation(defaultElevation = 2.dp)
        ) {
            Column(modifier = Modifier.padding(16.dp)) {
                Text(
                    text = "Mô tả",
                    fontSize = 14.sp,
                    fontWeight = FontWeight.Bold,
                    color = Color(0xFF212121)
                )
                Spacer(modifier = Modifier.height(8.dp))
                Text(
                    text = product.description.ifBlank { "Không có mô tả" },
                    fontSize = 14.sp,
                    color = Color(0xFF424242)
                )
            }
        }

        Spacer(modifier = Modifier.height(8.dp))

        // Action Buttons Row: + Nhập thêm 1 | - Bán 1
        Row(
            modifier = Modifier.fillMaxWidth(),
            horizontalArrangement = Arrangement.spacedBy(12.dp)
        ) {
            Button(
                onClick = onAddStock,
                modifier = Modifier
                    .weight(1f)
                    .height(48.dp),
                shape = RoundedCornerShape(10.dp),
                colors = ButtonDefaults.buttonColors(containerColor = BluePrimary)
            ) {
                Text(
                    text = "+ Nhập thêm 1",
                    fontSize = 14.sp,
                    fontWeight = FontWeight.Bold,
                    color = Color.White
                )
            }

            Button(
                onClick = onSellOne,
                enabled = product.quantity > 0,
                modifier = Modifier
                    .weight(1f)
                    .height(48.dp),
                shape = RoundedCornerShape(10.dp),
                colors = ButtonDefaults.buttonColors(
                    containerColor = OrangeSell,
                    disabledContainerColor = OrangeSellBg,
                    disabledContentColor = TextGray
                )
            ) {
                Text(
                    text = "- Bán 1",
                    fontSize = 14.sp,
                    fontWeight = FontWeight.Bold,
                    color = Color.White
                )
            }
        }

        // Button Quay lại
        OutlinedButton(
            onClick = onBack,
            modifier = Modifier
                .fillMaxWidth()
                .height(48.dp),
            shape = RoundedCornerShape(10.dp),
            colors = ButtonDefaults.outlinedButtonColors(contentColor = BluePrimary)
        ) {
            Text(
                text = "Quay lại",
                fontSize = 15.sp,
                fontWeight = FontWeight.Bold
            )
        }

        // Button Xóa sản phẩm
        Button(
            onClick = onDelete,
            modifier = Modifier
                .fillMaxWidth()
                .height(48.dp),
            shape = RoundedCornerShape(10.dp),
            colors = ButtonDefaults.buttonColors(containerColor = RedDelete)
        ) {
            Text(
                text = "Xóa sản phẩm",
                fontSize = 15.sp,
                fontWeight = FontWeight.Bold,
                color = Color.White
            )
        }
    }
}
