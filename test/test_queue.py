import unittest
from random import randint
from source.data_structures import my_queue


class TestQueue(unittest.TestCase):

    def test_queue_case_1(self):
        queue = my_queue.Queue()
        i = randint(0, 20)
        queue.enqueue(i)
        self.assertEqual(queue.dequeue(), i)

    def test_queue_case_2(self):
        queue = my_queue.Queue()
        i = randint(0, 20)
        queue.enqueue(i)
        self.assertEqual(queue.dequeue(), i)

    def test_queue_case_3(self):
        queue = my_queue.Queue()
        i = randint(0, 20)
        queue.enqueue(i)
        self.assertEqual(queue.dequeue(), i)

    def test_queue_case_4(self):
        queue = my_queue.Queue()
        i = randint(0, 20)
        queue.enqueue(i)
        self.assertEqual(queue.dequeue(), i+ 1)


if __name__ == '__main__':
    unittest.main()