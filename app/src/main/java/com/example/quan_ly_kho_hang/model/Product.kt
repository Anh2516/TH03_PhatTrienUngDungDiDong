package com.example.quan_ly_kho_hang.model

data class Product(
    val id: Int = 0,
    val name: String,
    val price: Double,
    val quantity: Int,
    val category: String,
    val isSelling: Boolean = true,
    val description: String = ""
)
