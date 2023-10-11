#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    deaer = 0
    temp = 0

    for x in my_list:
        deaer += x[0] * x[1]
        temp += x[1]

    return (deaer / temp)

