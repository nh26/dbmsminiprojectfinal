from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class Employeeclass:
    def __init__(self, root):
        self.root =root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")
        self.root.focus_force()
         
        self.variable_searchby=StringVar()
        self.variable_searchtext=StringVar()

        self.variable_empid=StringVar()
        self.variable_gender=StringVar() 
        self.variable_contact=StringVar()
        self.variable_name=StringVar()
        self.variable_dob=StringVar()
        self.variable_doj=StringVar()
        self.variable_email=StringVar()
        self.variable_pass=StringVar()
        self.variable_utype=StringVar()
        self.variable_salary=StringVar()

        searchframe=LabelFrame(self.root,text="Search Employee",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE,bg="white")
        searchframe.place(x=250,y=20,width=600,height=70)

        cmb_search=ttk.Combobox(searchframe,textvariable=self.variable_searchby,values=("select","email","name","contact"),state='readonly',justify=CENTER,font=("times new roman",15))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        txt_search=Entry(searchframe,textvariable=self.variable_searchtext,font=("goudy old style",15),bg="lightyellow").place(x=200,y=10)
        searchbutton=Button(searchframe,text="Search",command=self.search,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=440,y=9,width=150,height=30)
        title=Label(self.root,text="Employee Details",font=("goudy old style",15),bg="#0f4d7d",fg="white").place(x=50,y=100,width=1000)

        label_empid=Label(self.root,text="Emp Id",font=("goudy old style",15),bg="white").place(x=50,y=150)
        label_gender=Label(self.root,text="Gender",font=("goudy old style",15),bg="white").place(x=350,y=150)
        label_contact=Label(self.root,text="Contact",font=("goudy old style",15),bg="white").place(x=750,y=150)

        text_empid=Entry(self.root,textvariable=self.variable_empid,font=("goudy old style",15),bg="lightyellow").place(x=150,y=150,width=180)
        #text_gender=Entry(self.root,textvariable=self.variable_gender,font=("goudy old style",15),bg="white")
        cmb_gender=ttk.Combobox(self.root,textvariable=self.variable_gender,values=("select","Male","Female","Other"),state='readonly',justify=CENTER,font=("times new roman",15))
        cmb_gender.place(x=500,y=150,width=180)
        cmb_gender.current(0)
        text_contact=Entry(self.root,textvariable=self.variable_contact,font=("goudy old style",15),bg="lightyellow").place(x=850,y=150,width=180)
      

        label_name=Label(self.root,text="Name",font=("goudy old style",15),bg="white").place(x=50,y=190)
        label_dob=Label(self.root,text="D.O.B",font=("goudy old style",15),bg="white").place(x=350,y=190)
        label_doj=Label(self.root,text="D.O.J",font=("goudy old style",15),bg="white").place(x=750,y=190)
        text_name=Entry(self.root,textvariable=self.variable_name,font=("goudy old style",15),bg="lightyellow").place(x=150,y=190,width=180)
        text_dob=Entry(self.root,textvariable=self.variable_dob,font=("goudy old style",15),bg="lightyellow").place(x=500,y=190,width=180)      
        text_doj=Entry(self.root,textvariable=self.variable_doj,font=("goudy old style",15),bg="lightyellow").place(x=850,y=190,width=180)


        label_email=Label(self.root,text="Email",font=("goudy old style",15),bg="white").place(x=50,y=230)
        label_password=Label(self.root,text="Password",font=("goudy old style",15),bg="white").place(x=350,y=230)
        label_utype=Label(self.root,text="User Type",font=("goudy old style",15),bg="white").place(x=750,y=230)
        text_email=Entry(self.root,textvariable=self.variable_email,font=("goudy old style",15),bg="lightyellow").place(x=150,y=230,width=180)
        text_password=Entry(self.root,textvariable=self.variable_pass,font=("goudy old style",15),bg="lightyellow").place(x=500,y=230,width=180)      
        #text_utype=Entry(self.root,textvariable=self.variable_utype,font=("goudy old style",15),bg="lightyellow").place(x=850,y=230,width=180)
        cmb_utype=ttk.Combobox(self.root,textvariable=self.variable_utype,values=("Admin","Employee"),state='readonly',justify=CENTER,font=("times new roman",15))
        cmb_utype.place(x=850,y=230,width=180)
        cmb_utype.current(0)    


        label_address=Label(self.root,text="Address",font=("goudy old style",15),bg="white").place(x=50,y=270)
        label_salary=Label(self.root,text="Salary",font=("goudy old style",15),bg="white").place(x=500,y=270)

        self.text_address=Text(self.root,font=("goudy old style",15),bg="lightyellow")
        self.text_address.place(x=150,y=270,width=300,height=60)
        text_salary=Entry(self.root,textvariable=self.variable_salary,font=("goudy old style",15),bg="lightyellow").place(x=600,y=270,width=180)

        addbutton=Button(self.root,text="Save",command=self.add,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=500,y=305,width=110,height=28)
        updatebutton=Button(self.root,text="Update",command=self.update,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=620,y=305,width=110,height=28)
        deletebutton=Button(self.root,text="Delete",command=self.delete,font=("goudy old style",15),bg="#f44336",fg="white",cursor="hand2").place(x=740,y=305,width=110,height=28)
        clearbutton=Button(self.root,text="Clear",command=self.clear,font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2").place(x=860,y=305,width=110,height=28)

        
        employeeframe=Frame(self.root,bd=3,relief=RIDGE)
        employeeframe.place(x=0,y=350,relwidth=1,height=150)

        Scrolly=Scrollbar(employeeframe,orient=VERTICAL)
        Scrollx=Scrollbar(employeeframe,orient=HORIZONTAL)

        self.employeetable=ttk.Treeview(employeeframe,columns=("eid","name","email","gender","contact","dob","doj","password","utype","address","salary"),yscrollcommand=Scrolly.set,xscrollcommand=Scrolly)
        Scrollx.pack(side=BOTTOM,fill=X)
        Scrolly.pack(side=RIGHT,fill=Y)

        self.employeetable.heading("eid",text="EMP Id")
        self.employeetable.heading("name",text="NAME")
        self.employeetable.heading("email",text="EMAIL")
        self.employeetable.heading("gender",text="GENDER")
        self.employeetable.heading("contact",text="CONTCT")
        self.employeetable.heading("dob",text="D.O.B")
        self.employeetable.heading("doj",text="D.O.J")
        self.employeetable.heading("password",text="PASSWORD")
        self.employeetable.heading("utype",text="USER TYPE")
        self.employeetable.heading("address",text="ADDRESS")
        self.employeetable.heading("salary",text="SALARY")
        self.employeetable["show"]="headings"
        
        self.employeetable.column("eid",width=90)
        self.employeetable.column("name",width=100)
        self.employeetable.column("email",width=100)
        self.employeetable.column("gender",width=100)
        self.employeetable.column("contact",width=100)
        self.employeetable.column("dob",width=100)
        self.employeetable.column("doj",width=100)
        self.employeetable.column("password",width=100)
        self.employeetable.column("utype",width=100)
        self.employeetable.column("address",width=100)
        self.employeetable.column("salary",width=100)
        self.employeetable.pack(fill=BOTH,expand=1)
        self.employeetable.bind("<ButtonRelease-1>",self.get_data)


        self.show()
#------------------------------------------------------------------------------------------------------
    def add(self):
        con=sqlite3.connect(database=r'DBMS.db')
        cur=con.cursor()
        try:
            if self.variable_empid.get()=="":
                messagebox.showerror("Error","Error Imp details must be filled",parent=self.root)
            else:
                cur.execute("Select * from employee where eid=?",(self.variable_empid.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This emp id already assined try different one",parent=self.root)
                else:
                    cur.execute("Insert into employee(eid,name,email,gender,contact,dob,doj,password,utype,address,salary) values(?,?,?,?,?,?,?,?,?,?,?)",(
                                                
                                                self.variable_empid.get(),
                                                self.variable_name.get(),
                                                self.variable_email.get(),
                                                self.variable_gender.get(),
                                                self.variable_contact.get(),
                                                self.variable_dob.get(),
                                                self.variable_doj.get(),
                                                self.variable_pass.get(),
                                                self.variable_utype.get(),
                                                self.text_address.get('1.0',END),
                                                self.variable_salary.get(),
                                            ))  
                    con.commit()
                    messagebox.showinfo("Success","Employee details added successfully",parent=self.root)
                    self.show() 



        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)

    
    def show(self):
        con=sqlite3.connect(database=r'DBMS.db')
        cur=con.cursor()
        try:
            cur.execute("select * from employee")
            rows=cur.fetchall()
            self.employeetable.delete(*self.employeetable.get_children())
            for row in rows:
                self.employeetable.insert('',END,values=row)


        
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)

    def get_data(self,ev):
        f=self.employeetable.focus()
        content=(self.employeetable.item(f))
        row=content['values']
        #print(row)
        self.variable_empid.set(row[0]),
        self.variable_name.set(row[1]),
        self.variable_email.set(row[2]),
        self.variable_gender.set(row[3]),
        self.variable_contact.set(row[4]),
        self.variable_dob.set(row[5]),
        self.variable_doj.set(row[6]),
        self.variable_pass.set(row[7]),
        self.variable_utype.set(row[8]),
        self.text_address.delete('1.0',END),
        self.text_address.insert(END,row[9]),
        self.variable_salary.set(row[10])

    def update(self):
        con=sqlite3.connect(database=r'DBMS.db')
        cur=con.cursor()
        try:
            if self.variable_empid.get()=="":
                messagebox.showerror("Error","Error Imp details must be filled",parent=self.root)
            else:
                cur.execute("Select * from employee where eid=?",(self.variable_empid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid employee id",parent=self.root)
                else:
                    cur.execute("Update employee set name=?,email=?,gender=?,contact=?,dob=?,doj=?,password=?,utype=?,address=?,salary=? where eid=? ",(
                                                
                                                
                                                self.variable_name.get(),
                                                self.variable_email.get(),
                                                self.variable_gender.get(),
                                                self.variable_contact.get(),
                                                self.variable_dob.get(),
                                                self.variable_doj.get(),
                                                self.variable_pass.get(),
                                                self.variable_utype.get(),
                                                self.text_address.get('1.0',END),
                                                self.variable_salary.get(),
                                                self.variable_empid.get(),
                                            ))  
                    con.commit()
                    messagebox.showinfo("Success","Employee details updated successfully",parent=self.root)
                    self.show() 



        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
    
    
    def delete(self):
        con=sqlite3.connect(database=r'DBMS.db')
        cur=con.cursor()
        try:
            if self.variable_empid.get()=="":
                messagebox.showerror("Error","Error Imp details must be filled",parent=self.root)
            else:
                cur.execute("Select * from employee where eid=?",(self.variable_empid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid employee id",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete ?",parent=self.root)
                    if op==True:
                        cur.execute("delete from employee where eid=?",(self.variable_empid.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Successfully deleted empid",parent=self.root)
                        self.clear()


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)    


    def clear(self):
        self.variable_empid.set(""),
        self.variable_name.set(""),
        self.variable_email.set(""),
        self.variable_gender.set("Select"),
        self.variable_contact.set(""),
        self.variable_dob.set(""),
        self.variable_doj.set(""),
        self.variable_pass.set(""),
        self.variable_utype.set("Admin"),
        self.text_address.delete('1.0',END),
        self.variable_salary.set("")
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

                cur.execute("select * from employee where "+self.variable_searchby.get()+" LIKE '%"+self.variable_searchtext.get()+"%'",)
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.employeetable.delete(*self.employeetable.get_children())
                    for row in rows:
                        self.employeetable.insert('',END,values=row)

                else:
                    messagebox.showerror("Error","No record found",parent=self.root)
            



        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)    

    

if __name__=="__main__":
    root=Tk()
    obj=Employeeclass(root)
    root.mainloop()         