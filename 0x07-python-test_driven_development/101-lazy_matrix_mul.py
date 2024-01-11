#!/usr/bin/python3
"""
this module are contain function that multpluy
two matrix using numpy
"""
from numpy import matmul


def lazy_matrix_mul(m_a, m_b):
    """function that multpluy two matrix using numpy"""
    return matmul(m_a, m_b)
