#!/usr/bin/python3
"""class Mylist"""


class Mylist(list):
    """Inherits from list"""

    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)"""
        print(sorted(self))
