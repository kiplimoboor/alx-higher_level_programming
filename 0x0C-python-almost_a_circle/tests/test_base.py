from models.base import Base

import unittest


def setUpModule():
    print("setup module")


def tearDownModule():
    print("teardown module")


class TestBase(unittest.TestCase):
    def setUp(self):
        print("setUp")
        self.b1 = Base()
        self.b2 = Base()
        self.b3 = Base(10)
        self.b4 = Base()

    def tearDown(self):
        print("tearDown")
        del self.b1
        del self.b2
        del self.b3
        del self.b4

    @classmethod
    def setUpClass(cls):
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    def test_init(self):
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b3.id, 10)
        self.assertEqual(self.b4.id, 3)


if __name__ == "__main__":
    unittest.main()
