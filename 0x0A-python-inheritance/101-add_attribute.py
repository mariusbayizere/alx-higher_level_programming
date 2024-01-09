#!/usr/bin/python3
"""Defines a function that adds attributes to objects."""


def add_attribute(obj, daw, data):
    """A brief description of the function.

    Args:
        obj: An object or instance of a class.
        daw: A parameter representing something (provide more details).
        data: Another parameter representing data (provide more details).

    Returns:
        The return value of the function"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, daw, data)
