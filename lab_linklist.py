class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        
class SLList:

    def __init__(self):
        self.first = None

    def add(self, data):
        self.__addNode(data, self.first)

    def search(self, ele):
        return self.__searchNode(ele, self.first)

    def show(self):
        self.__showNode(self.first)

    def len(self):
        return self.__lenNode(self.first)

    def delete(self, key):
        self.first = self.__delNode(key, self.first)

    def pop(self):
        if self.first.next == None:
            self.first = None
        else:
            self.__pop(self.first)
            
    def dequeue(self):
        self.first = self.first.next

    def enqueue(self, data):
        self.__addNode(data,self.first)
    
    def push(self,data):
        self.__addNode(data,self.first)
    
    def __pop(self, slist: Node):
        if slist.next.next == None:
            slist.next = None
        else:
            self.__pop(slist.next)
        

    def delV2(self, slist, key):
        if slist.data == key:
            print(slist.data == key)
            slist = slist.next
        elif slist.next.data == key:
            ptr = slist.next.next
            slist.next = ptr
        else:
            self.delV2(slist.next, key)

    def insert(self, idx, data):
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

    def __lenNode(self, slist: Node, var=0):
        if slist == None:
            return var
        else:
            return self.__lenNode(slist.next, var+1)

    def __showNode(self, slist: Node):
        if slist == None:
            return
        print(slist.data, ' --> ', end='')
        self.__showNode(slist.next)

    def __searchNode(self, data, slist: Node, start=0):
        if slist == None:
            return False
        elif slist.data == data:
            return start
        return self.__searchNode(data, slist.next, start+1)

    def __addNode(self, data, slist: Node):
        if slist.next == None:
            if type(data) == type(Node()):
                slist.next = data
            else:
                slist.next = Node(data)
        else:
            self.__addNode(data, slist.next)


if __name__ == '__main__':
    single_link = SLList()
    single_link.first = Node('O')
    for i in range(4, 6):
        single_link.add(i)
    single_link.pop()
    single_link.pop()
    single_link.pop()
    single_link.show()
