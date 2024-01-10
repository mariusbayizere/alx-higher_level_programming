#!/usr/bin/python3
"""this module  text file-reading function."""


def read_file(filename=""):
    """function that display the contents of a UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
