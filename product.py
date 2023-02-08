from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3

class productclass:
    def __init__(self, root):
        self.root =root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")
        self.root.focus_force()
        #-----------------------------------------------------
        self.variable_searchby=StringVar()
        self.variable_searchtext=StringVar()
        
        self.variable_pid=StringVar()
        self.variable_cat=StringVar()
        self.variable_sup=StringVar()
        self.cat_list=[]
        self.sup_list=[]
        self.cat_sup()

        self.variable_name=StringVar()
        self.variable_price=StringVar()
        self.variable_qty=StringVar()
        self.variable_status=StringVar()
        

        product_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        product_Frame.place(x=10,y=10,width=450,height=480)

        title=Label(product_Frame,text="Product Details",font=("goudy old style",18),bg="#0f4d7d",fg="white").pack(side=TOP,fill=X)
        #COLUMN1
        lbl_category=Label(product_Frame,text="Category",font=("goudy old style",18),bg="white").place(x=30,y=60)
        lbl_supplier=Label(product_Frame,text="Supplier",font=("goudy old style",18),bg="white").place(x=30,y=110)
        lbl_Name=Label(product_Frame,text="Name",font=("goudy old style",18),bg="white").place(x=30,y=160)
        lbl_Price=Label(product_Frame,text="Price",font=("goudy old style",18),bg="white").place(x=30,y=210)
        lbl_QTY=Label(product_Frame,text="QTY",font=("goudy old style",18),bg="white").place(x=30,y=260)
        lbl_status=Label(product_Frame,text="Status",font=("goudy old style",18),bg="white").place(x=30,y=310)


        #lbl_category=Label(product_Frame,text="Category",font=("goudy old style",18),bg="white").place(x=30,y=60)
        #---------combobox
        #COLUMN2
        cmb_cat=ttk.Combobox(product_Frame,textvariable=self.variable_cat,values=self.cat_list,state='readonly',justify=CENTER,font=("times new roman",15))
        cmb_cat.place(x=150,y=60,width=200)
        cmb_cat.current(0)


        cmb_sup=ttk.Combobox(product_Frame,textvariable=self.variable_sup,values=self.sup_list,state='readonly',justify=CENTER,font=("times new roman",15))
        cmb_sup.place(x=150,y=110,width=200)
        cmb_sup.current(0)

        txt_name=Entry(product_Frame,textvariable=self.variable_name,font=("times new roman",15),bg='lightyellow').place(x=150,y=160,width=200)
        txt_price=Entry(product_Frame,textvariable=self.variable_price,font=("times new roman",15),bg='lightyellow').place(x=150,y=210,width=200)
        txt_qty=Entry(product_Frame,textvariable=self.variable_qty,font=("times new roman",15),bg='lightyellow').place(x=150,y=260,width=200)

        cmb_status=ttk.Combobox(product_Frame,textvariable=self.variable_status,values=("Active","Inactive"),state='readonly',justify=CENTER,font=("times new roman",15))
        cmb_status.place(x=150,y=310,width=200)
        cmb_status.current(0)


        addbutton=Button(product_Frame,text="Save",command=self.add,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=10,y=400,width=100,height=40)
        updatebutton=Button(product_Frame,text="Update",command=self.update,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=120,y=400,width=100,height=40)
        deletebutton=Button(product_Frame,text="Delete",command=self.delete,font=("goudy old style",15),bg="#f44336",fg="white",cursor="hand2").place(x=230,y=400,width=100,height=40)
        clearbutton=Button(product_Frame,text="Clear",command=self.clear,font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2").place(x=340,y=400,width=100,height=40)


        searchframe=LabelFrame(self.root,text="Search Employee",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE,bg="white")
        searchframe.place(x=480,y=10,width=600,height=80)

        cmb_search=ttk.Combobox(searchframe,textvariable=self.variable_searchby,values=("Select","Category","Supplier","Name"),state='readonly',justify=CENTER,font=("times new roman",15))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        txt_search=Entry(searchframe,textvariable=self.variable_searchtext,font=("goudy old style",15),bg="lightyellow").place(x=200,y=10)
        searchbutton=Button(searchframe,text="Search",command=self.search,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=440,y=9,width=150,height=30)
        

        p_frame=Frame(self.root,bd=3,relief=RIDGE)
        p_frame.place(x=480,y=100,width=600,height=390)

        Scrolly=Scrollbar(p_frame,orient=VERTICAL)
        Scrollx=Scrollbar(p_frame,orient=HORIZONTAL)

        self.product_table=ttk.Treeview(p_frame,columns=("pid","Supplier","Category","Name","price","qty","status"),yscrollcommand=Scrolly.set,xscrollcommand=Scrolly)
        Scrollx.pack(side=BOTTOM,fill=X)
        Scrolly.pack(side=RIGHT,fill=Y)

        self.product_table.heading("pid",text="pid")
        self.product_table.heading("Category",text="Category")
        self.product_table.heading("Supplier",text="Supplier")
        self.product_table.heading("Name",text="Name")
        self.product_table.heading("price",text="price")
        self.product_table.heading("qty",text="qty")
        self.product_table.heading("status",text="status")
        self.product_table["show"]="headings"
        
        self.product_table.column("pid",width=90)
        self.product_table.column("Supplier",width=100)
        self.product_table.column("Category",width=100)
        self.product_table.column("Name",width=100)
        self.product_table.column("price",width=100)
        self.product_table.column("qty",width=100)
        self.product_table.column("status",width=100)
       
        self.product_table.pack(fill=BOTH,expand=1)
        self.product_table.bind("<ButtonRelease-1>",self.get_data)

        self.show()
        


    def cat_sup(self):
        self.cat_list.append("Empty")
        self.sup_list.append("empty") 
        con=sqlite3.connect(database=r'DBMS.db')
        cur=con.cursor()
        try:
            cur.execute("Select name from category")
            cat=cur.fetchall()
            #print(cat)
            if len(cat)>0:
                del self.cat_list[:]
                self.cat_list.append("Select")
                for i in cat:
                    self.cat_list.append(i[0])

            cur.execute("Select name from supplier")
            sup=cur.fetchall()
            #print(sup)
            if len(sup)>0:
                del self.sup_list[:]
                self.sup_list.append("Select")
                for i in sup:
                    self.sup_list.append(i[0])
            
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)


    def add(self):
        con=sqlite3.connect(database=r'DBMS.db')
        cur=con.cursor()
        try:
            if self.variable_cat.get()=="Select" or self.variable_cat.get()=="Empty" or self.variable_sup.get()=="Select" or self.variable_sup.get()=="Empty" or self.variable_name.get()=="Select":
                messagebox.showerror("Error","Error All fields are required",parent=self.root)
            else:
                cur.execute("Select * from product where Name=?",(self.variable_name.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This product already exists try different one",parent=self.root)
                else:
                    cur.execute("Insert into product(Supplier,Category,Name,price,qty,status) values(?,?,?,?,?,?)",(
                                                
                                                self.variable_sup.get(),
                                                self.variable_cat.get(),
                                                self.variable_name.get(),
                                                self.variable_price.get(),
                                                self.variable_qty.get(),
                                                self.variable_status.get(),
                                                   ))  
                    con.commit()
                    messagebox.showinfo("Success","Product details added successfully",parent=self.root)
                    self.show() 



        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)




    def show(self):
        con=sqlite3.connect(database=r'DBMS.db')
        cur=con.cursor()
        try:
            cur.execute("select * from product")
            rows=cur.fetchall()
            self.product_table.delete(*self.product_table.get_children())
            for row in rows:
                self.product_table.insert('',END,values=row)


        
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)

    def get_data(self,ev):
        f=self.product_table.focus()
        content=(self.product_table.item(f))
        row=content['values']
        print(row)
        self.variable_pid.set(row[0])
        self.variable_sup.set(row[1])
        self.variable_cat.set(row[2])
        self.variable_name.set(row[3])
        self.variable_price.set(row[4])
        self.variable_qty.set(row[5])
        self.variable_status.set(row[6])
        

    def update(self):
        con=sqlite3.connect(database=r'DBMS.db')
        cur=con.cursor()
        try:
            if self.variable_pid.get()=="":
                messagebox.showerror("Error","select products from the list",parent=self.root)
            else:
                cur.execute("Select * from product where pid=?",(self.variable_pid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Product id",parent=self.root)
                else:
                    cur.execute("Update product set Category=?,Supplier=?,Name=?,price=?,qty=?,status=?where pid=? ",(
                                                
                                                
                                                self.variable_sup.get(),
                                                self.variable_cat.get(),
                                                self.variable_name.get(),
                                                self.variable_price.get(),
                                                self.variable_qty.get(),
                                                self.variable_status.get(),
                                                self.variable_pid.get(),
                                            ))  
                    con.commit()
                    messagebox.showinfo("Success","Product details updated successfully",parent=self.root)
                    self.show() 



        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
    
    
    def delete(self):
        con=sqlite3.connect(database=r'DBMS.db')
        cur=con.cursor()
        try:
            if self.variable_pid.get()=="":
                messagebox.showerror("Error","Error Imp details must be filled",parent=self.root)
            else:
                cur.execute("Select * from product where pid=?",(self.variable_pid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid product id",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete ?",parent=self.root)
                    if op==True:
                        cur.execute("delete from product where pid=?",(self.variable_pid.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Successfully deleted product",parent=self.root)
                        self.clear()


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)    


    def clear(self):     
        self.variable_pid.set("")
        self.variable_sup.set("Select")
        self.variable_cat.set("Select")
        self.variable_name.set("")
        self.variable_price.set("")
        self.variable_qty.set("")
        self.variable_status.set("Active")
        
        self.variable_searchby.set("Select")
        self.variable_searchtext.set("")
        self.show()
        

    def search(self):
        con=sqlite3.connect(database=r'DBMS.db')
        cur=con.cursor()
        try:
            if self.variable_searchby.get()=="Select":
                messagebox.showerror("Error","Select search by option",parent=self.root)
            elif self.variable_searchtext.get()=="":
                messagebox.showerror("Error","Select anything other than search",parent=self.root)
            else:

                cur.execute("select * from product where "+self.variable_searchby.get()+" LIKE '%"+self.variable_searchtext.get()+"%'",)
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.product_table.delete(*self.product_table.get_children())
                    for row in rows:
                        self.product_table.insert('',END,values=row)

                else:
                    messagebox.showerror("Error","No record found",parent=self.root)
            



        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)    

if __name__=="__main__":
    root=Tk()
    obj=productclass(root)
    root.mainloop()