#!/usr/bin/python3
"""class Mylist"""


class MyList(list):
    """Inherits from list"""

    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)"""
        print(sorted(self))
