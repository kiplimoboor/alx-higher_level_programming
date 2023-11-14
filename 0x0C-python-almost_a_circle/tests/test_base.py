import unittest
from models.base import Base


class TestBaseInit(unittest.TestCase):
    def test_no_args(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_with_args(self):
        b1 = Base(10)
        b2 = Base(100)
        self.assertEqual(b1.id, 10)
        self.assertEqual(b2.id, 100)

    def test_with_none(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b2.id, b1.id + 1)

    def test_with_other_type_arg(self):
        self.assertEqual(Base("Hello").id, "Hello")
        self.assertEqual(Base([1, 2, 3]).id, [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
