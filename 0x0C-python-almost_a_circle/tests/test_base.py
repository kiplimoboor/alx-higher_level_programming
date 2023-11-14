import unittest
from models.base import Base


def setUpModule():
    print("setup module")


def tearDownModule():
    print("teardown module")


class TestFib(unittest.TestCase):

    def setUp(self):
        print("setUp")
        self.b1 = Base()
        self.b2 = Base()
        self.b3 = Base(10)
        self.b4 = Base()
        self.b5 = Base(100)
        self.b6 = Base("String")

    def tearDown(self):
        print("tearDown")
        del self.b1
        del self.b2
        del self.b3
        del self.b4
        del self.b5
        Base.reset()

    @classmethod
    def setUpClass(cls):
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    def test_no_args(self):
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b4.id, 3)

    def test_args(self):
        self.assertEqual(self.b3.id, 10)
        self.assertEqual(self.b5.id, 100)
        self.assertEqual(self.b6.id, "String")
        self.assertEqual(Base(2.4).id, 2.4)

    def test_no_args_plus_args(self):
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b3.id, 10)
        self.assertEqual(self.b4.id, 3)

    def test_change_id(self):
        self.b1.id = 10
        self.assertEqual(self.b1.id, 10)
        self.b2.id = "String"
        self.assertEqual(self.b2.id, "String")

    def test_private_instance_access(self):
        with self.assertRaises(AttributeError):
            instances = self.b1.__nb_instances


if __name__ == "__main__":
    unittest.main()
