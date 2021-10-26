import kivy
from kivy import Config
import time
from kivy.clock import Clock
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.properties import StringProperty, NumericProperty
from module.TableCard import TableCard
from module.MenuCard import MenuCard
from module.BillCard import BillCard
from kivymd.uix.spinner import MDSpinner
from threading import Thread
from functools import partial
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.animation import Animation
kv_file = ["IntroScreen", 'TableScreen', 'MenuScreen', 'CheckBillScreen']
for i in kv_file:
    Builder.load_file(f"kv_file/{i}.kv")


class IntroScreen(MDScreen):
    def __init__(self, root, **kw):
        super(IntroScreen, self).__init__(**kw)
        self.main_manager = root
        self.root = self.main_manager.root
    def on_press(self):
        field_tables = self.ids.field_tables.text
        if field_tables.isnumeric() and int(field_tables) <= 20:
            self.root.active_true_refresh()
            Clock.schedule_once(
                partial(self.add_tablecard, field_tables), 0.05*int(field_tables))

    def next_to_tablescreen(self, *e):
        self.manager.transition.direction = 'left'
        self.manager.transition.duration = 0.2
        self.manager.current = 'table_screen'
        self.ids.field_tables.text = ''
        self.main_manager.disabled = False
        self.root.active_false_refresh()
        
    def add_tablecard(self, field_tables, *e):
        self.main_manager.disabled = True
        for i in range(1, int(field_tables)+1):
            self.main_manager.all_frame['TableScreen'].ids.tablelst.add_widget(
                TableCard(number_table=i, press=self.card_onPress))
        Clock.schedule_once(self.next_to_tablescreen, 0.05*int(field_tables))
        
    def add_menuscreen(self,table_num,*e):
        self.main_manager.disabled = True
        self.main_manager.add_widget(MenuScreen(table_no=int(table_num)))
        
    def card_onPress(self, instance):
        table_num = instance.number_table
        menu_instance= self.main_manager.all_frame['MenuScreen']
        menu_instance.table_no = table_num
        self.manager.transition.direction = 'left'
        self.manager.transition.duration = 0.2
        self.manager.current = 'menu_screen'
        
        


class TableScreen(MDScreen):
    def __init__(self, root, **kw):
        super(TableScreen, self).__init__(**kw)

    def back_onPress(self):
        self.ids.tablelst.clear_widgets()
        self.manager.transition.direction = 'right'
        self.manager.transition.duration = 0.2
        self.manager.current = 'intro_screen'


class MenuScreen(MDScreen):
    table_no = NumericProperty()

    def __init__(self,root, **kw):
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

    def reset_menu_number(self):
        for i in self.ids.menulst.children:
            i.ids.count_menu.text = '0'
            i.reduce()
class CheckBillScreen(MDScreen):
    table_no = NumericProperty()

    def __init__(self, **kw):
        super(CheckBillScreen, self).__init__(**kw)


class MainManager(ScreenManager):
    def __init__(self,root, **kw):
        super(MainManager, self).__init__(**kw)
        self.all_frame = {}
        self.root = root
        for i in [IntroScreen, TableScreen,MenuScreen]:
            self.all_frame[i.__name__] = i(self)
            self.add_widget(self.all_frame[i.__name__])

class Home(MDFloatLayout):
    def __init__(self,**kw):
        super(Home, self).__init__(**kw)
        self.refresh_layout = MDSpinner(size_hint=(0.1,0.1),pos_hint={'center_x':0.5,'center_y':-0.1})
        self.add_widget(MainManager(self))
        self.add_widget(self.refresh_layout)
    
    def active_true_refresh(self):
        anim = Animation(pos_hint={'center_x':0.5,'center_y':0.5},duration = 0.2)
        anim.start(self.refresh_layout)
        self.refresh_layout.active = True
        
    def active_false_refresh(self):
        anim = Animation(pos_hint={'center_x':0.5,'center_y':-0.1},duration=0.2)
        anim.start(self.refresh_layout)
        self.refresh_layout.active = False
class CafeHeap(MDApp):
    def build(self):
        return Home()


if __name__ == '__main__':
    CafeHeap().run()
