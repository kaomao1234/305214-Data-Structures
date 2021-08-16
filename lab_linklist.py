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

    def insertAfter(self, idx, data):
        prev_node = None
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node


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
    print('Default : ', ' --> '.join(SinglyObj.node2array()))
    SinglyObj.insertV2(1, 'Z')
    print('Insert Z into index 1 : ', ' --> '.join(SinglyObj.node2array()))
    SinglyObj.delV2('M')
    print('Delete M : ', ' --> '.join(SinglyObj.node2array()))
