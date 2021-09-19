from BinaryHeap import HeapNode
class MinHeapTree:
    def __init__(self):
        self.order = 0
    
    def mark_traversal(self):
        idx_number = self.order_node
        route_pin = []
        while idx_number >= 2:
            idx_number //= 2
            route_pin.append(idx_number)
        return route_pin[::-1]