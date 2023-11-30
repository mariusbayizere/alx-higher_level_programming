#!/usr/bin/python3

from calculator_1 import add, sub, mul, div

if __name__ == "__main__":

    x = 10
    y = 5

    print("{:g} + {:g} = {:g}".format(x, y, add(x, y)))
    print("{:g} - {:g} = {:g}".format(x, y, sub(x, y)))
    print("{:g} * {:g} = {:g}".format(x, y, mul(x, y)))
    print("{:g} / {:g} = {:g}".format(x, y, div(x, y)))

