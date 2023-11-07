#!/usr/bin/python3
"""Module that checks if an instance is a subclass"""


def inherits_from(obj, a_class):
    """Checks if an instance is a subclass

    Args:
        obj (class): instance to check
        a_class (class): parent class to check against
    """

    return issubclass(type(obj),  a_class) and type(obj) is not a_class
