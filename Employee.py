
from kivy.lang import Builder
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
import sqlite3
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
Builder.load_file('Employee.kv') # it will load .kv file


class tabbedscreen(Screen):
    pass

class Test(TabbedPanel):
    def new(self):
        self.ids['mainscreen'].background_color = .7, .7, 1.0, 1.0
    def new1(self):
        self.ids['mainscreen'].background_color = 0.0, 0.0, 0.0, 0.0
    def insert_emp(self, ID, EmpName, Pno, Salary, Date):
        if (ID.isdigit() == True and EmpName.isdigit() == False and Pno.isdigit() == True and Salary.isdigit()==True and Date.isalpha()==False) :
            conn = sqlite3.connect('app.db')
            c = conn.cursor()
            c.execute('''SELECT Emp_ID FROM Employee''')
            valid_emp = c.fetchall()
            result1 = []
            for t in valid_emp:
                for x in t:
                    result1.append(x)
            flag = False
            for emp in result1:
                if ID == str(emp):
                    flag = True
            if flag == False:
                c.execute('''INSERT INTO Employee(Emp_ID, Emp_name, Emp_P_No,Emp_salary, Emp_DOJ) VALUES( ?, ?, ?, ?, ? )''', (ID, EmpName, Pno, Salary, Date))
                conn.commit()
                conn.close()
                self.ids.ID.text = ''
                self.ids.EmpName.text = ''
                self.ids.Salary.text = ''
                self.ids.Date.text = ''
                self.ids.Pno.text = ''
                self.pop_up('Successfully registered')
            else:
                self.pop_up('Employee Already Exists')
                self.ids.ID.text = ''
                self.ids.EmpName.text = ''
                self.ids.Salary.text = ''
                self.ids.Date.text = ''
                self.ids.Pno.text = ''
        else:
            self.pop_up('kindly read fields carefully and enter valid data')
            self.ids.ID.text = ''
            self.ids.EmpName.text = ''
            self.ids.Salary.text = ''
            self.ids.Date.text = ''
            self.ids.Pno.text = ''

    def del_emp(self,ID_to_remove):
        print(ID_to_remove)
        if (ID_to_remove.isdigit()==True):
            conn = sqlite3.connect('app.db')
            c = conn.cursor()
            c.execute('''SELECT emp_Id FROM Employee''')
            valid_emp = c.fetchall()
            result1 = []
            for t in valid_emp:
                for x in t:
                    result1.append(x)
            print(result1)
            flag = False
            for emp in result1:
                if ID_to_remove ==str(emp):
                    flag = True

            if flag==True:
                com = 'DELETE FROM Employee where emp_Id = ' + ID_to_remove
                print(com)
                c.execute(com)
                conn.commit()
                self.pop_up('Employee of ID=' + ID_to_remove + 'is removed')
                self.ids.ID_to_remove.text = ''
                conn.close()
            else:
                self.pop_up('Employee of ID='+ID_to_remove+' not Exists')
                self.ids.ID_to_remove.text=''
        else:
            self.pop_up('Enter data carefully')
            self.ids.ID_to_remove.text = ''
    def pop_up(self,string2):
        content = Button(text='CLick to exit!')
        popup = Popup(title=string2,
                      content=content, auto_dismiss=False, size_hint=(None, None), size=(400, 400))
        content.bind(on_press=popup.dismiss)
        popup.open()
    def view_emp(self):
        Builder.load_file('scrollview.kv')
        conn = sqlite3.connect('app.db')
        c = conn.cursor()
        c.execute('''SELECT * FROM Employee ''')
        emp_data = c.fetchall()
        sub_data = []
        sub_sub_data = []
        for i in emp_data:
            sub_data.append(i)
            for j in sub_data:
                sub_sub_data.append(list(j))
                sub_data = []
        two_d_list_to_one_d_list = sum(sub_sub_data, [])
        self.layout = GridLayout(cols=6, padding=-1, spacing=-3,
                size_hint=(None, None), width=1000)
        info = ['EMP ID', 'EMP NAME', 'PHONE NUMBER','SALARY', 'DATA OF JOIN','ARREARS']
        for i in info:
            btn = Button(text=str(i), size=(140, 38),size_hint=(None, None),background_color = (.6,.6, .6,.6))
            self.layout.add_widget(btn)
        self.layout.bind(minimum_height=self.layout.setter('height'))
        for i in two_d_list_to_one_d_list:
            btn = Button(text=str(i), size=(140, 38),
                         size_hint=(None, None))
            self.layout.add_widget(btn)

        # create a scroll view, with a size < size of the grid
        self.root1 = ScrollView(size_hint=(None, None), size=(800, 660),
                pos_hint={'center_x': .5, 'center_y': .5}, do_scroll_x=False)
        self.root1.add_widget(self.layout)
        self.ids['tb'].add_widget(self.root1)


