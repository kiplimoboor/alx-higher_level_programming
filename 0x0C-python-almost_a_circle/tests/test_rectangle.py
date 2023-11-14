from models.rectangle import Rectangle
from models.base import Base
import io
import sys
import unittest


class TestRectangleInit(unittest.TestCase):
    def test_parent_class(self):
        r1 = Rectangle(1, 1)

        self.assertTrue(type(r1), Base)

    def test_id(self):
        r1 = Rectangle(1, 1)
        r2 = Rectangle(1, 1)
        self.assertEqual(r2.id, r1.id + 1)

        r3 = Rectangle(1, 1, 1, 1, 5)
        self.assertEqual(r3.id, 5)

    def test_width(self):
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.width, 1)

        with self.assertRaises(TypeError):
            r2 = Rectangle("Hello", 2)

        with self.assertRaises(ValueError):
            r2 = Rectangle(0, 2)
        with self.assertRaises(ValueError):
            r2 = Rectangle(-1, 2)

    def test_height(self):
        r1 = Rectangle(3, 4)
        self.assertEqual(r1.height, 4)

        with self.assertRaises(TypeError):
            r2 = Rectangle(3, "World")

        with self.assertRaises(ValueError):
            r2 = Rectangle(3, 0)
        with self.assertRaises(ValueError):
            r2 = Rectangle(3, -4)

    def test_x(self):
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.x, 0)

        r2 = Rectangle(1, 2, 3, 4)
        self.assertEqual(r2.x, 3)

        with self.assertRaises(TypeError):
            r3 = Rectangle(1, 2, "Hello", 1)

        with self.assertRaises(ValueError):
            r3 = Rectangle(0, 2, -1, 2)

    def test_y(self):
        r1 = Rectangle(3, 4)
        self.assertEqual(r1.y, 0)

        r2 = Rectangle(1, 2, 3, 4)
        self.assertEqual(r2.y, 4)

        with self.assertRaises(TypeError):
            r3 = Rectangle(1, 2, 3, "Hello")

        with self.assertRaises(ValueError):
            r3 = Rectangle(1, 0, 1, -2)


class TestRectangleMethods(unittest.TestCase):
    def test_area(self):
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(1, 5, 1, 1, 1)
        self.assertEqual(r2.area(), 5)

    def test_str(self):
        output = io.StringIO()
        sys.stdout = output

        r1 = Rectangle(4, 6, 2, 1, 12)
        print(r1)
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "[Rectangle] (12) 2/1 - 4/6\n")

    def test_display(self):
        r1 = Rectangle(1, 1)
        r2 = Rectangle(2, 2, 2, 2, 5)

        output = io.StringIO()
        sys.stdout = output
        r1.display()
        self.assertEqual(output.getvalue(), "#\n")

        output = io.StringIO()
        sys.stdout = output
        r2.display()
        self.assertEqual(output.getvalue(), "\n\n  ##\n  ##\n")
