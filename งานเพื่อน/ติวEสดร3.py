class Node:
    def __init__(self, data=None):
        self.data = data
        self.right = None
        self.left = None

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

    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            self.__insert(self.root, data)

    def isleaf(self, node: Node):
        if node.left == None and node.right == None:
            return True
        else:
            return False

    def maxNodeVal(self, node: Node, val=0):
        if node == None:
            return val
        elif val == 0:
            val = node.data
            return self.maxNodeVal(node, val)
        elif val < node.data:
            val = node.data
            return self.maxNodeVal(node.right, val)
        else:
            return self.maxNodeVal(node.right, val)

    def search(self, key):
        return self.__search(self.root, key)

    def __search(self, node: Node, data):
        if node == None:
            return False
        elif node.data == data:
            return True
        elif node.data < data:
            return self.__search(node.right, data)
        else:
            return self.__search(node.left, data)

    def __insert(self, node: Node, data):
        if node.data < data:
            if node.right == None:
                node.right = Node(data)
            else:
                self.__insert(node.right, data)
        elif node.data > data:
            if node.left == None:
                node.left = Node(data)
            else:
                self.__insert(node.left, data)

    def delete(self, key):
        self.__delete(self.root, key)

    def __delete(self, node: Node, key):
        if node != None:
            if node.data == key:
                if self.isleaf(node) == True:
                    return None
                else:
                    if node.right == None:
                        return node.left
                    elif node.left == None:
                        return node.right
                    else:
                        ptr_st = Node(self.maxNodeVal(node.left))
                        self.__delete(node, ptr_st.data)
                        ptr_st.left = node.left
                        ptr_st.right = node.right
                        return ptr_st
            else:
                node.left = self.__delete(node.left, key)
                node.right = self.__delete(node.right, key)
        return node


if __name__ == '__main__':
    array = [25, 8, 4, 53, 42, 37, 31, 39, 86, 64, 99]
    bstree = BSTree()
    for i in array:
        bstree.insert(i)
    bstree.root.display()
    bstree.delete(53)
    bstree.delete(42)
    bstree.root.display()