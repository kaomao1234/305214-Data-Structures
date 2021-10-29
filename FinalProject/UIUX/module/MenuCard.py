from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import StringProperty, NumericProperty            
Builder.load_string("""
<MenuCard@MDBoxLayout>:
    orientation: 'horizontal'
    adaptive_height:True
    red:(1.0, 0.0, 0.0, 1.0)
    black:get_color_from_hex("#000000")
    orange:get_color_from_hex("#FF8B3D")
    canvas:
        Color:
            rgba: get_color_from_hex("#000000")
        Line:
            width: 1
            rectangle: self.x, self.y, self.width,self.height 
    ThreeLineListItem:
        id:menu_detail
        text: "{}".format(root.menu_name)
        secondary_text: "Price {}".format(root.price)
        tertiary_text: "{}/15".format(count_menu.text)
        secondary_theme_text_color:'Custom'
        secondary_text_color:root.orange
        secondary_font_style:'Subtitle1'
        _no_ripple_effect: True
    AnchorLayout:
        anchor_y: 'center'
        size_hint_x:None
        width:self.children[0].width
        MDIconButton:
            adaptive_width:True
            icon: "plus" 
            on_press: root.add()
    MDLabel:
        id:count_menu
        size_hint_x:None
        width:30
        text:'0'
        valign: "center"
        halign: "center"
        theme_text_color:'Custom'
        font_style:'H5'
    AnchorLayout:
        anchor_y: 'center'
        size_hint_x:None
        width:self.children[0].width
        MDIconButton:
            adaptive_width:True
            icon: "minus" 
            on_press:root.reduce()
""")
class MenuCard(MDBoxLayout):
    menu_name = StringProperty()
    price = NumericProperty()
    def __init__(self,root,**kw):
        super(MenuCard, self).__init__(**kw)
        self.total = root.ids.total
        self.menu = root.menu

    def add(self):
        value = int(self.ids.count_menu.text)
        if value < 15:
            value += 1
            self.ids.count_menu.text = str(value)
            self.ids.menu_detail.tertiary_theme_text_color ='Custom'
            self.ids.menu_detail.tertiary_text_color=self.red
            self.total.text = str(int(self.total.text)+self.menu[self.menu_name])

    def reduce(self):
        value = int(self.ids.count_menu.text)
        if value > 0:
            value -= 1
            self.ids.count_menu.text = str(value)
            self.total.text = str(int(self.total.text)-self.menu[self.menu_name])
            if value == 0:
                self.ids.menu_detail.tertiary_theme_text_color = 'Secondary'
                
            else:
                self.ids.menu_detail.tertiary_theme_text_color ='Custom'
                self.ids.menu_detail.tertiary_text_color=self.red
        else:
            self.ids.menu_detail.tertiary_theme_text_color = 'Secondary'