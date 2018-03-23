from kivy.lang import Builder
import sqlite3
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from login1 import loginMain
from signup import SingupMain
from customer import CustomerMain
from Employee import EmployeeMain

Builder.load_string('''
<GreenButton@Button>:
    background_color: 1, 1, 1, 1
    size_hint_y: None
    height: self.parent.height * 0.120
<CustomLabel@Label>:
    text_size: self.size
    valign: "middle"
    padding_x: 5

<Home>:
    orientation: 'vertical'
    row_default_height: '30dp'

    BoxLayout:#window box

        # halign:'center'
        orientation: 'vertical'
        spacing:20,20
        padding: 180,10,10,150

        BoxLayout: #ADD1
            orientation:'vertical'
            size_hint:.6,1.1
            CustomLabel:
                padding_x:70
                text:'TUITION PROVIDER '
                # pos_hint: .5
                size_hint:2.99,.5
                font_size:28
                color:(0,1,1,1)

            BoxLayout:#home view for tutor
                orientation:'vertical'
                padding:100,10,5,10
                spacing:10,10
                GreenButton:
                    id: Tutorr
                    halign: 'right'
                    size_hint: .7, 2.9
                    text: 'Are You a Tutor?'

                    on_press:root.manager.current='SingupMain'
                Label:

                GreenButton: 
                    halign: 'left'
                    readonly: True
                    size_hint: .7, 2.9         
                    text:'Are You a Parent?'  
                    on_press:root.manager.current='loginMain'

''')


class Home(Screen,BoxLayout):
    def build(self):
        pass

sm = ScreenManager()
sm.add_widget(Home(name='Home'))
sm.add_widget(loginMain(name='Parent_Registration'))
sm.add_widget(SingupMain (name='Parent_Post_Liked_by_Tutors'))
#sm.add_widget(CustomerMain(name='Parent_Post'))
sm.add_widget(EmployeeMain(name='Post_Adds'))
class Tuition_Provider(App):
    def build(self):
        return sm
Tuition_Provider().run()

