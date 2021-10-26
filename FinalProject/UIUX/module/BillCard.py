from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import StringProperty, NumericProperty
from kivymd.app import MDApp
class BillCard(MDBoxLayout):
    number_table = NumericProperty()
    def __init__(self, **kw):
        super(BillCard, self).__init__(**kw)
        
Builder.load_string("""
<BillCard@MDBoxLayout>:
    orientation:'vertical'
    adaptive_height:True
    red:get_color_from_hex("#FF0000")
    black:get_color_from_hex("#000000")
    number_table:''
    canvas:
        Color:
            rgba: get_color_from_hex("#000000")
        Line:
            width: 1
            rectangle: self.x, self.y, self.width,self.height
    TwoLineAvatarIconListItem:
        id:table_detail
        text: "Table {}".format(root.number_table)
        secondary_text: "number of seats 6/6"
        secondary_theme_text_color:'Custom'
        secondary_text_color:root.red
        IconLeftWidgetWithoutTouch:
            icon:'food-fork-drink'
""")