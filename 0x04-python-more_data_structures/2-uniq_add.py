#!/usr/bin/python3
def uniq_add(my_list=[]):
    bitos = set(my_list)
    temp = 0

    for x in bitos:
        temp += x

    return (temp)

