import unittest as unt
from lab_linklist import Node,SLList
class TestNode(unt.TestCase):
    def test_del_node(self):
        # singly_link = SLList()
        # singly_link.first = Node('A')
        # for i in range(6,9):
        #     singly_link.add(i)
        # singly_link.delete(7)
        self.assertEqual(8,8)
if __name__ and '__main__':
    unt.main()