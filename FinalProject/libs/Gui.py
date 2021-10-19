from prettytable import PrettyTable as pt
import random
from threading import Thread
import os
from backen_code import Hnode, BinaryHeap
from pprint import pprint


class CafeHeap:
    def __init__(self):
        self.refresh_run()

    def refresh_run(self):
        self.num_of_table = int(input("กรุณาใส่จำนวนโต๊ะ : "))
        self.menu = {i: random.randint(20, 50)
                     for i in range(1, 11)}
        self.bin_heap = BinaryHeap()
        self.table_detail = {}
        for i in range(1, self.num_of_table+1):
            self.table_detail[i] = 'ว่าง'
            self.bin_heap.insert(i)
        self.pre_info_customers = {}
        self.sheet_menu = pt()
        self.sheet_table = pt()
        self.sheet_menu.field_names = ["Menu", "Value"]
        self.sheet_table.field_names = ["โต๊ะ", 'สถานะ']
        self.multi_back_run()
        self.run()

    def update_info_hnode(self, cus_info, data, node):
        if node != None:
            if node.data == data:
                node.info[data].update(cus_info)
            self.update_info_hnode(cus_info, data, node.left)
            self.update_info_hnode(cus_info, data, node.right)

    def update_full_hnode(self, data, node):
        if node != None:
            if node.data == data:
                node.info[data]['สถานะ'] = 'ไม่ว่าง'
            self.update_full_hnode(data, node.left)
            self.update_full_hnode(data, node.right)

    def update_empty_hnode(self, data, node):
        if node != None:
            if node.data == data:
                node.info[data]['สถานะ'] == 'ว่าง'
            self.update_empty_hnode(data, node.left)
            self.update_empty_hnode(data, node.right)

    def check_freeHnode(self, node, data, proof):
        if node != None:
            if node.data == data and node.info[data]['สถานะ'] == 'ว่าง':
                proof.append(True)
            self.check_freeHnode(node.left, data, proof)
            self.check_freeHnode(node.right, data, proof)

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
            proof = []
            self.check_freeHnode(self.bin_heap.head, i, proof)
            if True in proof:
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
            elif choose_menu.isnumeric() == False:
                print('กรุณากรอกข้อมูลให้ถูกต้อง')
            elif int(choose_menu) > 10:
                print("เมนูนี้ไม่มีอยู่ในลิสต์ {}".format(choose_menu))
            elif int(choose_menu) <= 10:
                cus_info[table_no]['รายการที่สั่ง']["Menu {}".format(
                    choose_menu)] = self.menu[int(choose_menu)]

    def res_fuction(self):
        self.disp_free_table()
        res_table = int(input("ระบุโต๊ะที่ต้องการ : "))
        try:
            proof = []
            self.check_freeHnode(self.bin_heap.head, res_table, proof)
            if True in proof:
                acception = input("กรุณายืนยันโต๊ะนี้\nYes(Y)/No(N) : ")
                if acception in ['y', 'Y']:
                    self.update_full_hnode(res_table, self.bin_heap.head)
                    customer_info = {res_table: {
                        "จำนวนคน": None, "รายการที่สั่ง": {}}}
                    self.choose_menu(customer_info, res_table)
                    self.update_info_hnode(
                        customer_info[res_table], res_table, self.bin_heap.head)
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
        recipe_sheet = pt()
        bill_sheet.field_names = ["โต๊ะ", 'ราคาทั้งหมด']
        recipe_sheet.field_names = ['ราการ', 'ราคา']
        for i in range(1, self.num_of_table+1):
            data = self.bin_heap.get_node_info(i)
            if data[i]['สถานะ'] == 'ไม่ว่าง':
                bill_sheet.add_row(["โต๊ะ {}".format(i), sum(
                    list(data[i]['รายการที่สั่ง'].values()))])
        print(bill_sheet)
        while True:
            print("หากต้องการยกเลิกรายการ พิมพ์ N")
            res_table = input('กรุณาระบุโต๊ะที่ต้องการเก็บเงิน : \n')
            if res_table in ['N', 'n']:
                break
            res_table = int(res_table)
            try:
                data = self.bin_heap.get_node_info(res_table)
                data = data[res_table]
                for i, v in data['รายการที่สั่ง'].items():
                    recipe_sheet.add_row([i, v])
                print("{}".format("โต๊ะ {}".format(res_table).center(20, ' ')))
                print(recipe_sheet)
                print("{}".format("ราคาทั้งหมด {}".format(
                    str(sum(list(data['รายการที่สั่ง'].values())))).center(20, " ")))
                self.update_empty_hnode(res_table, self.bin_heap.head)
            except:
                print('กรุณากรอกลำดับโต๊ะที่อยู่ในลิสต์')

    def run(self):
        while True:
            # os.system('cls||clear')
            choice = int(
                input("{}\n1.จองโต๊ะ\n2.เช็คบิล\n3.เลือกจำนวนโต๊ะอีกครั้ง\n --> ".format("-"*50)))
            if choice == 1:
                self.res_fuction()
            elif choice == 2:
                self.checkbill()
                pass
            elif choice == 3:
                self.refresh_run()
            else:
                print('กรุณาเลือกตัวเลือก')


obj = CafeHeap()
obj.run()
