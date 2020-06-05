class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class CircularLinkedList(object):
    def __init__(self):
        self.head = None
        self.node = None

    def add(self, value):
        """ Adding nodes.
        """
        node = Node(value)

        if not self.head:
            self.head = node
        
        if self.node:
            self.node.next = node

        self.node = node
        self.node.next = self.head

    def get(self, iter_count):
        """ Getting nodes.
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

    linkedlist = CircularLinkedList()
    elements = (0,1,2,3,4,5,6,7,8,9)
    for i in elements:
        linkedlist.add(i)

    linkedlist_values = linkedlist.get(20)
    for i in linkedlist_values:
        print (i)

    
