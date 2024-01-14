from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.core.window import Window




class MainScreen(GridLayout):
        def __init__(self,**kwargs):
            super(MainScreen, self).__init__(**kwargs)
            self.cols = 1

            self.top_grid=GridLayout()
            self.top_grid.cols=1

            self.top_grid.add_widget(Label(text="Welcome to BMI Calculator"))
            self.top_grid.add_widget(Label(text="Please enter your Name: "))
            self.name = TextInput(multiline=False)
            self.top_grid.add_widget(self.name)
            self.add_widget(self.top_grid)

            self.start=Button(text="Start",
                              font_size=40,
                              size_hint_y=None,
                              height=50
                              )
            self.start.bind(on_press=self.press)
            self.add_widget(self.start)

        def press(self):
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
class MyApp(App):
       def build(sself):
        #       Window.clearcolor=(1,1,1,1 )
              return MainScreen()
if __name__ =="__main__":
         MyApp().run()