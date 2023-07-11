#!/usr/bin/python3
"""returns the JSON representation of an object"""
import json


def to_json_string(my_obj):
    """don’t need to manage exceptions if object can’t be serialized."""

    return json.dumps(my_obj)
