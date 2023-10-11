#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    temp = list(a_dictionary.keys())
    temp.sort()
    for x in temp:
        print("{}: {}".format(x, a_dictionary.get(x)))

