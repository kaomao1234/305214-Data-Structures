class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None


class DLinkList:
    def __init__(self, head=None):
        self.head = head

    def create(self, data):
        self.__create(self.head, data)

    def disp(self):
        disp_var = []  # todo เก็บค่าของNode
        self.__disp(self.head, disp_var)
        print(" --> ".join(disp_var))

    def insert(self, idx: int, data):
        if idx == 0:
            self.head = self.head.next
            self.head.prev = None
        else:
            self.__insert(self.head, idx, data)

    def delete(self, key):
        self.__del(self.head, key)

    def __insert(self, node: Node, idx: int, data):
        if idx-1 == 0:
            ptr_p = Node(data)  # todo Node(10)
            ptr = node.next  # todo 2 --> 4
            ptr_p.next = ptr  # todo 10 --> 2 --> 4
            ptr.prev = node  # todo 5 --> 7 --> 10 --> 2 --> 4
            node.next = ptr_p  # todo 2 --> 4 = 10 --> 2 --> 4
            ptr.prev = ptr_p  # todo 2 --> 4 .prev = 10 --> 2 --> 4
            return
        self.__insert(node.next, idx-1, data)

    def __create(self, node: Node, data):
        if node.next == None:
            newNode = Node(data)
            newNode.prev = node
            node.next = newNode
            return
        self.__create(node.next, data)

    def __del(self, node: Node, key):
        if node == None:
            return
        elif node.next.data == key:
            ptr = node.next  # todo Node(2)
            node.next = node.next.next
            if node.next != None:
                node.next.prev = node
        self.__del(node.next, key)

    def __disp(self, node: Node, disp_arr: list):
        if node == None:
            return
        else:
            disp_arr.append(str(node.data))
            self.__disp(node.next, disp_arr)


root = Node(5)
dlink = DLinkList(root)
dlink.create(7)
dlink.create(2)
dlink.create(4)
dlink.insert(1, 4)
dlink.disp()
dlink.delete(4)
dlink.disp()