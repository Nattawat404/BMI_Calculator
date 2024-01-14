from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.widget import Widget


class MainScreen(Widget):
        
           

        def press(self,instance):
             pass

# class GenderScreen(Screen):
#       pass
# class AgeScreen(Screen):
#      pass
# class HightScreen(Screen):
#      pass
# class WeightScreen(Screen):
#      pass
# class BMIScreen(Screen):     
class BMICalculator(App):
       def build(self):
       
              return MainScreen()
if __name__ =="__main__":
         BMICalculator().run()