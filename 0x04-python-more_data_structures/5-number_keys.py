#!/usr/bin/python3

def number_keys(a_dictionary):

    x = 0

    number_keys = list(a_dictionary.keys())

    for i in number_keys:
        x = x + 1

    return x
