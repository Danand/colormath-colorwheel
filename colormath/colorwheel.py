from typing import List

from colormath.color_objects import ColorBase, sRGBColor, HSLColor, LabColor
from colormath.color_conversions import convert_color

from .colorwheel_utils import rotate_color, colors_equal
from .colorwheel_utils_delta_e import calc_delta_e, find_color_nearest_by_delta_e

class Wheel:
    def __init__(self, colors: List[ColorBase]):
        self.colors = colors

    @staticmethod
    def create_from_hex(hex_colors: List[str]):
        colors: ColorBase = [sRGBColor.new_from_rgb_hex(hex_color) for hex_color in hex_colors]
        return Wheel(colors)

    def rotate_from_to_hex(self, hex_color_from: str, hex_color_to: str) -> List[str]:
        color_from: ColorBase = sRGBColor.new_from_rgb_hex(hex_color_from)
        color_to: ColorBase = sRGBColor.new_from_rgb_hex(hex_color_to)

        colors = self.rotate_from_to(color_from, color_to)

        rgb_colors: List[sRGBColor] = [convert_color(color, sRGBColor) for color in colors]

        return [rgb_color.get_rgb_hex() for rgb_color in rgb_colors]

    def rotate_from_to(self, color_from: ColorBase, color_to: ColorBase) -> List[ColorBase]:
        hsl_color_from: HSLColor = convert_color(color_from, HSLColor)
        hsl_color_to: HSLColor = convert_color(color_to, HSLColor)

        diff_hue = hsl_color_to.hsl_h - hsl_color_from.hsl_h
        diff_saturation = hsl_color_to.hsl_s - hsl_color_from.hsl_s
        diff_lightness = hsl_color_to.hsl_l - hsl_color_from.hsl_l

        hsl_colors: List[HSLColor] = [convert_color(color, HSLColor) for color in self.colors]

        colors_rotated: List[ColorBase] = []

        for hsl_color in hsl_colors:
            color_rotated = rotate_color(hsl_color, diff_hue, diff_saturation, diff_lightness)
            colors_rotated.append(color_rotated)

        return colors_rotated

    def rotate_readable_from_to_hex(
            self,
            hex_color_from: str,
            hex_color_to: str,
            hex_color_background: str,
            hex_color_accent: str,
        ) -> List[str]:
        color_from: ColorBase = sRGBColor.new_from_rgb_hex(hex_color_from)
        color_to: ColorBase = sRGBColor.new_from_rgb_hex(hex_color_to)
        color_background: ColorBase = sRGBColor.new_from_rgb_hex(hex_color_background)
        color_accent: ColorBase = sRGBColor.new_from_rgb_hex(hex_color_accent)

        colors = self.rotate_readable_from_to(
            color_from,
            color_to,
            color_background,
            color_accent,
        )

        rgb_colors: List[sRGBColor] = [convert_color(color, sRGBColor) for color in colors]

        return [rgb_color.get_rgb_hex() for rgb_color in rgb_colors]

    def rotate_readable_from_to(
            self,
            color_from: ColorBase,
            color_to: ColorBase,
            color_background: ColorBase,
            color_accent: ColorBase,
        )-> List[ColorBase]:
        hsl_color_from: HSLColor = convert_color(color_from, HSLColor)
        hsl_color_to: HSLColor = convert_color(color_to, HSLColor)
        hsl_color_background: HSLColor = convert_color(color_background, HSLColor)
        hsl_color_accent: HSLColor = convert_color(color_accent, HSLColor)

        diff_hue = hsl_color_to.hsl_h - hsl_color_from.hsl_h
        diff_saturation = hsl_color_to.hsl_s - hsl_color_from.hsl_s
        diff_lightness = hsl_color_to.hsl_l - hsl_color_from.hsl_l

        color_accent_rotated = rotate_color(hsl_color_accent, diff_hue, diff_saturation, diff_lightness)

        lab_color_background: LabColor = convert_color(color_background, LabColor)
        lab_color_accent: LabColor = convert_color(color_accent, LabColor)
        lab_color_accent_rotated: LabColor  = convert_color(color_accent_rotated, LabColor)

        delta_e_background = calc_delta_e(lab_color_accent, lab_color_background)

        color_background_corrected = find_color_nearest_by_delta_e(lab_color_accent_rotated, delta_e_background)

        hsl_colors: List[HSLColor] = [convert_color(color, HSLColor) for color in self.colors]

        colors_rotated: List[ColorBase] = []

        for hsl_color in hsl_colors:
            if colors_equal(hsl_color, hsl_color_background):
                colors_rotated.append(color_background_corrected)
            elif colors_equal(hsl_color, hsl_color_accent):
                colors_rotated.append(color_accent_rotated)
            else:
                # TODO: Correct with Delta E.
                color_rotated = rotate_color(hsl_color, diff_hue, diff_saturation, diff_lightness)
                colors_rotated.append(color_rotated)

        return colors_rotated
