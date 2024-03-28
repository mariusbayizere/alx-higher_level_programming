#!/usr/bin/python3
"""Write a function that finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """ Finds the peak in a list of integers """
    if list_of_integers == []:
        return None

    many = len(list_of_integers)
    k = int(many / 2)
    li = list_of_integers

    if k - 1 < 0 and k + 1 >= many:
        return li[k]
    elif k - 1 < 0:
        return li[k] if li[k] > li[k + 1] else li[k + 1]
    elif k + 1 >= many:
        return li[k] if li[k] > li[k - 1] else li[k - 1]

    if li[k - 1] < li[k] > li[k + 1]:
        return li[k]

    if li[k + 1] > li[k - 1]:
        return find_peak(li[k:])
    return find_peak(li[:k])
