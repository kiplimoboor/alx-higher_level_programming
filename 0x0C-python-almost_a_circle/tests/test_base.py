import unittest
from models.base import Base


class TestBaseInit(unittest.TestCase):
    def test_no_args(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_with_args(self):
        b1 = Base(1)
        b2 = Base(10)
        b3 = Base(100)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 10)
        self.assertEqual(b3.id, 100)


if __name__ == "__main__":
    unittest.main()
