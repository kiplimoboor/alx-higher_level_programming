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

        if isinstance(attrs, list) and\
                all(isinstance(el, str) for el in attrs):
            attributes = {}
            for attribute in attrs:
                try:
                    attributes[attribute] = getattr(self, attribute)
                except AttributeError:
                    continue
        else:
            attributes = self.__dict__

        return attributes
