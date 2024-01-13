from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen


class MainScreen(Screen):
      pass
class GenderScreen(Screen):
      pass
class AgeScreen(screen):
     pass
class HightScreen(Screen):
     pass
class WeightScreen(Screen):
     pass
class BMIScreen(Screen,FloatLayout):
        
class ScreenManagement(ScreenManager):
    pass

presentation = Builder.load_file("BMICalculator.kv")

class MainApp(App):
    def build(self):
        return presentation

if __name__ == "__main__":
        MainApp().run()