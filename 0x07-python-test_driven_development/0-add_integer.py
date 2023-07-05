#!/usr/bin/python3

def add_integer(a, b=98):
    """
    Returns a + b

    Floats are casted into ints before addition

    Raises:
        TypeError: if a or b are not integers or floats
    """
    
    if type(a) not in [int, float] or a is None:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float] or b is None:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
