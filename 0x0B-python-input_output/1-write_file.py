#!/usr/bin/python3
"""
writes a string to a text file
returns the number of characters written
"""


def write_file(filename="", text=""):
    """
    use the with statement
    don’t need to manage file permission exceptions.
    should create the file if doesn’t exist.
    should overwrite the content of the file if it already exists.
    """

    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
