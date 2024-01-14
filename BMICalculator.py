import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config

Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '600')

class Calculator(GridLayout):
    def calculate_bmi(self, weight, height):
        try:
            bmi = float(weight) / ((float(height) / 100) ** 2)
            return bmi
        except Exception as e:
            print(e)
            return None

class BMICalculatorApp(App):
    def build(self):
        return Calculator()
        print(bmi)

if __name__ == '__main__':
    BMICalculatorApp().run()
