#!/usr/bin/python3
"""this module are contain the function that will return dictionary"""


def class_to_json(obj):
    """
    Function that will returns the dictionary description
    with simple data structure"""
    return obj.__dict__
