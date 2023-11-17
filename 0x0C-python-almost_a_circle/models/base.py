#!/usr/bin/python3
"""A class module"""

import json
import csv
import turtle


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """gets JSON string representation of list_dictionaries

        Args:
            list_dictionaries (dict): list of dictionaries

        Returns:
            JSON String: JSON string representation of list_dictionaries
        """
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes JSON string representation of an object to a file

        Args:
            list_objs (list): list of objects to be saved
        """

        filename = cls.__name__ + ".json"

        with open(filename, 'w') as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dictionaries = [i.to_dictionary() for i in list_objs]
                file.write(cls.to_json_string(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """finds and returns the list of the JSON string representation
            json_string

        Args:
            json_string (str): json string representing list of dicts

        Returns:
            list: list represented by json_string
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns instance with all attributes already set

        Returns:
            object: instance of a class object
        """

        instance = cls(1, 1) if cls.__name__ == "Rectangle" else cls(1)
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """loads json representation of an instance and creates it

        Returns:
            list: list of the instances
        """
        filename = cls.__name__ + ".json"

        try:
            with open(filename, 'r') as file:
                json_list = cls.from_json_string(file.read())
        except FileNotFoundError:
            return []

        list_instance = [cls.create(**instance) for instance in json_list]
        return list_instance

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """saves class instances into csv file

        Args:
            list_objs (list): list of class instances
        """

        filename = cls.__name__ + ".csv"

        with open(filename, 'w') as file:
            if not list_objs:
                file.write("")
            else:
                data = [i.to_dictionary() for i in list_objs]
                fieldnames = list(data[0].keys())
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(data)

    @classmethod
    def load_from_file_csv(cls):
        """Loads instances of a class from csv files

        Returns:
            list: a list of class instances
        """
        filename = cls.__name__ + ".csv"
        rectangles = []

        try:
            with open(filename, 'r') as csvfile:
                rows = list(csv.DictReader(csvfile))
                for row in rows:
                    for key, value in row.items():
                        row[key] = int(value)
                    rectangles.append(cls.create(**row))
                return rectangles

        except FileNotFoundError:
            return rectangles

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draws all Rectangles and Squares.

            For demonstration, run the draw.py file
            in the root folder of this project.

            Make sure to have the Turtle graphics module
            installed on your device.

        Args:
            list_rectangles (list): rectangle instances
            list_squares (list): square instances
        """

        t = turtle.Turtle()
        t.penup()
        t.setpos(-300, 300)
        t.pendown()
        t.write("Rectangles", move=False, align='center',
                font=('Arial', 15, 'normal'))

        t.penup()
        t.setpos(-300, 285)
        t.pendown()

        for r in list_rectangles:
            width = r.width
            height = r.height

            t.forward(width)
            t.right(90)
            t.forward(height)
            t.right(90)
            t.forward(width)
            t.right(90)
            t.forward(height)
            t.right(90)

            t.penup()
            t.forward(width + 20)
            t.pendown()

        t.penup()
        t.goto(-300, 0)
        t.pendown()

        t.write("Squares", move=False, align='center',
                font=('Arial', 15, 'normal'))

        t.penup()
        t.goto(-300, -15)
        t.pendown()

        for s in list_squares:
            size = s.size

            for _ in range(4):
                t.forward(size)
                t.right(90)

            t.penup()
            t.forward(size + 20)
            t.pendown()

        t.hideturtle()
        turtle.done()
