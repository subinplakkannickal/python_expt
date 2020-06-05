

class Stack(object):
    def __init__(self):
        self._items = []

    def __repr__(self):
        return "Stack({})".format(self._items)

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self._items:
            return self._items.pop()

    @property
    def top(self):
        if self._items:
            return self._items[-1]