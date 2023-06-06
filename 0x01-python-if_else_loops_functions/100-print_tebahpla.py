#!/usr/bin/python3
x = 0
for i in range(122, 96, -1):
    if x == 0:
        print("{}".format(chr(i - x)), end="")
        x = 32
    else:
        print("{}".format(chr(i - x)), end="")
        x = 0
