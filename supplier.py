from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class supplierclass:
    def __init__(self, root):
        self.root =root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")
        self.root.focus_force()
         
        self.variable_searchby=StringVar()
        self.variable_searchtext=StringVar()

        self.variable_supplierinvoice=StringVar()
        self.variable_contact=StringVar()
        self.variable_name=StringVar()

        searchframe=LabelFrame(self.root,text="Search supplier",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE,bg="white")
        searchframe.place(x=250,y=60,width=600,height=70)

        lbl_search=Label(searchframe,text="Search by Invoice No.",font=("times new roman",15))
        lbl_search.place(x=10,y=10)

        txt_search=Entry(searchframe,textvariable=self.variable_searchtext,font=("goudy old style",15),bg="lightyellow").place(x=200,y=10)
        searchbutton=Button(searchframe,text="Search",command=self.search,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=440,y=9,width=150,height=30)
       
        title=Label(self.root,text="Supplier Details",font=("goudy old style",20),bg="#0f4d7d",fg="white").place(x=50,y=10,width=1000)

        label_sup_invoice=Label(self.root,text="Invoice No.",font=("goudy old style",15),bg="white").place(x=50,y=150)
        text_sup_invoice=Entry(self.root,textvariable=self.variable_supplierinvoice,font=("goudy old style",15),bg="lightyellow").place(x=150,y=150,width=180)
  

        label_name=Label(self.root,text="Name",font=("goudy old style",15),bg="white").place(x=50,y=190)
        text_name=Entry(self.root,textvariable=self.variable_name,font=("goudy old style",15),bg="lightyellow").place(x=150,y=190,width=180)



        label_contact =Label(self.root,text="Contact",font=("goudy old style",15),bg="white").place(x=50,y=230)
        text_contact=Entry(self.root,textvariable=self.variable_contact,font=("goudy old style",15),bg="lightyellow").place(x=150,y=230,width=180)
           

        label_desc=Label(self.root,text="Description",font=("goudy old style",15),bg="white").place(x=50,y=270)

        self.text_desc=Text(self.root,font=("goudy old style",15),bg="lightyellow")
        self.text_desc.place(x=150,y=270,width=300,height=60)

        addbutton=Button(self.root,text="Save",command=self.add,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=500,y=305,width=110,height=28)
        updatebutton=Button(self.root,text="Update",command=self.update,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=620,y=305,width=110,height=28)
        deletebutton=Button(self.root,text="Delete",command=self.delete,font=("goudy old style",15),bg="#f44336",fg="white",cursor="hand2").place(x=740,y=305,width=110,height=28)
        clearbutton=Button(self.root,text="Clear",command=self.clear,font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2").place(x=860,y=305,width=110,height=28)

        
        supplierframe=Frame(self.root,bd=3,relief=RIDGE)
        supplierframe.place(x=0,y=350,relwidth=1,height=150)

        Scrolly=Scrollbar(supplierframe,orient=VERTICAL)
        Scrollx=Scrollbar(supplierframe,orient=HORIZONTAL)

        self.suppliertable=ttk.Treeview(supplierframe,columns=("invoice","name","contact","desc"),yscrollcommand=Scrolly.set,xscrollcommand=Scrolly)
        Scrollx.pack(side=BOTTOM,fill=X)
        Scrolly.pack(side=RIGHT,fill=Y)

        self.suppliertable.heading("invoice",text="INVOICE")
        self.suppliertable.heading("name",text="NAME")
        self.suppliertable.heading("contact",text="CONTACT")
        self.suppliertable.heading("desc",text="DESCRIPTION")
        self.suppliertable["show"]="headings"
        
        self.suppliertable.column("invoice",width=90)
        self.suppliertable.column("name",width=100)
        self.suppliertable.column("contact",width=100)
        self.suppliertable.column("desc",width=100)
        self.suppliertable.pack(fill=BOTH,expand=1)
        self.suppliertable.bind("<ButtonRelease-1>",self.get_data)


        self.show()
#------------------------------------------------------------------------------------------------------
    def add(self):
        con=sqlite3.connect(database=r'DBMS.db')
        cur=con.cursor()
        try:
            if self.variable_supplierinvoice.get()=="":
                messagebox.showerror("Error","invoice must be required",parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",(self.variable_supplierinvoice.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This invoice no. already exists try different one",parent=self.root)
                else:
                    cur.execute("Insert into supplier(invoice,name,contact,desc) values(?,?,?,?)",(
                                                
                                                self.variable_supplierinvoice.get(),
                                                self.variable_name.get(),
                                                self.variable_contact.get(),
                                                self.text_desc.get('1.0',END),
                                            ))  
                    con.commit()
                    messagebox.showinfo("Success","Supplier details added successfully",parent=self.root)
                    self.show() 



        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)

    
    def show(self):
        con=sqlite3.connect(database=r'DBMS.db')
        cur=con.cursor()
        try:
            cur.execute("select * from supplier")
            rows=cur.fetchall()
            self.suppliertable.delete(*self.suppliertable.get_children())
            for row in rows:
                self.suppliertable.insert('',END,values=row)


        
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)

    def get_data(self,ev):
        f=self.suppliertable.focus()
        content=(self.suppliertable.item(f))
        row=content['values']
        print(row)
        self.variable_supplierinvoice.set(row[0]),
        self.variable_name.set(row[1]),
        self.variable_contact.set(row[2]),
        self.text_desc.delete('1.0',END),
        self.text_desc.insert(END,row[3]),

    def update(self):
        con=sqlite3.connect(database=r'DBMS.db')
        cur=con.cursor()
        try:
            if self.variable_supplierinvoice.get()=="":
                messagebox.showerror("Error","Error Invoice no. must be filled",parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",(self.variable_supplierinvoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid invoice number",parent=self.root)
                else:
                    cur.execute("Update supplier set name=?,contact=?,desc=? where invoice=? ",(
                                                
                                                
                                                self.variable_name.get(),
                                                self.variable_contact.get(),
                                                self.text_desc.get('1.0',END),   
                                                self.variable_supplierinvoice.get(),
                    ))                       
                    con.commit()
                    messagebox.showinfo("Success","Supplier details updated successfully",parent=self.root)
                    self.show() 



        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
    
    
    def delete(self):
        con=sqlite3.connect(database=r'DBMS.db')
        cur=con.cursor()
        try:
            if self.variable_supplierinvoice.get()=="":
                messagebox.showerror("Error","Error Invoice no. must be filled",parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",(self.variable_supplierinvoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid supplier id",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete ?",parent=self.root)
                    if op==True:
                        cur.execute("delete from supplier where invoice=?",(self.variable_supplierinvoice.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Successfully deleted supplier",parent=self.root)
                        self.clear()


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)    


    def clear(self):
        self.variable_supplierinvoice.set(""),
        self.variable_name.set(""),  
        self.variable_contact.set(""),
        self.text_desc.delete('1.0',END),
        self.variable_searchtext.set("")
        self.show()
        

    def search(self):
        con=sqlite3.connect(database=r'DBMS.db')
        cur=con.cursor()
        try:
            if self.variable_searchtext.get()=="":
                messagebox.showerror("Error","invoice no should be required",parent=self.root)

            else:

                cur.execute("select * from supplier where invoice=?",(self.variable_searchtext.get()))
                rows=cur.fetchall()
                if rows!=0:
                    self.suppliertable.delete(*self.suppliertable.get_children())
                    for row in rows:
                        self.suppliertable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record found",parent=self.root)



        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)    



if __name__=="__main__":
    root=Tk()
    obj=supplierclass(root)
    root.mainloop()         