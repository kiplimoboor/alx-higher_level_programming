from models.square import Square
from models.rectangle import Rectangle
from models.base import Base
import sys
import unittest
from helper import print_io


class TestSquareInit(unittest.TestCase):
    def test_parent_class(self):
        self.assertTrue(type(Square(1, 1)), Rectangle)

    def test_id(self):
        s1 = Square(1)
        s2 = Square(1)
        self.assertEqual(s2.id, s1.id + 1)

        self.assertEqual(Square(1, 1, 1, 5).id, 5)

    def test_attr(self):
        s = Square(1)
        r = Rectangle(1, 1)
        self.assertEqual(s.__dict__.keys(), r.__dict__.keys())

    def test_size(self):
        s = Square(1)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.width, 1)
        self.assertEqual(s.height, 1)

        with self.assertRaises(TypeError):
            Square("Hello")

        with self.assertRaises(ValueError):
            Square(0)
        with self.assertRaises(ValueError):
            Square(-1)
