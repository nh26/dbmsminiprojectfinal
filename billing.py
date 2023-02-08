from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
import time
import os
import tempfile
class billing:
    def __init__(self, root):
        self.root =root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")
        self.icon_title=PhotoImage(file="images/logo1.gif")
        title=Label(self.root, text="Inventory Management System",image=self.icon_title,compound=LEFT, font=("times new roman",40,"bold"),bg="black",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)
        btnlogout=Button(self.root,text="Logout",command=self.logout,font=("times new roman",15,"bold"),bg="yellow",cursor="hand2").place(x=1100,y=10,height=50,width=150)

#        self.labelclock=Label(self.root, text="Welcome to Inventory Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS", font=("times new roman",15,"bold"),bg="#4d636d",fg="white")
#        self.labelclock.place(x=0,y=70,relwidth=1,height=30)

        self.cart_list=[]
        self.chk_print=0
        self.variable_search=StringVar()
        self.variable_cname=StringVar()
        self.variable_contact=StringVar()
        self.variable_pid=StringVar()
        self.variable_pname=StringVar()
        self.variable_price=StringVar()
        self.variable_qty=StringVar()
        self.variable_stock=StringVar()
        self.variable_cal_inp=StringVar()
        
        
        
        
        

        Product_Frame1=Frame(self.root,bd=4,relief=RIDGE,bg='white')
        Product_Frame1.place(x=6,y=110,width=410,height=550)
        ptitle=Label(Product_Frame1,text='All products',font=("goudy old style",20,'bold'),bg='#262626',fg='white').pack(side=TOP,fill=X)

        Product_Frame2=Frame(Product_Frame1,bd=2,relief=RIDGE,bg='white')
        Product_Frame2.place(x=2,y=42,width=398,height=90)

        lbl_search=Label(Product_Frame2,text="Search product by name",font=("times new roman",15,"bold"),bg="white",fg="green").place(x=2,y=5)

        lbl_search=Label(Product_Frame2,text="Product Name",font=("times new roman",15,"bold"),bg="white").place(x=5,y=45)
        txt_search=Entry(Product_Frame2,textvariable=self.variable_search,font=("times new roman",15,"bold"),bg="lightyellow").place(x=129,y=47,width=150,height=22)

        btn_search=Button(Product_Frame2,text="Search",command=self.search,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=285,y=45,width=100,height=25)
        btn_show_all=Button(Product_Frame2,text="Show all",command=self.show,font=("goudy old style",15),bg="#083531",fg="white",cursor="hand2").place(x=285,y=10,width=100,height=25)


        Product_Frame3=Frame(Product_Frame1,bd=3,relief=RIDGE)
        Product_Frame3.place(x=2,y=140,width=398,height=385)

        Scrolly=Scrollbar(Product_Frame3,orient=VERTICAL)
        Scrollx=Scrollbar(Product_Frame3,orient=HORIZONTAL)

        self.product_table=ttk.Treeview(Product_Frame3,columns=("pid","name","price","qty","status"),yscrollcommand=Scrolly.set,xscrollcommand=Scrolly)
        Scrollx.pack(side=BOTTOM,fill=X)
        Scrolly.pack(side=RIGHT,fill=Y)

        self.product_table.heading("pid",text="PID")
        self.product_table.heading("name",text="NAME")
        self.product_table.heading("price",text="PRICE")
        self.product_table.heading("qty",text="QTY")
        self.product_table.heading("status",text="STATUS")
        
        self.product_table["show"]="headings"
        
        self.product_table.column("pid",width=40)
        self.product_table.column("name",width=100)
        self.product_table.column("price",width=100)
        self.product_table.column("qty",width=40)
        self.product_table.column("status",width=90)
        
        self.product_table.pack(fill=BOTH,expand=1)
        self.product_table.bind("<ButtonRelease-1>",self.get_data)

        #-----------------Customer--------------#

        Customer_Frame=Frame(self.root,bd=4,relief=RIDGE,bg='white')
        Customer_Frame.place(x=420,y=110,width=530,height=70)
        ctitle=Label(Customer_Frame,text='Customer details',font=("goudy old style",15),bg='lightgray').pack(side=TOP,fill=X)

        lbl_name=Label(Customer_Frame,text="Name",font=("times new roman",15),bg="white").place(x=5,y=35)
        txt_name=Entry(Customer_Frame,textvariable=self.variable_cname,font=("times new roman",15),bg="lightyellow").place(x=75,y=35,width=180)

        lbl_contact=Label(Customer_Frame,text="Contact No. ",font=("times new roman",15),bg="white").place(x=270,y=35)
        txt_contact=Entry(Customer_Frame,textvariable=self.variable_contact,font=("times new roman",15),bg="lightyellow").place(x=380,y=35,width=140)


        calculator_cart_Frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        calculator_cart_Frame.place(x=420,y=190,width=530,height=360)
        
        calculator_Frame=Frame(calculator_cart_Frame,bd=8,relief=RIDGE,bg='white')
        calculator_Frame.place(x=5,y=10,width=260,height=340)

        txt_cal_inp=Entry(calculator_Frame,textvariable=self.variable_cal_inp,font=("arial",15,'bold'),width=21,bd=10,relief=GROOVE,state='readonly',justify='right')
        txt_cal_inp.grid(row=0,columnspan=4)

        btn_7=Button(calculator_Frame,text='7',font=("arial",15,'bold'),command=lambda:self.get_input(7),bd=5,width=4,pady=10,cursor='hand2').grid(row=1,column=0)
        btn_8=Button(calculator_Frame,text='8',font=("arial",15,'bold'),command=lambda:self.get_input(8),bd=5,width=4,pady=10,cursor='hand2').grid(row=1,column=1)
        btn_9=Button(calculator_Frame,text='9',font=("arial",15,'bold'),command=lambda:self.get_input(9),bd=5,width=4,pady=10,cursor='hand2').grid(row=1,column=2)
        btn_sum=Button(calculator_Frame,text='+',font=("arial",15,'bold'),command=lambda:self.get_input('+'),bd=5,width=4,pady=10,cursor='hand2').grid(row=1,column=3)
        tn4=Button(calculator_Frame,text='4',font=("arial",15,'bold'),command=lambda:self.get_input(4),bd=5,width=4,pady=10,cursor='hand2').grid(row=2,column=0)
        btn_5=Button(calculator_Frame,text='5',font=("arial",15,'bold'),command=lambda:self.get_input(5),bd=5,width=4,pady=10,cursor='hand2').grid(row=2,column=1)
        btn_6=Button(calculator_Frame,text='6',font=("arial",15,'bold'),command=lambda:self.get_input(6),bd=5,width=4,pady=10,cursor='hand2').grid(row=2,column=2)
        btn_sub=Button(calculator_Frame,text='-',font=("arial",15,'bold'),command=lambda:self.get_input('-'),bd=5,width=4,pady=10,cursor='hand2').grid(row=2,column=3)
        btn_1=Button(calculator_Frame,text='1',font=("arial",15,'bold'),command=lambda:self.get_input(1),bd=5,width=4,pady=10,cursor='hand2').grid(row=3,column=0)
        btn_2=Button(calculator_Frame,text='2',font=("arial",15,'bold'),command=lambda:self.get_input(2),bd=5,width=4,pady=10,cursor='hand2').grid(row=3,column=1)
        btn_3=Button(calculator_Frame,text='3',font=("arial",15,'bold'),command=lambda:self.get_input(3),bd=5,width=4,pady=10,cursor='hand2').grid(row=3,column=2)
        btn_mul=Button(calculator_Frame,text='*',font=("arial",15,'bold'),command=lambda:self.get_input('*'),bd=5,width=4,pady=10,cursor='hand2').grid(row=3,column=3)
        btn_0=Button(calculator_Frame,text='0',font=("arial",15,'bold'),command=lambda:self.get_input(0),bd=5,width=4,pady=16,cursor='hand2').grid(row=4,column=0)
        btn_c=Button(calculator_Frame,text='C',font=("arial",15,'bold'),command=self.clear_cal,bd=5,width=4,pady=16,cursor='hand2').grid(row=4,column=1)
        btn_eq=Button(calculator_Frame,text='=',font=("arial",15,'bold'),command=self.perform_cal,bd=5,width=4,pady=16,cursor='hand2').grid(row=4,column=2)
        btn_div=Button(calculator_Frame,text='/',font=("arial",15,'bold'),command=lambda:self.get_input('/'),bd=5,width=4,pady=16,cursor='hand2').grid(row=4,column=3)










        
        cart_frame=Frame(calculator_cart_Frame,bd=3,relief=RIDGE)
        cart_frame.place(x=280,y=8,width=245,height=342)

        self.cart_title=Label(cart_frame,text='Cart total products: [0]',font=("goudy old style",15),bg='lightgray')
        self.cart_title.pack(side=TOP,fill=X)


        Scrolly=Scrollbar(cart_frame,orient=VERTICAL)
        Scrollx=Scrollbar(cart_frame,orient=HORIZONTAL)

        self.cart_table=ttk.Treeview(cart_frame,columns=("pid","name","price","qty"),yscrollcommand=Scrolly.set,xscrollcommand=Scrolly)
        Scrollx.pack(side=BOTTOM,fill=X)
        Scrolly.pack(side=RIGHT,fill=Y)

        self.cart_table.heading("pid",text="PID")
        self.cart_table.heading("name",text="NAME")
        self.cart_table.heading("price",text="PRICE")
        self.cart_table.heading("qty",text="QTY")
        
        
        self.cart_table["show"]="headings"
        
        self.cart_table.column("pid",width=40)
        self.cart_table.column("name",width=90)
        self.cart_table.column("price",width=90)
        self.cart_table.column("qty",width=30)
        
        
        self.cart_table.pack(fill=BOTH,expand=1)
        self.cart_table.bind("<ButtonRelease-1>",self.get_data_cart)
        
        #---------MENU----------------

        widget_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        widget_frame.place(x=420,y=550,width=530,height=110)

        lbl_p_name=Label(widget_frame,text="Product name",font=("times new roman",15),bg="white").place(x=5,y=5)
        txt_p_name=Entry(widget_frame,textvariable=self.variable_pname,font=("times new roman",15),bg="lightyellow",state="readonly").place(x=5,y=35,width=190,height=22)
        
        lbl_p_price=Label(widget_frame,text="Price per QTY",font=("times new roman",15),bg="white").place(x=230,y=5)
        txt_p_price=Entry(widget_frame,textvariable=self.variable_price,font=("times new roman",15),bg="lightyellow",state="readonly").place(x=230,y=35,width=150,height=22)
        
        lbl_p_qty=Label(widget_frame,text="Quantity",font=("times new roman",15),bg="white").place(x=390,y=5)
        txt_p_qty=Entry(widget_frame,textvariable=self.variable_qty,font=("times new roman",15),bg="lightyellow").place(x=390,y=35,width=130,height=22)

        self.lbl_inStock=Label(widget_frame,text="In stock",font=("times new roman",15),bg="white")
        self.lbl_inStock.place(x=5,y=70)

        btn_clear_cart=Button(widget_frame,text="Clear",command=self.clear_cart,font=("times new roman",15,"bold"),bg="lightgray",cursor="hand2").place(x=180,y=70,height=30,width=150)
        btn_add_cart=Button(widget_frame,text="Add | Update",command=self.add_upd,font=("times new roman",15,"bold"),bg="orange",cursor="hand2").place(x=340,y=70,height=30,width=180)


        #Billing area........
        bill_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        bill_frame.place(x=953,y=110,width=410,height=410)
        btitle=Label(bill_frame,text='Customer bill area',font=("goudy old style",20,'bold'),bg='#262626',fg='white').pack(side=TOP,fill=X)
        Scrolly=Scrollbar(bill_frame,orient=VERTICAL)
        Scrolly.pack(side=RIGHT,fill=Y)
        self.txt_billarea=Text(bill_frame,yscrollcommand=Scrolly.set)
        self.txt_billarea.pack(fill=BOTH,expand=1)
        Scrolly.config(command=self.txt_billarea.yview)


        #buttons....
        billmenu_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        billmenu_frame.place(x=953,y=520,width=410,height=140)

        self.lbl_amount=Label(billmenu_frame,text="Bill Amount\n[0]",font=("goudy old style",15,'bold'),bg='#3f51b5',fg='white')
        self.lbl_amount.place(x=2,y=5,width=120,height=70)

        self.lbl_Discount=Label(billmenu_frame,text="Discount\n[5%]",font=("goudy old style",15,'bold'),bg='green',fg='white')
        self.lbl_Discount.place(x=124,y=5,width=120,height=70)

        self.lbl_netpay=Label(billmenu_frame,text="Net Pay\n[0]",font=("goudy old style",15,'bold'),bg='#607d8b',fg='white')
        self.lbl_netpay.place(x=246,y=5,width=160,height=70)

        btn_print=Button(billmenu_frame,text="Print",command=self.printbill,font=("goudy old style",15,'bold'),bg='#3f51b5',fg='white',cursor="hand2")        
        btn_print.place(x=2,y=80,width=120,height=50)
        btn_clear_all=Button(billmenu_frame,text="Clear all",command=self.clear_all,font=("goudy old style",15,'bold'),bg='white',fg='black',cursor="hand2")
        btn_clear_all.place(x=124,y=80,width=120,height=70)        
        btn_generate=Button(billmenu_frame,text="Generate Bill",command=self.generate_bill,font=("goudy old style",15,'bold'),bg='#607d8b',fg='white',cursor="hand2")
        btn_generate.place(x=246,y=80,width=160,height=70)

        self.show()
        #self.bill_top()



        #--------------Functions------------------------
    def get_input(self,num):
        xnum=self.variable_cal_inp.get()+ str(num)
        self.variable_cal_inp.set(xnum)

    def clear_cal(self):
        self.variable_cal_inp.set('')
    
    def perform_cal(self):
        result=self.variable_cal_inp.get()
        self.variable_cal_inp.set(eval(result))

    def show(self):
        con=sqlite3.connect(database=r'DBMS.db')
        cur=con.cursor()
        try:
            
            cur.execute("select pid,name,price,qty,status from product  where status ='Active'")
            rows=cur.fetchall()
            self.product_table.delete(*self.product_table.get_children())
            for row in rows:
                self.product_table.insert('',END,values=row)
        
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
    


    def search(self):
        con=sqlite3.connect(database=r'DBMS.db')
        cur=con.cursor()
        try:
            if self.variable_search.get()=="":
                messagebox.showerror("Error","Select anything other than search",parent=self.root)
            else:

                cur.execute("select pid,name,price,qty,status from product where Name LIKE '%"+self.variable_search.get()+"%' and status ='Active'",)
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.product_table.delete(*self.product_table.get_children())
                    for row in rows:
                        self.product_table.insert('',END,values=row)

                else:
                    messagebox.showerror("Error","No record found",parent=self.root)
            



        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)   
    

    def get_data(self,ev):
        f=self.product_table.focus()
        content=(self.product_table.item(f))
        row=content['values']
        self.variable_pid.set(row[0])
        self.variable_pname.set(row[1])
        self.variable_price.set(row[2])
        self.lbl_inStock.config(text=f'In stock[{str(row[3])}]')
        self.variable_stock.set(row[3])
        self.variable_qty.set('1')



    def get_data_cart(self,ev):
        f=self.cart_table.focus()
        content=(self.cart_table.item(f))
        row=content['values']
        self.variable_pid.set(row[0])
        self.variable_pname.set(row[1])
        self.variable_price.set(row[2])
        self.lbl_inStock.config(text=f'In stock[{str(row[4])}]')
        self.variable_stock.set(row[4])
        self.variable_qty.set(row[3])




    def add_upd(self):
        if self.variable_qty.get()=="" or self.variable_pid.get()=="":
            messagebox.showerror("Error","Quantity or product is not entered",parent=self.root)
        elif int(self.variable_qty.get())>int(self.variable_stock.get()):
            
            messagebox.showerror("Error","Invalid Quantity",parent=self.root)
        
        else:

                # price=float(int(self.variable_qty.get())*float(self.variable_price.get()))
            price=self.variable_price.get( )
            cart_data=[self.variable_pid.get(),self.variable_pname.get(),price,self.variable_qty.get(),self.variable_stock.get()]
            #update
            p='no'
            index=0
            for row in self.cart_list:
                if self.variable_pid.get()==row[0]:
                    p='yes'
                    break
                index+=1
                
            if p=="yes":
                op=messagebox.askyesno("Confirm","Product already present update/remove ",parent=self.root)
                if op==True:
                    if self.variable_qty.get()=='0':
                        self.cart_list.pop(index)
                    else:
                        #self.cart_list[index][2]=price
                        self.cart_list[index][3]=self.variable_qty.get()

            else:
                self.cart_list.append(cart_data)
            self.show_cart()
            self.bill_update()

    def bill_update(self):
        self.bill_amnt=0
        self.newt_pay=0
        self.discount=0
        for row in self.cart_list:
            self.bill_amnt=self.bill_amnt+(float(row[2])*int(row[3]))
        self.discount=(self.bill_amnt*5)/100
        self.newt_pay=(self.bill_amnt*95)/100
        self.lbl_amount.config(text=f"Bill Amount(Rs.)\n[{str(self.bill_amnt)}]")
        
        self.lbl_netpay.config(text=f"Bill Amount(Rs.)\n[{str(self.newt_pay)}]")

        self.cart_title.config(text=f"Cart \t Total Product : [{str(len(self.cart_list))}]")



    def show_cart(self):
        try:
            self.cart_table.delete(*self.cart_table.get_children())
            for row in self.cart_list:
                self.cart_table.insert('',END,values=row)
    
            
        
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)


    def generate_bill(self):
        if self.variable_cname.get=="" or self.variable_contact.get()=="":
            messagebox.showerror("Error",f"Customer details are required",parent=self.root)
        elif len(self.cart_list)==0:
            messagebox.showerror("ERROR","Please add product to the cart")
        else:
            #TOP
            self.bill_top()
            #MIDDLE
            self.bill_middle()
            # BOTTOM
            self.bill_bottom()
            
            fp=open(f'bill/{str(self.invoice)}.txt','w')
            fp.write(self.txt_billarea.get('1.0',END))
            fp.close()
            messagebox.showinfo("saved","Bill has been generated",parent=self.root)
            self.chk_print=1
    
    def bill_top(self):
        self.invoice=int(time.strftime("%H%M%S"))+int(time.strftime("%d%m%Y"))
        #print(invoice)
        bill_top_temp=f'''
\t\t KN INVENTORY
\t Phone No. 7892882083,Kota-576221
{str("="*47)}
Customer Name: {self.variable_cname.get()}
Phone No:{self.variable_contact.get()}
Bill No:{str(self.invoice)}\t\t DDate: {str(time.strftime("%d/%m/%Y"))}
{str("="*47)}
Product Name \t\t\tQTY\tPrice
{str("="*47)}
        '''
        self.txt_billarea.delete('1.0',END)
        self.txt_billarea.insert('1.0',bill_top_temp)


    def bill_bottom(self):
        bill_bottom_temp=f'''
{str("="*47)}
Bill Amount\t\t\t\tRs.{self.bill_amnt}
Discount\t\t\t\tRs.{self.discount}
Net Pay\t\t\t\tRs.{self.newt_pay}
{str("="*47)}\n
        '''
        self.txt_billarea.insert(END,bill_bottom_temp)
    

    def bill_middle(self):
        con=sqlite3.connect(database=r'DBMS.db')
        cur=con.cursor()
        try:
            for row in self.cart_list:
                pid=row[0]
                name=row[1]
                qty=int(row[4])-int(row[3])
                if int(row[3])==int(row[4]):
                    status='Inactive'
                if int(row[3])!=int(row[4]):
                    status='Active'
                price=float(row[2])*int(row[3])
                price=str(price)
                self.txt_billarea.insert(END,"\n"+name+"\t\t\t"+row[3]+"\tRs."+price)

                cur.execute('Update Product set qty=?,status=? where pid=?',(
                qty,
                status,
                pid
                ))    
                con.commit()
            con.close()
            self.show()    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)         
                
            

    def clear_cart(self):
        self.variable_pid.set("")
        self.variable_pname.set("")
        self.variable_price.set("")
        self.lbl_inStock.config(text=f'In stock')
        self.variable_stock.set("")
        self.variable_qty.set("")

    def clear_all(self):
        del self.cart_list[:]
        self.variable_cname.set("")
        self.variable_contact.set("")
        self.txt_billarea.delete('1.0',END)
        self.cart_title.config(text=f"Cart \t Total Product:[0]")
        self.variable_search.set('')
        self.clear_cart()
        self.show()
        self.show_cart()
#   def update_date(self):
#            time_=time.strftime("%I:%M:%S")
#            date_=time.strftime("%d-%m-%Y")
#            self.labelclock.config(text=f"Welcome to Inventory Mangement System\t\t Date: {str(date_)}\t\t Time:{str(time_)}")
#           self.labelclock.after(200,self.update_date)
            
        
    def logout(self):
        self.root.destroy()
        os.system("python login.py")

    def printbill(self):
        if self.chk_print==1:
            messagebox.showinfo("print","please wait",parent=self.root)
            new_fiile=tempfile.mktemp('.txt')
            open(new_fiile,'w').write(self.txt_billarea.get('1.0',END))
            os.startfile(new_fiile,'print')            
        else:
            messagebox.showerror("print","please generate bill",parent=self.root)


if __name__=="__main__":
    root=Tk()
    obj=billing(root)
    root.mainloop() 