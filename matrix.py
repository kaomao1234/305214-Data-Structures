from ast import literal_eval
import numpy
import sys

# todo function ที่ส่งค่ากลับเป็น row ,column ของ matrix


def checkRowCol(matrix): return (len(matrix), len(matrix[0]))


mat1 = literal_eval(input('Input matrix 1 :'))  # todo แปลงInputเป็น list
mat2 = literal_eval(input('Input matrix 2 :'))  # todo แปลงInputเป็น list
row1, column1 = checkRowCol(mat1)
row2, column2 = checkRowCol(mat2)
result = [[0 for j in range(column2)]
          for i in range(row1)]
if column1 != row2:  # todo ถ้า column1 ไม่เท่ากับ row2 ไม่สามารถ dot Matrix ได้
    print('Cannot dot Matrix.')
    sys.exit()
#todo loop row 1
for i in range(row1):
    #todo loop row 2 
    for j in range(column2):
        # todo loop column 2
        for k in range(row2):
            #todo mat1[i][k] คือการเข้าถึง สมาชิก แถวที่ i คอลัมน์ k
            #todo mat2[k][j] คือการเข้าถึง สมาชิก แถวที่ k คอลัมน์ j
            #todo นำมาคูณกัน
            print(i,k,'=>',mat1[i][k],'x',mat2[k][j])
            # todo นำผลลัธ์ไปเพิ่มใน matrix ผลคูณ result แถวที่ i คอลัมน์ j
            result[i][j] += mat1[i][k] * mat2[k][j]

print(numpy.matrix(result))