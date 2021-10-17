import kivy
from kivy import Config
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '640')
Config.set('graphics', 'minimum_width', '360')
Config.set('graphics', 'minimum_height', '640')
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'multisamples', '0')
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivy.utils import get_color_from_hex
for i in ['introScreen','Queue_table(table)']:
    Builder.load_file(f"{i}.kv")
class MainScreen(MDBoxLayout):
    def __init__(self,**kw):
        super(MainScreen,self).__init__(**kw)
        self.md_bg_color = get_color_from_hex("#FFFFFF")
class Container(MDBoxLayout):
    def __init__(self,**kw):
        super(Container,self).__init__(**kw)
        self.add_layout()
    def add_layout(self):
        q_table_screen = QueueTabelScreen
        self.ids[q_table_screen.id] = q_table_screen(self)
        self.ids.container_manager.add_widget(self.ids[q_table_screen.id])
    def next_sc(self):
        self.ids.container_manager.transition.direction='left'
        self.ids.container_manager.transition.duration =0.2
        self.ids.container_manager.current = 'queuetable'
class QueueTabelScreen(MDScreen):
    id='queuetable'
    def __init__(self,root,**kw):
        super(QueueTabelScreen,self).__init__(**kw)
        self.name = 'queuetable'
        self.root = root
class CafeHeap(MDApp):
    def build(self):
        mc = MainScreen(padding=[20,20])
        mc.add_widget(Container(padding=[2,2]))
        return mc

if __name__ == '__main__':
    CafeHeap().run()