#!/usr/bin/python3


def matrix_mul(m_a, m_b):
    """
    function matrix multiplaction of two matrix
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not manirar_matrix_test(m_a):
        raise TypeError("m_a must be a list of lists")
    if not manirar_matrix_test(m_b):
        raise TypeError("m_b must be a list of lists")

    if not test_matrix_dev(m_a):
        raise ValueError("m_a can't be empty")
    if not test_matrix_dev(m_b):
        raise ValueError("m_b can't be empty")

    if not elemenent_matrix(m_a):
        raise TypeError("m_a should contain only integers or floats")
    if not elemenent_matrix(m_b):
        raise TypeError("m_b should contain only integers or floats")

    if not rectangle_matrix(m_a):
        raise TypeError("each row of m_a must should be of the same size")
    if not rectangle_matrix(m_b):
        raise TypeError("each row of m_a must should be of the same size")

    if not check_matrix(m_a, m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    if len(m_a) > len(m_b[0]):
        res_len = len(m_a)
    elif len(m_a) < len(m_b[0]):
        res_len = len(m_b[0])
    else:
        res_len = len(m_a)

    new_matrix = []
    for row_i in range(0, len(m_a)):
        values = []
        for col_i in range(0, len(m_b[0])):
            res = 0
            for j in range(0, len(m_a[row_i])):
                res += m_a[row_i][j] * m_b[j][col_i]
            values.append(res)
        new_matrix.append(values)
    return new_matrix


def check_matrix(m_a, m_b):
    """function that check two matrix can possible be multiplied
    """
    return (len(m_a) == len(m_b[0]) or len(m_b) == len(m_a[0]))


def manirar_matrix_test(matrix):
    """function checking if a list is a list of matrix
    """
    for row in matrix:
        if not isinstance(row, list):
            return False
    return True


def elemenent_matrix(matrix):
    """checks if a matrix (list of lists) contains non ints/floats
    """
    for row in matrix:
        for xx in row:
            if not isinstance(xx, (int, float)):
                return False
    return True


def rectangle_matrix(matrix):
    """checks if a matrix is a rectangle
    """
    pivot_list = -1
    for row in matrix:
        if pivot_list != -1 and pivot_list != len(row):
            return False
        pivot_list = len(row)
    return True


def test_matrix_dev(m):
    """function that check the empty list of matrix
    """
    if ((m is None or len(m) == 0) or (m[0] is None or len(m[0]) == 0)):
        return False
    return True
