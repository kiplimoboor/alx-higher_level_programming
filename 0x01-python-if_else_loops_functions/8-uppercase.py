#!/usr/bin/python3
def uppercase(str):
    for char in (str):
        upper = char
        if (ord(char) >= 97):
            upper = chr(ord(char) - 32)
        print("{}".format(upper), end="")
    print("")
