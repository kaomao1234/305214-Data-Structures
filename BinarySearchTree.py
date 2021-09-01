from pyfiglet import figlet_format
from termcolor import cprint


class Node:
    def __init__(self, data=None):
        self.data = data
        self.parent = None
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
        else:
            self.__create(self.root, data)

    def search(self, data):
        return self.__search(self.root, data)

    def index(self, data):
        self.__index(self.root, data)

    def delete(self, key):
        self.__del(self.root, key)

    def insert(self, data):
        if self.__search(self.root, data) == None:
            self.__create(self.root, data)
        else:
            print('Data is already in node.')

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
                newNode.parent = node
                node.left = newNode
            else:
                self.__create(node.left, data)
        elif node.data < data:
            if node.right == None:
                newNode.parent = node
                node.right = newNode
            else:
                self.__create(node.right, data)

    def __del(self, node: Node, key):
        if key < node.data:
            #* Case 1
            if node.left.data == key and self.isleaf(node.left) == True:
                node.left = None
            #* Case 2
            elif node.left.data == key:
                if node.left.right != None:
                    node.left = node.left.right
                else:
                    node.left = node.left.left
            else:
                self.__del(node.left, key)
        elif key > node.data:
            #* Case 1
            if node.right.data == key and self.isleaf(node.right) == True:
                node.right = None
            #* Case 2
            elif node.right.data == key:
                if node.right.right != None:
                    node.right = node.right.right
                elif node.right.left == None:
                    node.right = node.right.left
            else:
                self.__del(node.right, key)


if __name__ == '__main__':
    bstree = BSTree()
    list_number = [25,8,53,4,42,37,31,39,86,64,99]
    for i in list_number:
        bstree.create(i)
    # cprint(figlet_format('BinarySearchTree', font='digital'), 'green')
    bstree.index(53)
    bstree.delete(53)
    # bstree.index(53)
    print()
