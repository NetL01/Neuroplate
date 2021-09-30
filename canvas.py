from kivy.clock import Clock
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import (Color, Ellipse, Rectangle, Line)
from kivy.uix.button import Button
from kivy.core.window import Window
from random import random



KV = """
MDScreen:

    FitImage:
        source: 'cafe.jpg'

    MDRaisedButton:
        text: "CLICK ME"
        pos_hint: {"center_x": .5, "center_y": .5}
"""



class PainterWidget(Widget):
    def on_touch_down(self, touch):
        with self.canvas:
            Color(1., 0, 0, 0.49)
            rad = 10
            Ellipse(pos = (touch.x - rad/2, touch.y - rad/2), size= (rad, rad))
            touch.ud['line'] = Line(points = (touch.x, touch.y), width = 10)

    def on_touch_move(self, touch):
        touch.ud['line'].points += (touch.x, touch.y)

class PaintApp(App):
    def build(self):
        parent = Widget()
        self.painter = PainterWidget()
        parent.add_widget(self.painter)
        Clock.schedule_once(self.set_background, 0)

        parent.add_widget(Button(text="Назад", on_press=self.save_canvas, size=(100, 50)))
        parent.add_widget(Button(text="Очистить", on_press=self.clear_canvas, size=(100, 50), pos = (100, 0)))
        parent.add_widget(Button(text="Отправить", on_press=self.screen_canvas, size=(100, 50), pos=(200, 0)))
        return parent

    def clear_canvas(self, instance):
        self.painter.canvas.clear()

    def save_canvas(self, instance):
        self.painter.size = (Window.size[0], Window.size[1])
        self.painter.export_to_png('image.png')

    def screen_canvas(self, instance):
        Window.screenshot('screem.png')
        print('This message has been sended for: 278 peoples')

    def set_background(self, *args):
        self.root_window.bind(size=self.do_resize)
        with self.root_window.canvas.before:
            self.bg = Rectangle(source='map.png', pos=(0, 0), size=(self.root_window.size))

    def do_resize(self, *args):
        self.bg.size = self.root_window.size

if __name__ == "__main__":
    PaintApp().run()