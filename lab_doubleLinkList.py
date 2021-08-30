from termcolor import colored,cprint
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLL:
    def __init__(self, head=None):
        self.head = head

    def len(self):
        return self.__len(self.head)

    def add(self, data):
        self.__add(self.head, data)

    def index(self, key):
        return self.__index(self.head, key)

    def insert(self, key, idx: int):
        if idx == 0:
            p = Node(key)
            self.head.prev = p
            p.next = self.head
            self.head = p
        else:
            self.__insert(self.head, key, idx)

    def delete(self, key):
        if key == self.head.data:
            self.head = self.head.next
            self.head.prev = None
        else:
            self.__del(self.head, key)

    def contain(self, data):
        return self.__contain(self.head, data)

    def disp(self):
        dispVar = []
        return self.__disp(self.head,dispVar)

    def __insert(self, slist: Node, key, idx):
        if idx-1 == 0:
            p = Node(key)
            prev = slist.next
            if prev != None:
                prev.prev = p
            p.next = prev
            p.prev = slist.next
            slist.next = p
        else:
            self.__insert(slist.next, key, idx-1)

    def __del(self, slist: Node, key):
        if slist.next.data == key:
            if slist.next.next != None:
                slist.next.next.prev = slist.next
            slist.next = slist.next.next
        else:
            self.__del(slist.next, key)

    def __len(self, slist, var=0):
        if slist == None:
            return var
        else:
            return self.__len(slist.next, var+1)

    def __index(self, slist, key, count=0):
        if slist == None:
            indexNodeError = '{} is not in LinkedList.'.format(key)
            raise Exception(indexNodeError)
        elif slist.data == key:
            return count
        else:
            return self.__index(slist.next, key, count+1)

    def __add(self, slist: Node, data):
        if slist.next == None:
            nodeData = Node(data)
            nodeData.prev = slist
            slist.next = nodeData
        else:
            self.__add(slist.next, data)

    def __contain(self, slist, data):
        if slist.data == data:
            return True
        else:
            return self.__contain(data, slist.next)

    def __disp(self, slist: Node, dispVar:list):
        if slist == None:
            result = ' --> '.join(dispVar)
            print(result)
            return result
        else:
            dispVar.append(colored(str(slist.data),'green'))
            self.__disp(slist.next,dispVar)


if __name__ == '__main__':
    double_link = DoubleLL(Node('A'))
    double_link.add('B')
    double_link.add('C')
    double_link.add('D')
    cprint('Double linkedList','red','on_white')
    double_link.disp()
    cprint('insert M at 0.','magenta')
    double_link.insert('M', 0)
    double_link.disp()
    cprint('delete A from Node.','magenta')
    double_link.delete('A')
    double_link.disp()