class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.node = None

    def add_node(self, value):
        
        node = Node(value)
        if not self.head:
            self.head = node

        if self.node:
            self.node.next = node

        self.node = node

    def get_nodes(self):
        yield self.head.value
        next_node = self.head.next
        while True:
            if next_node:
                yield next_node.value
                next_node = next_node.next
            else: break
        

if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.add_node(10)
    linked_list.add_node(20)
    linked_list.add_node(30)
    linked_list.add_node(40)
    linked_list.add_node(50)
    list_values = linked_list.get_nodes()
    for i in list_values:
        print (i)
