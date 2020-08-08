import unittest
from source.algorithm.sorting.quick_sort import quick_sort

class TestQuickSort(unittest.TestCase):

    def test_case_1(self):
        input = [64, 82, 100, 34, 25, 12, 22, 11, 90]
        expected_output = sorted(input)
        self.assertEqual(quick_sort(input), expected_output)

    def test_case_2(self):
        self.assertEqual(quick_sort([1, 2, 3]), [1, 2, 3])


if __name__ == '__main__':
    unittest.main()
