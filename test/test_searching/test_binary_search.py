import unittest
from random import randint, choice

from source.algorithm.searching.binary_searching import binary_searching

class TestBinarySearch(unittest.TestCase):

    def test_case_1(self):
        input_list = [8, 8, 10, 11, 15, 18, 21, 22, 26, 31, 34, 34, 36, 37, 40, 41, 42, 46, 48, 49]
        element = 22
        self.assertEqual(binary_searching(input_list, element), input_list.index(element) )

if __name__ == '__main__':
    unittest.main()
