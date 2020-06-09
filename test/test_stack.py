import unittest
from random import randint
from source.data_structures import my_stack


class TestStack(unittest.TestCase):

    def test_stack_case_1(self):
        stack = my_stack.Stack()
        i = randint(0, 20)
        stack.push(i)
        self.assertEqual(stack.pop(), i)

    def test_stack_case_2(self):
        stack = my_stack.Stack()
        i = randint(0, 20)
        stack.push(i)
        self.assertEqual(stack.pop(), i)

    def test_stack_case_3(self):
        stack = my_stack.Stack()
        i = randint(0, 20)
        stack.push(i)
        self.assertEqual(stack.pop(), i)

    def test_stack_case_4(self):
        stack = my_stack.Stack()
        i = randint(0, 20)
        stack.push(i)
        self.assertEqual(stack.pop(), i)


if __name__ == '__main__':
    unittest.main()