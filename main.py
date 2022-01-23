from typing import Text
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
import kivy.properties as kyprops

from kivy.metrics import dp


class WidgetsExample(GridLayout):
    my_text = kyprops.StringProperty("1")
    text_input_str = kyprops.StringProperty("foo")
    #slider_txt = kyprops.StringProperty("1")
    count = 1
    count_enabled = kyprops.BooleanProperty(False)

    def on_button_click(self):
        if self.count_enabled:
            self.count += 1
            print("Button clicked")
            self.my_text = str(self.count)

    def on_toggle_button_state(self, widget):
        print("toggle state " + widget.state)
        if widget.state == "normal":
            widget.text = "OFF"
            self.count_enabled = False
        else:
            widget.text = "ON"
            self.count_enabled = True

    def on_switch_active(self, widget):
        print("switch state " + str(widget.active))

    def on_text_validate(self, widget):
        self.text_input_str = widget.text

    # def on_slider_value(self, widget):
    #     print("Slider " + str(int(widget.value)))
    #     #self.slider_txt = str(int(widget.value))





# class GridLayoutExample(GridLayout):
#     pass

class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #self.orientation = "lr-bt"
        for i in range(0, 100):
            #size = dp(100) + i*10
            size = dp(100)
            b = Button(text=str(i+1),size_hint=(None, None), size=(size, size))
            self.add_widget(b)

class AnchorLayoutExample(AnchorLayout):
    pass

class BoxLayoutExample(BoxLayout):
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     self.orientation = "vertical"
    #     b1 = Button(text="A")
    #     b2 = Button(text="B")
    #     b3 = Button(text="C")
    #     self.add_widget(b1)
    #     self.add_widget(b2)
    #     self.add_widget(b3)
    pass

class MainWidget(Widget):
    pass

class TheLabApp(App):
    pass

class CanvasExample1(Widget):
    pass

app = TheLabApp()

app.run()
