
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from signup import signupView
from login1 import loginView
from Employee import Test, tabbedscreen
from afterlogin import Afterlogin
from Customer1 import MainScreen
from Customer1 import POPUP
from Customer1 import new_cust
from Customer1 import new_order
from Customer1 import exis_order
from Customer1 import bill1
from Customer1 import Final_bill

sm=ScreenManager()
sm.add_widget(loginView(name='loginView'))
sm.add_widget(signupView(name='signupView'))
sm.add_widget(tabbedscreen(name='TabbedScreen'))
sm.get_screen(name='TabbedScreen').add_widget(Test(id='Test'))
sm.add_widget(Afterlogin(name='Afterlogin'))
sm.add_widget(MainScreen(name='mainscreen'))
sm.add_widget(new_cust(name='Newcust'))
sm.add_widget(new_order(name='Neworder'))
sm.add_widget(exis_order(name='Exisorder'))
sm.add_widget(bill1(name='Bill1'))
sm.add_widget(Final_bill(name='Final_bill'))
class APP(App):
    def build(self):
        return sm
if __name__ == '__main__':
    APP().run()