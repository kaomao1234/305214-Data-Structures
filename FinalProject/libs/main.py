import kivy
from kivy import Config
import os
from kivy.core.text import markup
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '640')
Config.set('graphics', 'minimum_width', '360')
Config.set('graphics', 'minimum_height', '640')
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'multisamples', '0')
from kivymd.uix.button import MDRoundFlatButton, MDFlatButton
from kivy.uix.label import Label
from kivymd.uix.dialog import MDDialog
from kivy.properties import StringProperty, NumericProperty
from kivymd.uix.card import MDCard
from kivy.utils import get_color_from_hex
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.behaviors import ButtonBehavior
for i in ['introScreen', 'Queue_table(table)']:
    Builder.load_file(f"{i}.kv")


class TableCard(MDCard,ButtonBehavior):
    num_table = NumericProperty()


class MainScreen(MDBoxLayout):
    def __init__(self, **kw):
        super(MainScreen, self).__init__(**kw)
        self.md_bg_color = get_color_from_hex("#FFFFFF")


class Container(MDBoxLayout):
    def __init__(self, **kw):
        super(Container, self).__init__(**kw)
        # self.ids.text_num_table.bind(text=)
        self.add_layout()

    def on_table_num_error(self):
        content = MDBoxLayout(orientation='vertical', size_hint_y=None)
        content.add_widget(Label(text='ใส่ได้เฉพาะตัวเลขเท่านั้น !!!',
                           font_name=self.my_font_name, markup=True, color=self.black, font_size=20))
        dialog = MDDialog(title="User error !!!",
                               content_cls=content, radius=[20, 7, 20, 7],
                               type='custom')
        dialog.open()

    def add_layout(self):
        q_table_screen = QueueTabelScreen
        self.ids[q_table_screen.id] = q_table_screen(self)
        self.ids.container_manager.add_widget(self.ids[q_table_screen.id])

    def next_sc(self):
        queuetable = self.ids.queuetable
        text_num_table = self.ids.text_num_table
        if text_num_table.text.isnumeric():
            self.ids.container_manager.transition.direction = 'left'
            self.ids.container_manager.transition.duration = 0.2
            self.ids.container_manager.current = 'queuetable'
            for i in range(1, int(self.ids.text_num_table.text)+1):
                queuetable.ids.table_view.add_widget(TableCard(num_table=i))
            text_num_table.text = ''
        else:
            self.on_table_num_error()


class QueueTabelScreen(MDScreen):
    id = 'queuetable'

    def __init__(self, root, **kw):
        super(QueueTabelScreen, self).__init__(**kw)
        self.name = 'queuetable'
        self.root = root


    def switch_sc(self):
        self.ids.table_view.clear_widgets()
        self.manager.transition.direction = 'right'
        self.manager.transition.duration = 0.2
        self.manager.current = 'intro'


class CafeHeap(MDApp):
    def build(self):
        mc = MainScreen(padding=[20, 20])
        mc.add_widget(Container(padding=[2, 2]))
        return mc


if __name__ == '__main__':
    os.system('cls')
    CafeHeap().run()
