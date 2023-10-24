from sys import stderr

from colormath.color_objects import sRGBColor

def normalize_saturation(saturation: float) -> float:
    if saturation == 1:
        return saturation
    else:
        return saturation % 1

def parse_rgb_from_hex(hex_color: str) -> sRGBColor | str:
    try:
        return sRGBColor.new_from_rgb_hex(hex_color)
    except:
        print(f"warning: Failed to parse `{hex_color}` as color", file=stderr)
        return hex_color
