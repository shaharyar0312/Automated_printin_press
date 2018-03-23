
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, StringProperty
import sqlite3
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
Builder.load_file('login_window.kv')

class loginView(Screen,BoxLayout):
    status=ObjectProperty(None)

    def want(self):
        self.ids['want_register'].color = .7, .7, 1.0, 1.0
    def leave(self):
        self.ids['want_register'].color = 1, 1, 1, 1
    def validate(self,username1,password1):
        aa = self.ids
        if type(username1) == str and type(password1) == str and aa.password1.text != '' and aa.username1.text != '':
            conn = sqlite3.connect('app.db')
            c = conn.cursor()
            c.execute('''SELECT * FROM Admin WHERE ( Username=? AND Password=? )''', (username1, password1))
            admin_data = []
            admin_data = c.fetchall()
            if  admin_data == []:
                self.ids.password1.text = ''
                self.ids.username1.text = ''
                self.pop_up('No Record Found')
            else:
                self.ids.password1.text = ''
                self.ids.username1.text = ''
                self.pop_up('Successfully Login')
                self.manager.current='Afterlogin'

        else:
            self.pop_up('kindly enter valid input')

    def pop_up(self,string2):
        content = Button(text='CLick to exit!')
        popup = Popup(title=string2,
                      content=content, auto_dismiss=False, size_hint=(None, None), size=(400, 400))
        content.bind(on_press=popup.dismiss)
        popup.open()



