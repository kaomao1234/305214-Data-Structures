class BNode:
    def __init__(self,leaf=False):
        self.leaf = leaf
        self.keys = []
        self.child = []
class BTree:
    def __init__(self,order:int):
        self.root = BNode(True)
        self.order = order
    # - This function splits a node to create a parent node.
    def split_child(self,node:BNode):
        set_lengt = self.order-1
if __name__ == '__main__':
    btree = BTree(3)
    btree.root.keys = [2,3,6]
    btree.split_child(btree.root)
    print(btree.root.keys)