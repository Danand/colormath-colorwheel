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

