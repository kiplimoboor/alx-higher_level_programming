#!/usr/bin/pyhton3
def add_tuple(tuple_a=(), tuple_b=()):
    left = 0
    right = 0
    if len(tuple_a) > 0:
        left += tuple_a[0]
        if len(tuple_a) > 1:
            right += tuple_a[1]

    if len(tuple_b) > 0:
        left += tuple_b[0]
        if len(tuple_b) > 1:
            right += tuple_b[1]

    return (left, right)
