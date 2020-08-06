import unittest
from random import randint
from source.data_structures import my_stack


class TestStack(unittest.TestCase):

    def test_pop(self):
        stack = my_stack.Stack()
        i = randint(0, 20)
        stack.push(i)
        self.assertEqual(stack.pop(), i)

    def test_top(self):
        stack = my_stack.Stack()
        i = randint(0, 30)
        stack.push(i)
        self.assertEqual(stack.top, i)

    def test_push(self):
        stack = my_stack.Stack()
        i = randint(0, 20)
        stack.push(i)
        self.assertEqual(stack._items, [i])

    def test_pop_2(self):
        stack = my_stack.Stack()
        i = randint(0, 20)
        stack.push(i)
        self.assertEqual(stack._items, [i])
        stack.pop()
        self.assertEqual(stack._items, [])


if __name__ == '__main__':
    unittest.main()
