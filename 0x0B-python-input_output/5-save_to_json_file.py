#!/usr/bin/python3
"""writes an Object to a text file, using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """
    must use the with statement
    don’t need to manage exceptions if object can’t be serialized.
    don’t need to manage file permission exceptions.
    """

    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
