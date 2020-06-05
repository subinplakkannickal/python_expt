import queue

class BinaryTreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
            
def pre_order_traversal(root):
    """ Visit nodes in pre order method.
    """
    print (root.value)

    if root.left:
        pre_order_traversal(root.left)
        
    if root.right:
        pre_order_traversal(root.right)
        
def in_order_traversal(root):
    """ Visit nodes in in order method.
    """
    if root.left:
        in_order_traversal(root.left)

    print (root.value)
    
    if root.right:
        in_order_traversal(root.right)
        
def post_order_traversal(root):
    """ Visit nodes in post order method.
    """
    if root.left:
        post_order_traversal(root.left)
    
    if root.right:
        post_order_traversal(root.right)
    
    print (root.value)

def level_order_traversal(root):
    """ Visit nodes in level order method.
    """
    _queue = queue.Queue()
    _queue.put(root)
    
    while not _queue.empty():
        node = _queue.get()

        print(node.value)

        if node.left:
            _queue.put(node.left)

        if node.right:
            _queue.put(node.right)


        
def print_traversal(traversal, root):
    if traversal == 'pre_order':
        pre_order_traversal(root)
    elif traversal == 'in_order':
        in_order_traversal(root)
    elif traversal == 'post_order':
        post_order_traversal(root)
    elif traversal == 'level_order':
        level_order_traversal(root)

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

    # root.right = BinaryTreeNode(2)
    # root.right.right = BinaryTreeNode(5)
    # root.right.right.left = BinaryTreeNode(3)
    # root.right.right.right = BinaryTreeNode(6)
    # root.right.right.left.right = BinaryTreeNode(4)

    return root
    

if __name__ == "__main__":
    tree = create_tree()
    print_traversal('in_order', tree)
    print ("==========")
    print_traversal('pre_order', tree)
    print ("==========")
    print_traversal('post_order', tree)
    print ("==========")
    print_traversal('level_order', tree)
