import unittest
from random import randint, choice

from source.algorithm.searching.binary_searching import binary_searching

class TestBinarySearch(unittest.TestCase):

    def test_case_1(self):
        input_list = sorted([randint(i, 50) for i in range(20)])
        element = choice(input_list)

        self.assertEqual(binary_searching(input_list, element), input_list.index(element) )



if __name__ == '__main__':
    unittest.main()
