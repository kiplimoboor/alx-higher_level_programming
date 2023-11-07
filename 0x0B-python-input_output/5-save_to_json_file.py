#!/usr/bin/python3
"""Writes JSON string to file"""
import json


def save_to_json_file(my_obj, filename):
    """Writes my_obj into a json file

    Args:
        my_obj (object): object to be written
        filename (str): file to be written into
    """
    with open(filename, mode='w') as f:
        json.dump(my_obj, f)
