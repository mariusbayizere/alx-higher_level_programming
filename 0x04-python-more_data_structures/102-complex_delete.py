#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    temp = list(a_dictionary.keys())

    for x in temp:
        if value == a_dictionary.get(x):
            del a_dictionary[x]

    return (a_dictionary)

