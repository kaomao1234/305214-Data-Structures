
import termcolor as tc


class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

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


class BHeap:
    def __init__(self, root=None):
        self.root = root
        self.last_route = 0

    def insert(self, data):
        if self.search(data) == False:
            self.last_route += 1
            if self.root == None:
                self.root = Node(data)
            else:
                print(data,'==>',self.direction(),'\n','route : ',self.last_route)
                self.__insert(self.root, data)

    def direction(self, c=None, k=None):
        if c is None and k is None:
            idx_number = self.last_route
            number_of_direct = []
            return self.direction(idx_number, number_of_direct)
        elif c >= 2:
            c //= 2
            k.append(c)
            return self.direction(c, k)
        else:
            return k[::-1]

    def search(self, data):
        p = []
        self.__search(self.root, data, p)
        return p[0] if len(p) == 1 else False

    def __search(self, node: Node, data, m: list):
        if node != None:
            if node.data == data:
                m.append(True)
            self.__search(node.left, data, m)
            self.__search(node.right, data, m)

    def __insert(self, node: Node, data, c=1):
        get_d = self.direction()
        cur_d = self.last_route % 2
        newNode = Node(data)
        if c == len(get_d):
            if node.left == None and cur_d == 0:
                node.left = newNode
            elif node.right == None and cur_d != 0:
                node.right = newNode
        else:
            m = get_d[c]
            if m % 2 == 0:
                self.__insert(node.left, data, c+1)
            elif m % 2 != 0:
                self.__insert(node.right, data, c+1)


ht = BHeap()
for i in range(1, 9):
    ht.insert(i)
ht.root.display()