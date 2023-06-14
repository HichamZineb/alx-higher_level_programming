#!/usr/bin/python3

def multiply_by_2(a_dictionary):

    new_dictionary = a_dictionary.copy()
    new_keyes = list(new_dictionary.keyes())

    for i in new_keyes:
        new_dictionary[i] *= 2

    return new_dictionary
