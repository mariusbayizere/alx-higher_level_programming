#!/usr/bin/python3

"""This module contains a function that
prints text with 2 newline characters"""


def text_indentation(text):
    """This function is responsible for printing text with
    2 newline characters"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    string = ""
    specials = ['.', '?', ':']

    for x in text:
        string += x
        if x in specials:
            string += "\n\n"

    print(string, end="")
