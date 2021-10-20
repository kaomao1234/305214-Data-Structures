from threading import Thread

from prettytable import PrettyTable as pt

from backen_code import BinaryHeap, LinkedList


class CafeHeap:
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
        self.list_key_menu = list(self.menu.keys())
        self.refresh_run()

    def refresh_run(self):
        while True:
            try:
                self.num_of_table = int(input("กรุณาใส่จำนวนโต๊ะ : "))
            except:
                print("----> ใส่ได้เฉพาะตัวเลขเท่านั้น <----")
            else:
                if self.num_of_table >= 20 or self.num_of_table < 1:
                    print("----> ระบุได้ไม่เกิน 20 ตัว <----")
                else:
                    break
        self.bin_heap = BinaryHeap()
        self.linkList = LinkedList()
        self.table_detail = {}
        for i in range(1, self.num_of_table + 1):
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
            self.sheet_menu.add_row(["{}".format(i), self.menu[i]])

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

    def config_num_of_cus(self, cus_info: dict, table_no: int):
        while True:
            cus_info[table_no]['จำนวนคน'] = int(input('กรูณาระบุจำนวนคน : '))
            if cus_info[table_no]['จำนวนคน'] > 6:
                print("ระบุจำนวนได้ไม่เกิน 6.")
            else:
                break

    def choose_menu(self, cus_info: dict, table_no: int):
        self.config_num_of_cus(cus_info, table_no)
        print(self.sheet_menu)
        print("กรุณาเลือกเมนู\nหากเสร็จสิ้นแล้วพิมพ์ y:")
        while True:
            choose_menu = input()
            if choose_menu in ['Y', 'y']:
                break
            elif choose_menu.isnumeric() == False:
                print('กรุณากรอกข้อมูลให้ถูกต้อง')
            elif int(choose_menu) > 12 or int(choose_menu) <= 0:
                print("เมนูนี้ไม่มีอยู่ในลิสต์ {}".format(choose_menu))
            elif int(choose_menu) <= 12:
                menu = self.list_key_menu[int(choose_menu) - 1]
                cus_info[table_no]['รายการที่สั่ง'][menu] = self.menu[menu]

    def res_fuction(self):
        self.disp_free_table()
        try:
            res_table = int(input("ระบุโต๊ะที่ต้องการ : "))
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
                    self.linkList.add(res_table)
                elif acception in ['n', 'N']:
                    return
            else:
                print('! โต๊ะ {} เต็มแล้ว !'.format(res_table).center(20, '='))
        except:
            print('โต๊ะนี้ไม่มีอยู่ในลิสต์'.center(20, '='))

    def check_list_tableBill(self):
        bill_sheet = pt()
        bill_sheet.field_names = ["โต๊ะ", 'ราคาทั้งหมด']
        count = 0
        for i in range(1, self.num_of_table + 1):
            data = self.bin_heap.get_node_info(i)
            if data[i]['สถานะ'] == 'ไม่ว่าง':
                bill_sheet.add_row(["โต๊ะ {}".format(i), sum(
                    list(data[i]['รายการที่สั่ง'].values()))])
                count += 1
        if count == 0:
            print("----> ไม่มีโต๊ะที่ถูกจอง <----")
        else:
            print(bill_sheet)
        return count

    def checkbill(self):
        while self.check_list_tableBill() > 0:
            recipe_sheet = pt()
            recipe_sheet.field_names = ['รายการ', 'ราคา']
            print("----> หากต้องการยกเลิกรายการพิมพ์ N <----")
            while True:
                res_table = input('กรุณาระบุโต๊ะที่ต้องการเก็บเงิน : \n')
                if res_table in ['N', 'n']:
                    print("---> หยุดดำเนินการเช็คบิล <----")
                    return
                elif res_table.isnumeric():
                    res_table = int(res_table)
                    break
                else:
                    print("----> กรอกได้้เฉพาะตัวเลขเท่านั้น !!!! <----")
            try:
                data = self.bin_heap.get_node_info(res_table)
                data = data[res_table]
                for menu, value in data['รายการที่สั่ง'].items():
                    recipe_sheet.add_row([menu, value])
                total_value = sum(list(data['รายการที่สั่ง'].values()))
                print("{}".format("โต๊ะ {}".format(res_table).center(20, ' ')))
                print(recipe_sheet)
                print("ราคาทั้งหมด {}".format(total_value).center(20))
                self.update_empty_hnode(res_table, self.bin_heap.head)
                self.linkList.delete(res_table)
            except:
                print('----> โต๊ะ {} ไม่อยู่ในลิสต์ <----'.format(res_table))

    def run(self):
        while True:
            try:
                choice = int(
                    input(
                        "{}\n1.จองโต๊ะ\n2.เช็คบิล\n3.เลือกจำนวนโต๊ะอีกครั้ง\n4.พิมพ์ 4 เพื่อหยุดโปรแกรม \n --> ".format(
                            "-" * 20)))
            except:
                print("---> พิมพ์เฉพาะตัวเลขเท่านั้น <---")
            else:
                if choice == 1:
                    self.res_fuction()
                elif choice == 2:
                    self.checkbill()
                elif choice == 3:
                    self.refresh_run()
                elif choice == 4:
                    print("----> หยุดการทำงาน <-----".center(20, " "))
                    break
                else:
                    print('----> กรุณาเลือกตัวเลือก <----')


if __name__ == '__main__':
    CafeHeap()
