#!/usr/bin/python3
import sys

if __name__ != "__main__":
    exit()

argc = len(sys.argv) - 1

x = 0
sums = 0
for arg in sys.argv:
    if x != 0:
        sums += int(arg)
    else:
        x += 1
print("{:d}".format(sums))
