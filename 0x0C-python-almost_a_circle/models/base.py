#!/usr/bin/python3
"""A class module"""


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
