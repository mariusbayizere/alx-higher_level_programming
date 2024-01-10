#!/usr/bin/python3
"""this module are contain the function writes an Object to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """
    Serialize a Python object to a JSON-formatted string and save it to a file.

    Parameters:
    - my_obj: The Python object to be serialized to JSON.
    - filename (str): The name of the file where the JSON data will be saved.

    Returns:
    None
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
