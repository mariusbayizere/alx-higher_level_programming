#!/usr/bin/python3
"""this module are contain function that will divide matrix"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given divisor.

    Parameters:
    - matrix (list of lists): The matrix to be divided.
    - div (int or float): The divisor by which each element
    of the matrix will be divided.

    Returns:
    list of lists: A new matrix containing the results of
    the division operation.
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
        return matrix
    elif div == 0:
        raise ZeroDivisionError("division by zero")
        return matrix

    pasrrowlength = -1
    empty_list = []
    for row in matrix:
        if (pasrrowlength != len(row) and pasrrowlength != -1):
            raise TypeError("Each row of the matrix must have the same size")
            return matrix
        for column in row:
            if not isinstance(column, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of" +
                                " integers/floats")
                return matrix
            else:
                empty_list.append(round(column / div, 2))
        pasrrowlength = len(row)

    return empty_list
