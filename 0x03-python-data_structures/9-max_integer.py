#!/usr/bin/python3
# 9-max_integer.py


def max_integer(my_list=[]):
    """search the large integer in the list."""
    if len(my_list) == 0:
        return (None)

    temp = my_list[0]
    for x in range(len(my_list)):
        if my_list[x] > temp:
            temp = my_list[x]

    return (temp)

