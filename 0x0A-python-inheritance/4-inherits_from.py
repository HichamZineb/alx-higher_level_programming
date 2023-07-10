#!/usr/bin/python3
"""True or False"""


def inherits_from(obj, a_class):
    """True or False"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
