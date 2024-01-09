#!/usr/bin/python3
"""Define class MyList and inherets property of this list"""


class MyList(list):
    """implementation of class and function printing sorted list"""
    def print_sorted(self):
        """method that have responsible for printing sorted list"""
        print(sorted(self))
