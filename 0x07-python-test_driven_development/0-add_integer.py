#!/usr/bin/python3
"""A simple addition module"""


def add_integer(a, b=98):
    """Performs simple addition
    Args:
        a(int): The first parameter
        b(int): The second parameter

    Returns:
        int: the result of addition of the parameters

    Raises:
        TypeError: if a, b are neither int nor float.

    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
