#!/usr/bin/python3

"""Function that checks instances"""


def is_kind_of_class(obj, a_class):
    """Checks if obect is an instance of a class

    Args:
        obj (any): object whos instance is to be checked
        a_class (class): class whose object instance is compared against

    Return:
        True of object is instance of class, False otherwise
    """

    return isinstance(obj, a_class)
