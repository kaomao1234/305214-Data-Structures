class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SLList:

    def __init__(self):
        self.first = None

    def addNode(self, data):
        self.addAlg(data, self.first)

    def search(self, ele):
        return self.searchalg(ele, self.first)

    def show(self):
        self.showAlg(self.first)

    def lenNode(self):
        return self.lenAlg(self.first)

    def subNode(self, idx: int, end=None):
        if end == None:
            end = self.lenNode()
        return self.subAlg(self.first, idx, end)

    def node2array(self):
        arr = []
        return self.node2arrayAlg(self.first, arr)

    def array2node(self, arrNode: list, head=None, var=1):
        if head == None:
            head = Node(arrNode[0])
            return self.array2node(arrNode, head)
        elif var == len(arrNode):
            return head
        else:
            self.addAlg(arrNode[var], head)
            return self.array2node(arrNode, head, var+1)

    def insertNode(self, idx: int, data):
        ptp = Node(data)
        if idx-1 < 0:
            idx = 0
            ptp.next = self.subNode(idx)
            return ptp
        p = self.subNode(0, idx-1)
        ptp.next = self.subNode(idx)
        self.addAlg(ptp, p)
        return p

    def delNode(self, x):
        ptr = self.search(x)
        if ptr-1 <= 0:
            after = self.subNode(ptr+1)
            self.first = after
        else:
            back = self.subNode(0, ptr-1)
            after = self.subNode(ptr+1)
            self.addNode(after, back)
            self.first = back

    def lenAlg(self, slist: Node, var=0):
        if slist == None:
            return var
        else:
            return self.lenAlg(slist.next, var+1)

    def showAlg(self, slist: Node):
        if slist == None:
            return
        print(slist.data, ' --> ', end='')
        self.showAlg(slist.next)

    def searchAlg(self, data, slist: Node, start=0):
        if slist == None:
            return False
        elif slist.data == data:
            return start
        return self.searchAlg(data, slist.next, start+1)

    def addAlg(self, data, slist: Node):
        if slist.next == None:
            if type(data) == type(Node()):
                slist.next = data
            else:
                slist.next = Node(data)
        else:
            self.addAlg(data, slist.next)

    def subAlg(self, slst: Node, idx: int, end=None, newNode=None, start=0):
        if start == idx:  # todo กำหนดจุดเริ่มต้นของNode โดยถ้า start == idx ให้ สร้าง Node ใหม่ ที่เก็บข้อมูลของ Node ที่ idx
            newNode = Node(slst.data)
            return self.subAlg(slst.next, idx, end, newNode, start+1)
        elif start < idx:  # todo ถ้า idx > start ให้start+1 และเลื่อนNodeต่อไปจนกว่าจะถึง ที่idx
            return self.subAlg(slst.next, idx, end, newNode, start+1)
        elif start == end:  # todo เมื่อstart == end ส่งค่า Nodeใหม่ กลับมา
            return newNode
        elif start < end:  # todo ถ้า end > start ให้start+1 และเลื่อนNodeต่อไปจนกว่าจะถึง ที่end และ ทำการต่อ Node ของ Node ใหม่ ด้วยข้อมูลของ slst.data
            self.addAlg(slst.data, newNode)
            return self.subAlg(slst.next, idx, end, newNode, start+1)

    def node2arrayAlg(self, slist: Node, arrNode):
        if slist == None:
            return arrNode
        else:
            arrNode.append(slist.data)
            return self.node2arrayAlg(slist.next, arrNode)

    def insertV2(self, idx: int, x):
        m = self.node2array()
        imp_var = m[idx:]
        m = m[:idx]
        m.append(x)
        m = m+imp_var
        self.first = self.array2node(m)

    def delV2(self, x):
        m = self.node2array()
        m = self.delAlgV2(x, m, [])
        self.first = self.array2node(m)

    def delAlgV2(self, x, arrNode: list, newArr: list, var=0):
        if var == len(arrNode):
            return newArr
        elif arrNode[var] != x:
            newArr.append(arrNode[var])
            return self.delAlgV2(x, arrNode, newArr, var+1)
        else:
            return self.delAlgV2(x, arrNode, newArr, var+1)


if __name__ == '__main__':
    SinglyObj = SLList()
    SinglyObj.first = Node('A')
    SinglyObj.addNode('C')
    SinglyObj.addNode('M')
    SinglyObj.addNode('P')
    print('Default : ', ' --> '.join(SinglyObj.node2array()))
    SinglyObj.insertV2(1, 'Z')
    print('Insert Z into index 1 : ', ' --> '.join(SinglyObj.node2array()))
    SinglyObj.delV2('M')
    print('Delete M : ', ' --> '.join(SinglyObj.node2array()))