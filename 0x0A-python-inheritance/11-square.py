#!/usr/bin/python3

"""Module with Basic Square Class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Geometry class

    Args:
        Rectangle (class): parent class
    """

    def __init__(self, size):
        super().integer_validator("size", size)
        self.__width = size
        self.__height = size

    def __str__(self):
        return (f"[Rectangle] {self.__width}/{self.__height}")

    def area(self):
        return self.__width * self.__height
