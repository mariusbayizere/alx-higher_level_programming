#!/usr/bin/python3
"""this module are contain the function that will return json"""
import json

def to_json_string(my_obj):
    """
    Serialize a Python object to a JSON-formatted string.

    Parameters:
    - my_obj: The Python object to be serialized to JSON.

    Returns:
    str: A JSON-formatted string representing the serialized object.
    """
    return json.dumps(my_obj)
