from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, StringProperty
import sqlite3
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.popup import Popup
Builder.load_file('signup_window.kv')

class signupView(Screen,Widget):
    def want1(self):
        self.ids['want_login'].color = .7, .7, 1.0, 1.0
    def leave1(self):
        self.ids['want_login'].color = 1, 1, 1, 1
    status=ObjectProperty(None)
    def validate1(self,username,password,Aphone_no): # signup krega to sara record yahan aega phr db me jaega
        conn = sqlite3.connect('app.db')
        c = conn.cursor()
        c.execute('''SELECT Username from Admin ''')
        admin_usernames = c.fetchall()
        result = []
        for t in admin_usernames:
            for x in t:
                result.append(x)
        flag = False
        for admin_user in result:
            if username == str(admin_user):
                flag =True
        if (type(username) == str and (type(password) == str) and Aphone_no.isdigit() == True):
            if (flag == False):
                conn = sqlite3.connect('app.db')
                c = conn.cursor()
                c.execute('''INSERT INTO Admin(Username, Password, Adm_P_NO) VALUES( ?, ?, ? )''', (username, password, Aphone_no))
                conn.commit()
                conn.close()
                self.ids.password.text = ''
                self.ids.username.text = ''
                self.ids.Aphone_no.text = ''
                self.pop_up('Successfully Inserted')
                self.manager.current='loginView'

            else:
                self.pop_up('Username already exist')
                self.ids.password.text = ''
                self.ids.username.text = ''
                self.ids.Aphone_no.text = ''
        else:
            self.pop_up('kindly enter valid input')
            self.ids.password.text = ''
            self.ids.username.text = ''
            self.ids.Aphone_no.text = ''
            self.manager.current='signupView'
    def pop_up(self,string2):
        content = Button(text='CLick to exit!')
        popup = Popup(title=string2,
                      content=content, auto_dismiss=False, size_hint=(None, None), size=(400, 400))
        content.bind(on_press=popup.dismiss)
        popup.open()