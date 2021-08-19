# Python3 code to implement Jump Search
from math import *


def jumpSearch(arr, data):
    start = 0
    end = len(arr)
    jump_size = round(sqrt(end))
    for i in range(start, end):
        print(i)
        jump = i+jump_size-1
        prev_ar = jump-1
        next_ar = jump + 1
        if next_ar >= end:
            raise IndexError('list index out of range')
        elif arr[i] == data and i == 0:
            return i
        elif arr[prev_ar] == data:
            return prev_ar
        elif arr[jump] == data:
            return jump
        elif arr[next_ar] == data:
            return next_ar


# Driver code to test function
arr = [3, 2, 4, 9, 1, 5, 2, 6]
print(jumpSearch(arr, 5))
