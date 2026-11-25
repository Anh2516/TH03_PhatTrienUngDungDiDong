package com.example.quan_ly_kho_hang.ui.theme

import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.lightColorScheme
import androidx.compose.runtime.Composable
import androidx.compose.ui.graphics.Color

private val LightColorScheme = lightColorScheme(
    primary = BluePrimary,
    onPrimary = Color.White,
    primaryContainer = BlueLightContainer,
    onPrimaryContainer = BluePrimaryDark,
    secondary = BlueSecondary,
    onSecondary = Color.White,
    background = SurfaceBackground,
    surface = Color.White
)

@Composable
fun QuanLyKhoHangTheme(
    content: @Composable () -> Unit
) {
    MaterialTheme(
        colorScheme = LightColorScheme,
        typography = Typography,
        content = content
    )
}
