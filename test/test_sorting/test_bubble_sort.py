import unittest
from source.algorithm.sorting.bubble_sort import bubble_sort, recursive_bubble_sort

class TestBubbleSort(unittest.TestCase):

    def test_case_1(self):
        input = [64, 82, 100, 34, 25, 12, 22, 11, 90]
        expected_output = sorted(input)
        self.assertEqual(bubble_sort(input), expected_output)

    def test_case_2(self):
        self.assertEqual(bubble_sort([1, 2, 3]), [1, 2, 3])


class TestRecursiveBubbleSort(unittest.TestCase):

    def test_case_1(self):
        input = [64, 82, 100, 34, 25, 12, 22, 11, 90]
        expected_output = sorted(input)
        self.assertEqual(recursive_bubble_sort(input), expected_output)

    def test_case_2(self):
        self.assertEqual(recursive_bubble_sort([1, 2, 3]), [1, 2, 3])


if __name__ == '__main__':
    unittest.main()
