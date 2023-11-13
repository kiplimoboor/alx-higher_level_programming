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

    @staticmethod
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

    @classmethod
    def save_to_file(cls, list_objs):
        """writes JSON string representation of an object to a file

        Args:
            list_objs (list): list of objects to be saved
        """

        list_dictionaries = [i.to_dictionary() for i in list_objs]
        json_string = cls.to_json_string(list_dictionaries)
        filename = cls.__name__ + ".json"

        with open(filename, 'w') as json_file:
            json_file.write(json_string)
