import os
from kivy import Config
from kivy.core.text import markup
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '640')
Config.set('graphics', 'minimum_width', '360')
Config.set('graphics', 'minimum_height', '640')
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'multisamples', '0')
from kivymd.uix.button import MDRoundFlatButton, MDFlatButton, MDRaisedButton
from kivy.uix.behaviors import ButtonBehavior
from kivymd.app import MDApp
from functools import partial
from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivy.utils import get_color_from_hex
from kivymd.uix.card import MDCard
from kivy.properties import StringProperty, NumericProperty
from kivymd.uix.dialog import MDDialog
from kivy.uix.label import Label
import kivy
print(int("-1"))

for i in ['introScreen', 'Queue_table(table)', 'Queue_table(menu)']:
    Builder.load_file(f"{i}.kv")


class Num_customer(MDBoxLayout):
    pass


class MenuCard(MDCard):
    menu_name = StringProperty()
    value = NumericProperty()


class TableCard(MDCard, ButtonBehavior):
    num_table = NumericProperty()

    def __init__(self, root, **kw):
        super(TableCard, self).__init__(**kw)
        self.root = root
        self.container_manager = self.root.ids.container_manager
        self.checkbill_view = self.root.ids.queuetable.ids.checkbill_view
        
    def to_check_bill_sc(self):
        self.root
    def add_cus_onpress(self, dialog, container, text_event, btn):
        if text_event.text.isnumeric():
            if 0 < int(text_event.text) <= 6:
                self.ids.show_num_cus.text = '{}/6'.format(text_event.text)
                self.container_manager.transition.direction = 'left'
                self.container_manager.transition.duration = 0.2
                self.container_manager.current = 'menu_screen'
                dialog.dismiss()

            elif int(text_event.text) <= 0:
                container.ids.show_error_text.text = 'ต้องมากกว่า 0'
            else:
                container.ids.show_error_text.text = 'เพิ่มได้ไม่เกิน 6 คน'
        else:
            container.ids.show_error_text.text = 'ต้องใส่ตัวเลขเท่านั้น'

    def on_focus(self):
        content = Num_customer()
        dialog = MDDialog(title="Add number of customer.", radius=[20, 7, 20, 7],
                          type='custom', content_cls=content)
        content.ids.cancel_btn.bind(on_press=lambda *s: dialog.dismiss())
        content.ids.ok_btn.bind(on_press=partial(
            self.add_cus_onpress, dialog, content, content.ids.num_field))
        dialog.open()


class MainScreen(MDBoxLayout):
    def __init__(self, **kw):
        super(MainScreen, self).__init__(**kw)
        self.md_bg_color = get_color_from_hex("#FFFFFF")


class Container(MDBoxLayout):
    def __init__(self, **kw):
        super(Container, self).__init__(**kw)
        # self.ids.text_num_table.bind(text=)
        self.container_manager = self.ids.container_manager
        self.add_layout()

    def on_table_num_error(self, text: str):
        content = MDBoxLayout(orientation='vertical', size_hint_y=None)
        content.add_widget(Label(text=text,
                           font_name=self.my_font_name, markup=True, color=self.black, font_size=20))
        dialog = MDDialog(title="User error !!!",
                          content_cls=content, radius=[20, 7, 20, 7],
                          type='custom')
        dialog.open()

    def add_layout(self):
        q_table_screen = QueueTableScreen
        menu_screen = MenuScreen
        self.ids[menu_screen.id] = menu_screen(self)
        self.ids[q_table_screen.id] = q_table_screen(self)
        self.container_manager.add_widget(self.ids[q_table_screen.id])
        self.container_manager.add_widget(self.ids[menu_screen.id])

    def next_sc(self):
        queuetable = self.ids.queuetable
        text_num_table = self.ids.text_num_table
        if text_num_table.text.isnumeric() and int(text_num_table.text) > 21:
            self.on_table_num_error("ใส่ได้ไม่เกิน 20 โต๊ะ")
        elif text_num_table.text.isnumeric() == False:
            self.on_table_num_error("ใส่ได้เฉพาะตัวเลขที่นั้้น")
        elif text_num_table.text.isnumeric() and int(text_num_table.text) < 21:
            self.container_manager.transition.direction = 'left'
            self.container_manager.transition.duration = 0.2
            self.container_manager.current = 'queuetable'
            for i in range(1, int(text_num_table.text)+1):
                queuetable.ids.table_view.add_widget(
                    TableCard(self, num_table=i))
            text_num_table.text = ''


class QueueTableScreen(MDScreen):
    id = 'queuetable'

    def __init__(self, root, **kw):
        super(QueueTableScreen, self).__init__(**kw)
        self.name = 'queuetable'
        self.root = root
        self.table_view = self.ids.table_view
        self.menu_view = self.root.ids.menu_id.ids.menu_view

    def switch_sc(self):
        self.table_view.clear_widgets()
        self.manager.transition.direction = 'right'
        self.manager.transition.duration = 0.2
        self.manager.current = 'intro'


class MenuScreen(MDScreen):
    id = 'menu_id'

    def __init__(self, root, **kw):
        super(MenuScreen, self).__init__(**kw)
        self.root = root
        self.name = 'menu_screen'
        self.container_manager = self.root.ids.container_manager
        self.menu = {"Espressso":35,
                     "Cappuccino":45,
                     "Latte":50,
                     "Mocha":50,
                     "Tea":40,
                     "Green Tea(Milk)":40,
                     "Tea(milk)":40,
                     "Lemon tea":45,
                     "Black Tea":35,
                     "Dark Chocolate":55,
                     "Fresh milk":35,
                     "Chocotate":40}
        for name,value in self.menu.items():
            self.ids.menu_view.add_widget(MenuCard(menu_name=name, value=value))
        self.check_box_id = [
            i.ids.check_box for i in self.ids.menu_view.children]

    def switch_sc(self):
        for i in self.check_box_id:
            i.active = False
        self.container_manager.transition.direction = 'right'
        self.container_manager.transition.duration = 0.2
        self.container_manager.current = 'queuetable'


class CafeHeap(MDApp):
    def build(self):
        mc = MainScreen(padding=[20, 20])
        mc.add_widget(Container(padding=[2, 2]))
        return mc


if __name__ == '__main__':
    os.system('cls')
    CafeHeap().run()
