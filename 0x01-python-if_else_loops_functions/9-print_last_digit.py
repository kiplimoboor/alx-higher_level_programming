#!/usr/bin/bash
def print_last_digit(number):
    last = number % 10
    if (number < 0):
        last = ((number * -1) % 10)
    print(last, end="")

    return last
