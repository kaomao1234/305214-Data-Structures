import time
# ! 1. ให้เปิดNotepad พิมพ์ค่าต่อไปนี้แล้วsave เป็นชื่อdata.txt ให้อ่านข้อมูลจากไฟล์โดยแต่ละกําหนดindex เริ่มต้นเองให้สร้างfunctionชื่อว่าcreateมาเก็บในarray เพียง12 ค่าและแสดงค่า
# todo 34 24 3 66 47 18 8 26 55 82 29 32 17 6 72 27 23 9 44 12 60 89 10 57 46 54 7 33 95 56 77 22 51 19


class Array:
    def __init__(self, *arg: int):
        self.iterVal = arg[0] if type(arg[0]) in (list, tuple) else list(arg)

    #! Bubble sort method
    @property
    def BubbleSort(self):
        for i in range(len(self.iterVal)):
            # todo ตัวแปรที่ใช้หยุด loop เมื่อข้อมูลทุกตัวเรียงลำดับแล้ว
            stop = 0
            # todo loop กระทำ len(list)-1 รอบ เพื่อให้ตัวเลขสามรถจับคู่กัน โดย ไม่ให้ สมาชิกสุดท้ายเป็นตำแหน่งที่ n
            for j in range(0, len(self.iterVal)-1):
                # todo ถ้า ตำแหน่งที่ n มีค่ามากว่า n+1
                if self.iterVal[j] > self.iterVal[j+1]:
                    # todo here_ele คือตัวแปรที่ n, next_ele คือตัวแปรที่ n+1
                    here_ele, next_ele = self.iterVal[j], self.iterVal[j+1]
                    # todo สลับสมาชิก
                    self.iterVal[j] = next_ele
                    self.iterVal[j+1] = here_ele
                # todo เมื่อไม่เข้าเงื่อนไขด้านบน
                else:
                    stop += 1
            if stop == len(self.iterVal)-1:
                break

    #! Insertion sort method
    @property
    def InsertionSort(self):
        for i in range(1, len(self.iterVal)):
            # todo comparator คือตัวแปรที่ใช้สำหรับการ insert โดยให้เริ่มต้นตำแหน่งที่ 1 เสมอ
            comparator = self.iterVal[i]
            # todo reversed(self.iterVal[:i]) คือ reversed สมาชิกที่อยู่ใน array
            for j  in self.iterVal[i::-1]:
                # todo เปรียบเทียบระหว่าง j(สมาชิกตัวแรกที่อยู่ทางซ้ายของ comparator โดยนับจากตัวสุดท้าย) มากกว่า comparator
                if j > comparator:
                    # todo สลับตำแหน่ง เริ่มสลับตำแหน่ง
                    self.iterVal[self.iterVal.index(
                        comparator)], self.iterVal[self.iterVal.index(j)] = j, comparator

    #! Selection sort method
    @property
    def SelectionSort(self):
        for ex in range(len(self.iterVal)):
            # todo minx_idx คือ ตัวแปรที่หาจำนวนที่น้อยที่สุด โดย เริ่มต้นที่ตำแหน่งตัวเอง
            min_idx = ex
            # todo ex+1 คือการเริ่มต้นที่ตำแหน่งถัดไปของ ex
            for lt in range(ex+1, len(self.iterVal)):
               # todo เปรียบระหว่าง ตัวที่ min idx มากกกว่า ตัวที่ lt หรือไม่
                if self.iterVal[min_idx] > self.iterVal[lt]:
                    min_idx = lt  # todo ให้ min_idx มีค่าเท่ากับ lt เผื่อใช้หาตัวแหน่งที่น้อยกว่าในรอบถัดไป
            # todo สลับตำแหน่ง ตัวที่ ex(ตัวที่ใช้เปรียบเทียบ) และ ตัวที่ min_idx(ค่าน้อยที่สุด)
            maxVal = self.iterVal[ex]
            minVal = self.iterVal[min_idx]
            self.iterVal[ex], self.iterVal[min_idx] = minVal,maxVal

    #! Insert Method
    def insert_ele(self, idx: int, ele):
        # todo imp_var เก็บสมาชิค array ตั้งแต่ idx ถึง ตัวสุดท้าย
        imp_var = self.iterVal[idx:]
        # todo ให้ self.iterVal เก็บสมาชิกตั้งแต่ 0 ถึง idx-1 แทน
        self.iterVal = self.iterVal[:idx]
        # todo เพิ่ม ele เข้าต่อท้ายใน self.iterVal
        self.iterVal.append(ele)
        # todo รวม self.iterVal กับ imp_var เข้าด้วยกัน
        self.iterVal = self.iterVal+imp_var

    #! Delete Method
    def delete_ele(self, ele):
        # self.iterVal = list(filter(lambda s: s != ele, self.iterVal))
        self.iterVal = [i for i in self.iterVal if i != ele]

    #! Search Method
    def search_ele(self, ele, start=0):
        return self.iterVal.index(ele, start, len(self.iterVal))

    #! Min element
    @property
    def min_ele(self):
        self.BubbleSort
        return self.iterVal[0]

    #! Max element
    @property
    def max_ele(self):
        self.BubbleSort
        return self.iterVal[len(self.iterVal)-1]


if __name__ == '__main__':
    with open('data.txt', 'r') as f:
        read_num = f.read().split(' ')[0:12]
        num_lst = list(map(lambda s: int(s), read_num))
        arr_ins = Array(num_lst)
        print(arr_ins.iterVal)
        arr_ins.BubbleSort
        # print(arr_ins.search_ele(66))
        print(arr_ins.iterVal)
