import unittest as unt
from lab_linklist import Node,SLList
from termcolor import colored
class TestNode(unt.TestCase):
    def test_del_node(self):
        singly_link = SLList()
        singly_link.first = Node('A')
        for i in range(6,9):
            singly_link.add(i)
        singly_link.delete(7)
        print(colored('hello word','green'))
        self.assertEqual(singly_link.show(),self.Nodeform(['A',6,8]))
    
    def Nodeform(self,link:list):
        r = list(map(str,link))
        return ' --> '.join(r)
if __name__ and '__main__':
    unt.main()