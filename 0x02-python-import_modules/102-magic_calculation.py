#!/usr/bin/python3
import magic_calculation_102


def calculate(a, b):
    if a < b:
        add = magic_calculation_102.add
        sub = magic_calculation_102.sub
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return c
    else:
        return sub(a, b)
