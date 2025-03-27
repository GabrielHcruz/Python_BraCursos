from kivy.app import App
from kivy.uix.label import Label

class MeuApp(App):
    def build(self):
        return Label(text ='Olá Mundo',
                color= (1,0,0,1),font_size= 30)
    
if __name__ == '__main__':
    MeuApp().run()
    