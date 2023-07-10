#!/usr/bin/python3
"""adds a new attribute to an object if it’s possible"""


def add_attribute(obj, att, value):
    """Raise a TypeError exception if the object can’t have new attribute"""

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
