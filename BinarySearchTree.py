from pyfiglet import figlet_format
from termcolor import cprint


class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class BSTree:
    def __init__(self, root=None):
        self.root = root

    def isleaf(self, node: Node):
        if all(map(lambda s: s == None, (node.right, node.left))):
            return True
        else:
            return False

    def create(self, data):
        if self.root == None:
            self.root = Node(data)
        elif self.root.data == None:
            self.root.data = data
        else:
            self.__create(self.root, data)

    def search(self, data):
        return self.__search(self.root, data)

    def index(self, data):
        self.__index(self.root, data)

    def delete(self, key):
        if key == self.root.data:
            if self.isleaf(self.root) == True:
                self.root = Node()
            else:
                if self.root.right == None:
                    self.root = self.root.left
                elif self.root.left == None:
                    self.root = self.root.right
                else:
                    # rplace = self.maxValNode(self.root.left)
                    # self.__del(self.root, rplace.data)
                    # left = self.root.left
                    # right = self.root.right
                    # rplace.left = left
                    # rplace.right = right
                    # self.root = rplace
                    rplace = self.minValNode(self.root.right)
                    self.__del(self.root, rplace.data)
                    left = self.root.left
                    right = self.root.right
                    rplace.left = left
                    rplace.right = right
                    self.root = rplace
        else:
            self.__del(self.root, key)

    def insert(self, data):
        if self.__search(self.root, data) == None:
            self.__create(self.root, data)
        else:
            print('Data is already in node.')

    def maxValNode(self, node, var=0):
        if var == 0:
            var = node.data
            return self.maxValNode(node.right, var)
        elif node == None:
            return Node(var)
        elif node.data > var:
            var = node.data
            return self.maxValNode(node.right, var)
        else:
            return self.maxValNode(node.right, var)

    def minValNode(self, node: Node, var=0):
        if var == 0:
            var = node.data
            return self.minValNode(node.left, var)
        elif node == None:
            return Node(var)
        elif node.data < var:
            var = node.data
            return self.minValNode(node.left, var)
        else:
            return self.minValNode(node.left, var)

    def __index(self, node: Node, data, var=0):
        if node.data == data:
            cprint(f'Node: {node.data}', 'magenta')
            cprint('left: {}'.format(None if node.left ==
                   None else node.left.data), 'yellow')
            print('right: ', None if node.right == None else node.right.data)
        elif node.data > data:
            return self.__index(node.left, data, var+1)
        else:
            return self.__index(node.right, data, var+1)

    def __search(self, node: Node, data):
        if node.data == data:
            return True
        elif node.data > data:
            return self.__search(node.left, data)
        else:
            return self.__search(node.right, data)

    def __create(self, node: Node, data):
        newNode = Node(data)
        if node.data > data:
            if node.left == None:
                node.left = newNode
            else:
                self.__create(node.left, data)
        elif node.data < data:
            if node.right == None:
                node.right = newNode
            else:
                self.__create(node.right, data)

    def __del(self, node: Node, key):
        if key < node.data:
            if node.left.data == key:
                # * Case 1
                if self.isleaf(node.left) == True:
                    node.left = None
                else:
                    # * Case 2
                    if node.left.left == None:
                        node.left = node.left.right
                    elif node.left.right == None:
                        node.left = node.left.left
                    # *Case 3
                    else:
                        # *Case 3.1
                        # rplace = self.maxValNode(node.left.left)
                        # self.__del(node.left, rplace.data)
                        # left = node.left.left
                        # right = node.left.right
                        # rplace.left = left
                        # rplace.right = right
                        # node.left = rplace
                        # *Case 3.2
                        rplace = self.minValNode(node.left.right)
                        self.__del(node.left, rplace.data)
                        left = node.left.left
                        right = node.left.right
                        rplace.left = left
                        rplace.right = right
                        node.left = rplace
            else:
                self.__del(node.left, key)
        elif key > node.data:
            if node.right.data == key:
                # * Case 1
                if self.isleaf(node.right) == True:
                    node.right = None
                else:
                    # * Case 2
                    if node.right.right == None:
                        node.right = node.right.left
                    elif node.right.left == None:
                        node.right = node.right.right
                    # *Case 3
                    else:
                        # *Case 3.1
                        # rplace = self.maxValNode(node.right.left)
                        # self.__del(node.right, rplace.data)
                        # right = node.right.right
                        # left = node.right.left
                        # rplace.left = left
                        # rplace.right = right
                        # node.right = rplace
                        # *Case 3.2
                        rplace = self.minValNode(node.right.right)
                        self.__del(node.right, rplace.data)
                        left = node.right.left
                        right = node.right.right
                        rplace.left = left
                        rplace.right = right
                        node.right = rplace

            else:
                self.__del(node.right, key)


if __name__ == '__main__':
    bstree = BSTree()
    list_number = [25, 8, 53, 4, 42, 37, 31, 39, 86, 64, 99]
    for i in list_number:
        bstree.create(i)
