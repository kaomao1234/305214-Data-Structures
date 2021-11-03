from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import StringProperty, NumericProperty, OptionProperty, ObjectProperty
from kivymd.uix.list import TwoLineAvatarIconListItem
from kivy.uix.behaviors import ButtonBehavior
from threading import Thread
from kivymd.uix.label import MDLabel
from kivy.uix.recycleview.views import RecycleDataViewBehavior
Builder.load_string("""
#: import get_color_from_hex kivy.utils.get_color_from_hex
<PressCard@TwoLineAvatarIconListItem+ButtonBehavior>
<TableCard>:
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
        secondary_theme_text_color:root.second_text_color
        secondary_text: "number of seats {}/6".format(count_cus.text)
        divider:'Inset'
        IconLeftWidgetWithoutTouch:
            icon:'food-fork-drink'

    AnchorLayout:
        anchor_y: 'center'
        size_hint_x:None
        width:self.children[0].width
        MDIconButton:
            id:plus_btn
            adaptive_width:True
            icon: "plus" 
            on_press:root.add()
    MDLabel:
        id:count_cus
        size_hint_x:None
        size: self.texture_size
        text:str(root.count_number)        
        valign: "center"
        theme_text_color:'Primary'
        font_style:'H5'
    AnchorLayout:
        anchor_y: 'center'
        size_hint_x:None
        width:self.children[0].width
        MDIconButton:
            id:minus_btn
            adaptive_width:True
            icon: "minus" 
            on_press:root.reduce()
""")


class TableCard(MDBoxLayout, RecycleDataViewBehavior):
    number_table = NumericProperty()
    press = ObjectProperty()
    count_number = NumericProperty()
    owner = ObjectProperty()
    second_text_color = StringProperty('Primary')

    def __init__(self, **kw):
        super(TableCard, self).__init__(**kw)
        self.table_detail = self.ids.table_detail
        self.count_label: MDLabel = self.ids.count_cus

    def refresh_view_attrs(self, rv, index, data):
        self.update()
        return super(TableCard, self).refresh_view_attrs(rv, index, data)

    def update(self):
        if self.owner != None:
            for i in self.owner.data:
                if i['number_table'] == self.number_table:
                    index = self.owner.data.index(i)
                    self.owner.data[index]['count_number'] = self.count_number
                    self.owner.data[index]['second_text_color'] = self.second_text_color
                    break
            

    def add(self, *e):
        if int(self.ids.count_cus.text) < 6:
            self.count_number += 1
            self.second_text_color = 'Error'

    def reduce(self, *e):
        if int(self.ids.count_cus.text) > 0:
            self.count_number -= 1
            if int(self.ids.count_cus.text) == 0:
                self.second_text_color = 'Primary'
            else:
                self.second_text_color = 'Error'