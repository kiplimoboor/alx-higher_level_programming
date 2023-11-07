#!/usr/bin/python3
"""Module that converts python object to JSON"""
import json


def to_json_string(my_obj):
    """Converts python Object to JSON STring

    Args:
        my_obj (any): python object to be converted
    """

    return json.dumps(my_obj)
