class Node:  # สร้างคลาสโนด
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SLList:  # สร้างคลาส
    def __init__(self):
        self.first = None

    def append(self, data):
        self.appendList(data, self.first)

    def appendList(self, data, slist):  # data = "C" ,slist = B
        if slist.next == None:  # B.next
            slist.next = Node(data)  # B.next -> C
        else:
            self.appendList(data, slist.next)

    def show(self, slist):  # สร้างฟังก์ชันโชว์ รับค่า slist
        if slist == None:
            return
        elif slist.next == None:
            print(slist.data)
        else:
            print(str(slist.data) + " -> ", end="")
            self.show(slist.next)

    def NodeToArray(self, slist, thelist=[]):  # แปลงเป็นArray
        if slist == None:
            return thelist
        else:
            thelist.append(slist.data)
            return self.NodeToArray(slist.next, thelist)

    def ArrayToNode(self, theList: list, newNode=Node(), idx=0):
        if len(theList) == idx:
            newNode = newNode.next
            return newNode
        else:
            self.appendList(theList[idx], newNode)
            return self.ArrayToNode(theList, newNode, idx+1)

    def delNode(self, key):
        tolist = self.NodeToArray(self.first)
        tolist.remove(key)
        self.first = self.ArrayToNode(tolist)


Sll = SLList()
Sll.first = Node('A')
Sll.append('C')
Sll.append('M')
Sll.append('P')
Sll.delNode('M')
Sll.show(Sll.first)
