class BinaryTreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
            
    def pre_order_traversal(self):
        print (self.value)

        if self.left:
            self.left.pre_order_traversal()
            
        if self.right:
            self.right.pre_order_traversal()
            
    def in_order_traversal(self):
        if self.left:
            self.left.in_order_traversal()
        print (self.value)
        
        if self.right:
            self.right.in_order_traversal()
            
    def post_order_traversal(self):
        if self.left:
            self.left.in_order_traversal()
        
        if self.right:
            self.right.in_order_traversal()
        
        print (self.value)
            
    def print_traversal(self, traversal):
        if traversal == 'pre_order':
            self.pre_order_traversal()
        elif traversal == 'in_order':
            self.in_order_traversal()
        elif traversal == 'post_order':
            self.post_order_traversal()

def create_tree():
    root = BinaryTreeNode(1)

    root.left = BinaryTreeNode(2)
    root.right = BinaryTreeNode(3)
    root.left.left = BinaryTreeNode(4)
    root.left.right = BinaryTreeNode(5)
    root.right.left = BinaryTreeNode(6)
    root.right.right = BinaryTreeNode(7)
    root.left.left.left = BinaryTreeNode(8)
    root.left.left.right = BinaryTreeNode(9)
    root.left.right.left = BinaryTreeNode(10)
    root.left.right.right = BinaryTreeNode(11)
    root.right.left.left = BinaryTreeNode(12)
    root.right.left.right = BinaryTreeNode(13)
    root.right.right.left = BinaryTreeNode(14)
    root.right.right.right = BinaryTreeNode(15)

    return root
    

if __name__ == "__main__":
    tree = create_tree()
    tree.print_traversal('in_order')
    tree.print_traversal('pre_order')
    tree.print_traversal('post_order')
