class TreeNode(object):

    def __init__(self, name):
        self.name = name
        self.children = []
        self._parent = None
        self._level = 0

    @property
    def parent(self):
        return self._parent
    
    @property
    def level(self):
        return self._level

    def add_children(self, node):
        node._parent = self
        node._level = self.level + 1 
            
        self.children.append(node)
        
    def plot_tree(self):
        print ("{}- {}".format("\t|" * self.level, self.name))
        for child in self.children:
            child.plot_tree()


def create_tree():
    tree = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    tree.add_children(laptop)

    mac = TreeNode("mac")
    laptop.add_children(mac)

    surface = TreeNode("surface")
    laptop.add_children(surface)

    thinkpad = TreeNode("thinkpad")
    laptop.add_children(thinkpad)

    camera = TreeNode("camera")
    tree.add_children(camera)

    samsung = TreeNode("samsung")
    camera.add_children(samsung)

    canon = TreeNode("canon")
    camera.add_children(canon)

    nikon = TreeNode("nikon")
    camera.add_children(nikon)
    
    tv = TreeNode("TV")
    tree.add_children(tv)

    samsung = TreeNode("samsung")
    tv.add_children(samsung)

    panasonic = TreeNode("panasonic")
    tv.add_children(panasonic)

    sony = TreeNode("sony")
    tv.add_children(sony)
    return tree

if __name__ == "__main__":
    tree = create_tree()
    tree.plot_tree()

