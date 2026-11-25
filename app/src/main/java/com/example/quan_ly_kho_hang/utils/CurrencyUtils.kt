package com.example.quan_ly_kho_hang.utils

import java.text.DecimalFormat
import java.text.DecimalFormatSymbols

fun formatVND(amount: Double): String {
    val formatter = DecimalFormat("#,###")
    val symbols = DecimalFormatSymbols().apply {
        groupingSeparator = '.'
    }
    formatter.decimalFormatSymbols = symbols
    return "${formatter.format(amount)} đ"
}
