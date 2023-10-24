from sys import stderr

from typing import List

from colormath.color_objects import sRGBColor, HSLColor
from colormath.color_conversions import convert_color

from .colorwheel_utils import parse_rgb_from_hex, normalize_saturation

class Wheel:
    def __init__(self, hex_colors: List[str]):
        self.rgb_colors = [parse_rgb_from_hex(hex_color) for hex_color in hex_colors]

    def rotate_from_to(self, hex_color_from: str, hex_color_to: str) -> List[str]:
        rgb_color_from = sRGBColor.new_from_rgb_hex(hex_color_from)
        hsl_color_from: HSLColor = convert_color(rgb_color_from, HSLColor)

        rgb_color_to = sRGBColor.new_from_rgb_hex(hex_color_to)
        hsl_color_to: HSLColor = convert_color(rgb_color_to, HSLColor)

        diff_hue = hsl_color_to.hsl_h - hsl_color_from.hsl_h
        diff_saturation = hsl_color_to.hsl_s - hsl_color_from.hsl_s
        diff_lightness = hsl_color_to.hsl_l - hsl_color_from.hsl_l

        hex_colors: List[str] = []

        for rgb_color in self.rgb_colors:
            if not isinstance(rgb_color, sRGBColor):
                hex_colors.append(rgb_color)
                print(f"warning: `{rgb_color}` is not color, bypassing it on rotation", file=stderr)
                continue

            hsl_color: HSLColor = convert_color(rgb_color, HSLColor)

            new_hue = hsl_color.hsl_h + diff_hue
            new_saturation= normalize_saturation(hsl_color.hsl_s + diff_saturation)
            new_lightness = max(0, min(1, hsl_color.hsl_l + diff_lightness))

            hsl_color_rotated = HSLColor(new_hue, new_saturation, new_lightness)
            rgb_color_rotated: sRGBColor = convert_color(hsl_color_rotated, sRGBColor)

            hex_colors.append(rgb_color_rotated.get_rgb_hex())

        return hex_colors
