package com.example.quan_ly_kho_hang.ui.theme

import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.PathFillType
import androidx.compose.ui.graphics.SolidColor
import androidx.compose.ui.graphics.vector.ImageVector
import androidx.compose.ui.graphics.vector.path
import androidx.compose.ui.unit.dp

val ArrowBackIcon: ImageVector
    get() {
        if (_arrowBackIcon != null) {
            return _arrowBackIcon!!
        }
        _arrowBackIcon = ImageVector.Builder(
            name = "ArrowBack",
            defaultWidth = 24.dp,
            defaultHeight = 24.dp,
            viewportWidth = 24f,
            viewportHeight = 24f
        ).apply {
            path(
                fill = SolidColor(Color.White),
                pathFillType = PathFillType.NonZero
            ) {
                moveTo(20.0f, 11.0f)
                lineTo(7.83f, 11.0f)
                lineTo(13.42f, 5.41f)
                lineTo(12.0f, 4.0f)
                lineTo(4.0f, 12.0f)
                lineTo(12.0f, 20.0f)
                lineTo(13.41f, 18.59f)
                lineTo(7.83f, 13.0f)
                lineTo(20.0f, 13.0f)
                close()
            }
        }.build()
        return _arrowBackIcon!!
    }

private var _arrowBackIcon: ImageVector? = null

val ArrowDropDownIcon: ImageVector
    get() {
        if (_arrowDropDownIcon != null) {
            return _arrowDropDownIcon!!
        }
        _arrowDropDownIcon = ImageVector.Builder(
            name = "ArrowDropDown",
            defaultWidth = 24.dp,
            defaultHeight = 24.dp,
            viewportWidth = 24f,
            viewportHeight = 24f
        ).apply {
            path(
                fill = SolidColor(Color(0xFF666666)),
                pathFillType = PathFillType.NonZero
            ) {
                moveTo(7.0f, 10.0f)
                lineTo(12.0f, 15.0f)
                lineTo(17.0f, 10.0f)
                close()
            }
        }.build()
        return _arrowDropDownIcon!!
    }

private var _arrowDropDownIcon: ImageVector? = null
