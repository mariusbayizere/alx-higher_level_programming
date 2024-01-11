#!/usr/bin/python3

""" this module are comtain funtion that will print the square of  character"""


def print_square(size):
    """function that prints the square of # character
    args
        size - receives the size
    """
    if not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")
    elif size < 0:
        if isinstance(size, float):
            raise TypeError("size must be an integer")
        else:
            raise ValueError("size must be >= 0")

    size = int(size)
    x = 0
    for x in range(x, size):
        y = 0
        for y in range(y, size):
            print("#", end="")
        print()
