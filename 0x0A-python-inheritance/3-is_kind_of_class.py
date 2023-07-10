#!/usr/bin/python3
"""Returns True or False"""


def is_kind_of_class(obj, a_class):
    """Returns True if the object is an instance."""

    if isinstance(obj, a_class):
        return True
    return False
