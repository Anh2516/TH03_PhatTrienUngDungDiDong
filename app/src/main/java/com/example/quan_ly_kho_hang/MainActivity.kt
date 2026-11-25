package com.example.quan_ly_kho_hang

import android.content.Intent
import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.activity.result.contract.ActivityResultContracts
import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.example.quan_ly_kho_hang.database.DatabaseHelper
import com.example.quan_ly_kho_hang.model.Product
import com.example.quan_ly_kho_hang.ui.theme.*
import com.example.quan_ly_kho_hang.utils.formatVND

class MainActivity : ComponentActivity() {
    private lateinit var dbHelper: DatabaseHelper
    private val productsState = mutableStateOf<List<Product>>(emptyList())

    // Id sản phẩm vừa được thêm, dùng để highlight sau khi quay lại danh sách
    private val highlightProductId = mutableStateOf<Int?>(null)

    private val addProductLauncher = registerForActivityResult(
        ActivityResultContracts.StartActivityForResult()
    ) { result ->
        if (result.resultCode == RESULT_OK) {
            val newId = result.data?.getIntExtra(AddProductActivity.EXTRA_PRODUCT_ID, -1) ?: -1
            if (newId != -1) {
                highlightProductId.value = newId
            }
            // Nạp lại danh sách + thống  kê
            loadProducts()
        }
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        dbHelper = DatabaseHelper(this)
        enableEdgeToEdge()

        setContent {
            QuanLyKhoHangTheme {
                val products by productsState
                val highlightId by highlightProductId
                Scaffold(
                    modifier = Modifier.fillMaxSize(),
                    topBar = {
                        Box(
                            modifier = Modifier
                                .fillMaxWidth()
                                .background(BluePrimaryDark)
                                .statusBarsPadding()
                                .padding(vertical = 16.dp, horizontal = 20.dp)
                        ) {
                            Text(
                                text = "Kho hàng của tôi",
                                color = Color.White,
                                fontSize = 20.sp,
                                fontWeight = FontWeight.Bold
                            )
                        }
                    },
                    bottomBar = {
                        Surface(
                            modifier = Modifier.fillMaxWidth(),
                            shadowElevation = 8.dp
                        ) {
                            Column(
                                modifier = Modifier
                                    .fillMaxWidth()
                                    .navigationBarsPadding()
                                    .padding(16.dp),
                                horizontalAlignment = Alignment.CenterHorizontally
                            ) {
                                Text(
                                    text = "(nhấn vào một sản phẩm để xem chi tiết)",
                                    fontSize = 12.sp,
                                    color = TextGray,
                                    textAlign = TextAlign.Center
                                )
                                Spacer(modifier = Modifier.height(8.dp))
                                Button(
                                    onClick = {
                                        val intent = Intent(this@MainActivity, AddProductActivity::class.java)
                                        addProductLauncher.launch(intent)
                                    },
                                    modifier = Modifier
                                        .fillMaxWidth()
                                        .height(48.dp),
                                    shape = RoundedCornerShape(12.dp),
                                    colors = ButtonDefaults.buttonColors(containerColor = BluePrimary)
                                ) {
                                    Text(
                                        text = "+ Thêm sản phẩm",
                                        fontSize = 16.sp,
                                        fontWeight = FontWeight.Bold,
                                        color = Color.White
                                    )
                                }
                            }
                        }
                    }
                ) { innerPadding ->
                    MainScreenContent(
                        products = products,
                        highlightProductId = highlightId,
                        modifier = Modifier.padding(innerPadding),
                        onProductClick = { product ->
                            val intent = Intent(this@MainActivity, ProductDetailActivity::class.java).apply {
                                putExtra("PRODUCT_ID", product.id)
                            }
                            startActivity(intent)
                        }
                    )
                }
            }
        }
    }

    override fun onResume() {
        super.onResume()
        loadProducts()
    }

    private fun loadProducts() {
        productsState.value = dbHelper.getAllProducts()
    }
}

@Composable
fun MainScreenContent(
    products: List<Product>,
    modifier: Modifier = Modifier,
    highlightProductId: Int? = null,
    onProductClick: (Product) -> Unit
) {
    val totalProducts = products.size
    val totalValue = products.sumOf { it.price * it.quantity }
    val lowStockCount = products.count { it.quantity in 1..5 }
    val outOfStockCount = products.count { it.quantity == 0 }

    Column(
        modifier = modifier
            .fillMaxSize()
            .background(SurfaceBackground)
            .padding(horizontal = 16.dp)
    ) {
        Spacer(modifier = Modifier.height(12.dp))

        // Inventory Statistics Card
        Card(
            modifier = Modifier.fillMaxWidth(),
            shape = RoundedCornerShape(16.dp),
            colors = CardDefaults.cardColors(containerColor = BlueLightContainer)
        ) {
            Column(modifier = Modifier.padding(16.dp)) {
                Text(
                    text = "Thống kê kho",
                    fontSize = 14.sp,
                    fontWeight = FontWeight.Bold,
                    color = BluePrimaryDark
                )
                Spacer(modifier = Modifier.height(12.dp))
                Row(
                    modifier = Modifier.fillMaxWidth(),
                    horizontalArrangement = Arrangement.SpaceBetween,
                    verticalAlignment = Alignment.CenterVertically
                ) {
                    // Total Products
                    Column(
                        horizontalAlignment = Alignment.Start,
                        modifier = Modifier.weight(1f)
                    ) {
                        Text(
                            text = "$totalProducts",
                            fontSize = 22.sp,
                            fontWeight = FontWeight.Bold,
                            color = BluePrimaryDark
                        )
                        Text(
                            text = "Sản phẩm",
                            fontSize = 12.sp,
                            color = TextGray
                        )
                    }

                    // Total Value
                    Column(
                        horizontalAlignment = Alignment.Start,
                        modifier = Modifier.weight(1.5f)
                    ) {
                        Text(
                            text = formatVND(totalValue),
                            fontSize = 18.sp,
                            fontWeight = FontWeight.Bold,
                            color = BluePrimaryDark
                        )
                        Text(
                            text = "Giá trị kho",
                            fontSize = 12.sp,
                            color = TextGray
                        )
                    }
                }

                Spacer(modifier = Modifier.height(12.dp))
                HorizontalDivider(color = Color(0xFFBBDEFB))
                Spacer(modifier = Modifier.height(12.dp))

                Row(
                    modifier = Modifier.fillMaxWidth(),
                    horizontalArrangement = Arrangement.SpaceBetween,
                    verticalAlignment = Alignment.CenterVertically
                ) {
                    // Low Stock - nằm dưới "Sản phẩm"
                    Column(
                        horizontalAlignment = Alignment.Start,
                        modifier = Modifier.weight(1f)
                    ) {
                        Text(
                            text = "$lowStockCount",
                            fontSize = 18.sp,
                            fontWeight = FontWeight.Bold,
                            color = OrangeSell
                        )
                        Text(
                            text = "Sắp hết hàng",
                            fontSize = 12.sp,
                            color = TextGray
                        )
                    }

                    // Out of Stock - nằm dưới "Giá trị kho"
                    Column(
                        horizontalAlignment = Alignment.Start,
                        modifier = Modifier.weight(1.5f)
                    ) {
                        Text(
                            text = "$outOfStockCount",
                            fontSize = 18.sp,
                            fontWeight = FontWeight.Bold,
                            color = RedBadgeText
                        )
                        Text(
                            text = "Hết hàng",
                            fontSize = 12.sp,
                            color = TextGray
                        )
                    }
                }
            }
        }

        Spacer(modifier = Modifier.height(16.dp))

        Text(
            text = "Danh sách sản phẩm",
            fontSize = 16.sp,
            fontWeight = FontWeight.Bold,
            color = Color(0xFF212121)
        )

        Spacer(modifier = Modifier.height(8.dp))

        if (products.isEmpty()) {
            Box(
                modifier = Modifier
                    .fillMaxWidth()
                    .weight(1f),
                contentAlignment = Alignment.Center
            ) {
                Text(
                    text = "Chưa có sản phẩm nào trong kho",
                    color = TextGray,
                    fontSize = 14.sp
                )
            }
        } else {
            LazyColumn(
                modifier = Modifier.weight(1f),
                verticalArrangement = Arrangement.spacedBy(10.dp),
                contentPadding = PaddingValues(bottom = 8.dp)
            ) {
                items(products) { product ->
                    ProductListItem(
                        product = product,
                        isHighlighted = product.id == highlightProductId,
                        onClick = { onProductClick(product) }
                    )
                }
            }
        }
    }
}

@Composable
fun ProductListItem(
    product: Product,
    onClick: () -> Unit,
    isHighlighted: Boolean = false
) {
    Card(
        modifier = Modifier
            .fillMaxWidth()
            .clickable { onClick() },
        shape = RoundedCornerShape(12.dp),
        colors = CardDefaults.cardColors(
            containerColor = if (isHighlighted) BlueLightContainer else Color.White
        ),
        border = if (isHighlighted) {
            androidx.compose.foundation.BorderStroke(1.5.dp, BluePrimary)
        } else {
            null
        },
        elevation = CardDefaults.cardElevation(defaultElevation = if (isHighlighted) 6.dp else 2.dp)
    ) {
        Column(modifier = Modifier.padding(14.dp)) {
            Row(
                modifier = Modifier.fillMaxWidth(),
                horizontalArrangement = Arrangement.SpaceBetween,
                verticalAlignment = Alignment.CenterVertically
            ) {
                Text(
                    text = product.name,
                    fontSize = 16.sp,
                    fontWeight = FontWeight.Bold,
                    color = Color(0xFF212121)
                )
                Text(
                    text = "SL: ${product.quantity}",
                    fontSize = 14.sp,
                    fontWeight = FontWeight.Bold,
                    color = if (product.quantity == 0) RedBadgeText else Color(0xFF333333)
                )
            }

            Spacer(modifier = Modifier.height(4.dp))

            Text(
                text = "Giá bán: ${formatVND(product.price)}",
                fontSize = 13.sp,
                color = TextGray
            )

            Spacer(modifier = Modifier.height(8.dp))

            Row(
                horizontalArrangement = Arrangement.spacedBy(8.dp),
                verticalAlignment = Alignment.CenterVertically
            ) {
                // Category Chip
                Box(
                    modifier = Modifier
                        .clip(RoundedCornerShape(6.dp))
                        .background(BlueLightContainer)
                        .padding(horizontal = 8.dp, vertical = 4.dp)
                ) {
                    Text(
                        text = product.category,
                        fontSize = 12.sp,
                        fontWeight = FontWeight.Medium,
                        color = BluePrimaryDark
                    )
                }

                // Out of Stock Chip if quantity == 0
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
                }
                // Low Stock Chip if 1 <= quantity <= 5
                else if (product.quantity <= 5) {
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
        }
    }
}
