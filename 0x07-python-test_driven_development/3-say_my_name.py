#!/usr/bin/python3
"""this module are contain function that will print name"""


def say_my_name(first_name, last_name=""):
    """Function that print lastname and firstname"""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("Myname is {} {}".format(first_name, last_name))
