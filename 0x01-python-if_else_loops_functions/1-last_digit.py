#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if (number < 0):
    number *= -1
number = str(number)
length = len(number) - 1
if (int(number[length]) > 5):
    print(f"Last digit of {number} is {number[length]} and and is greater than 5")
elif (int(number[length]) == 0):
    print(f"Last digit of {number} is {number[length]} and is 0")
elif (int(number[length]) < 6 and int(number[length]) != 0):
    print(f"Last digit of {number} is {number[length]} and is less than 6 and not 0")
