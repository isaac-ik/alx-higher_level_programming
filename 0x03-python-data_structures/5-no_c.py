#!/usr/bin/python3
def no_c(my_string):
    newstring = ""
    for letter in my_string:
        if letter == 'c' or letter == 'C':
            pass
        else:
            newstring = newstring + letter
    return newstring
