#!/usr/bin/python3
# 0-add_integer.py
"""
Write a function that adds 2 integers.

a and b must be integers or floats, otherwise raise a TypeError
"""


def add_integer(a, b=98):
    """Returns a + b
    Raises TypeError if a or b are not ints or floats
    """
    if type(a) not in [int, float] or a is None:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float] or b is None:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
