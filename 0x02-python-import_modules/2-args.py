#!/usr/bin/python3
if __name__ == "__main__":

    import sys

    p = len(sys.argv) - 1
    if p == 0:
        print("0 arguments.")
    elif p == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(p))
    for x in range(p):
        print("{}: {}".format(x + 1, sys.argv[x + 1]))
