#!/usr/bin/python3
"""Module for returning dictionary representation of a class"""


class Student:
    """Defines a student
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves dict representation of a Student instance
        """
        return self.__dict__
