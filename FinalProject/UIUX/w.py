from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.spinner import MDSpinner
from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.utils import get_color_from_hex

KV = '''
<Content>
    orientation: "vertical"
    size_hint_y: None
    height: "120dp"
    MDSpinner:
        active:True
        # size_hint:
        pos_hint:{'center_x': .5, 'center_y': .5}


MDFloatLayout:
    MDFlatButton:
        text: "ALERT DIALOG"
        pos_hint: {'center_x': .5, 'center_y': .5}
        on_release: app.show_confirmation_dialog()
'''


class Content(BoxLayout):
    pass


class Example(MDApp):
    dialog = None

    def build(self):
        return Builder.load_string(KV)

    def show_confirmation_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                type="custom",
                content_cls=Content()
            )
        self.dialog.open()
Example().run()