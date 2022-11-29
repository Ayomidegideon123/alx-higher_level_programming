#!/usr/bin/python3
"""Printing all possible combinations of two digits in ascending order
"""
for a in range(0, 10):
    for b in range(a + 1, 10):
        if a == 8 and b == 9:
            print("{}{}".format(a, b))
        else:
            print("{}{}".format(a, b), end=", ")
