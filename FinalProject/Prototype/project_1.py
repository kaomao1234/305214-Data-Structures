from threading import Thread

from prettytable import PrettyTable as pt

from backen_code import BinaryHeap, LinkedList


class CafeComRun:
    def __init__(self):
        self.menu = {"1.Espressso": 35,
                     "2.Cappuccino": 45,
                     "3.Latte": 50,
                     "4.Mocha": 50,
                     "5.Tea": 40,
                     "6.Green Tea(Milk)": 40,
                     "7.Tea(milk)": 40,
                     "8.Lemon tea": 45,
                     "9.Black Tea": 35,
                     "10.Dark Chocolate": 55,
                     "11.Fresh milk": 35,
                     "12.Chocotate": 40}
        self.number_map_menu = {i: list(self.menu.keys())[
            i-1] for i in range(1, 13)}
        self.input_numtable = None
        self.bin_heap = BinaryHeap()
        self.linkList = LinkedList()
        self.sheet_menu = pt()
        self.sheet_table = pt()
        self.sheet_menu.field_names = ["Menu", "Value"]
        self.sheet_table.field_names = ["โต๊ะ", 'สถานะ']

    def display_table(self):  # todo แสดงโต๊ะที่ว่าง
        table = self.read_binary_heap()
        for no, stat in table.items():
            if stat['สถานะ'] == 'ว่าง':
                self.sheet_table.add_row([no, stat['สถานะ']])
        print(self.sheet_table.get_string(title='ที่นั่งทั้งหมด'))

    def display_billtable(self):  # todo แสดงโต๊ะที่สามารถเก็บเงินได้
        sheet_bill = pt()
        table = self.read_binary_heap()
        sheet_bill.field_names = ['โต๊ะ', 'ราคา']
        count = 0
        for no, data in table.items():
            if 'สถานะ' in data and data['สถานะ'] == 'ไม่ว่าง':
                total_value = 0
                for name, val in data['รายการที่สั่ง'].items():
                    total_value += self.menu[name]*val
                sheet_bill.add_row([no, total_value])
                count += 1
        if count > 0:
            print(sheet_bill.get_string(title='ที่นั่งทั้งหมด'))
            return True
        else:
            print("----> ไม่มีโต๊ะที่ถูกจอง <----")
            return False

    def check_minus_num(self, number):  # todo ตรวจสอบจำนวนติดลบ
        try:
            if int(number) < 0:
                return True
            elif self.check_float_num(number) == True:
                return 'float'
            else:
                return False
        except:
            return "str"

    def config_menu(self):
        for menu, value in self.menu.items():
            self.sheet_menu.add_row([menu, value])

    def create_table(self):  # todo กำหนดโต๊ะขึ้นมา
        for i in range(1, self.input_numtable+1):
            self.bin_heap.insert(i)

    def read_binary_heap(self):  # todo อ่านข้อมูลใน node
        table = {}
        for i in range(1, self.input_numtable + 1):
            data = self.bin_heap.get_node_info(i)
            table.update({i: data})
        return table

    def check_float_num(self, number):  # todo ตรวจสอบจำนวนทศนิยม
        num_float = float(number)
        num_int = int(num_float)
        if num_float - num_int > 0:
            return True
        else:
            return False

    def input_tablefunc(self):  # todo ฟังก์ชันสำหรับ Input จำนวนโต๊ะ
        while True:
            self.input_numtable = input("กรุณาใส่จำนวนโต๊ะ : ")
            if self.check_minus_num(self.input_numtable) == "str":
                print("----> กรอกได้เฉพาะตัวเลขเท่านั้น <----")
            elif self.check_minus_num(self.input_numtable) == True:
                print("----> กรอกจำนวนต้องไม่ติดลบ <----")
            elif self.check_float_num(self.input_numtable):
                print("----> กรอกได้เฉพาะจำนวนเต็มเท่านั้น <----")
            else:
                self.input_numtable = int(self.input_numtable)
                if self.input_numtable == 0:
                    print("----> กรอกจำนวนต้องมากกว่า 0 <----")
                elif self.input_numtable > 20:
                    print("----> กรอกจำนวนไม่เกิน 20 ตัว <----")
                else:
                    break

    # todo ฟังก์ชันสำหรับ Input จำนวนลูกค้า
    def input_numof_customer(self, customer_info: dict):
        while True:
            customer_info['จำนวนคน'] = input("กรูณาระบุจำนวนคน : ")
            if self.check_minus_num(customer_info['จำนวนคน']) == True:
                print("----> กรอกจำนวนต้องไม่ติดลบ <----")
            elif self.check_minus_num(customer_info['จำนวนคน']) == 'str':
                print("----> กรอกได้เฉพาะตัวเลขเท่านั้น <----")
            elif self.check_float_num(customer_info['จำนวนคน']):
                print("----> กรอกได้เฉพาะจำนวนเต็มเท่านั้น <----")
            else:
                customer_info['จำนวนคน'] = int(customer_info['จำนวนคน'])
                if customer_info['จำนวนคน'] == 0:
                    print("----> กรอกจำนวนต้องมากกว่า 0 <----")
                elif customer_info['จำนวนคน'] > 6:
                    print("----> กรอกจำนวนได้ไม่เกิน 6 คน <----")
                else:
                    break

    def acception_func(self):  # todo ฟังก์ชันสำหรับ Input ตัวแปร acception
        while True:
            acception = input("กรุณายืนยันโต๊ะนี้\nYes(Y)/No(N) : ")
            if acception in ['y', 'Y']:
                return 'y'
            elif acception in ['n', 'N']:
                return 'n'
            else:
                print("----> กรอกเฉพาะ Y หรือ N เท่านั้น <----")

    # todo ฟังก์ชันสำหรับ Input จำนวนสินค้า
    def num_menu_func(self, name_menu, customer_info):
        while True:
            print("หากไม่ต้องการให้กรอก 0")
            num_menu_var = input("{} จำนวน : ".format(name_menu))
            if self.check_minus_num(num_menu_var) == True:
                print("----> กรอกจำนวนต้องไม่ติดลบ <----")
            elif self.check_minus_num(num_menu_var) == 'str':
                print("----> กรอกได้เฉพาะตัวเลขเท่านั้น <----")
            elif self.check_float_num(num_menu_var):
                print("----> กรอกได้เฉพาะจำนวนเต็มเท่านั้น <----")
            else:
                num_menu_var = int(num_menu_var)
                if num_menu_var == 0:
                    print("----> ยกเลิกเมนูนี้ <----")
                    break
                elif num_menu_var > 15:
                    print("----> กรอกจำนวนไม่เกิน 15 ชิ้น <----")
                else:
                    customer_info['รายการที่สั่ง'].update(
                        {name_menu: num_menu_var})
                    break

    def choose_table(self):  # todo ฟังก์ชันเลือกโต๊ะ
        self.display_table()
        table_info = self.read_binary_heap()
        choose_table_var = input("ระบุโต๊ะที่ต้องการ : ")
        if self.check_minus_num(choose_table_var) == True:
            print("----> กรอกจำนวนต้องไม่ติดลบ<----")
        elif self.check_minus_num(choose_table_var) == 'str':
            print("----> กรอกได้เฉพาะตัวเลขเท่านั้น <----")
        elif self.check_float_num(choose_table_var):
            print("----> กรอกได้เฉพาะจำนวนเต็มเท่านั้น <----")
        else:
            choose_table_var = int(choose_table_var)
            if choose_table_var == 0:
                print("----> กรอกจำนวนต้องมากกว่า 0 <----")
            elif choose_table_var > self.input_numtable or table_info[choose_table_var] == 'ไม่ว่าง':
                print('----> กรอกเฉพาะโต๊ะที่แสดงเท่านั้น <----')
            else:
                acception_var = self.acception_func()
                if acception_var == 'y':
                    customer_info = {'จำนวน': None,
                                     'รายการที่สั่ง': {}, 'สถานะ': 'ไม่ว่าง'}
                    self.choose_menu(customer_info)
                    self.bin_heap.update_info_node(
                        choose_table_var, customer_info)
                    self.linkList.add(choose_table_var)
                elif acception_var == 'n':
                    return

    def choose_menu(self, customer_info: dict):  # todo ฟังก์ชันเลือกเมนู
        self.config_menu()
        self.input_numof_customer(customer_info)
        print(self.sheet_menu)
        print("กรุณาเลือกเมนู\nหากเสร็จสิ้นแล้วพิมพ์ y:")
        while True:
            input_menu = input("กรุณาเลือกเมนู: ")
            if input_menu in ['Y', 'y']:
                break
            elif self.check_minus_num(input_menu) == True:
                print("----> กรอกจำนวนต้องไม่ติดลบ <----")
            elif self.check_minus_num(input_menu) == 'str':
                print("----> ไม่พบตัวเลือก {} <----".format(input_menu))
            elif self.check_float_num(input_menu):
                print("----> กรอกได้เฉพาะจำนวนเต็มเท่านั้น <----")
            elif self.check_float_num(input_menu) == False and self.check_minus_num(input_menu) == False:
                input_menu = int(input_menu)
                if input_menu in self.number_map_menu == False:
                    print("เมนูนี้ไม่มีอยู่ในลิสต์ {}".format(input_menu))
                else:
                    self.num_menu_func(
                        self.number_map_menu[input_menu], customer_info)

    def checkbill(self):  # todo ฟังก์ชันเช็คบิล
        while True:
            if self.display_billtable() == False:
                break
            print("----> หากต้องการยกเลิกรายการพิมพ์ N <----")
            choose_table = input('กรุณาระบุโต๊ะที่ต้องการเก็บเงิน : \n')
            if choose_table in ['n', 'N']:
                break
            elif self.check_minus_num(choose_table) == True:
                print("----> กรอกจำนวนต้องไม่ติดลบ <----")
            elif self.check_float_num(choose_table):
                print("----> กรอกได้เฉพาะจำนวนเต็มเท่านั้น <----")
            elif self.check_minus_num(choose_table) == False and self.check_float_num(choose_table) == False:
                choose_table = int(choose_table)
                if choose_table == 0:
                    print("----> กรอกจำนวนต้องมากกว่า 0 <----")
                else:
                    try:
                        self.display_recipe(choose_table)
                    except:
                        print(
                            '----> โต๊ะ {} ไม่อยู่ในลิสต์ <----'.format(choose_table))
            else:
                print("----> ไม่พบตัวเลือก {} <----".format(choose_table))

    def display_recipe(self, table_idx):  # todo ฟังก์ชันแสดงใบเสร็จรับเงิน
        recipe_sheet = pt()
        recipe_sheet.field_names = ['รายการ', 'จำนวน', 'ราคา']
        data = self.bin_heap.get_node_info(table_idx)
        total_value = 0
        for menu, value in data['รายการที่สั่ง'].items():
            recipe_sheet.add_row([menu, value, self.menu[menu]*value])
            total_value += self.menu[menu]*value
        print(recipe_sheet.get_string(title='โต๊ะ {}'.format(table_idx)))
        print("ราคาทั้งหมด {}".format(total_value).center(20))
        self.bin_heap.update_info_node(
            table_idx, {'สถานะ': 'ว่าง', 'รายการที่สั่ง': None})
        self.linkList.delete(table_idx)

    def reset_pro(self):  # todo ฟังก์ชันตั้งต่าโปรแกรมใหม่
        self.input_tablefunc()
        self.sheet_menu = pt()
        self.sheet_table = pt()
        self.sheet_menu.field_names = ["Menu", "Value"]
        self.sheet_table.field_names = ["โต๊ะ", 'สถานะ']
        self.bin_heap.reset_node()
        self.linkList.reset_node()
        self.create_table()

    def choice_screen(self):  # todo ฟังก์ชันหน้าแรกของโรปแกรม
        self.input_tablefunc()
        self.create_table()
        while True:
            choice = input(
                "1.จองโต๊ะ\n2.เช็คบิล\n3.เริ่มโปรแกรมใหม่\n4.พิมพ์ 4 เพื่อหยุดโปรแกรม \n --> ")
            if self.check_minus_num(choice) == True:
                print("----> กรอกจำนวนต้องไม่ติดลบ <----")
            elif self.check_minus_num(choice) == 'str':
                print("----> กรอกได้เฉพาะตัวเลขเท่านั้น <----")
            elif self.check_float_num(self.input_numtable):
                print("----> กรอกได้เฉพาะจำนวนเต็มเท่านั้น <----")
            else:
                choice = int(choice)
                if choice == 0:
                    print("----> กรอกจำนวนต้องมากกว่า 0 <----")
                else:
                    if choice == 1:
                        self.choose_table()
                    elif choice == 2:
                        self.checkbill()
                    elif choice == 3:
                        self.reset_pro()
                    elif choice == 4:
                        print("----> หยุดการทำงาน <-----".center(20, " "))
                        break
                    else:
                        print('----> กรอกเฉพาะตัวเลือกที่แสดงเท่านั้น <----')


if __name__ == '__main__':
    cafe_obj = CafeComRun()
    cafe_obj.choice_screen()
