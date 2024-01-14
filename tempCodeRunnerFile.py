from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.screenmanager import ScreenManager, Screen

class BMICalculator(BoxLayout):
    def __init__(self, **kwargs):
        super(BMICalculator, self).__init__(**kwargs)

        self.orientation = 'vertical'

        self.label = Label(text='Enter weight (kg) and height (cm)')
        self.add_widget(self.label)

        self.dropdown = DropDown()
        self.dropdown.bind(on_select=lambda instance, x: setattr(self, 'dropdown_selection', x))
        self.dropdown.add_widget(Label(text='Ideal', height=40))
        self.dropdown.add_widget(Label(text='Adjusted', height=40))
        self.dropdown.add_widget(Label(text='Muscular', height=40))

        self.dropbtn = Button(text='Method', size_hint=(1, 0.5))
        self.dropbtn.bind(on_release=self.dropdown.open)
        self.add_widget(self.dropbtn)

        self.weight_input = TextInput(hint_text='Weight (kg)', size_hint=(1, 0.5))
        self.add_widget(self.weight_input)

        self.height_input = TextInput(hint_text='Height (cm)', size_hint=(1, 0.5))
        self.add_widget(self.height_input)

        self.calculate_button = Button(text='Calculate BMI', size_hint=(1, 0.5))
        self.calculate_button.bind(on_press=self.calculate_bmi)
        self.add_widget(self.calculate_button)

        self.result_label = Label(text='', size_hint=(1, 0.5))
        self.add_widget(self.result_label)

    def calculate_bmi(self, instance):
        weight = float(self.weight_input.text)
        height = float(self.height_input.text)

        if self.dropdown_selection == 'Ideal':
            bmi = weight / (height / 100) ** 2
        elif self.dropdown_selection == 'Adjusted':
            bmi = weight / (height / 100) ** 2 * 58.2
        elif self.dropdown_selection == 'Muscular':
            bmi = weight / (height / 100) ** 2 * 90
        else:
            bmi = None

        if bmi is not None:
            self.result_label.text = f'Your BMI is: {bmi:.2f}'
        else:
            self.result_label.text = 'Invalid method selected'

class BMICalculatorApp(App):
    def build(self):
        return BMICalculator()

if __name__ == '__main__':
    BMICalculatorApp().run()
