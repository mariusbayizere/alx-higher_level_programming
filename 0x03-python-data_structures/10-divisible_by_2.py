#!/usr/bin/python3
# 10-divisible_by_2.py


def divisible_by_2(my_list=[]):
    """search all number multiples by 2 in a list."""
    demom = []
    for x in range(len(my_list)):
        if my_list[x] % 2 == 0:
            demom.append(True)
        else:
            demom.append(False)

    return (demom)

