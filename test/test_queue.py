import unittest
from random import randint
from source.data_structures import my_queue


class TestQueue(unittest.TestCase):

    def test_dequeue(self):
        queue = my_queue.Queue()
        i = randint(0, 20)
        queue.enqueue(i)
        self.assertEqual(queue.dequeue(), i)

    def test_enqueue(self):
        queue = my_queue.Queue()
        i = randint(0, 20)
        queue.enqueue(i)
        self.assertEqual(queue._items, [i])

    def test_size(self):
        queue = my_queue.Queue()
        i = randint(0, 20)
        queue.enqueue(i)
        self.assertEqual(queue.size, 1)

    def test_peek(self):
        queue = my_queue.Queue()
        i = randint(0, 20)
        queue.enqueue(i)
        self.assertEqual(queue.peek, i)


if __name__ == '__main__':
    unittest.main()