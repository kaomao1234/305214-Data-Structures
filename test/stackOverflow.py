class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

    def pop(self):
        current_node = self
        while current_node.next:
            if current_node.next.next == None:
                current_node.next = None
            else:
                current_node = current_node.next

    def printlist(self):
        current_node = self
        lst = [current_node.value]
        while current_node.next:
            current_node = current_node.next
            lst.append(current_node.value)
        print(lst)


node_A = LinkedList(1)
node_B = LinkedList(2)
node_C = LinkedList(3)

node_A.next = node_B
node_B.next = node_C

# try:
node_A.pop()
node_A.pop()
node_A.pop()
node_A.printlist()
# except NameError:
#     pass