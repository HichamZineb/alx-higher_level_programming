#!/usr/bin/python3

def number_keys(a_dictionary):

    x = 0

    keys = list(a_dictionary.keys())

    for i in keys:
        x = x + i

    return x
