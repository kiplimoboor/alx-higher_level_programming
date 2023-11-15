from models.square import Square
from models.rectangle import Rectangle
from models.base import Base
import sys
import unittest
from helper import print_io


class TestSquareInit(unittest.TestCase):
    def test_parent(self):
        s = Square(1)
        r = Rectangle(1, 1)

        self.assertTrue(type(s), Rectangle)
        self.assertEqual(s.__dict__.keys(), r.__dict__.keys())

    def test_id(self):
        s1 = Square(1)
        s2 = Square(1)
        self.assertEqual(s2.id, s1.id + 1)

        self.assertEqual(Square(1, 2, 4, 5).id,  5)

    def test_size(self):
        s1 = Square(1)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.width, s1.height)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("Hello",)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1)


class TestSquareDisplay(unittest.TestCase):

    def test_str(self):
        s = Square(3, 0, 0, 1)
        self.assertEqual(print_io(s), "[Square] (1) 0/0 - 3\n")

        s = Square(5, 7, 10, 10)
        self.assertEqual(print_io(s), "[Square] (10) 7/10 - 5\n")

    def test_display(self):
        self.assertEqual(print_io(Square(2), "display"), "##\n##\n")

        s = Square(2, 2, 2, 5)
        self.assertEqual(print_io(s, "display"), "\n\n  ##\n  ##\n")
