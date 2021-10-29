from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import StringProperty, NumericProperty,OptionProperty,ObjectProperty
from kivymd.app import MDApp
from kivy.uix.button import Button
class TableCard(MDBoxLayout):
    number_table = NumericProperty()
    press = ObjectProperty()
    def __init__(self, **kw):
        super(TableCard, self).__init__(**kw)
        
    def add(self):
        value = int(self.ids.count_cus.text)
        if value < 6:
            value += 1
            self.ids.count_cus.text = str(value)
            self.ids.table_detail.secondary_theme_text_color ='Custom'
            self.ids.table_detail.secondary_text_color=self.red
            

    def reduce(self):
        value = int(self.ids.count_cus.text)
        if value > 0:
            value -= 1
            self.ids.count_cus.text = str(value)
            if value == 0:
                self.ids.table_detail.secondary_theme_text_color ='Secondary'
            else:
                self.ids.table_detail.tertiary_theme_text_color ='Custom'
                self.ids.table_detail.tertiary_text_color=self.red
        else:
            self.ids.table_detail.secondary_theme_text_color ='Secondary'
            
Builder.load_string("""
#: import get_color_from_hex kivy.utils.get_color_from_hex
<PressCard@TwoLineAvatarIconListItem+ButtonBehavior>
<TableCard@MDBoxLayout>:
    orientation: 'horizontal'
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
        id:table_detail
        text: "Table {}".format(root.number_table)
        on_press:root.press(root)
        secondary_text: "number of seats {}/6".format(count_cus.text)
        divider:'Inset'
        IconLeftWidgetWithoutTouch:
            icon:'food-fork-drink'

    AnchorLayout:
        anchor_y: 'center'
        size_hint_x:None
        width:self.children[0].width
        MDIconButton:
            adaptive_width:True
            icon: "plus" 
            on_press: root.add()
    MDLabel:
        id:count_cus
        size_hint_x:None
        size: self.texture_size
        text:'0'
        valign: "center"
        theme_text_color:'Custom'
        font_style:'Body1'
    AnchorLayout:
        anchor_y: 'center'
        size_hint_x:None
        width:self.children[0].width
        MDIconButton:
            adaptive_width:True
            icon: "minus" 
            on_press:root.reduce()
""")




