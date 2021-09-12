"""
Array = กลุ่มข้อมูล
list,set,dict = mutable(เปลี่ยนแปลงได้) เพิ่ม,ลดได้
tuple = imutable เพิ่มได้ ลดไม่ได้
"""
d = [1, 2, 3]
dd = [[1, 2, 3]]
ddd = [[[1, 2, 3]]]


def a(d: list):
    d[1] = 4


d = [5, 3]
a(d)
"""! LinkList
Node(โนด(ปม))
    - data(ข้อมูล) = None
    - pointer next(ตัวชี้ตัวถัดไป)  = None
head or root  = Node(2)
Node(2) --> Node(3) 
2 --> 6 --> 7 --> 8
0     1     2     3
insert = 3
idx = 1
2 --> 3 --> 6 --> 7 --> 8
temp = 2 -->
delete  = 6
2 --> 6 --> 7 --> 8
temp = 7 --> 8
Node(2).next = temp
2 --> 7 --> 8
"""


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SLinkList:
    def __init__(self, head=None):
        self.head = head

    def delete(self, key):
        if key == self.head.data:
            self.head = self.head.next
        else:
            self.__del(self.head, key)

    def create(self, data):
        self.__create(self.head, data)

    def disp(self):
        disp_var = []  # todo เก็บค่าของNode
        self.__disp(self.head, disp_var)
        print(" --> ".join(disp_var))

    def insert(self, idx: int, data):
        if idx == 0:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode
        else:
            self.__insert(self.head, idx, data)

    def __disp(self, node: Node, disp_arr: list):
        if node == None:
            return
        else:
            disp_arr.append(str(node.data))
            self.__disp(node.next, disp_arr)

    def __insert(self, node: Node, idx: int, data):
        if idx-1 == 0:
            newNode = Node(data)
            temp = node.next
            newNode.next = temp
            node.next = newNode
            return
        self.__insert(node.next, idx-1, data)

    def __create(self, node: Node, data):
        if node.next == None:
            node.next = Node(data)
            return
        self.__create(node.next, data)

    def __del(self, node: Node, key):
        if node.next.data == key:
            temp = node.next.next
            node.next = temp
            return
        self.__del(node.next, key)


root = Node(2)
root.next = Node(3)
root.next.next = Node(4)
train = SLinkList()
train.head = Node(2)
train.create(6)
for i in range(7, 9):
    train.create(i)
train.disp()
train.delete(2)
train.disp()
# print(train.head.next.data)

