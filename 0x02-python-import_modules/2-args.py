#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    cursor = len(sys.argv) - 1
    if cursor == 0:
        print("0 arguments.")
    elif cursor == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(cursor))
    for x in range(cursor):
        print("{}: {}".format(x + 1, sys.argv[x + 1]))

