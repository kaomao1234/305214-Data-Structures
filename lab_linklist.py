
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SLList:

    def __init__(self):
        self.first = None

    def add(self, data):
        self.__add(data, self.first)

    def search(self, ele):
        return self.__search(ele, self.first)

    def show(self):
        self.__show(self.first)

    def len(self):
        return self.__len(self.first)

    def delete(self, key):
        if key == self.first.data:
            self.first = self.first.next
        else:
            self.__del(self.first, key)

    def pop(self):
        if self.first.next == None:
            self.first = None
        else:
            self.__pop(self.first)

    def dequeue(self):
        self.first = self.first.next

    def enqueue(self, data):
        self.__add(data, self.first)

    def push(self, data):
        self.__add(data, self.first)

    def insert(self, data, idx: int):
        if idx-1 < 0:
            p = Node(data)
            p.next = self.first
            self.first = p
        else:
            self.__insert(self.first, data, idx)

    def __insert(self, slist: Node, data, idx: int):
        if idx-1 == 0:
            p = Node(data)
            ptr = slist.next
            p.next = ptr
            slist.next = p
        else:
            self.__insert(slist.next, data, idx-1)

    def __pop(self, slist: Node):
        if slist.next.next == None:
            slist.next = None
        else:
            self.__pop(slist.next)

    def __del(self, slist: Node, key):
        if slist.next.data == key:
            slist.next = slist.next.next
        else:
            self.__del(slist.next, key)

    def __len(self, slist: Node, var=0):
        if slist == None:
            return var
        else:
            return self.__len(slist.next, var+1)

    def __show(self, slist: Node):
        if slist == None:
            return
        print(slist.data, ' --> ', end='')
        self.__show(slist.next)

    def __search(self, data, slist: Node, start=0):
        if slist == None:
            return False
        elif slist.data == data:
            return start
        return self.__search(data, slist.next, start+1)

    def __add(self, data, slist: Node):
        if slist.next == None:
            if type(data) == type(Node()):
                slist.next = data
            else:
                slist.next = Node(data)
        else:
            self.__add(data, slist.next)

    def insertV2(self, idx, data):
        # todo ตัวแปรที่เก็บตั้งแต่ Node แรก ถึง Node idx
        st_toidx = self.headtoIdx(idx, self.first, Node())
        # todo ตัวแปรที่เก็บตั้งแต่ Node ที่ idx ถึง Node สุดท้าย
        prev_node = self.idxtoLast(idx, self.first)
        new_node = Node(data)  # todo สร้าง Node ใหม่จาก data
        if idx > 0:  # todo ถ้า idx มากกว่า 0
            st_toidx = st_toidx.next  # todo ตัวแปรที่เก็บตั้งแต่ Node แรก ถึง Node idx
            new_node.next = prev_node  # todo  นำ new_node ไปต่อกับ Node ที่เหลือ
            # todo นำ new_node มาต่อกับ st_toidx
            self.__addNode(new_node, st_toidx)
            self.first = st_toidx

        elif idx == 0:  # todo ถ้า idx เท่ากับ 0
            new_node.next = prev_node  # todo  นำ new_node มาต่อเป็น Node แรก
            self.first = new_node

    # todo สร้าง fuction delNode กำหนดและ new_node เป็น node ใหม่
    def __delNode(self, key, slist: Node, new_node=Node()):
        if slist == None:  # todo ถ้าslist == None
            new_node = new_node.next
            return new_node
        elif slist.data != key:  # todo ถ้า varที่ต้องการลบ ไม่เท่ากับ data
            # todo เพิ่มข้อมูลเข้าไปใน new_node
            self.__addNode(slist.data, new_node)
            return self.__delNode(key, slist.next, new_node)
        else:
            return self.__delNode(key, slist.next, new_node)

    # todo function ที่เก็บNode ตั้งแต่ Node แรก ถึง Node ที่ idx
    def headtoIdx(self, idx, head: Node, newNode: Node):
        if idx == 0:
            return newNode
        else:
            self.__addNode(head.data, newNode)
            return self.headtoIdx(idx-1, head.next, newNode)

    # todo function ที่เก็บตั้งแต่ Nodeที่ idx ถึง Node สุดท้าย
    def idxtoLast(self, idx, head: Node):
        if idx == 0:
            return head
        else:
            return self.idxtoLast(idx-1, head.next)


if __name__ == '__main__':
    singly_link = SLList()
    singly_link.first = Node('O')
    for i in range(4, 6):
        singly_link.add(i)
    singly_link.delete()
    singly_link.show()