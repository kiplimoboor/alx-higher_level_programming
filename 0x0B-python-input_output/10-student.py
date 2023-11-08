#!/usr/bin/python3
"""Module for returning dictionary representation of a class"""


class Student:
    """Defines a student
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """_summary_

        Args:
            attrs (list, optional): attributes to be checked. Defaults to None.

        Returns:
            dict: dictionary representation of the student instance
        """

        if (type(attrs) == list and all(type(el) == str for el in attrs)):
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
        else:
            return self.__dict__

        return attributes
