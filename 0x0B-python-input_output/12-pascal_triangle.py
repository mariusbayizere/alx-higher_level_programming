#!/usr/bin/python3
"""This module provides a Pascal's Triangle function."""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the specified number of rows.

    Args:
        n (int): The number of rows to generate.

    Returns:
        list: A list of lists representing Pascal's Triangle.

    Example:
        >>> pascal_triangle(3)
        [[1], [1, 1], [1, 2, 1]]
    """
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        last_row = triangle[-1]
        new_row = [1]
        for i in range(len(last_row) - 1):
            new_row.append(last_row[i] + last_row[i + 1])
        new_row.append(1)
        triangle.append(new_row)

    return triangle
