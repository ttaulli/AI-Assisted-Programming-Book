from typing import Union

def add_numbers(a: Union[int, float], b: Union[int, float]) -> float:
    """
    Adds two numbers and returns the result.

    Args:
        a (int | float): The first number.
        b (int | float): The second number.

    Returns:
        float: The sum of a and b.

    Raises:
        TypeError: If a or b is not a number.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be int or float.")
    return float(a + b)