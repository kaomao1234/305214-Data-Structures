from termcolor import colored


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SLList:

    def __init__(self):
        self.first = None

    def add(self, data):
        if self.first.data == None:
            self.first = Node(data)
        else:
            self.__add(data, self.first)

    def search(self, ele):
        return self.__search(ele, self.first)

    def show(self):
        return self.__show(self.first)

    def len(self):
        return self.__len(self.first)

    def delete(self, key):
        if key == self.first.data:
            self.first = self.first.next
        else:
            self.__del(self.first, key)

    def pop(self):
        if self.first.data == None:
            return 'Emty Node.'
        elif self.first.next == None:
            getPop = self.first.data
            self.first = Node()
            return getPop
        else:
            return self.__pop(self.first)

    def dequeue(self):
        if self.first.data == None:
            return 'Emty Node.'
        elif self.first == None:
            self.first = Node()
            return 'Emty Node.'
        else:
            getDequeue = self.first.data
            self.first = self.first.next
            return getDequeue

    def enqueue(self, data):
        if self.first.data == None:
            self.first = Node(data)
        else:
            self.__add(data, self.first)

    def push(self, data):
        if self.first.data == None:
            self.first = Node(data)
        else:
            self.__add(data, self.first)

    def insert(self, data, idx: int):
        if idx-1 < 0:
            p = Node(data)
            p.next = self.first
            self.first = p
        else:
            self.__insert(self.first, data, idx)

    def __insert(self, slist: Node, data, idx: int):
        if idx-1 == 0:
            p = Node(data)
            ptr = slist.next
            p.next = ptr
            slist.next = p
        else:
            self.__insert(slist.next, data, idx-1)

    def __pop(self, slist: Node):
        if slist.next.next == None:
            getPop = slist.next.data
            slist.next = None
            return getPop
        else:
            return self.__pop(slist.next)

    def __del(self, slist: Node, key):
        if slist.next.data == key:
            slist.next = slist.next.next
        else:
            self.__del(slist.next, key)

    def __len(self, slist: Node, var=0):
        if slist == None:
            return var
        else:
            return self.__len(slist.next, var+1)

    def __show(self, slist: Node, disp=[]):
        if slist == None:
            print(' --> '.join(disp))
            return ' --> '.join(disp)
        elif slist.data != None:
            disp.append(colored(str(slist.data), 'green'))
            return self.__show(slist.next)

    def __search(self, data, slist: Node, start=0):
        if slist == None:
            return False
        elif slist.data == data:
            return start
        return self.__search(data, slist.next, start+1)

    def __add(self, data, slist: Node):
        if slist.next == None:
            if type(data) == type(Node()):
                slist.next = data
            else:
                slist.next = Node(data)
        else:
            self.__add(data, slist.next)


if __name__ == '__main__':
    singly_link = SLList()
    singly_link.first = Node('O')
    for i in range(4, 7):
        singly_link.add(i)
    # print(singly_link.dequeue())
    print(singly_link.pop())
    print(singly_link.pop())
    print(singly_link.pop())
    print(singly_link.pop())
    print(singly_link.dequeue())
    singly_link.push('M')
    singly_link.enqueue(8)
    singly_link.pop()
    singly_link.dequeue()
    singly_link.show()