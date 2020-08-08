import unittest
from source.algorithm.sorting.insertion_sort import insertion_sort

class TestInsertionSort(unittest.TestCase):

    def test_case_1(self):
        input = [64, 82, 100, 34, 25, 12, 22, 11, 90]
        sorted_array = None
        for i in input:
            sorted_array = insertion_sort(i, sorted_array)

        expected_output = sorted(input)
        self.assertEqual(sorted_array, expected_output)


if __name__ == '__main__':
    unittest.main()
