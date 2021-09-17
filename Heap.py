import heapq
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
        self.array = None
        self.root = None
        self.order_node = 0

    def reheap(self):
        pass

    def insert(self, data):
        if self.root == None:
            self.root = HeapNode(data)
            self.order_node += 1
        else:
            self.__insert(self.root, data)

    def mark_traversal(self, data):
        way_lst = []
        if self.array.index(data) > 0:
            dot = self.array.index(data)+1
            while dot >= 2:
                dot = dot/2
                way_lst.append(math.floor(dot))
                # way_lst.append(dot)
            return way_lst[::-1]
        else:
            return 1

    def __insert(self, node: HeapNode, data,c=0):
        mapping = self.mark_traversal(data)
        # print(mapping)
        idx_node = self.array.index(node.data)+1
        print(mapping)


# array = [14, 10, 8, 7, 6, 9, 3, 2, 4, 1]
array = [16, 14, 10, 8, 7]
ht = HeapTree()
ht.array = array
for i in array:
    ht.insert(i)
    # print(ht.mark_traversal(i))
# ht.root.display()