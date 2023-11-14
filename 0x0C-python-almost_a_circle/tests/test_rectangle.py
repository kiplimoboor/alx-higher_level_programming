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


# class TestRectangleMethods(unittest.TestCase):
#     def test_area(self):
#         r1 = Rectangle(3, 2)
#         self.assertEqual(r1.area(), 6)

#         r2 = Rectangle(1, 5, 1, 1, 1)
#         self.assertEqual(r2.area(), 5)

#     def test_str(self):
#         r1 = Rectangle(3, 5, 0, 0, 1)
#         output = io.StringIO()
#         sys.stdout = output
#         print(r1)
#         self.assertEqual(output.getvalue(), "[Rectangle] (1) 0/0 - 3/5\n")

#         r2 = Rectangle(4, 6, 2, 1, 12)
#         output = io.StringIO()
#         sys.stdout = output
#         print(r2)
#         self.assertEqual(output.getvalue(), "[Rectangle] (12) 2/1 - 4/6\n")

#     def test_display(self):
#         r1 = Rectangle(1, 1)
#         output = io.StringIO()
#         sys.stdout = output
#         r1.display()
#         self.assertEqual(output.getvalue(), "#\n")

#         r2 = Rectangle(2, 2, 2, 2, 5)
#         output = io.StringIO()
#         sys.stdout = output
#         r2.display()
#         self.assertEqual(output.getvalue(), "\n\n  ##\n  ##\n")

#     def test_update_with_args(self):
#         r1 = Rectangle(1, 10, 3, 5, 25)
#         output = io.StringIO()
#         sys.stdout = output
#         print(r1)
#         self.assertEqual(output.getvalue(), "[Rectangle] (25) 3/5 - 1/10\n")

#         r1.update(1, 3, 2, 4, 3)
#         output = io.StringIO()
#         sys.stdout = output
#         print(r1)
#         self.assertEqual(output.getvalue(), "[Rectangle] (1) 4/3 - 3/2\n")

#     def test_update_with_kwargs(self):
#         r1 = Rectangle(1, 10, 3, 5, 25)

#         r1.update(height=5, x=10, width=15, y=21, id=3)
#         self.assertEqual(r1.id, 3)
#         self.assertEqual(r1.width, 15)
#         self.assertEqual(r1.height, 5)
#         self.assertEqual(r1.x, 10)
#         self.assertEqual(r1.y, 21)

#     def test_update_with_args_and_kwargs(self):
#         r1 = Rectangle(1, 10, 3, 5, 25)
#         args = 1, 3, 2, 4, 3
#         kwargs = {"height": 5, "x": 10, "width": 15, "y": 21, "id": 3}
#         r1.update(*args, **kwargs)

#         self.assertEqual(r1.id, 1)
#         self.assertEqual(r1.width, 3)
#         self.assertEqual(r1.height, 2)
#         self.assertEqual(r1.x, 4)
#         self.assertEqual(r1.y, 3)
