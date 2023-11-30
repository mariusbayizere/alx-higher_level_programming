#!/usr/bin/python3
import sys
import hidden_4 as hidden

if __name__ != "__main__":
    exit()

for x in dir(hidden):
    if x[0:2] != "__":
        print(x)
