#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
roma = abs(number) % 10

if number < 0:
    roma = -roma

print("Last digit of {} is {} and is ".format(number, roma), end="")

if roma > 5:
    print("greater than 5")
elif roma == 0:
    print("0")
else:
    print("less than 6 and not 0")
