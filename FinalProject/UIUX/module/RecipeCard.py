from kivy.lang import Builder
from kivy.properties import StringProperty,NumericProperty
from kivymd.uix.boxlayout import MDBoxLayout
# from kivymd.uix.screen import MDScreen
class RecipeCard(MDBoxLayout):
    menu_name = StringProperty()
    count= NumericProperty()
    price = NumericProperty()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
Builder.load_string("""
<RecipeCard@MDBoxLayout>:
    orientation: 'vertical'
    size_hint_y: None
    height: dp(30)
    MDBoxLayout:
        orientation: 'horizontal'
        MDLabel:
            text: root.menu_name.replace(" ",'')
            font_style:'Body1'
            halign: "center"
        MDLabel:
            text: "{}x{}".format(root.count,root.price)
            font_style:'Body1'
            halign: "center"
        MDLabel:
            text: '{} Bath'.format(root.count*root.price)
            font_style:'Body1'
            halign: "center"
    MDSeparator:
        height: "1dp"
        md_bg_color:(0,0,0,1)
""")