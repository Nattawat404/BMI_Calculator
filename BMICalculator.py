import kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label


  

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
                                return "Underweight"
                           elif 18.5<= float(result)<=22.9:
                                return "Normal"
                           elif 23.0<=float(result)<=24.9:
                                return "Chubby"
                           elif 25<=float(result)<=29.9:
                                 return "Overweight"
                           elif 30<=float(result)<=34.9:
                                 return "Obese"
                           else:
                                 return "Extremely obese"
                    except Exception:
                          return "Eror"
                           
    
if __name__=='__main__':
    BMI().run()

