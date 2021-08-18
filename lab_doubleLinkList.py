class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLL:
    def __init__(self, head=None):
        self.head = head
        self.add = lambda data: self.__addNode__(self.head, data)
        self.disp = lambda: self.__dispNode__(self.head)
        self.incheck = lambda data: self.__inNode__(self.head, data)
        self.index = lambda data: self.__idxNode__(self.head, data)
        self.insert = lambda idx, data: self.__insertNode__(
            self.head, idx, data)

    def __insertNode__(self, slist: Node, idx, data):
        if idx-1 < 0:
            ptr = slist
            print(id(ptr) == id(slist))
        elif idx == 0:
            print(1)
        else:
            self.__insertNode__(slist.next, idx-1, data)

    def __idxNode__(self, slist, data, count=0):
        if slist == None:
            indexNodeError = '{} is not in LinkedList.'.format(data)
            raise Exception(indexNodeError)
        elif slist.data == data:
            return count
        else:
            return self.__idxNode__(slist.next, data, count+1)

    def __addNode__(self, slist: int, data):
        if slist.next == None:
            nodeData = Node(data)
            nodeData.prev = slist
            slist.next = nodeData
        else:
            self.__addNode__(slist.next, data)

    def __inNode__(self, slist, data):
        if slist.data == data:
            return True
        else:
            return self.__inNode__(data, slist.next)

    def __dispNode__(self, slist: Node):
        if slist == None:
            return
        else:
            print(slist.data, end=' --> ')
            self.__dispNode__(slist.next)


Object = DoubleLL(Node('A'))
Object.add('B')
Object.insert(0, 'M')
Object.disp()
