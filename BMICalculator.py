from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

Builder.load_file('BMICalculator.kv')
class MainScreen(Widget):
        name= ObjectProperty(None)

        def press(self):
             pass

class GenderScreen(Screen):
      pass
# class AgeScreen(Screen):
#      pass
# class HightScreen(Screen):
#      pass
# class WeightScreen(Screen):
#      pass
# class BMIScreen(Screen):     
class MyApp(App):
       def build(self):
       
              return MainScreen()
if __name__ =="__main__":
         MyApp().run()