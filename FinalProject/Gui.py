from prettytable import PrettyTable as pt
import random
from threading import Thread
import os
from pprint import pprint


class CafeHeap:
    def __init__(self):
        self.refresh_run()

    def refresh_run(self):
        self.num_of_table = int(input("กรุณาใส่จำนวนโต๊ะ : "))
        self.menu = {i: random.randint(20, 50)
                     for i in range(1, 11)}
        self.table_detail = {i: "ว่าง" for i in range(1, self.num_of_table+1)}
        self.pre_info_customers = {}
        self.sheet_menu = pt()
        self.sheet_table = pt()
        self.sheet_menu.field_names = ["Menu", "Value"]
        self.sheet_table.field_names = ["โต๊ะ", 'สถานะ']
        self.multi_back_run()
        self.run()

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
        cus_info[table_no]['จำนวนคน'] = int(input('กรูณาระบุจำนวนคน : '))
        while cus_info[table_no]['จำนวนคน'] > 6:
            print("ระบุจำนวนได้ไม่เกิน 6.")
            cus_info[table_no]['จำนวนคน'] = int(input('กรูณาระบุจำนวนคน : '))
        print(self.sheet_menu)
        print("กรุณาเลือกเมนู\nหากเสร็จสิ้นแล้วพิมพ์ y:")
        while True:
            choose_menu = input()
            if choose_menu in ['Y', 'y']:
                break
            elif int(choose_menu)>10:
                print("เมนูนี้ไม่มีอยู่ในลิสต์ {}".format(choose_menu))
            elif int(choose_menu)<=10:
                cus_info[table_no]['รายการที่สั่ง']["Menu {}".format(
                    choose_menu)] = self.menu[int(choose_menu)]
            else:
                print('กรุณากรอกข้อมูลให้ถูกต้อง')

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
                elif acception in ['n', 'N']:
                    return
            else:
                print('โต๊ะ {} เต็มแล้ว'.format(res_table).center(50))
                self.run()
        except:
            print('โต๊ะนี้ไม่มีอยู่ในลิสต์'.center(50))
            self.run()

    def checkbill(self):
        bill_sheet = pt()
        bill_sheet.field_names = ["โต๊ะ", 'ราคาทั้งหมด']
        for i in self.pre_info_customers:
            vale = sum([k for (i, k) in self.pre_info_customers[i]
                       ['รายการที่สั่ง'].items()])
            bill_sheet.add_row([f"{i}", "{}".format(vale)])
            print(bill_sheet)
        while True:
            table = int(input("ระบุโต๊ะที่ต้องการ : \n"))
            receipt = pt()
            cus_table = self.pre_info_customers[table]['รายการที่สั่ง']
            receipt.field_names = [f"โต๊ะ {table}"]
            for (menu, cost) in cus_table.items():
                receipt.add_row(["{} {}".format(menu, cost)])
            receipt.add_row(['ราคาทั้งหมด {}'.format(
                sum([k for (i, k) in cus_table.items()]))])
            # print(receipt)
            self.table_detail[table] = 'ว่าง'
            receipt_table = pt()
            receipt_table.field_names = ['รายการ','ราคา']
            for i in cus_table:
                receipt_table.add_row([i,cus_table[i]])
            print("{}".format("โต๊ะ {} ".format(table).center(20," ")))
            print(receipt_table)
            print("รวมทั้งสิ้น : {} บาท".format( sum([k for (i, k) in cus_table.items()])))
            if input('พิมพ์ Y หากต้องการดำเนินการต่อ หรือ N หากต้องการหยุด :\n') in ['n', 'N']:
                break

    def run(self):
        while True:
            # os.system('cls||clear')
            choice = int(
                input("{}\n1.จองโต๊ะ\n2.เช็คบิล\n3.เลือกจำนวนโต๊ะอีกครั้ง\n --> ".format("-"*50)))
            if choice == 1:
                self.res_fuction()
            elif choice == 2:
                self.checkbill()
            elif choice == 3:
                self.refresh_run()
            else:
                print('กรุณาเลือกตัวเลือก')


obj = CafeHeap()
obj.run()
