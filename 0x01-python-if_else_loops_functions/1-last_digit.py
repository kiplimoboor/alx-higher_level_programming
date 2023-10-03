#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if (number < 0):
    strNum = str((number * -1))
strNum = str(number)
length = len(strNum) - 1

if (int(strNum[length]) > 5):
    print(f"Last digit of {number} is {strNum[length]} and is \
greater than 5")
elif (int(strNum[length]) == 0):
    print(f"Last digit of {number} is 0 and is 0")
elif (int(strNum[length]) < 6 and int(strNum[length]) != 0):
    print(f"Last digit of {number} is {strNum[length]} and is \
less than 6 and not 0")
