from kivy.config import KIVY_CONFIG_VERSION


from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.snackbar.snackbar import BaseSnackbar
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import StringProperty, NumericProperty,ListProperty
Builder.load_string("""
<LoadingBar@BaseSnackbar>:
    MDBoxLayout:
        pos_hint: {"center_y": 0.5}
        orientation: 'vertical'
        MDLabel:
            text: 'Loading...'
        MDProgressBar:
            color:root.progess_color
            id: progress
            type: "indeterminate"

<Container@MDBoxLayout>:
    orientation: 'vertical'
    MDFillRoundFlatButton:
        text: 'click'
        on_press: root.click()
""")
class LoadingBar(BaseSnackbar):
    progess_color=ListProperty(None)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def open(self,*e):
        super().open()
        self.ids.progress.start()
    def dismiss(self, *args):
        super().dismiss(*args)
        self.ids.progress.stop()