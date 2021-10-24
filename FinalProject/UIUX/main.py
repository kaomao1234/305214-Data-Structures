from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.lang import Builder
kv_file = ["IntroScreen",'TableScreen']
for i in kv_file:
    Builder.load_file(f"{i}.kv")
class IntroScreen(MDScreen):
    pass
class TableScreen(MDScreen):
    pass
class MainScreen(ScreenManager):
    def __init__(self,**kw):
        super(MainScreen,self).__init__(**kw)
        self.add_widget(TableScreen())
        
class CafeHeap(MDApp):
    def build(self):
        return MainScreen()

if __name__ == '__main__':
    CafeHeap().run()
    