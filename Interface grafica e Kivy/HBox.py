# import random
# from kivy.app import App
# from kivy.uix.button import Button
# from kivy.uix.boxlayout import BoxLayout


# red = [1, 0, 0, 1]
# green = [0, 1, 0, 1]
# blue = [0, 0, 1, 1]
# purple = [1, 0, 1, 1]


# class Hbox(App):
#     def build(self):
#         layd = BoxLayout(padding=10)
#         colors = [red, green, blue, purple]

#     for i in range(5):
#         btn = Button(text=f"Essse é o butão#{i+1}",
#                      background_color=random.choice(colors)
#                      )

#     layd.add_widget(btn)
#     return layd


# if __name__ == '__main__':
#     app = Hbox()
#     app.run()
