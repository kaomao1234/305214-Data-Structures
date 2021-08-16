class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SLList:

    def __init__(self):
        self.first = None

    def add(self, data):
        self.addNode(data, self.first)

    def search(self, ele):
        return self.searchNode(ele, self.first)

    def show(self):
        self.showNode(self.first)

    def len(self):
        return self.lenNode(self.first)

    def delete(self, key):
        self.delNode(key, self.first)
        self.show()

    def push(self, new_data):
        if type(Node()) == new_data:
            new_data.next = self.first
            self.head = new_data
        else:
            new_data = Node(new_data)
            new_data.next = self.first
            self.head = new_data

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
            self.addNode(new_node, st_toidx)
            self.showNode(st_toidx)
        elif idx == 0:  # todo ถ้า idx เท่ากับ 0
            new_node.next = prev_node  # todo  นำ new_node มาต่อเป็น Node แรก
            self.showNode(new_node)

    def delNode(self, key, slist: Node):
        if slist.data == key:
            slist = slist.next
            self.showNode(slist)
        else:
            self.delNode(key, slist.next)

    def deleteNode(self, key):

        # Store head node
        temp = self.first

        # If head node itself holds the key to be deleted
        if (temp is not None):
            if (temp.data == key):
                self.first = temp.next
                temp = None
                return

        # Search for the key to be deleted, keep track of the
        # previous node as we need to change 'prev.next'
        while(temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        # if key was not present in linked list
        if(temp == None):
            return

        # Unlink the node from linked list
        prev.next = temp.next

        temp = None

    # todo function ที่เก็บNode ตั้งแต่ Node แรก ถึง Node ที่ idx
    def headtoIdx(self, idx, head: Node, newNode: Node):
        if idx == 0:
            return newNode
        else:
            self.addNode(head.data, newNode)
            return self.headtoIdx(idx-1, head.next, newNode)

    # todo function ที่เก็บNode ตั้งแต่ Nodeที่ idx ถึง Node สุดท้าย
    def idxtoLast(self, idx, head: Node):
        if idx == 0:
            return head
        else:
            return self.idxtoLast(idx-1, head.next)

    def lenNode(self, slist: Node, var=0):
        if slist == None:
            return var
        else:
            return self.lenNode(slist.next, var+1)

    def showNode(self, slist: Node):
        if slist == None:
            return
        print(slist.data, ' --> ', end='')
        self.showNode(slist.next)

    def searchNode(self, data, slist: Node, start=0):
        if slist == None:
            return False
        elif slist.data == data:
            return start
        return self.searchNode(data, slist.next, start+1)

    def addNode(self, data, slist: Node):
        if slist.next == None:
            if type(data) == type(Node()):
                slist.next = data
            else:
                slist.next = Node(data)
        else:
            self.addNode(data, slist.next)


if __name__ == '__main__':
    SinglyObj = SLList()
    SinglyObj.first = Node('A')
    SinglyObj.add('C')
    SinglyObj.add('M')
    SinglyObj.add('P')
    # SinglyObj.insert(4, 'X')
    SinglyObj.delete('C')
    # SinglyObj.show()
