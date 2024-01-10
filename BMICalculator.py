import kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager,Screen

class MainScreen(Screen):
      pass
class BMIScreen(Screen,FloatLayout):
    def __init__(self,**kwargs):
        super(BMIScreen,self).__init__(**kwargs)
    def calculate_BMI(self,weight,hight):
        if  weight != "" and hight !="":
                try:
                        return str(round((float(weight)/(float(hight)**2)),2))
                except Exception:
                      return "Eror"
        else:
            return ""
                
class BMI(App):

    def build(self):
        Window.size=[400,600]
        return Label(text='welcome to CALCULATOR')
    
    def BMI_result(self,result):
        if result == "":
                    return ""
        else:
                    try:
                           if float(result)<=18.5:
                                return " underweight"
                           elif float(result)<=24.9:
                                return "Normal"
                           elif float(result)<=29.9:
                                return "Overweight"
                           elif float(result)<=34.9:
                                 return "severely overweight"
                           elif float(result)<=39.9:
                                 return "Obese"
                           else:
                                 return "Severely obese"
                    except Exception:
                          return "Eror"
                    
class SceenManagment(ScreenManager):
      pass
presentation=Builder.load_file("BMICalculator.kv")               

class MainApp(App):
      def build(self):
          return presentation
if __name__=='__main__':
    MainApp().run()

