import unittest
from random import randint
from source.problem_solvinig import fibonacci


class TestFibonacci(unittest.TestCase):

    def test_fibonacci_1(self):
        fib = fibonacci.fibonacci(0)
        self.assertEqual(fib, 1)

    def test_fibonacci_2(self):
        fib = fibonacci.fibonacci(10)
        self.assertEqual(fib, 89)

    def test_factorial_1(self):
        fib = fibonacci.factorial(0)
        self.assertEqual(fib, 1)

    def test_factorial_2(self):
        fib = fibonacci.factorial(10)
        self.assertEqual(fib, 3628800)


if __name__ == '__main__':
    unittest.main()
