#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return "None"

    for i in range(len(my_list)):
        for j in range(i, len(my_list)):
            if my_list[i] > my_list[j]:
                temp = my_list[i]
                my_list[i] = my_list[j]
                my_list[j] = temp

    return my_list[len(my_list) - 1]
