#!/usr/bin/python3
"""creates an Object from a JSON file"""
import json


def load_from_json_file(filename):
    """
    must use the with statement
    don’t need to manage exceptions if JSON string doesn’t represent an object.
    don’t need to manage file permissions / exceptions.
    """

    with open(filename, encoding='utf-8') as file:
        return json.loads(file)
