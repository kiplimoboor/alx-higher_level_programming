from models.rectangle import Rectangle
from models.base import Base
import io
import sys
import unittest


class TestRectangleInit(unittest.TestCase):
    def test_parent_class(self):
        self.assertTrue(type(Rectangle(1, 1)), Base)

    def test_id(self):
        r1 = Rectangle(1, 1)
        r2 = Rectangle(1, 1)
        self.assertEqual(r2.id, r1.id + 1)

        self.assertEqual(Rectangle(1, 1, 1, 1, 5).id, 5)

    def test_width(self):
        self.assertEqual(Rectangle(1, 2).width, 1)

        with self.assertRaises(TypeError):
            Rectangle("Hello", 2)

        with self.assertRaises(ValueError):
            Rectangle(0, 2)
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

    def test_height(self):
        self.assertEqual(Rectangle(3, 4).height, 4)

        with self.assertRaises(TypeError):
            Rectangle(3, "World")

        with self.assertRaises(ValueError):
            Rectangle(3, 0)
        with self.assertRaises(ValueError):
            Rectangle(3, -4)

    def test_x(self):
        self.assertEqual(Rectangle(1, 2).x, 0)

        self.assertEqual(Rectangle(1, 2, 3, 4).x, 3)

        with self.assertRaises(TypeError):
            Rectangle(1, 2, "Hello", 1)

        with self.assertRaises(ValueError):
            Rectangle(0, 2, -1, 2)

    def test_y(self):
        self.assertEqual(Rectangle(3, 4).y, 0)

        self.assertEqual(Rectangle(1, 2, 3, 4).y, 4)

        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "Hello")

        with self.assertRaises(ValueError):
            Rectangle(1, 0, 1, -2)


class TestRectangleMethods(unittest.TestCase):
    @staticmethod
    def print_io(rectangle, method="print"):
        """prints to StringIO

        Args:
            rectangle (object): rectangle to be printed
            method (str, optional): Method to invoke. Defaults to "print".

        Returns:
            string: printed output
        """
        output = io.StringIO()
        sys.stdout = output
        if method == "print":
            print(rectangle)
        else:
            rectangle.display()
        sys.stdout = sys.__stdout__
        return output.getvalue()

    def test_area(self):
        self.assertEqual(Rectangle(3, 2).area(), 6)

        r = Rectangle(1, 5, 1, 1, 1)
        self.assertEqual(r.area(), 5)

        r.width = 10
        r.height = 20
        self.assertEqual(r.area(), 200)

    def test_str(self):
        r = Rectangle(3, 5, 0, 0, 1)
        self.assertEqual(self.print_io(r), "[Rectangle] (1) 0/0 - 3/5\n")

    def test_display(self):
        self.assertEqual(self.print_io(Rectangle(1, 1), "display"), "#\n")

        r = Rectangle(2, 2, 2, 2, 5)
        self.assertEqual(self.print_io(r, "display"), "\n\n  ##\n  ##\n")

    def test_update_with_args(self):
        r1 = Rectangle(1, 10, 3, 5, 25)
        output = io.StringIO()
        sys.stdout = output
        print(r1)
        self.assertEqual(output.getvalue(), "[Rectangle] (25) 3/5 - 1/10\n")

        r1.update(1, 3, 2, 4, 3)
        output = io.StringIO()
        sys.stdout = output
        print(r1)
        self.assertEqual(output.getvalue(), "[Rectangle] (1) 4/3 - 3/2\n")

    def test_update_with_kwargs(self):
        r1 = Rectangle(1, 10, 3, 5, 25)

        r1.update(height=5, x=10, width=15, y=21, id=3)
        self.assertEqual(r1.id, 3)
        self.assertEqual(r1.width, 15)
        self.assertEqual(r1.height, 5)
        self.assertEqual(r1.x, 10)
        self.assertEqual(r1.y, 21)

    def test_update_with_args_and_kwargs(self):
        r1 = Rectangle(1, 10, 3, 5, 25)
        args = 1, 3, 2, 4, 3
        kwargs = {"height": 5, "x": 10, "width": 15, "y": 21, "id": 3}
        r1.update(*args, **kwargs)

        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 3)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 3)
