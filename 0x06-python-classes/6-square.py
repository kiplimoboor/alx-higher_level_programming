#!/usr/bin/python3
"""Contains class that defines a square"""


class Square:
    """Defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is tuple\
                and len(value) == 2\
                and type(value[0]) is int\
                and type(value[1]) is int:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Returns Area of Square"""
        return self.size ** 2

    def my_print(self):
        """Prints Square"""
        if self.size == 0:
            print()
            return
        for y in range(self.position[1]):
            print()
        for length in range(self.size):
            for x in range(self.position[0]):
                print(" ", end="")
            for width in range(self.size):
                print("#", end="")
            print()
