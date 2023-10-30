#!/usr/bin/python3
"""Code containing class Rectangle"""


class Rectangle:
    """Defines Rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Computes and Returns the Area"""
        return self.height * self.width

    def perimeter(self):
        """Computes the perimeter"""
        if (self.width == 0 or self.height == 0):
            return 0
        return ((2 * self.width) + (2 * self.height))

    def __str__(self):
        """Prints the Rectangle"""
        if self.width == 0 or self.height == 0:
            return ""

        rectangle = ""
        for i in range(self.height):
            for j in range(self.width):
                rectangle += str(self.print_symbol)
            rectangle += "\n"
        return rectangle

    def __repr__(self):
        """Returns String Representation of the Rectangle"""
        return (f"Rectangle({self.width}, {self.height})")

    def __del__(self):
        """Deletes an instance of Rectangle"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
