import unittest
from source import generator

class TestGenerator(unittest.TestCase):

    def test_firstn(self):
        self.assertEqual(sum(generator.firstn(10)), 45)

    def test_FirstN(self):
        self.assertEqual(sum(generator.FirstN(10)), 45)


if __name__ == '__main__':
    unittest.main()