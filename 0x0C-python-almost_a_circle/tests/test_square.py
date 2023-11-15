from models.square import Square
from models.rectangle import Rectangle
from models.base import Base
import sys
import unittest
from helper import print_io


class TestSquareInit(unittest.TestCase):
    def test_init(self):
        self.assertTrue(type(Square(1)), Rectangle)

        self.assertEqual(Square(1, 2, 4, 5).id,  5)

    def test_size(self):
        s1 = Square(1)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.width, s1.height)
