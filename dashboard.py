from tkinter import*
from PIL import Image,ImageTk
from employee import Employeeclass
from supplier import supplierclass
from category import categoryclass
from product import productclass
from sales import salesclass
import sqlite3
from tkinter import messagebox
import os
import time
class IMS:
    def __init__(self, root):
        self.root =root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System")
        self.root.config(bg="bisque")

        self.icon_title=PhotoImage(file="images/logo1.gif")
        title=Label(self.root, text="Inventory Management System",image=self.icon_title,compound=LEFT, font=("times new roman",40,"bold"),bg="black",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)
       
       
        btnlogout=Button(self.root,text="Logout",command=self.logout,font=("times new roman",15,"bold"),bg="yellow",cursor="hand2").place(x=1100,y=10,height=50,width=150)
       #clock
        self.labelclock=Label(self.root, text="Welcome to Inventory Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS", font=("times new roman",15,"bold"),bg="#4d636d",fg="white")
        self.labelclock.place(x=0,y=70,relwidth=1,height=30)

       
        self.menulogo=Image.open("images/menu.png")
        self.menulogo=self.menulogo.resize((200,200),Image.LANCZOS)
        self.menulogo=ImageTk.PhotoImage(self.menulogo)
        Leftmenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Leftmenu.place(x=0,y=102,width=200,height=565)
        lblmenulogo=Label(Leftmenu,image=self.menulogo)
        lblmenulogo.pack(side=TOP,fill=X) 

        lmenu=Label(Leftmenu,text="Menu",font=("times new roman",20),bg="#009688").pack(side=TOP,fill=X)
        menuemp=Button(Leftmenu,text="Employee",command=self.employee,font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        menusupplier=Button(Leftmenu,text="Supplier",command=self.supplier,font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        menucategory=Button(Leftmenu,text="Category",command=self.category,font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        menuproduct=Button(Leftmenu,text="Product",command=self.product,font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        menusales=Button(Leftmenu,text="Sales",command=self.sales,font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        menuexit=Button(Leftmenu,text="Exit",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
         
        self.lblemployee=Label(self.root,text="Total Employee\n[ 0 ]",bd=5,relief=RIDGE,bg="gold",fg="white",font=("times new roman",20,"bold"))
        self.lblemployee.place(x=300,y=120,height=150,width=300)

        self.lblsupplier=Label(self.root,text="Total Supplier\n[ 0 ]",bd=5,relief=RIDGE,bg="red",fg="white",font=("times new roman",20,"bold"))
        self.lblsupplier.place(x=650,y=120,height=150,width=300)

        self.lblcategory=Label(self.root,text="Total Category\n[ 0 ]",bd=5,relief=RIDGE,bg="dark green",fg="white",font=("times new roman",20,"bold"))
        self.lblcategory.place(x=1000,y=120,height=150,width=300)

        self.lblproduct=Label(self.root,text="Total Product\n[ 0 ]",bd=5,relief=RIDGE,bg="orange",fg="white",font=("times new roman",20,"bold"))
        self.lblproduct.place(x=300,y=300,height=150,width=300)

        self.lblsales=Label(self.root,text="Total Sales\n[ 0 ]",bd=5,relief=RIDGE,bg="aquamarine3",fg="white",font=("times new roman",20,"bold"))
        self.lblsales.place(x=650,y=300,height=150,width=300)

        self.update()

    def employee(self):
        self.new_win=Toplevel(self.root)    
        self.new_obj=Employeeclass(self.new_win)

    def supplier(self):
        self.new_win=Toplevel(self.root)    
        self.new_obj=supplierclass(self.new_win)    

    def category(self):
        self.new_win=Toplevel(self.root)    
        self.new_obj=categoryclass(self.new_win)    
    def product(self):
        self.new_win=Toplevel(self.root)    
        self.new_obj=productclass(self.new_win)  
    def sales(self):
        self.new_win=Toplevel(self.root)    
        self.new_obj=salesclass(self.new_win)   

    def update(self):
        con=sqlite3.connect(database=r'DBMS.db')
        cur=con.cursor()
        try:
            cur.execute("select * from product")
            product=cur.fetchall()
            self.lblproduct.config(text=f'Total Products\n[ {str(len(product))} ]')

            cur.execute("select * from supplier")
            supplier=cur.fetchall()
            self.lblsupplier.config(text=f'Total supplier \n[ {str(len(supplier))} ]')

            cur.execute("select * from category")
            category=cur.fetchall()
            self.lblcategory.config(text=f'Total category\n[ {str(len(category))} ]')

            cur.execute("select * from employee")
            employee=cur.fetchall()
            self.lblemployee.config(text=f'Total employee\n[ {str(len(employee))} ]')
            bill=len(os.listdir('bill'))
            self.lblsales.config(text=f"Total Sales\n[{str(bill)}]")


            time_=time.strftime("%I:%M:%S")
            date_=time.strftime("%d-%m-%Y")
            self.labelclock.config(text=f"Welcome to Inventory Mangement System\t\t Date: {str(date_)}\t\t Time:{str(time_)}")
            self.labelclock.after(200,self.update)


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)    



    def logout(self):
        self.root.destroy()
        os.system("python login.py")
        


if __name__=="__main__":
    root=Tk()
    obj=IMS(root)
    root.mainloop() 
