import unittest
from source.algorithm.sorting.insertion_sort import insertion_sort

class TestBubbleSort(unittest.TestCase):

    def test_case_1(self):
        input = [64, 82, 100, 34, 25, 12, 22, 11, 90]
        expected_output = sorted(input)
        self.assertEqual(insertion_sort(input), expected_output)

    def test_case_2(self):
        self.assertEqual(insertion_sort([1, 2, 3]), [1, 2, 3])


if __name__ == '__main__':
    unittest.main()
