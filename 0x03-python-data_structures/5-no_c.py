#!/usr/bin/python3
def no_c(my_string):
    new_string = [my_string[i]
                  for i in range(len(my_string))if my_string[i] not in 'cC']

    return "".join(new_string)
