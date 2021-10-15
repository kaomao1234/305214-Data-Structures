from prettytable import PrettyTable as pt
import random
from threading import Thread
import os
from pprint import pprint


class CafeHeap:
    def __init__(self):
        self.num_of_table = int(input("กรุณาใส่จำนวนโต๊ะ : "))
        self.menu = {i: random.randint(20, 50)
                     for i in range(1, 11)}
        self.table_detail = {i: "ว่าง" for i in range(1, self.num_of_table)}
        self.pre_info_customers = {}
        self.sheet_menu = pt()
        self.sheet_table = pt()
        self.sheet_menu.field_names = ["Menu", "Value"]
        self.sheet_table.field_names = ["โต๊ะ", 'สถานะ']
        self.multi_back_run()

    def multi_back_run(self):
        task = [self.config_menu, self.config_node]
        for i in task:
            Thread(target=i).start()

    def config_menu(self):
        for i in self.menu:
            self.sheet_menu.add_row(["Menu {}".format(i), self.menu[i]])

    def config_node(self):
        for i in self.table_detail:
            self.sheet_table.add_row(
                ["โต๊ {}".format(i), self.table_detail[i]])

    def disp_free_table(self):
        free_table_sheet = pt()
        free_table_sheet.field_names = ["โต๊ะ", 'สถานะ']
        for i in self.table_detail:
            if self.table_detail[i] == 'ว่าง':
                free_table_sheet.add_row(["โต๊ะ {}".format(i), "ว่าง"])
        print(free_table_sheet)

    def choose_menu(self, cus_info: dict, table_no: int):
        print(self.sheet_menu)
        print("กรุณาเลือกเมนู\nหากเสร็จสิ้นแล้วพิมพ์ y:")
        while True:
            choose_menu = input()
            if choose_menu in ['Y', 'y']:
                break
            cus_info[table_no]['รายการที่สั่ง']["Menu {}".format(
                choose_menu)] = self.menu[int(choose_menu)]

    def res_fuction(self):
        self.disp_free_table()
        res_table = int(input("ระบุโต๊ะที่ต้องการ : "))
        try:
            if self.table_detail[res_table] == "ว่าง":
                acception = input("กรุณายืนยันโต๊ะนี้\nYes(Y)/No(N) : ")
                if acception in ['y', 'Y']:
                    self.table_detail[res_table] = 'ไม่ว่าง'
                    customer_info = {res_table: {
                        "จำนวนคน": None, "รายการที่สั่ง": {}}}
                    self.choose_menu(customer_info, res_table)
                    self.pre_info_customers.update(customer_info)
                    pprint(self.pre_info_customers)
                else:
                    self.run()
            else:
                print('โต๊ะ {} เต็มแล้ว'.format(res_table).center(50))
                self.run()
        except:
            print('โต๊ะนี้ไม่มีอยู่ในลิสต์'.center(50))
            self.run()

    def run(self):
        while True:
            # os.system('cls||clear')
            choice = int(input("{}\n1.จองโต๊ะ\n2.เช็คบิล\n".format("-"*50)))
            if choice == 1:
                self.res_fuction()
            else:
                break


obj = CafeHeap()
obj.run()
