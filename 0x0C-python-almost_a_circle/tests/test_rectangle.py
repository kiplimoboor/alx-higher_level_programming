from models.rectangle import Rectangle
from models.base import Base
import sys
import unittest
from helper import print_io


class TestRectangleInit(unittest.TestCase):
    def test_parent_class(self):
        self.assertTrue(type(Rectangle(1, 1)), Base)

    def test_id(self):
        r1 = Rectangle(1, 1)
        r2 = Rectangle(1, 1)
        self.assertEqual(r2.id, r1.id + 1)

        self.assertEqual(Rectangle(1, 1, 1, 1, 5).id, 5)

    def test_attrs(self):
        r = Rectangle(1, 1, 1, 1, 5)
        self.assertTrue(
            all([r.id == 5, r.width == 1, r.height == 1, r.x == 1, r.y == 1]))

    def test_width(self):
        r = Rectangle(1, 2)
        self.assertEqual(r.width, 1)
        r.width = 20
        self.assertEqual(r.width, 20)

        with self.assertRaises(TypeError):
            r.width = "Hello"

        with self.assertRaises(ValueError):
            r.width = 0
        with self.assertRaises(ValueError):
            r.width = -1

    def test_height(self):
        r = Rectangle(3, 4)
        self.assertEqual(r.height, 4)
        r.height = 20
        self.assertEqual(r.height, 20)

        with self.assertRaises(TypeError):
            r.height = "World"

        with self.assertRaises(ValueError):
            r.height = 0
        with self.assertRaises(ValueError):
            r.height = -4

    def test_x(self):
        self.assertEqual(Rectangle(1, 2).x, 0)
        self.assertEqual(Rectangle(1, 2, 0, 1).x, 0)

        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(r.x, 3)
        r.x = 15
        self.assertEqual(r.x, 15)

        with self.assertRaises(TypeError):
            r.x = "Hello"

        with self.assertRaises(ValueError):
            r.x = -1

    def test_y(self):
        self.assertEqual(Rectangle(3, 4).y, 0)
        self.assertEqual(Rectangle(3, 4, 1, 0).y, 0)

        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(r.y, 4)
        r.y = 10
        self.assertEqual(r.y, 10)

        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "Hello")

        with self.assertRaises(ValueError):
            Rectangle(1, 0, 1, -2)


class TestRectangleMethods(unittest.TestCase):
    def test_area(self):
        self.assertEqual(Rectangle(3, 2).area(), 6)

        r = Rectangle(1, 5, 1, 1, 1)
        self.assertEqual(r.area(), 5)

        r.width = 10
        r.height = 20
        self.assertEqual(r.area(), 200)


class TestRectangleDisplay(unittest.TestCase):

    def test_str(self):
        r = Rectangle(3, 5, 0, 0, 1)
        self.assertEqual(print_io(r), "[Rectangle] (1) 0/0 - 3/5\n")

        r = Rectangle(5, 7, 10, 10, 2)
        self.assertEqual(print_io(r), "[Rectangle] (2) 10/10 - 5/7\n")

    def test_display(self):
        self.assertEqual(print_io(Rectangle(2, 2), "display"), "##\n##\n")

        r = Rectangle(2, 2, 2, 2, 5)
        self.assertEqual(print_io(r, "display"), "\n\n  ##\n  ##\n")

        r = Rectangle(2, 2, 0, 2)
        self.assertEqual(print_io(r, "display"), "\n\n##\n##\n")


class TestRectangleUpdate(unittest.TestCase):
    def test_update_with_args(self):
        r = Rectangle(1, 10, 3, 5, 25)
        self.assertEqual(print_io(r), "[Rectangle] (25) 3/5 - 1/10\n")

        r.update(4)
        self.assertEqual(print_io(r), "[Rectangle] (4) 3/5 - 1/10\n")

        r.update(4, 5, 4)
        self.assertEqual(print_io(r), "[Rectangle] (4) 3/5 - 5/4\n")

        r.update(4, 5, 4, 4, 3)
        self.assertEqual(print_io(r), "[Rectangle] (4) 4/3 - 5/4\n")

        def test_update_with_kwargs(self):
            r = Rectangle(1, 10, 3, 5, 25)
            self.assertEqual(print_io(r), "[Rectangle] (25) 3/5 - 1/10\n")

            r.update(height=5, x=10, width=15, y=21, id=3)
            self.assertEqual(print_io(r), "[Rectangle] (3) 10/21 - 15/5\n")

        def test_update_with_args_and_kwargs(self):
            r = Rectangle(1, 10, 3, 5, 25)
            self.assertEqual(print_io(r), "[Rectangle] (25) 3/5 - 1/10\n")

            args = 1, 3, 2, 4, 3
            kwargs = {"height": 5, "x": 10, "width": 15, "y": 21, "id": 3}
            r.update(*args, **kwargs)
            self.assertEqual(print_io(r), "[Rectangle] (1) 4/3 - 3/2\n")
