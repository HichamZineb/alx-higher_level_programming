#!/usr/bin/python3
"""reads a text file"""


def read_file(filename=""):
    """
    use the with statement
    don’t need to manage exceptions.
    """

    with open(filename, encoding='utf-8') as file:
        print(file.read(), end='')
