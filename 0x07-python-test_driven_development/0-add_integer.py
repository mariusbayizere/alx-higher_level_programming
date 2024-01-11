#!/usr/bin/python3

"""this module are contain the python script"""


def add_integer(a, b=98):
    """function that adds two numbers (integer or float)

    Args:
        a (int or float): The first number.
        b (int or float, optional): The second number. Defaults to 98.

    Returns:
        int: The sum of a and b.

    Raises:
        TypeError: If either a or b is not an integer or float.
        """
    if not isinstance(a, int):
        if isinstance(a, float):
            a = int(a)
        else:
            raise TypeError('a must be an integer')
    if not isinstance(b, int):
        if isinstance(b, float):
            b = int(b)
        else:
            raise TypeError('b must be an integer')
    return a + b
