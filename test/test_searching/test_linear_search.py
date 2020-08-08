import unittest
from random import randint, choice

from source.algorithm.searching.linear_searching import linear_searching

class TestLinearSearch(unittest.TestCase):

    def test_case_1(self):
        input_list = sorted([randint(i, 50) for i in range(20)])
        element = choice(input_list)

        self.assertEqual(linear_searching(input_list, element), input_list.index(element) )

    def test_case_2(self):
        input_list = [1, 2, 3, 4, 5, 6, 7]

        self.assertEqual(linear_searching(input_list, 10), None )



if __name__ == '__main__':
    unittest.main()
