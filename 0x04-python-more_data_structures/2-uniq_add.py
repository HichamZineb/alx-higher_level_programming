#!/usr/bin/python3

def uniq_add(my_list=[]):

    unique = set(my_list)

    x = 0

    for i in unique:
        x = x + i

    return x
