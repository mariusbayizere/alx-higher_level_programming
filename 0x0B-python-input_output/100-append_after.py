#!/usr/bin/python3
"""this module are  file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """function that insertion text after line containing string in a file.

    Args:
        filename (str): name of the file must be string.
        search_string (str): string to search for within the file.
        new_string (str): string to insert.
    """
    new_line = ""
    with open(filename) as r:
        for line in r:
            new_line += line
            if search_string in line:
                new_line += new_string
    with open(filename, "w") as w:
        w.write(new_line)
