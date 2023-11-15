from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os
import io
import unittest


class TestBaseInit(unittest.TestCase):
    def test_with_no_args(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_with_args(self):
        b1 = Base(10)
        b2 = Base(100)
        self.assertEqual(b1.id, 10)
        self.assertEqual(b2.id, 100)


class TestBaseRepresentations(unittest.TestCase):
    def test_to_json_string(self):
        r = Rectangle(10, 7, 2, 8)
        dictionary = r.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertTrue(type(json_dictionary) == str)

        s = Square(10, 2, 4)
        dictionary = s.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertTrue(type(json_dictionary) == str)
