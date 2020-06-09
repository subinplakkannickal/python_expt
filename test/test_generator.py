import unittest
from source import generator

class TestGenerator(unittest.TestCase):

    def test_generator_case_1(self):
        self.assertEqual(sum(generator.firstn(10)), 45)

    def test_generator_case_2(self):
        self.assertEqual(sum(generator.firstn(100)), 4950)

    def test_generator_case_3(self):
        self.assertEqual(sum(generator.FirstN(10)), 45)

    def test_generator_case_4(self):
        self.assertEqual(sum(generator.FirstN(100)), 4950)


if __name__ == '__main__':
    unittest.main()