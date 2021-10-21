from kaki.app import App
from kivy.factory import Factory
from kivymd.app import MDApp
class Live(App,MDApp):
    CLASSES ={
        "MainScreen":"main"
        }
    AUTORELOADER_PATHS=[
        (".",{"recursive":True})
    ]
    def build_app(self, first=False):
        print("Auto reloading.")
        return Factory.MainScreen()
Live().run()