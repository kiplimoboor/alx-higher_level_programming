#!/usr/bin/python3
"""Class-To-JSON Module"""


def class_to_json(obj):
    """ returns the dictionary description with
        simple data structure (list, dictionary, string, integer and boolean)
        for JSON serialization of an object

    Args:
        obj (object): The object whose attributes are to be found
    """

    return obj.__dict__
