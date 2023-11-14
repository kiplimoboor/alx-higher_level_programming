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


if __name__ == "__main__":
    unittest.main()
