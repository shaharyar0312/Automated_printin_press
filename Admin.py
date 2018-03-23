
import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder

# Builder.load_file('ClassOne.kv')
# Builder.load_file('ClassTwo.kv')
#
# class ClassOne(Widget):
#     pass
#
# class ClassTwo(Widget):
#     pass

class MyGrid(GridLayout):

    def printer(self, text):
        print(text)

class ProgramApp(App):
    def build(self):
        return MyGrid()


if __name__=="__main__":
    ProgramApp().run()
