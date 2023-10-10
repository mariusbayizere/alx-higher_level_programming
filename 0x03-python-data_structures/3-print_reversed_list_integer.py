#!/usr/bin/python3
# 3-print_reversed_list_integer.py


def print_reversed_list_integer(my_list=[]):
    """displaying all element of a list in reverse order."""
    if isinstance(my_list, list):
        my_list.reverse()
        for x in my_list:
            print("{:d}".format(x))

