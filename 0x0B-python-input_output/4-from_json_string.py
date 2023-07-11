#!/usr/bin/python3
"""returns an object (Python data structure) represented by a JSON string"""
import json


def from_json_string(my_str):
    """don’t need to manage exceptions
    if JSON string doesn’t represent an object."""

    return json.loads(my_str)
