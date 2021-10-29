from kivymd.uix.snackbar.snackbar import BaseSnackbar
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.properties import StringProperty, NumericProperty,ListProperty
from kivymd.uix.button import MDFillRoundFlatButton
from kivy.lang import Builder
Builder.load_string("""
#: import Window kivy.core.window.Window
<MessageBar@BaseSnackbar>:
    snackbar_x:"10dp"
    snackbar_y:"10dp"
    sukumvit_font:'font/SukhumvitSet-Medium'
    radius:[15,15,15,15]
    elevation:30
    size_hint_x:(Window.width - (self.snackbar_x * 2)) / Window.width
    canvas:
        Color: 
            rgb:root.border_color
        Line:
            width:root.border_weight
            rounded_rectangle:(self.x,self.y,self.width,self.height,self.radius[0],self.radius[1],self.radius[2],self.radius[3])
            
    MDIconButton:
        icon: root.icon
        opposite_colors: True
        pos_hint: {'center_y': .5}
    MDLabel:
        id: text_bar
        size_hint_y: None
        halign:'left'
        valign:'top'
        height: self.texture_size[1]
        text: root.text
        font_size: root.font_size
        font_name: root.sukumvit_font
        theme_text_color: 'Custom'
        text_color: root.text_color
        pos_hint: {'center_y': .5}
""")
class MessageBar(BaseSnackbar):
    text = StringProperty(None)
    text_color = ListProperty(None)
    icon = StringProperty(None)
    font_size = NumericProperty("15sp")
    border_color = ListProperty(None)
    border_weight = NumericProperty(1)
    def __init__(self, **kwargs):
        super(MessageBar,self).__init__(**kwargs)