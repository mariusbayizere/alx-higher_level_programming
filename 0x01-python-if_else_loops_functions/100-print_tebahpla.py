#!/usr/bin/python3

x = 0
for k in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(k - x)), end="")
    x = 32 if x == 0 else 0
