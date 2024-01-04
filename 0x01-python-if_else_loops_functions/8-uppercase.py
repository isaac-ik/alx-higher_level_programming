#!/usr/bin/python3
def uppercase(str):
    new = ""
    for letter in str:
        if ord(letter) > 96 and ord(letter) < 123:
            new = new + chr(ord(letter) - 32)
        else:
            new = new + letter
    print("{}".format(new))
