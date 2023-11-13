#!/usr/bin/python3
"""Module with rectangle class"""

from models.base import Base


class Rectangle(Base):
    """A rectangle class

    Args:
        Base (class): Parent class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super(Rectangle, self).__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """Displays the rectangle information

        Returns:
            string: The rectangle information
        """
        return (f"[Rectangle] ({self.id}) {self.x}/{self.y}" +
                f" - {self.width}/{self.height}")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Calculates the area of the rectange

        Returns:
            int: Area of rectange
        """
        return self.width * self.height

    def display(self):
        """Displays the rectange
        """
        for y in range(self.y):
            print()
        for i in range(self.height):
            for x in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """Updates the rectangle
        """
        if args:
            length = len(args)
            if length > 0:
                self.id = args[0]
            if length > 1:
                self.width = args[1]
            if length > 2:
                self.height = args[2]
            if length > 3:
                self.x = args[3]
            if length > 4:
                self.y = args[4]
        else:
            for attr in kwargs:
                if hasattr(self, attr):
                    self.attr = attr
