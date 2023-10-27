from typing import List, Tuple

from colormath.color_objects import LabColor, sRGBColor
from colormath.color_conversions import convert_color

from colormath.color_diff import _get_lab_color1_vector, _get_lab_color2_matrix
from colormath.color_diff_matrix import delta_e_cie2000

def calc_delta_e(color_left: LabColor, color_right: LabColor) -> float:
    color_left_vector = _get_lab_color1_vector(color_left)
    color_right_matrix = _get_lab_color2_matrix(color_right)

    delta_e = delta_e_cie2000(color_left_vector, color_right_matrix, 1, 1, 1)[0]

    return delta_e.item()

def find_color_nearest_by_delta_e(color: LabColor, delta_e: float) -> sRGBColor:
    colors_to_delta_e_diff: List[Tuple[float, LabColor]] = []

    for color_lab_l in range(0, 10001):
        color_other = LabColor(color_lab_l / 100.0, color.lab_a, color.lab_b)
        delta_e_other = calc_delta_e(color, color_other)

        delta_e_diff = abs(delta_e_other - delta_e)

        colors_to_delta_e_diff.append((delta_e_diff, color_other))

    color_to_delta_e_diff_min = min(colors_to_delta_e_diff, key=lambda color_to_delta_e_diff: color_to_delta_e_diff[0])

    nearest_color_rgb: sRGBColor = convert_color(color_to_delta_e_diff_min[1], sRGBColor)

    return nearest_color_rgb
