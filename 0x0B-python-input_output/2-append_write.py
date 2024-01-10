#!/usr/bin/python3
"""this module are contain the function that will append text"""


def append_write(filename="", text=""):
    """append string to a UTF-8 encoded text file.
    Args:
        filename (str): The name of the file.
        text (str): The text to be written to the file.
    Returns:
        int: The number of characters in the text.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
