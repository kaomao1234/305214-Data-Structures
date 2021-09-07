class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None


class DoubleLL:
    def __init__(self):
        self.head = None

    def add(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            self.__add(self.head, data)

    def delete(self, key):
        if key == self.head.data:
            pp = Node('Backup')
            pp.next = self.head
            self.__del(pp, key)
            self.head = pp.next
        else:
            self.__del(self.head, key)

    def show(self):
        self.__show(self.head)

    def insert(self, idx: int, data):
        if idx == 0:
            p = Node(data)
            p.next = self.head
            self.head.prev = p
        else:
            self.__insert(self.head, idx, data)

    def __show(self, node: Node):
        if node == None:
            return
        else:
            print(node.data, end=" --> ")
            self.__show(node.next)

    def __add(self, node: Node, data):
        if node == None:
            return Node(data)
        else:
            node.next = self.__add(node.next, data)
            node.next.prev = node
        return node

    def __del(self, node: Node, key):
        if node.data == key:
            if node.next != None:
                node.next.prev = node.prev
            return node.next
        else:
            node.next = self.__del(node.next, key)
        return node

    def __insert(self, node: Node, idx: int, data):
        if idx-1 == 0:
            p = Node(data)
            ptr = node
            p.prev = ptr
            p.next = ptr.next
            ptr.next = p
            return ptr
        else:
            node.next = self.__insert(node.next, idx-1, data)
        return node


if __name__ == '__main__':
    double_link = DoubleLL()
    double_link.head = Node("P")
    double_link.add('L')
    double_link.add('M')
    double_link.delete("P")
    double_link.show()
