from kivy.app import App
from kivy.lang import Builder

Gui = Builder.load_file("tela.kv")

class MeuApp(App):
    def build(self):
        return Gui  
    

MeuApp().run()