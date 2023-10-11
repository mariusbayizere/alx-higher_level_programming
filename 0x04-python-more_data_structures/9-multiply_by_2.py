#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    temp = a_dictionary.copy()
    demo = list(temp.keys())

    for x in demo:
        temp[x] *= 2

    return (temp)

