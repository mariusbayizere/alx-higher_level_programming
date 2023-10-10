#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for temp in matrix:
        for ptr in temp:
            print("{:d}".format(ptr), end=" " if ptr != temp[-1] else "")
        print()

