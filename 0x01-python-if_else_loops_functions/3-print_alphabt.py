#!/usr/bin/python3
for ASCIIVALUE in range(97, 123):
    if chr(ASCIIVALUE) == 'q' or chr(ASCIIVALUE) == 'e':
        pass
    else:
        print(f"{chr(ASCIIVALUE)}", end='')
