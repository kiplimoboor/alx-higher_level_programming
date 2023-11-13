#!/usr/bin/python3
"""A class module"""

import json


class Base:
    """Simple class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes new Base object

        Args:
            id (int, optional): ID for the object. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """gets JSON string representation of list_dictionaries

        Args:
            list_dictionaries (dict): list of dictionaries

        Returns:
            JSON String: JSON string representation of list_dictionaries
        """
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)
