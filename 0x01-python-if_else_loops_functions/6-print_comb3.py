#!/usr/bin/python3
for digit1 in range(0, 9):
    for digit2 in range(digit1 + 1, 10):
        if digit1 < 8:
            print("{:02d}, ".format(digit1 * 10 + digit2), end="")
        else:
            print("{:02d}".format(digit1 * 10 + digit2))
