import time
class Node:
    def __init__(self,array):
        self.array = array
    def filess(self,node):
        temp = list(filter(lambda s : s<node,self.array))
        return temp
    def filthan(self,node):
        temp = list(filter(lambda s : s>node,self.array))
        return temp

if __name__ == '__main__':
    obj = Node([4,6,3,1,5,8,9]) 