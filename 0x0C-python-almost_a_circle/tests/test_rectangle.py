import unittest

from models.rectangle import Rectangle
from models.base import Base


class TestRectangleInite(unittest.TestCase):
    def test_parent_class(self):
        r1 = Rectangle(1, 1)

        self.assertTrue(type(r1), Base)

    def test_id(self):
        r1 = Rectangle(1, 1)
        r2 = Rectangle(1, 1)
        self.assertEqual(r2.id, r1.id + 1)

        r3 = Rectangle(1, 1, 1, 1, 5)
        self.assertEqual(r3.id, 5)

    def test_width_height(self):
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)

        with self.assertRaises(TypeError):
            r2 = Rectangle("Hello", 2)
        with self.assertRaises(TypeError):
            r2 = Rectangle(2, "World")

        with self.assertRaises(ValueError):
            r2 = Rectangle(0, 2)
        with self.assertRaises(ValueError):
            r2 = Rectangle(1, 0)

        with self.assertRaises(ValueError):
            r2 = Rectangle(0, 2)
        with self.assertRaises(ValueError):
            r2 = Rectangle(1, 0)

    def test_x_y(self):
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

        r2 = Rectangle(1, 2, 3, 4)
        self.assertEqual(r2.x, 3)
        self.assertEqual(r2.y, 4)

        with self.assertRaises(TypeError):
            r3 = Rectangle(1, 2, "Hello", 1)
        with self.assertRaises(TypeError):
            r3 = Rectangle(1, 2, 3, "Hello")

        with self.assertRaises(ValueError):
            r3 = Rectangle(0, 2, -1, 2)
        with self.assertRaises(ValueError):
            r3 = Rectangle(1, 0, 1, -2)
