from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class categoryclass:
    def __init__(self, root):
        self.root =root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")
        self.root.focus_force()

        self.variable_catid=StringVar()
        self.variable_name=StringVar()        


        label_title=Label(self.root,text="Manage Product Category",font=("goudy old style",30),bg="#184a45",fg="white").pack(side=TOP,fill=X)

        labelname=Label(self.root,text="Enter Invoice Id",font=("times new roman",15),bg="white").place(x=50,y=60)
        txtname=Entry(self.root,textvariable=self.variable_catid,font=("goudy old style",18),bg="lightyellow").place(x=50,y=90,width=300) 

        label_name=Label(self.root,text="Enter Category Name",font=("times new roman",15),bg="white").place(x=50,y=140)
        txt_name=Entry(self.root,textvariable=self.variable_name,font=("goudy old style",18),bg="lightyellow").place(x=50,y=170,width=300) 

        addbutton=Button(self.root,text="ADD",command=self.add,font=("goudy old style",15),bg="green",fg="white",cursor="hand2").place(x=360,y=170,width=150,height=30) 
        delbutton=Button(self.root,text="DELETE",command=self.delete,font=("goudy old style",15),bg="red",fg="white",cursor="hand2").place(x=520,y=170,width=150,height=30) 

        categoryframe=Frame(self.root,bd=3,relief=RIDGE)
        categoryframe.place(x=700,y=100,width=380,height=390)

        Scrolly=Scrollbar(categoryframe,orient=VERTICAL)
        Scrollx=Scrollbar(categoryframe,orient=HORIZONTAL)

        self.categorytable=ttk.Treeview(categoryframe,columns=("cid","name"),yscrollcommand=Scrolly.set,xscrollcommand=Scrolly)
        Scrollx.pack(side=BOTTOM,fill=X)
        Scrolly.pack(side=RIGHT,fill=Y)
        Scrollx.config(command=self.categorytable.xview)
        Scrolly.config(command=self.categorytable.yview)        

        self.categorytable.heading("cid",text="CID")
        self.categorytable.heading("name",text="NAME")
        self.categorytable["show"]="headings"
        
        self.categorytable.column("cid",width=90)        
        self.categorytable.column("name",width=100)
        self.categorytable.pack(fill=BOTH,expand=1)
        self.categorytable.bind("<ButtonRelease-1>",self.get_data)

        self.image1=Image.open("images/cat2.png")
        self.image1=self.image1.resize((610,260),Image.LANCZOS)
        self.image1=ImageTk.PhotoImage(self.image1)

       
        self.labelimage1=Label(self.root,image=self.image1)
        self.labelimage1.place(x=50,y=220)
        self.show()
#------------------------functions--------------------------#
    def add(self):
        con=sqlite3.connect(database=r'DBMS.db')
        cur=con.cursor()
        try:
            if self.variable_name.get()=="":
                messagebox.showerror("Error","category id  must be required",parent=self.root)
            else:
                cur.execute("Select * from category where cid=?",(self.variable_catid.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This Category exists",parent=self.root)
                else:
                    cur.execute("Insert into category(cid,name) values(?,?)",(self.variable_catid.get(),self.variable_name.get(),
                                            
                    ))  
                    con.commit()
                    messagebox.showinfo("Success","Category details added successfully",parent=self.root)
                    self.show() 



        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)

 
    def show(self):
        con=sqlite3.connect(database=r'DBMS.db')
        cur=con.cursor()
        try:
            cur.execute("select * from category")
            rows=cur.fetchall()
            self.categorytable.delete(*self.categorytable.get_children())
            for row in rows:
                self.categorytable.insert('',END,values=row)


        
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
 
    def get_data(self,ev):
        f=self.categorytable.focus()
        content=(self.categorytable.item(f))
        row=content['values']
        #print(row)
        self.variable_catid.set(row[0])
        self.variable_name.set(row[1])

    def delete(self):
        con=sqlite3.connect(database=r'DBMS.db')
        cur=con.cursor()
        try:
            if self.variable_catid.get()=="":
                messagebox.showerror("Error","Select or Enter Category Name",parent=self.root)
            else:
                cur.execute("Select * from category where cid=?",(self.variable_catid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Try Again",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete ?",parent=self.root)
                    if op==True:
                        cur.execute("delete from category where cid=?",(self.variable_catid.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Successfully deleted category",parent=self.root)
                        self.show()
                        self.variable_catid.set("")
                        self.variable_name.set("")


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)    


if __name__=="__main__":
    root=Tk()
    obj=categoryclass(root)
    root.mainloop() 