#!/usr/bin/python3
"""this module are contain class-checking function."""


def inherits_from(obj, a_class):
    """function checking if an object is an inherited of a class.

    Args:
        obj (any): object to check.
        a_class (type): class to match the type of obj to.
    Returns:
         obj is an inherited instance of a_class - True.
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
