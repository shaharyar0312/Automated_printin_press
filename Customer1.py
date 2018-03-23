from kivy.lang import Builder
import sqlite3
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
Builder.load_file("Customer1.kv")

class MainScreen(Screen):
    def view1(self):
        objp = POPUP()
        objp.view_customer()
    def view2(self):
        objO =POPUP()
        objO.view_orders()

class POPUP(Popup):
    def view_customer(self):
        Builder.load_file('scrollview.kv')
        conn = sqlite3.connect('app.db')
        c = conn.cursor()
        c.execute('''SELECT * FROM Customer ''')
        cus_data = c.fetchall()
        cus_sub_data = []
        sub_sub_data = []
        for i in cus_data:
            cus_sub_data.append(i)
            for j in cus_sub_data:
                sub_sub_data.append(list(j))
                cus_sub_data = []
        two_d_list_to_one_d_list = sum(sub_sub_data, [])

        self.layout = GridLayout(cols=4, padding=-1, spacing=-3,
                                 size_hint=(None, None), width=1000, size_hint_x=100)
        self.layout.bind(minimum_height=self.layout.setter('height'))
        btn_cus_back = Button(text='Click to exit', size=(210, 38), size_hint=(None, None))
        self.layout.add_widget(btn_cus_back)

        jugar_list = [' ', ' ', ' ']
        for i in jugar_list:
            self.layout.add_widget(Button(text=str(i), size=(210, 38), size_hint=(None, None)))
        info = ['CUSTOMER ID', 'CUSTOMER NAME', 'PHONE NUMBER', 'ARREARS']
        for i in info:
            btn_cus_head= Button(text=str(i), size=(210, 38), size_hint=(None, None),)
            self.layout.add_widget(btn_cus_head)


        for i in two_d_list_to_one_d_list:
            btn_vi_cus = Button(text=str(i), size=(210, 38),
                         size_hint=(None, None))
            self.layout.add_widget(btn_vi_cus)
        self.root1 = ScrollView(size_hint=(None, None), size=(800, 660),
                                pos_hint={'center_x': .5, 'center_y': .5}, do_scroll_x=False)
        content1 = self.root1.add_widget(self.layout)
        popup = Popup(title='Customer',pos_hint={'x':0.01, 'y':0.3},
                      content=self.root1, auto_dismiss=False, size_hint=(None, None),size=(200,200))
        btn_cus_back.bind(on_press=popup.dismiss)
        popup.open()

    def view_orders(self):
        Builder.load_file('scrollview.kv')
        conn = sqlite3.connect('app.db')
        c = conn.cursor()
        c.execute('''SELECT * FROM Orders ''')
        or_data = c.fetchall()
        or_sub_data = []
        or_sub_sub_data = []
        for i in or_data:
            or_sub_data.append(i)
            for j in or_sub_data:
                or_sub_sub_data.append(list(j))
                or_sub_data = []
        two_d_list_to_one_d_list1 = sum(or_sub_sub_data, [])

        self.layout = GridLayout(cols=11, padding=-1, spacing=-3,
                                 size_hint=(None, None), width=1300, size_hint_x=129)
        self.layout.bind(minimum_height=self.layout.setter('height'))
        btn_or_back = Button(text='Click to exit', size=(129, 38), size_hint=(None, None))
        self.layout.add_widget(btn_or_back)
        jugar_list = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        for i in jugar_list:
            self.layout.add_widget(Button(text=str(i), size=(129, 38), size_hint=(None, None)))
        info = ['ORDER ID', 'ORDER NAME', 'ORDER DATE', 'DATE OF COMPLETION', 'DATE OF PAYMENT', 'MATERIAL',
                'FRONT COLOR', 'BACK COLOR', 'CUSTOMER ID', 'QUANTITY', 'PRICE']
        for i in info:
            btn_or_head = Button(text=str(i), size=(129, 38), size_hint=(None, None),
                         font_size=11)
            self.layout.add_widget(btn_or_head)

        for i in two_d_list_to_one_d_list1:
            btn_vi_or = Button(text=str(i), size=(129, 38), font_size=12,
                         size_hint=(None, None))
            self.layout.add_widget(btn_vi_or)

        self.root1 = ScrollView(size_hint=(None, None), size=(1365, 710),
                                pos_hint={'center_x': .5, 'center_y': .5}, do_scroll_x=False)
        self.root1.add_widget(self.layout)

        popup = Popup(title='Customer',pos_hint={'x':0.001, 'y':0.2},
                      content=self.root1, auto_dismiss=False, size_hint=(None, None),size=(400,400))
        btn_or_back.bind(on_press=popup.dismiss)
        popup.open()

class new_cust(Screen):
    def new_cus_to_order(self, custid, custname, p_no):
        if (custid.isdigit() == True and custname.isdigit() == False and p_no.isdigit() == True):

            conn = sqlite3.connect('app.db')
            c = conn.cursor()
            c.execute('''SELECT Cust_ID FROM Customer''')
            valid_cust = c.fetchall()
            result_in_cus = []
            for t in valid_cust:
                for x in t:
                    result_in_cus.append(x)
            flag = False
            for cust_id_loop in result_in_cus:
                if custid == str(cust_id_loop):
                    flag = True
            if flag == False:
                c.execute('''INSERT INTO Customer(Cust_ID, Cust_name, Cust_P_No) VALUES(?, ?, ?)''',
                          (custid, custname, p_no))
                conn.commit()
                que = 'SELECT * FROM Customer WHERE Cust_ID =' + str(custid)
                c.execute(que)
                Cus_id1 = c.fetchall()
                self.pop_up(str(Cus_id1[0][1]) + ', you are successfully registered')
                self.ids.custid.text = ''
                self.ids.custname.text = ''
                self.ids.p_no.text = ''

            else:
                self.pop_up('Customer Already Exists')
                self.ids.custid.text = ''
                self.ids.custname.text = ''
                self.ids.p_no.text = ''
        else:
            self.pop_up('kindly read fields carefully and enter valid data')
            self.ids.custid.text = ''
            self.ids.custname.text = ''
            self.ids.p_no.text = ''

    def pop_up(self, string2):
        content_ins_cus = Button(text='CLick to exit!')
        popup = Popup(title=string2,
                      content=content_ins_cus, auto_dismiss=False, size_hint=(None, None), size=(400, 400))
        content_ins_cus.bind(on_press=popup.dismiss)
        popup.open()




class new_order(Screen):
    def ins_order(self, orid, orname, ordate, ordatecomplete, ordatepay, ormaterial, fcolor, bcolor, ordqty, ordprice,or_cus_id):
        newvar = self.ids
        conn = sqlite3.connect('app.db')
        c = conn.cursor()
        if (orid.isdigit() == True and orname.isdigit() == False and ormaterial.isdigit() == False and fcolor.isdigit() == True and bcolor.isdigit() == True and ordprice.isdigit() == True and ordqty.isdigit() == True and or_cus_id.isdigit()== True):
            c.execute('''SELECT Order_ID FROM Orders''')
            valid_ord = c.fetchall()
            result_new_or = []
            for t in valid_ord:
                for x in t:
                    result_new_or.append(x)
            flag = False
            for ord_id_loop in result_new_or:
                if orid == str(ord_id_loop):
                    flag = True
            if flag == False:
                or_cusID = 'SELECT Cust_ID FROM Customer'
                c.execute(or_cusID)
                valid_cusID = c.fetchall()
                result_new_or_exis_cus = []
                for t in valid_cusID:
                    for x in t:
                        result_new_or_exis_cus.append(x)
                flag_v_cid = False
                for cus_id_loop in result_new_or_exis_cus:
                    if or_cus_id == str(cus_id_loop):
                        flag_v_cid = True
                if flag_v_cid == True:

                    c.execute('''INSERT INTO Orders(Order_ID, Order_name, Order_date, date_of_completion, Expected_date_of_payment, Material, F_Color_qty, B_Color_qty, Cust_ID, Quantity, Price_Per_kg) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                        (orid, orname, ordate, ordatecomplete, ordatepay, ormaterial, fcolor, bcolor, or_cus_id, ordqty,
                         ordprice))
                    conn.commit()
                    newvar.orid.text = ''
                    newvar.orname.text = ''
                    newvar.ordate.text = ''
                    newvar.ordatecomplete.text = ''
                    newvar.ordatepay.text = ''
                    newvar.ormaterial.text = ''
                    newvar.fcolor.text = ''
                    newvar.bcolor.text = ''
                    newvar.ordqty.text = ''
                    newvar.ordprice.text = ''
                    newvar.or_cus_id.text = ''
                    self.pop_up('Successfully Inserted')
                    checker = 0
                else:
                    self.pop_up('Customer Does not exist')

                    newvar.or_cus_id.text = ''
            else:
                self.pop_up('Order Already Exists')
                newvar.orid.text = ''


        else:
            self.pop_up('kindly read fields carefully and enter valid data')
            newvar.orid.text = ''
            newvar.orname.text = ''
            newvar.ordate.text = ''
            newvar.ordatecomplete.text = ''
            newvar.ordatepay.text = ''
            newvar.ormaterial.text = ''
            newvar.fcolor.text = ''
            newvar.bcolor.text = ''
            newvar.ordqty.text = ''
            newvar.ordprice.text = ''

    def pop_up(self, string2):
        content_new_or = Button(text='CLick to exit!')
        popup = Popup(title=string2,
                      content=content_new_or, auto_dismiss=False, size_hint=(None, None), size=(400, 400))
        content_new_or.bind(on_press=popup.dismiss)
        popup.open()

class exis_order(Screen):
    def order_id_search(self, orid_for_search,today_date):
        conn = sqlite3.connect('app.db')
        c = conn.cursor()
        c.execute('''SELECT Order_ID FROM Orders''')
        valid_ord = c.fetchall()
        result_exis_or = []
        for t in valid_ord:
            for x in t:
                result_exis_or.append(x)
        flag = False
        for ex_ord_id_loop in result_exis_or:
            if orid_for_search == str(ex_ord_id_loop):
                flag = True
        if flag == True:
            var1 = 'SELECT * FROM Orders WHERE Order_ID ='+ str(orid_for_search)
            c.execute(var1)
            exis_rec = c.fetchall()
            result3 = []
            for t in exis_rec:
                for x in t:
                    result3.append(x)
            global bill_stuffs_or
            bill_stuffs_or = result3[0]
            conn = sqlite3.connect('app.db')
            c = conn.cursor()
            c.execute('''SELECT Order_ID from Bill''')
            or_bilIDS = c.fetchall()
            result_or_billids = []
            for t in or_bilIDS:
                for x in t:
                    result_or_billids.append(x)
            flag_check_ids = False
            for ex_ord_billids_loop in result_or_billids:
                if bill_stuffs_or == ex_ord_billids_loop:
                    flag_check_ids = True
            if flag_check_ids == False:
                Complete_bill = 'INSERT INTO Bill( Date, Order_ID, Cust_ID) VALUES(' + str(today_date) + ',' + str(result3[0]) + ',' + str(result3[8]) + ')'
                c.execute(Complete_bill)
                conn.commit()
                awaein ='CUST ID='+ str(result3[8]) +', Order Name = ' + str(result3[1]) + ', Order Id = ' + str(result3[0])
                self.pop_up(awaein)
                self.ids.orid_for_search.text = ''
                self.ids.today_date.text = ''
                self.parent.current = 'Final_bill'
            else:
                self.pop_up("This Order is Already in Bill's record")
        else:
            self.pop_up('No record Found')
            self.ids.orid_for_search.text = ''

    def pop_up(self, string2):
        content_exis_order = Button(text='CLick to exit!')
        popup = Popup(title=string2,
                      content=content_exis_order, auto_dismiss=False, size_hint=(None, None),size=(400, 400))
        content_exis_order.bind(on_press=popup.dismiss)
        popup.open()

class bill1(Screen):
    pass


class Final_bill(Screen):
    def billvi(self):
        conn = sqlite3.connect('app.db')
        c = conn.cursor()
        global bill_stuffs_or
        total_bill = 'SELECT  Bill_ID, Date,  Cust_name, Order_name, Quantity,Price_Per_kg, Quantity*Price_Per_kg As Amount FROM Customer, Orders, Bill WHERE  Customer.Cust_ID = Bill.Cust_ID AND Orders.Order_ID = Bill.Order_ID AND Bill.Order_ID='+str(bill_stuffs_or)
        c.execute(total_bill)
        admin_data = c.fetchall()
        result_bill = []
        for t in admin_data:
            for x in t:
                result_bill.append(x)

        self.ids.bill.text = str(result_bill[0])
        self.ids.date1.text = str(result_bill[1])
        self.ids.name.text = str(result_bill[2])
        self.ids.order.text = str(result_bill[3])
        self.ids.quantity.text = str(result_bill[4])
        self.ids.price.text = str(result_bill[5])
        self.ids.amount.text = str(result_bill[6])


# class CustomerMain(App):
#     def build(self):
#         global sm
#         sm = ScreenManagement()
#
#         return presentation
#
#
# CustomerMain().run()
