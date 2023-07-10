#!/usr/bin/python3
"""Function that returns True or False"""


def is_same_class(obj, a_class):
    """
    True if the object is exactly an instance of the specified class.
    Otherwise False.
    """

    if type(obj) == a_class:
        return True
    else:
        return False
