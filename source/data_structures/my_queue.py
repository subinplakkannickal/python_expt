
class Queue(object):
    def __init__(self):
        self._items = []

    def __repr__(self):
        return "Queue({})".format(self._items)

    def enqueue(self, item):
        self._items.insert(0, item)

    def dequeue(self):
        if self._items:
            return self._items.pop()

    def is_empty(self):
        return self._items == []

    @property
    def peek(self):
        if self._items:
            return self._items[-1]
    
    @property
    def size(self):
        return len(self._items)

    