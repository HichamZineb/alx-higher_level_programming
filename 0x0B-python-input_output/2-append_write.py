#!/usr/bin/python3
"""
appends a string at the end of a text file
returns the number of characters added
"""


def write_file(filename="", text=""):
    """
    use the with statement
    don’t need to manage file permission exceptions.
    should create the file if doesn’t exist.
    """

    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
