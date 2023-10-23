# `colormath-colorwheel`

Extension for [`python-colormath`](https://github.com/gtaylor/python-colormath) implementing calculation of custom color wheel with HSL rotation.

## Installation

```bash
pip install git+https://github.com/Danand/colormath-colorwheel.git
```

## Usage

```python
wheel = Wheel(colors_original)
colors_rotated = wheel.rotate_from_to(color_from, color_to)
```
