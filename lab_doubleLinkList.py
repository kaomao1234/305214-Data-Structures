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
        self.len = lambda: self.__lenNode__(self.head)

    def insert(self, idx: int, data):
        new_node = Node(data)
        if idx == 0:
            self.__insertNode__(self.head, idx, data, new_node)
            self.head = new_node
        elif idx == self.len()+1:
            self.__addNode__(self.head, data)
        else:
            self.__insertNode__(self.head, idx, data, new_node)

    def __insertNode__(self, slist: Node, idx, data, newNode):
        if idx-1 < 0:
            slist.prev = newNode
            newNode.next = slist
        elif idx-1 == 0:
            newNode.prev = slist
            newNode.next = slist.next
            slist.next.prev = newNode
            slist.next = newNode
        else:
            return self.__insertNode__(slist.next, idx-1, data, newNode)

    def __lenNode__(self, slist, var=0):
        if slist == None:
            return var
        else:
            return self.__lenNode__(slist.next, var+1)

    def __idxNode__(self, slist, data, count=0):
        if slist == None:
            indexNodeError = '{} is not in LinkedList.'.format(data)
            raise Exception(indexNodeError)
        elif slist.data == data:
            return count
        else:
            return self.__idxNode__(slist.next, data, count+1)

    def __addNode__(self, slist: Node, data):
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


if __name__ == '__main__':
    Object = DoubleLL(Node('A'))
    Object.add('B')
    Object.add('C')
    Object.insert(4, 'M')
    Object.disp()
