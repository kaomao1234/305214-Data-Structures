from threading import Thread
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import NumericProperty
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from module.LoadingBar import LoadingBar
from module.MenuCard import MenuCard
from module.MessageBar import MessageBar
from module.TableCard import TableCard
from module.RecipeCard import RecipeCard
from module.BillCard import BillCard
from kivy.uix.recycleview import RecycleView
kv_file = ["IntroScreen", 'TableScreen', 'MenuScreen', 'CheckBillScreen']
for i in kv_file:
    Builder.load_file(f"kv_file/{i}.kv")


class IntroScreen(MDScreen):
    def __init__(self, root, **kw):
        super(IntroScreen, self).__init__(**kw)
        self.root: MainManager = root
        self.loading = LoadingBar(
            auto_dismiss=False, bg_color=self.dr_white, duration=0.5, progess_color=self.black)
        self.show_msg = MessageBar(text='กรุณาเพิ่มจำนวนลูกค้าก่อนเลือกโต๊ะ', bg_color=self.dr_white,
                                   icon='alert-decagram-outline',
                                   text_color=self.black, font_size=18, border_color=self.red, border_weight=1.2,
                                   duration=0.5)

    def on_press(self):
        field_tables = self.ids.field_tables.text
        if field_tables.isnumeric() and int(field_tables) <= 20:
            self.loading.open()
            self.root.disabled = True
            Thread(target=self.add_tablecard, args=(field_tables,)).start()
            Clock.schedule_once(self.to_tablescreen, 0.05 * int(field_tables))

    def to_tablescreen(self, *e):
        self.loading.dismiss()
        self.root.switch_screen('table_screen', 'left', 0.2)
        self.ids.field_tables.text = ''
        self.root.disabled = False

    def add_tablecard(self, field_tables: str, *e):
        tablelst: RecycleView = self.root.all_frame['TableScreen'].ids.tablelst
        tablelst.data = [{'number_table': i,
                          'press': self.card_onPress,
                          'owner': tablelst,
                          'count_number': 0,
                          'second_text_color': 'Primary'}
                         for i in range(1, int(field_tables) + 1)]

    def card_onPress(self, instance: TableCard):
        table_num = instance.number_table
        number_cus = instance.ids.count_cus.text
        menu_instance = self.root.all_frame['MenuScreen']
        menu_instance.table_no = table_num
        menu_instance.count_cus = int(instance.ids.count_cus.text)
        if int(number_cus) > 0:
            self.root.switch_screen('menu_screen', 'left', 0.2)
        else:
            self.show_msg.open()


class TableScreen(MDScreen):
    def __init__(self, root, **kw):
        super(TableScreen, self).__init__(**kw)
        self.root:MainManager = root

    def back_onPress(self):
        self.ids.tablelst.data = {}
        self.ids.table_manager.current = 'screen_1'
        self.root.switch_screen('intro_screen', 'right', 0.2)


class MenuScreen(MDScreen):
    table_no = NumericProperty(0)
    count_cus = NumericProperty(0)

    def __init__(self, root, **kw):
        super(MenuScreen, self).__init__(**kw)
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
        for name, value in self.menu.items():
            self.ids.menulst.add_widget(
                MenuCard(root=self, menu_name=name, price=value))
        self.root:MainManager = root
        self.show_msg = MessageBar(text='กรุณาเลือกเครื่องดื่ม', bg_color=self.dr_white, icon='alert-decagram-outline',
                                   text_color=self.black, font_size=18, border_color=self.red, border_weight=1.2,
                                   duration=0.5)

    def menu_info(self, instance):
        bill_info = instance.bill_info[instance.number_table].items()
        bill_info = dict(
            sorted(bill_info, key=lambda s: int(s[0].split(".")[0])))
        menu_view = self.root.all_frame['CheckBillScreen'].ids.menu_list
        for name, value in bill_info.items():
            price = self.menu[name]
            menu_view.add_widget(RecipeCard(
                menu_name=name, count=value, price=price))
        self.root.all_frame['CheckBillScreen'].ids.total.text = str(
            instance.bill_info['ราคาทั้งหมด'])

    def billcard_press(self, instance):
        self.root.all_frame['TableScreen'].ids.table_manager.current = 'screen_1'
        self.root.all_frame['CheckBillScreen'].table_no = self.table_no
        self.menu_info(instance)
        self.root.switch_screen('checkbill_screen', 'left', 0.2)

    def on_press(self):
        total = self.ids.total.text
        if int(total) == 0:
            self.show_msg.open()
        else:
            self.add_billcard()
            self.remove_tablecard()
            self.reset_menu_number()
            self.root.switch_screen('table_screen', 'right', 0.2)

    def add_billcard(self):
        data = self.get_data()
        billlst = self.root.all_frame['TableScreen'].ids.billlst
        billlst.data.append({'number_table': self.table_no, 'number_cus': data['จำนวนคน'], 'bill_info': data,
                             'press': self.billcard_press})

    def remove_tablecard(self):
        table_lst:RecycleView = self.root.all_frame['TableScreen'].ids.tablelst
        for i in table_lst.data:
            if i['number_table'] == self.table_no:
                index = table_lst.data.index(i)
                table_lst.data.pop(index)

    def get_data(self):
        menulst = self.ids.menulst
        data_sold = {self.table_no: {}, 'จำนวนคน': self.count_cus,
                     "ราคาทั้งหมด": self.ids.total.text}
        for i in menulst.children:
            if int(i.ids.count_menu.text) > 0:
                data_sold[self.table_no][i.menu_name] = int(
                    i.ids.count_menu.text)
        return data_sold

    def reset_menu_number(self):
        for i in self.ids.menulst.children:
            i.ids.count_menu.text = '0'
            i.reduce()


class CheckBillScreen(MDScreen):
    table_no = NumericProperty(0)

    def __init__(self, root, **kw):
        super(CheckBillScreen, self).__init__(**kw)
        self.root: MainManager= root
        self.show_msg = MessageBar(
            text='ยืนยันเรียบร้อย',
            text_color=self.black,
            icon='alert-decagram-outline',
            bg_color=self.dr_white,
            duration=0.5
        )

    def on_press(self):
        self.show_msg.open()
        info_instance: IntroScreen = self.root.all_frame['IntroScreen']
        bill_list = self.root.all_frame['TableScreen'].ids.billlst
        table_list = self.root.all_frame['TableScreen'].ids.tablelst
        for i in bill_list.data:
            if i['number_table'] == self.table_no:
                bill_list.data.remove(i)
                table_card = {'number_table': self.table_no,
                              'press': info_instance.card_onPress,
                              'owner': table_list,
                              'count_number': 0,
                              'second_text_color': 'Primary'}
                table_list.data.insert(self.table_no-1, table_card)
        self.root.switch_screen('table_screen', 'right', 0.2)

    def back_click(self):
        self.ids.menu_list.clear_widgets()
        self.root.switch_screen('table_screen', 'right', 0.2)


class MainManager(ScreenManager):
    def __init__(self, **kw):
        super(MainManager, self).__init__(**kw)
        self.all_frame = {}
        for i in [IntroScreen, TableScreen, MenuScreen, CheckBillScreen]:
            self.all_frame[i.__name__] = i(self)
            self.add_widget(self.all_frame[i.__name__])

    def switch_screen(self, current, direction=None, duration=0):
        self.transition.direction = direction
        self.transition.duration = duration
        self.current = current


class CafeHeap(MDApp):
    def build(self):
        return MainManager()


if __name__ == '__main__':
    CafeHeap().run()
