class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class DoublyLinkedList(object):
    def __init__(self):
        self.head = None
        self.node = None
        self.prev = None

    def add(self, value):
        """ Adding nodes
        """
        node = Node(value)

        if not self.head:
            self.head = node
        
        self.head.prev = node

        if self.node:
            node.prev = self.node
            self.node.next = node

        self.node = node
        self.node.next = self.head

    def rev_get(self, iter_count):
        """ Get in backward direction.
        """
        yield self.head.value
        prev_node = self.head.prev
        for i in range(iter_count):
            if prev_node:
                yield prev_node.value
                prev_node = prev_node.prev

    def get(self, iter_count):
        """ Get in forward direction.
        """
        yield self.head.value
        next_node = self.head.next
        for i in range(iter_count):
            if next_node:
                yield next_node.value
                next_node = next_node.next
        

if __name__ == "__main__":
    """ elements = [1,2,3,4,5,6,7,8,9]
    """

    linkedlist = DoublyLinkedList()
    elements = (0,1,2,3,4,5,6,7,8,9)
    for i in elements:
        linkedlist.add(i)

    linkedlist_values = linkedlist.get(20)
    for i in linkedlist_values:
        print (i)

    
