from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import StringProperty, NumericProperty,ObjectProperty, ListProperty, DictProperty
from kivymd.app import MDApp        
Builder.load_string("""
<PressCard@TwoLineAvatarIconListItem+ButtonBehavior>
<BillCard>:
    orientation:'vertical'
    adaptive_height:True
    red:get_color_from_hex("#FF0000")
    black:get_color_from_hex("#000000")
    canvas:
        Color:
            rgba: get_color_from_hex("#000000")
        Line:
            width: 1
            rectangle: self.x, self.y, self.width,self.height
    PressCard:
        on_press:root.press(root)
        id:table_detail
        text: "Table {}".format(root.number_table)
        secondary_text: "number of seats {}/6".format(root.number_cus)
        secondary_theme_text_color:'Custom'
        secondary_text_color:root.red
        IconLeftWidgetWithoutTouch:
            icon:'food-fork-drink'
""")
class BillCard(MDBoxLayout):
    number_table = NumericProperty()
    press = ObjectProperty(lambda x :x )
    number_cus = NumericProperty()
    bill_info =  DictProperty(None)
    def __init__(self, **kw):
        super(BillCard, self).__init__(**kw)