#!/usr/bin/python3


def matrix_divided(matrix, div):
    """
    Divides  elements int  matrix, elements are
        int or float type
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
