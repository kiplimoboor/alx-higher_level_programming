#!/usr/bin/python3
"""Containes class that defines a square"""


class Square:
    """Defines a square"""

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Finds area"""
        return (self.__size ** 2)

    def my_print(self):
        """Prints the square"""
        if self.size == 0:
            print("")
        for i in range(self.size):
            for j in range(self.size):
                print("#", end="")
            print("")
