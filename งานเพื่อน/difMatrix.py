from numpy import *
from sympy import symbols, solve
Mtx1 = [[1,2,3],
        [4,5,6],
        [7,8,9]]
Mtx2 = [[10,12,-3],[-4,5,-6],[-7,-8,9]]
row,column = len(Mtx1),len(Mtx1[0])
# Mtx1 = [j for i in Mtx1 for j in i ]
reMtx1 = []
for i in Mtx1:
    print(i)
    for j in i:
        print(j)
        reMtx1.append(j)
Mtx2 = [j for i in Mtx2 for j in i ]
result = []
print(Mtx2)
for i in range(len(reMtx1)):
    result.append(reMtx1[i]-Mtx2[i])
result = array(result).reshape(row,column)
# result = array([i-j for (i,j) in zip(Mtx1,Mtx2)]).reshape(row,column)
print(result)