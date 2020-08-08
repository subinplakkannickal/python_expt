import unittest
from source import decorator

class TestDecorator(unittest.TestCase):

    def test_func_1(self):
        self.assertEqual(decorator.func(4), 16)

    def test_func_2(self):
        self.assertNotEqual(decorator.func(4), 25)

    def test_func_3(self):
        self.assertNotEqual(decorator.func(4), 0)


if __name__ == '__main__':
    unittest.main()
