import unittest
from source import decorator

class TestDecorator(unittest.TestCase):

    def test_func(self):
        self.assertEqual(decorator.func(4), 16)


if __name__ == '__main__':
    unittest.main()