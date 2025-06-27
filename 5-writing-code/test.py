def add_numbers(a: float, b: float) -> float:

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers (int or float).")
    return a + b