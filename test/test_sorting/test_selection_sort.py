import unittest
from source.algorithm.sorting.selection import selection_sorting

class TestSelectionSort(unittest.TestCase):

    def test_case_1(self):
        input = [64, 82, 100, 34, 25, 12, 22, 11, 90]
        expected_output = sorted(input)
        self.assertEqual(selection_sorting(input), expected_output)

    def test_case_2(self):
        self.assertEqual(selection_sorting([1, 2, 3]), [1, 2, 3])


if __name__ == '__main__':
    unittest.main()
