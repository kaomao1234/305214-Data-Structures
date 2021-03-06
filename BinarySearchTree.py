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
            real_char = '%s' % self.data
            line = tc.colored('%s' % self.data, 'green')
            width = len(real_char)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            real_char = '%s' % self.data
            s = tc.colored('%s' % self.data, 'green')
            u = len(real_char)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            real_char = '%s' % self.data
            s = tc.colored('%s' % self.data, 'green')
            u = len(real_char)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        real_char = '%s' % self.data
        s = tc.colored('%s' % self.data, 'green')
        u = len(real_char)
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
        if node.right == None and node.left == None:
            return True
        else:
            return False

    def find_level(self):
        lst_level = []
        self.__findlevel(self.root, lst_level)
        print("The highest level : ", lst_level[len(lst_level)-1])
        return lst_level[len(lst_level)-1]

    def all_node(self):
        count = []
        self.__allOfNode(self.root, count)
        print("All node : ", len(count))
        return len(count)

    def create(self, data):
        if self.root == None:
            self.root = Node(data)
        elif self.root.data == None:
            self.root.data = data
        else:
            self.__create(self.root, data)

    def search(self, data):
        booleen = self.__search(self.root, data)
        return booleen

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
        inorder_lst = []
        self.inorder(self.root, inorder_lst)
        print(' '.join(inorder_lst))

    def printPost(self):
        postorder_lst = []
        self.postorder(self.root, postorder_lst)
        print(' '.join(postorder_lst))

    def printPre(self):
        preorder_lst = []
        self.inorder(self.root, preorder_lst)
        print(' '.join(preorder_lst))

    def treesucceesor(self, data):
        inorder_lst = []
        self.inorder(self.root, inorder_lst)
        return inorder_lst[inorder_lst.index(str(data))+1]

    def treemaximum(self):
        cur = self.root
        while cur.right != None:
            cur = cur.right
        return cur.data

    def treeminimum(self):
        cur = self.root
        while cur.left != None:
            cur = cur.left
        return cur.data

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

    def __findlevel(self, node: Node, lst_level: list, c=1):
        if node != None:
            if c not in lst_level:
                lst_level.append(c)
            self.__findlevel(node.left, lst_level, c+1)
            self.__findlevel(node.right, lst_level, c+1)

    def __allOfNode(self, node, c: list):
        if node != None:
            c.append(node.data)
            self.__allOfNode(node.left, c)
            self.__allOfNode(node.right, c)

    def __index(self, node: Node, data, var=0):
        if node.data == data:
            return node
        elif node.data > data:
            return self.__index(node.left, data, var+1)
        else:
            return self.__index(node.right, data, var+1)

    def __search(self, node: Node, data):
        if node == None:
            return False
        elif node.data == data:
            return True
        elif node.data > data:
            return self.__search(node.left, data)
        else:
            return self.__search(node.right, data)

    def __create(self, node: Node, data):
        newNode = Node(data)
        if node == None:
            return newNode
        else:
            if node.data > data:
                node.left = self.__create(node.left, data)
            elif node.data < data:
                node.right = self.__create(node.right, data)
        return node

    def delete(self, key):
        if key == self.root.data:
            pp = Node(self.root.data+1)
            pp.left = self.root
            self.__del(pp, key)
            self.root = pp.left
        else:
            self.__del(self.root, key)

    def __del(self, node, key):
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
                        self.__del(node, rplace.data)
                        rplace.left = node.left
                        rplace.right = node.right
                        return rplace
            else:
                node.left = self.__del(node.left, key)
                node.right = self.__del(node.right, key)
        return node


if __name__ == '__main__':
    bstree = BSTree()
    list_number = [64, 21, 31, 59, 9, 96, 4,
                   11, 3, 32, 35, 68, 90, 100, 6, 2, 1]
    for i in list_number:
        bstree.create(i)
        bstree.root.display()
    bstree.delete(59)
    bstree.root.display()
    # bstree.printIn()
    # print(bstree.treesucceesor(59))
    # print(bstree.treemaximum())
    # print(bstree.treeminimum())
    # bstree.root.display()
    # bstree.find_level()
    # bstree.all_node()
