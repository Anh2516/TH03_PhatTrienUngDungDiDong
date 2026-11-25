package com.example.quan_ly_kho_hang.database

import android.content.ContentValues
import android.content.Context
import android.database.sqlite.SQLiteDatabase
import android.database.sqlite.SQLiteOpenHelper
import com.example.quan_ly_kho_hang.model.Product

class DatabaseHelper(context: Context) : SQLiteOpenHelper(context, DATABASE_NAME, null, DATABASE_VERSION) {

    companion object {
        private const val DATABASE_NAME = "quan_ly_kho_hang.db"
        private const val DATABASE_VERSION = 1

        const val TABLE_PRODUCTS = "products"
        const val COLUMN_ID = "id"
        const val COLUMN_NAME = "name"
        const val COLUMN_PRICE = "price"
        const val COLUMN_QUANTITY = "quantity"
        const val COLUMN_CATEGORY = "category"
        const val COLUMN_IS_SELLING = "is_selling"
        const val COLUMN_DESCRIPTION = "description"
    }

    override fun onCreate(db: SQLiteDatabase) {
        val createTableQuery = """
            CREATE TABLE $TABLE_PRODUCTS (
                $COLUMN_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                $COLUMN_NAME TEXT NOT NULL,
                $COLUMN_PRICE REAL NOT NULL,
                $COLUMN_QUANTITY INTEGER NOT NULL,
                $COLUMN_CATEGORY TEXT NOT NULL,
                $COLUMN_IS_SELLING INTEGER NOT NULL DEFAULT 1,
                $COLUMN_DESCRIPTION TEXT
            )
        """.trimIndent()
        db.execSQL(createTableQuery)

        // Seed initial sample data matching the specification/screenshot
        seedSampleData(db)
    }

    override fun onUpgrade(db: SQLiteDatabase, oldVersion: Int, newVersion: Int) {
        db.execSQL("DROP TABLE IF EXISTS $TABLE_PRODUCTS")
        onCreate(db)
    }

    private fun seedSampleData(db: SQLiteDatabase) {
        val sampleProducts = listOf(
            Product(
                name = "Chuột không dây",
                price = 150000.0,
                quantity = 20,
                category = "Điện tử",
                isSelling = true,
                description = "Chuột không dây 2.4GHz kết nối nhanh"
            ),
            Product(
                name = "Bàn phím cơ",
                price = 450000.0,
                quantity = 3,
                category = "Điện tử",
                isSelling = true,
                description = "Bàn phím cơ switch xanh, có đèn nền"
            ),
            Product(
                name = "Sổ tay A5",
                price = 25000.0,
                quantity = 40,
                category = "Văn phòng phẩm",
                isSelling = true,
                description = "Sổ tay bìa da A5, 200 trang"
            )
        )

        for (product in sampleProducts) {
            val values = ContentValues().apply {
                put(COLUMN_NAME, product.name)
                put(COLUMN_PRICE, product.price)
                put(COLUMN_QUANTITY, product.quantity)
                put(COLUMN_CATEGORY, product.category)
                put(COLUMN_IS_SELLING, if (product.isSelling) 1 else 0)
                put(COLUMN_DESCRIPTION, product.description)
            }
            db.insert(TABLE_PRODUCTS, null, values)
        }
    }

    fun getAllProducts(): List<Product> {
        val productList = mutableListOf<Product>()
        val db = readableDatabase
        val cursor = db.query(
            TABLE_PRODUCTS,
            null, null, null, null, null,
            "$COLUMN_ID DESC"
        )

        cursor.use { c ->
            val idIndex = c.getColumnIndexOrThrow(COLUMN_ID)
            val nameIndex = c.getColumnIndexOrThrow(COLUMN_NAME)
            val priceIndex = c.getColumnIndexOrThrow(COLUMN_PRICE)
            val quantityIndex = c.getColumnIndexOrThrow(COLUMN_QUANTITY)
            val categoryIndex = c.getColumnIndexOrThrow(COLUMN_CATEGORY)
            val isSellingIndex = c.getColumnIndexOrThrow(COLUMN_IS_SELLING)
            val descIndex = c.getColumnIndexOrThrow(COLUMN_DESCRIPTION)

            while (c.moveToNext()) {
                val product = Product(
                    id = c.getInt(idIndex),
                    name = c.getString(nameIndex),
                    price = c.getDouble(priceIndex),
                    quantity = c.getInt(quantityIndex),
                    category = c.getString(categoryIndex),
                    isSelling = c.getInt(isSellingIndex) == 1,
                    description = c.getString(descIndex) ?: ""
                )
                productList.add(product)
            }
        }
        return productList
    }

    fun getProductById(id: Int): Product? {
        val db = readableDatabase
        val cursor = db.query(
            TABLE_PRODUCTS,
            null,
            "$COLUMN_ID = ?",
            arrayOf(id.toString()),
            null, null, null
        )

        cursor.use { c ->
            if (c.moveToFirst()) {
                val idIndex = c.getColumnIndexOrThrow(COLUMN_ID)
                val nameIndex = c.getColumnIndexOrThrow(COLUMN_NAME)
                val priceIndex = c.getColumnIndexOrThrow(COLUMN_PRICE)
                val quantityIndex = c.getColumnIndexOrThrow(COLUMN_QUANTITY)
                val categoryIndex = c.getColumnIndexOrThrow(COLUMN_CATEGORY)
                val isSellingIndex = c.getColumnIndexOrThrow(COLUMN_IS_SELLING)
                val descIndex = c.getColumnIndexOrThrow(COLUMN_DESCRIPTION)

                return Product(
                    id = c.getInt(idIndex),
                    name = c.getString(nameIndex),
                    price = c.getDouble(priceIndex),
                    quantity = c.getInt(quantityIndex),
                    category = c.getString(categoryIndex),
                    isSelling = c.getInt(isSellingIndex) == 1,
                    description = c.getString(descIndex) ?: ""
                )
            }
        }
        return null
    }

    fun insertProduct(product: Product): Long {
        val db = writableDatabase
        val values = ContentValues().apply {
            put(COLUMN_NAME, product.name)
            put(COLUMN_PRICE, product.price)
            put(COLUMN_QUANTITY, product.quantity)
            put(COLUMN_CATEGORY, product.category)
            put(COLUMN_IS_SELLING, if (product.isSelling) 1 else 0)
            put(COLUMN_DESCRIPTION, product.description)
        }
        return db.insert(TABLE_PRODUCTS, null, values)
    }

    fun updateProduct(product: Product): Boolean {
        val db = writableDatabase
        val values = ContentValues().apply {
            put(COLUMN_NAME, product.name)
            put(COLUMN_PRICE, product.price)
            put(COLUMN_QUANTITY, product.quantity)
            put(COLUMN_CATEGORY, product.category)
            put(COLUMN_IS_SELLING, if (product.isSelling) 1 else 0)
            put(COLUMN_DESCRIPTION, product.description)
        }
        val rows = db.update(TABLE_PRODUCTS, values, "$COLUMN_ID = ?", arrayOf(product.id.toString()))
        return rows > 0
    }

    fun updateQuantity(id: Int, delta: Int): Boolean {
        val product = getProductById(id) ?: return false
        val newQuantity = (product.quantity + delta).coerceAtLeast(0)
        val db = writableDatabase
        val values = ContentValues().apply {
            put(COLUMN_QUANTITY, newQuantity)
        }
        val rows = db.update(TABLE_PRODUCTS, values, "$COLUMN_ID = ?", arrayOf(id.toString()))
        return rows > 0
    }

    fun deleteProduct(id: Int): Boolean {
        val db = writableDatabase
        val rows = db.delete(TABLE_PRODUCTS, "$COLUMN_ID = ?", arrayOf(id.toString()))
        return rows > 0
    }
}
