#!/usr/bin/python3
print("{:02d},".format(1), end="")
for i in range (8):
    for j in range (2,10):
        if (j > i):
            print(" {}{},".format(i, j),end="")
print(" {}".format(89))
