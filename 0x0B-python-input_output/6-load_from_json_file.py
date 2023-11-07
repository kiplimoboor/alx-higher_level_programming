#!/usr/bin/python3
"""Loads from JSON file"""

import json


def load_from_json_file(filename):
    """creates an Object from a “JSON file

    Args:
        filename (string): file to be loaded from
    """

    with open(filename) as f:
        return json.load(f)
