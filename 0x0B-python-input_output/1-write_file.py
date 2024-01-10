#!/usr/bin/python3
"""this module are contain the function that write string text"""


def write_file(filename="", text=""):
    """
    Write a string to a UTF-8 encoded text file.

    Args:
        filename (str): The name of the file.
        text (str): The text to be written to the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
