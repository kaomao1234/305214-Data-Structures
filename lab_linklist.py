class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SLList:
    nodeIdx = 0

    def __init__(self):
        self.first = None

    def addData(self, data):
        self.addNode(data, self.first)

    def addNode(self, data, slist):
        if slist.next == None:
            if type(data) == type(Node()):
                slist.next = data
            else:
                slist.next = Node(data)
        else:
            self.addNode(data, slist.next)

    def search(self, data, slist: Node, end=0, start=0):
        if slist == None:
            return
        elif slist.data == data:
            return True
        return self.search(data, slist.next, end, start+1)

    def showNode(self, slist: Node):
        if slist == None:
            return
        print(slist.data, ' --> ', end='')
        self.showNode(slist.next)

    def lenghtNode(self, slist=False, var=0):
        if slist == False:
            self.lenghtNode(self.first, var)
        elif slist == None:
            return var
        else:
            self.lenghtNode(slist.next, var)+1

    def IndexToEnd(self, idx: int, slist=False, end=0, NewNode=None):
        if slist == False:
            return self.IndexToEnd(idx, self.first, end, NewNode)
        elif idx == end:
            return NewNode
        else:
            NewNode = slist
            return self.IndexToEnd(idx, slist.next, end+1, NewNode.next)

    def ZeroToIndex(self, NewNode: Node, idx: int, slist=False, start=0):
        if slist == False:
            self.ZeroToIndex(NewNode, idx, self.first.next, start)
        elif idx == start:
            return
        else:
            self.addNode(slist.data, NewNode)
            self.ZeroToIndex(NewNode, idx, slist.next, start+1)

    def insertNode(self, idx: int, data):
        ptr = self.IndexToEnd(idx)
        ptp = Node(self.first.data)
        self.ZeroToIndex(ptp, idx)
        p = Node(data)
        p.next = ptr
        self.addNode(p, ptp)
        self.showNode(ptr)

    def delNode(self):
        pass


if __name__ == '__main__':
    cList = SLList()
    cList.first = Node('A')
    cList.addData('C')
    cList.addData('M')
    cList.addData('P')
    # cList.insertNode(1,'U')
    print()
    # cList.showNode(cList.first)
    # cList.showNode(cList.first)
