from time import strftime
from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from matplotlib import widgets

class MainWidgets(Widget): 
    text = StringProperty()

    def __init__(self, **kwargs):
        super(MainWidgets, self).__init__(**kwargs)
        self.text = ''
        
    def update_time(self, nap):
        self.root.ids.cpu.text = strftime("%H:%M:%S") 
        #self.root.ids.cpu.text = strftime("%H:%M:%S") 

    def on_start(self):
        Clock.schedule_interval(self.update_time, 1)

    def button_clicked(self):
        pass

class MainApp(App):
    def __init__(self, **kwargs):
        super(MainApp, self).__init__(**kwargs)
        self.title = 'WSM'

    def build(self):
        return MainWidgets()

if __name__ == '__main__':
    MainApp().run()
