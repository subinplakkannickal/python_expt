class BinarySearchTreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.search_result = False


    def insert(self, node):
                
        if self.value > node.value:
            if not self.left:
                self.left = node
            else:
                self.left.insert(node)
        
        elif self.value < node.value:
            if not self.right:
                self.right = node
            else:
                self.right.insert(node)
                
    def search(self, value):
        if self.value == value:
            return True
        
        if self.value > value and self.left:
             if self.left.search(value):
                return True
        
        elif self.value < value and self.right:
            if self.right.search(value):
                return True
        
        return False
        
def in_order_traversal(root):
    if root.left:
        in_order_traversal(root.left)

    print (root.value)
    
    if root.right:
        in_order_traversal(root.right)        

    
def add_node(tree, value):
    node = BinarySearchTreeNode(value)
    tree.insert(node)

def create_tree(elements_list):
    tree = None
    for i in elements_list:
        if not tree:
            tree = BinarySearchTreeNode(i)
        else:
            add_node(tree, i)

    return tree
    

if __name__ == "__main__":
    """ [8, 10, 3, 12, 1, 6, 5, 7, 11, 13, 2, 4, 9, 14, 15] 

                    8
                  /   \
                 /     \
                3       10
              /  \      / \
            1      6   9   12
             \    / \      / \
              2  5   7    11  13
                /               \
               4                14
                                  \
                                   15
                 
    """
    elements_list = [8, 10, 3, 12, 1, 6, 5, 7, 11, 13, 2, 4, 9, 14, 15]
    tree = create_tree(elements_list)
    in_order_traversal(tree)
    print(tree.search(100))
    add_node(tree, 100)
    print(tree.search(100))
    print(tree.search(0))
