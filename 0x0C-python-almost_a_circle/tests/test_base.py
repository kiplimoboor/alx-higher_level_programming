from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from helper import print_io
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
        self.assertTrue(type(json_dictionary) is str)

        s = Square(10, 2, 4)
        dictionary = s.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertTrue(type(json_dictionary) is str)

    def test_from_json_string(self):
        list_input = [Rectangle(10, 20).to_dictionary()]
        json_list = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list)

        self.assertTrue(type(json_list) is str)
        self.assertEqual(list_input, list_output)

    def test_create(self):
        r1 = Rectangle(3, 5, 1, 4, 6)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)

        self.assertTrue(type(r2) is Rectangle)
        self.assertEqual(print_io(r1, "display"), print_io(r2, "display"))


class TestFileRepresentations(unittest.TestCase):
    def test_save_to_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        filename = "Rectangle.json"

        with self.assertRaises(FileNotFoundError):
            with open(filename, 'r') as file:
                file.read()

        Rectangle.save_to_file([r1, r2])
        self.assertTrue(os.path.exists(filename))
