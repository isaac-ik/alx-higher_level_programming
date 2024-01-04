#!/usr/bin/python3
for firstDigit in range(0, 10):
    for secondDigit in range(0, 10):
        if firstDigit > secondDigit:
            pass
        elif firstDigit == secondDigit:
            pass
        else:
            if firstDigit < 8 and secondDigit < 10:
                print("{}{}".format(firstDigit, secondDigit), end=", ")
            else:
                print("{}{}".format(firstDigit, secondDigit), end="\n")
