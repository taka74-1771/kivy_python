from time import strftime
from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.label import Label

class MainApp(App):
    def update_time(self, nap):
        self.root.ids.time.text = strftime("%H:%M:%S") 

    def on_start(self):
        Clock.schedule_interval(self.update_time, 1)
        
if __name__ == '__main__':
    MainApp().run()
