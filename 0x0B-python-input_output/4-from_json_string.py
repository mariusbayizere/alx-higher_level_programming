#!/usr/bin/python3
"""this module are contain function that return obectof string"""
import json


def from_json_string(my_str):
    """
    Deserialize a JSON-formatted string to a Python object.

    Parameters:
    - my_str (str): A JSON-formatted string to be deserialized.

    Returns:
    obj: The Python object resulting from deserialization.
    """
    return json.loads(my_str)
