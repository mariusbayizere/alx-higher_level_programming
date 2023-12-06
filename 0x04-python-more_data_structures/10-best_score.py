#!/usr/bin/python3


def best_score(a_dictionary):
    """
    gets the best value from a dictionary (greatest integer)
    """
    samu = 0
    zaru = None
    if type(a_dictionary) is dict:
        for (key, value) in a_dictionary.items():
            if value > samu:
                samu = value
                zaru = key
    return zaru

