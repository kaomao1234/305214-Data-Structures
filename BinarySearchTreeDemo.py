import pyfiglet as pg
import termcolor as tc


class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    # * Display Tree form in Terminal
    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * \
            '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + \
            (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + \
            [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


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
        return self.__index(self.root, data)

    def delete(self, key):
        if key == self.root.data:
            pointer = Node(self.root.data+1)
            pointer.left = self.root
            self.__del(pointer, key)
            self.root = pointer.left
        else:
            self.__del(self.root, key)

    def insert(self, data):
        if self.__search(self.root, data) == None:
            self.__create(self.root, data)
        else:
            print('Data is already in node.')

    def printIn(self):
        lst = []
        self.inorder(self.root, lst)
        print(' '.join(lst))

    def printPost(self):
        lst = []
        self.postorder(self.root, lst)
        print(' '.join(lst))

    def printPre(self):
        lst = []
        self.preorder(self.root, lst)
        print(' '.join(lst))

    def inorder(self, node, lst: list):
        if node != None:
            self.inorder(node.left, lst)
            lst.append(str(node.data))
            self.inorder(node.right, lst)

    def postorder(self, node, lst: list):
        if node != None:
            self.postorder(node.left, lst)
            self.postorder(node.right, lst)
            lst.append(str(node.data))

    def preorder(self, node, lst: list):
        if node != None:
            lst.append(str(node.data))
            self.preorder(node.left, lst)
            self.preorder(node.right, lst)

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
            return node
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

    def del2(self, key):
        if key == self.root.data:
            pp = Node(self.root.data+1)
            pp.left = self.root
            self.deldemo(pp,key)
            self.root = pp.left
        else:
            self.deldemo(self.root,key)

    def deldemo(self, node, key):
        if node != None:
            if node.data == key:
                if self.isleaf(node) == True:
                    return None
                else:
                    if node.left == None:
                        return node.right
                    elif node.right == None:
                        return node.left
                    else:
                        rplace = self.minValNode(node.right)
                        self.deldemo(node,rplace.data)
                        rplace.left = node.left
                        rplace.right = node.right
                        return rplace
            else:
                node.left = self.deldemo(node.left, key)
                node.right = self.deldemo(node.right, key)
        else:
            return node

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
    # file = open('treeData.txt', mode='r')
    # list_number = file.read().split(',')
    # list_number = list(map(int, list_number))
    # file.close()
    for i in list_number:
        bstree.create(i)
    bstree.root.display()
    bstree.del2(53)
    bstree.root.display()


0  ,1 ,2,
"""
0 --> 9
2+2 = 4
9+1 = 10
0,1
9 to base 2
(1*2^3)+(0*2^2)+(0*2^1)+(1*2^0) = 1001
"""
10,11,12