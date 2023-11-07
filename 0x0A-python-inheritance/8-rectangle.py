#!/usr/bin/python3

"""Module with Basic Rectangle Class"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from Geometry class

    Args:
        BaseGeometry (class): parent class
    """

    bg = BaseGeometry()

    def __init__(self, width, height):
        if Rectangle.bg.integer_validator('width', width):
            self.__width = width
        if Rectangle.bg.integer_validator('height', height):
            self.__height = height
