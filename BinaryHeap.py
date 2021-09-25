import termcolor as tc
import math


class HeapNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def display(self):
        # * Display Tree form in Terminal
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


class HeapTree:
    def __init__(self):
        self.root = None
        self.order_node = 0

    def insert(self, data):
        if self.root == None:
            self.root = HeapNode(data)
            self.order_node += 1
        else:
            if self.search(data) == False:
                self.order_node += 1
                self.__max_insert(self.root, data)
            else:
                print("{} is already in heap.".format(data))

    def mark_traversal(self):
        idx_number = self.order_node
        route_pin = []
        while idx_number >= 2:
            idx_number //= 2
            route_pin.append(idx_number)
        return route_pin[::-1]

    def search(self, data):
        boolean = [False]
        self.__search(self.root, data, boolean)
        return boolean[0]

    def isleaf(self, node: HeapNode):
        if node.left == None and node.right == None:
            return True
        else:
            return False

    def isbinary(self, node: HeapNode):
        if node.left != None and node.right != None:
            return True
        else:
            return False

    def delete(self, key):
        self.__delete(self.root, key)
        self.min_reheap(self.root)

    def min_node(self, *args):
        c = sorted(args, key=lambda s: s.data)
        return c[0]

    def max_node(self, *args):
        c = sorted(args, key=lambda s: s.data, reverse=True)
        return c[0]

    def del_lastnode(self, node: HeapNode, c=1):
        last_way = self.mark_traversal()
        if c == len(last_way):
            temp = ''
            if node.right == None:
                temp = node.left.data
                node.left = None
            else:
                temp = node.right.data
                node.right = None
            return temp
        else:
            m = last_way[c]
            if m % 2 == 0:
                return self.del_lastnode(node.left, c+1)
            elif m % 2 != 0:
                return self.del_lastnode(node.right, c+1)

    def __search(self, node: HeapNode, data, boolean):
        if node != None:
            self.__search(node.left, data, boolean)
            self.__search(node.right, data, boolean)
            if node.data == data:
                boolean[0] = True

    def __insert(self, node: HeapNode, data, c=1):
        route_pin = self.mark_traversal()
        cur_idx = self.order_node % 2
        newNode = HeapNode(data)
        if c == len(route_pin):
            if node.left == None and cur_idx == 0:
                node.left = newNode
            elif node.right == None and cur_idx != 0:
                node.right = newNode
        else:
            m = route_pin[c]
            if m % 2 == 0:
                self.__insert(node.left, data, c+1)
            elif m % 2 != 0:
                self.__insert(node.right, data, c+1)

    def __min_insert(self, node: HeapNode, data, c=1):
        route_pin = self.mark_traversal()
        cur_idx = self.order_node % 2
        newNode = HeapNode(data)
        temp = data
        if node.data > newNode.data:
            temp = node.data
            node.data = newNode.data
            newNode.data = temp
        if c == len(route_pin):
            if node.left == None and cur_idx == 0:
                node.left = newNode
            elif node.right == None and cur_idx != 0:
                node.right = newNode
        else:
            m = route_pin[c]
            if m % 2 == 0:
                self.__min_insert(node.left, temp, c+1)
            elif m % 2 != 0:
                self.__min_insert(node.right, temp, c+1)

    def __max_insert(self, node: HeapNode, data, c=1):
        route_pin = self.mark_traversal()
        cur_idx = self.order_node % 2
        newNode = HeapNode(data)
        temp = data
        if node.data < newNode.data:
            temp = node.data
            node.data = newNode.data
            newNode.data = temp
        if c == len(route_pin):
            if node.left == None and cur_idx == 0:
                node.left = newNode
            elif node.right == None and cur_idx != 0:
                node.right = newNode
        else:
            m = route_pin[c]
            if m % 2 == 0:
                self.__max_insert(node.left, temp, c+1)
            elif m % 2 != 0:
                self.__max_insert(node.right, temp, c+1)

    def __delete(self, node: HeapNode, key):
        if node != None:
            if node.data == key:
                node.data = self.del_lastnode(self.root)
            else:
                self.__delete(node.left, key)
                self.__delete(node.right, key)

    def min_reheap(self, node: HeapNode):
        if node != None:
            if self.isbinary(node) == True:
                temp = node.data
                if node.data > self.max_node(node.left, node.right).data:
                    get_node = self.min_node(node.left, node.right)
                    node.data = get_node.data
                    get_node.data = temp
                    self.min_reheap(get_node)
                else:
                    self.min_reheap(node.left)
                    self.min_reheap(node.right)
            else:
                if node.left != None and self.max_node(node, node.left) == node:
                    temp = node.data
                    node.data = node.left.data
                    node.left.data = temp
                elif node.right != None and self.max_node(node, node.right) == node:
                    temp = node.data
                    node.data = node.right.data
                    node.right.data = temp


array = [10, 34, 24, 3, 66, 47, 18, 8, 26, 55, 82, 29, 32, 17, 6, 72]
# file = open(
#     'C:/Users/borip/Documents/GitHub/305214-Data-Structures/treeData.txt', mode='r')
# array = file.read().split(',')
# array = list(map(int, array))
# file.close()
ht = HeapTree()
for i in array:
    ht.insert(i)
ht.root.display()
