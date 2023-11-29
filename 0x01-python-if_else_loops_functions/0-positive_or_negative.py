#!/usr/bin/python3
import random

roma = random.randint(-10, 10)

if roma > 0:
    print("{} is positive".format(roma))
elif roma == 0:
    print("{} is zero".format(roma))
else:
    print("{} is negative".format(roma))
