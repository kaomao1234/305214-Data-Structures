class Node:
    def __init__(self, data=None):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
    
class BSTree:
    def __init__(self,root=None):
        self.root = root
    
    def __add(self,node:Node,data):
        pass
if __name__ == '__main__':
    bstree= BSTree()
    bstree.root = Node(8) 