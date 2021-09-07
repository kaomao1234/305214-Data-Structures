import random 
class BNode:
    def __init__(self, data=None):
        self.val = []
        self.key = []
        self.child = []
class BTree:
    def __init__(self,size=None):
        self.root = None
        self.size = size
    def insert(self,data):
        self.__insert(self.root,data)
    def __insert(self, node:BNode,data):
        pass
    

if __name__ == '__main__':
    array = [22, 8, 35, 12, 10, 6, 42]
    array = random.sample(array,len(array))
    print(array)