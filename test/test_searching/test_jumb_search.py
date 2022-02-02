import unittest
from random import sample, choice
from math import sqrt

from source.algorithm.searching.jump_searching import jump_searching

class TestJumbSearch(unittest.TestCase):

    def test_case_1(self):
        input_list = sample(range(50), 20)
        input_list.sort()

        element, step = choice(input_list), int(sqrt(len(input_list)))
        print(input_list, element, step)

        self.assertEqual(jump_searching(input_list, element, step), input_list.index(element))

    def test_case_2(self):
        input_list = [0, 1, 2, 3, 4, 5, 6, 7]
        element, step = choice(input_list), int(sqrt(len(input_list)))
        print(element, step)

        self.assertEqual(jump_searching(input_list, element, step), input_list.index(element))



if __name__ == '__main__':
    unittest.main()
