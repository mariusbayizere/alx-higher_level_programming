#!/usr/bin/python3
for number_one in range(0, 10):
    for number_two in range(number_one + 1, 10):
        if number_one == 8 and number_two == 9:
            print("{}{}".format(number_one, number_two))
        else:
            print("{}{}".format(number_one, number_two), end=", ")
