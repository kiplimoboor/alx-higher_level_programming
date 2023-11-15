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
        s = Square(1)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.width, s.height)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("Hello")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.size = "Hello"

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.size = 0

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.size = -1


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


class TestSquareUpdate(unittest.TestCase):
    def test_update_with_args(self):
        s = Square(1, 3, 5, 25)
        self.assertEqual(print_io(s), "[Square] (25) 3/5 - 1\n")

        s.update(4)
        self.assertEqual(print_io(s), "[Square] (4) 3/5 - 1\n")

        s.update(4, 5, 4)
        self.assertEqual(print_io(s), "[Square] (4) 4/5 - 5\n")

        s.update(4, 5, 4, 4)
        self.assertEqual(print_io(s), "[Square] (4) 4/4 - 5\n")

    def test_update_with_kwargs(self):
        s = Square(10, 3, 5, 25)
        self.assertEqual(print_io(s), "[Square] (25) 3/5 - 10\n")

        s.update(size=5, x=10, y=21, id=3)
        self.assertEqual(print_io(s), "[Square] (3) 10/21 - 5\n")

    def test_update_with_args_and_kwargs(self):
        s = Square(10, 3, 5, 25)
        self.assertEqual(print_io(s), "[Square] (25) 3/5 - 10\n")

        args = 1, 3, 4, 3
        kwargs = {"size": 5, "x": 10, "y": 21, "id": 3}
        s.update(*args, **kwargs)
        self.assertEqual(print_io(s), "[Square] (1) 4/3 - 3\n")


class TestSquareRepresentations(unittest.TestCase):
    def test_to_dictionary(self):
        s1 = Square(10, 2, 1)
        s1_dict = s1.to_dictionary()
        self.assertTrue(type(s1_dict) == dict)

        s2 = Square(1)
        s2.update(**s1_dict)
        s2_dict = s2.to_dictionary()
        self.assertTrue(type(s2_dict) == dict)

        self.assertEqual(s1_dict, s2_dict)
