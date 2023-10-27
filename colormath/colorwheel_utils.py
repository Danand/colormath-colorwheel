from colormath.color_objects import HSLColor

def normalize_saturation(saturation: float) -> float:
    if saturation == 1:
        return saturation
    else:
        return saturation % 1

def rotate_color(
        color: HSLColor,
        diff_hue: float,
        diff_saturation: float,
        diff_lightness: float,
    ) -> HSLColor:
    new_hue = color.hsl_h + diff_hue
    new_saturation = normalize_saturation(color.hsl_s + diff_saturation)
    new_lightness = max(0, min(1, color.hsl_l + diff_lightness))

    color_rotated = HSLColor(new_hue, new_saturation, new_lightness)

    return color_rotated

def colors_equal(color_left: HSLColor, color_right: HSLColor) -> bool:
    return abs(color_left.hsl_h - color_right.hsl_h) < 0.01 and \
           abs(color_left.hsl_s - color_right.hsl_s) < 0.01 and \
           abs(color_left.hsl_l - color_right.hsl_l) < 0.01
