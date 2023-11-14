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


# class TestBaseMethods(unittest.TestCase):
#     def test_to_json_string(self):
#         r1 = Rectangle(10, 2, 4, 5, 2)
#         s1 = Square(1, 2, 2, 3)

#         r1_dict = r1.to_dictionary()
#         self.assertTrue(type(r1_dict) is dict)
#         s1_dict = s1.to_dictionary()
#         self.assertTrue(type(s1_dict) is dict)

#         json_dict = Base.to_json_string([r1_dict])
#         self.assertTrue(type(json_dict) is str)

#         json_dict = Base.to_json_string([s1_dict])
#         self.assertTrue(type(json_dict) is str)

#         json_dict = Base.to_json_string([r1_dict, s1_dict])
#         self.assertTrue(type(json_dict) is str)

#         json_dict = Base.to_json_string([])
#         self.assertTrue(json_dict == "[]")

#     def test_save_to_file(self):
#         r1 = Rectangle(10, 7, 2, 8)
#         r2 = Rectangle(2, 4)

#         filename = "Rectangle.json"

#         self.assertFalse(os.path.exists(filename))

#         Rectangle.save_to_file([r1, r2])

#         self.assertTrue(os.path.exists(filename))
#         os.remove(filename)
