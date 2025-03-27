from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import *

class AppImagem(App):
    def build(self):
       Img = AsyncImage(source='https://supermariorun.com/assets/img/stage/mario03.png',
                        size_hint= (1,.5))
       pos_hint={'center_x':.5, 'center_y':.5}
       return Img
    
if __name__ == '__main__':
    App = AppImagem()
    App.run()
