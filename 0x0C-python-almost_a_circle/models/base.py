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

        filename = cls.__name__ + ".json"

        with open(filename, 'w') as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dictionaries = [i.to_dictionary() for i in list_objs]
                file.write(cls.to_json_string(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """finds and returns the list of the JSON string representation
            json_string

        Args:
            json_string (str): json string representing list of dicts

        Returns:
            list: list represented by json_string
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns instance with all attributes already set

        Returns:
            object: instance of a class object
        """

        if cls.__name__ == "Rectangle":
            instance = cls(1, 1)
        elif cls.__name__ == "Square":
            instance = cls(1)
        instance.update(**dictionary)
        return instance
