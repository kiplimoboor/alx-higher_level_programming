#!/usr/bin/python3
"""Loads JSON"""
import json


def from_json_string(my_str):
    """Loads JSON

    Args:
        my_str (JSON string): The JSON to be converted into Python object
    """

    return json.loads(my_str)
