import unittest
from source import decorator

class TestDecorator(unittest.TestCase):

    def test_decorator_case_1(self):
        self.assertEqual(decorator.func(0), 0)

    def test_decorator_case_2(self):
        self.assertEqual(decorator.func(1), 1)

    def test_decorator_case_3(self):
        self.assertEqual(decorator.func(2), 4)

    def test_decorator_case_4(self):
        self.assertEqual(decorator.func(3), 9)


if __name__ == '__main__':
    unittest.main()