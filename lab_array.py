import time
# ! 1. ให้เปิดNotepad พิมพ์ค่าต่อไปนี้แล้วsave เป็นชื่อdata.txt ให้อ่านข้อมูลจากไฟล์โดยแต่ละกําหนดindex เริ่มต้นเองให้สร้างfunctionชื่อว่าcreateมาเก็บในarray เพียง12 ค่าและแสดงค่า
# todo 34 24 3 66 47 18 8 26 55 82 29 32 17 6 72 27 23 9 44 12 60 89 10 57 46 54 7 33 95 56 77 22 51 19


class Array:
    def __init__(self, *arg: int):
        self.get_array = arg[0] if type(arg[0]) in (list, tuple) else list(arg)

    #! Bubble sort method
    @property
    def bubble_sort(self):
        for i in range(len(self.get_array)):
            # todo ตัวแปรที่ใช้หยุด loop เมื่อข้อมูลทุกตัวเรียงลำดับแล้ว
            stop = 0
            # todo loop กระทำ len(list)-1 รอบ เพื่อให้ตัวเลขสามรถจับคู่กัน โดย ไม่ให้ สมาชิกสุดท้ายเป็นตำแหน่งที่ n
            for j in range(0, len(self.get_array)-1):
                # todo ถ้า ตำแหน่งที่ n มีค่ามากว่า n+1
                if self.get_array[j] > self.get_array[j+1]:
                    # todo here_ele คือตัวแปรที่ n, next_ele คือตัวแปรที่ n+1
                    here_ele, next_ele = self.get_array[j], self.get_array[j+1]
                    # todo สลับสมาชิก
                    self.get_array[j] = next_ele
                    self.get_array[j+1] = here_ele
                # todo เมื่อไม่เข้าเงื่อนไขด้านบน
                else:
                    stop += 1
            if stop == len(self.get_array)-1:
                break

    #! Insertion sort method
    @property
    def insertion_sort(self):
        for i in range(1, len(self.get_array)):
            # todo ins_ele คือตัวแปรที่ใช้สำหรับการ insert โดยให้เริ่มต้นตำแหน่งที่ 1 เสมอ
            ins_ele = self.get_array[i]
            # todo left_ele คือ array ที่แบ่งออกมาจากทางด้ายของ ins_ele เพื่อใช้สำหรับการสลับที่
            left_ele = self.get_array[:self.get_array.index(ins_ele)]
            # todo left_ele[::-1] คือ reversed สมาชิกที่อยู่ใน array
            for j in left_ele[::-1]:
                # todo เปรียบเทียบระหว่าง j(สมาชิกตัวแรกที่อยู่ทางซ้ายของ ins_ele โดยนับจากตัวสุดท้าย) มากกว่า ins_ele
                if j > ins_ele:
                    # todo สลับตำแหน่ง เริ่มสลับตำแหน่ง
                    self.get_array[self.get_array.index(
                        ins_ele)], self.get_array[self.get_array.index(j)] = j, ins_ele

    #! Selection sort method
    @property
    def selection_sort(self):
        for ex in range(len(self.get_array)):
            # todo minx_idx คือ ตัวแปรที่หาจำนวนที่น้อยที่สุด โดย เริ่มต้นที่ตำแหน่งตัวเอง
            min_idx = ex
            # todo ex+1 คือการเริ่มต้นที่ตำแหน่งถัดไปของ ex
            for lt in range(ex+1, len(self.get_array)):
               # todo เปรียบระหว่าง ตัวที่ min idx มากกกว่า ตัวที่ lt หรือไม่
                if self.get_array[min_idx] > self.get_array[lt]:
                    min_idx = lt  # todo ให้ min_idx มีค่าเท่ากับ lt เผื่อใช้หาตัวแหน่งที่น้อยกว่าในรอบถัดไป
            # todo สลับตำแหน่ง ตัวที่ ex(ตัวที่ใช้เปรียบเทียบ) และ ตัวที่ min_idx(ค่าน้อยที่สุด)
            self.get_array[ex], self.get_array[min_idx] = self.get_array[min_idx], self.get_array[ex]

    #! Insert Method
    def insert_ele(self, idx: int, ele):
        # todo imp_var เก็บสมาชิค array ตั้งแต่ idx ถึง ตัวสุดท้าย
        imp_var = self.get_array[idx:]
        # todo ให้ self.get_array เก็บสมาชิกตั้งแต่ 0 ถึง idx-1 แทน
        self.get_array = self.get_array[:idx]
        # todo เพิ่ม ele เข้าต่อท้ายใน self.get_array
        self.get_array.append(ele)
        # todo รวม self.get_array กับ imp_var เข้าด้วยกัน
        self.get_array = self.get_array+imp_var

    #! Delete Method
    def delete_ele(self, ele):
        self.get_array = list(filter(lambda s: s != ele, self.get_array))

    #! Search Method
    def search_ele(self, ele, start=0):
        return self.get_array.index(ele, start, len(self.get_array))

    #! Min element
    @property
    def min_ele(self):
        self.bubble_sort
        return self.get_array[0]

    #! Max element
    @property
    def max_ele(self):
        self.bubble_sort
        return self.get_array[len(self.get_array)-1]


if __name__ == '__main__':
    with open('data.txt', 'r') as f:
        read_num = f.read().split(' ')[:12]
        num_lst = list(map(lambda s: int(s), read_num))
        print(f'Unort : {read_num}')
        arr_ins = Array(num_lst)
        arr_ins.insertion_sort
        print('Sorted :', arr_ins.get_array)
