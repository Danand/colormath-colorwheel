def normalize_saturation(saturation: float) -> float:
    if saturation == 1:
        return saturation
    else:
        return saturation % 1
