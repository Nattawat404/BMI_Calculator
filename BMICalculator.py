import kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label

class Login(App):

    def build(self):
        Window.size=[400,600]
        return Label(text='')
    
    
    
if __name__=='__main__':
    Login().run()