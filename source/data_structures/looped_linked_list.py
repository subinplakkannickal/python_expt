""" Adding a new attribute id in each node and it will be unique in linked list.
Considering that id of a node will be always less than id of next node.
The loop checking is in base of id, which id of a node id greater than next node means that thee current node is linked to a previous node
"""

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.id = None

class LinkedList(object):
    def __init__(self):
        self.head = None
        self._node = None

    def add_node(self, node):
        """ Adding nodes.
        """
        if not self.head:
            self.head = node
            self.head.id = 0

        if self._node:
            self._node.next = node
            node.id = self._node.id + 1

        self._node = node
        
def loop_checker(linked_list):
    node = linked_list.head

    while node.next:
        if node.id > node.next.id:
            return True
        
        node = node.next
    
    return False

if __name__ == "__main__":
    linked_list = LinkedList()
    # Creating nodes with following values
    for i in [10, 20, 30, 40, 50]:
        node = Node(i)
        linked_list.add_node(node)

    # Creating a loop in linked list
    node.next = linked_list.head.next.next

    loop = loop_checker(linked_list)
    print(loop)
