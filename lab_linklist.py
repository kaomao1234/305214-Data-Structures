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

    def push(self, new_data):
        if type(Node()) == new_data:
            new_data.next = self.first
            self.head = new_data
        else:
            new_data = Node(new_data)
            new_data.next = self.first
            self.head = new_data

    def insert(self, idx, data):
        st_toidx = self.headtoIdx(idx, self.first, Node())
        prev_node = self.idxtoLast(idx, self.first)
        new_node = Node(data)
        if idx > 0:
            st_toidx = st_toidx.next
            new_node.next = prev_node
            self.addAlg(new_node, st_toidx)
            self.showAlg(st_toidx)
        elif idx == 0:
            new_node.next = prev_node
            self.showAlg(new_node)

    def headtoIdx(self, idx, head: Node, newNode: Node):
        if idx == 0:
            return newNode
        else:
            self.addAlg(head.data, newNode)
            return self.headtoIdx(idx-1, head.next, newNode)

    def idxtoLast(self, idx, head: Node):
        if idx == 0:
            return head
        else:
            return self.idxtoLast(idx-1, head.next)

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


if __name__ == '__main__':
    SinglyObj = SLList()
    SinglyObj.first = Node('A')
    SinglyObj.addNode('C')
    SinglyObj.addNode('M')
    SinglyObj.addNode('P')
    SinglyObj.insert(4, 'X')
