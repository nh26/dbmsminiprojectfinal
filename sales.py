from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
import os

class salesclass:
    def __init__(self, root):
        self.root =root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")
        self.root.focus_force()
        self.bill_list=[]
        self.variable_invoice=StringVar()

        label_title=Label(self.root,text="Customer bills",font=("goudy old style",30),bg="#184a45",fg="white").pack(side=TOP,fill=X)

        label_invoice=Label(self.root,text="Invoice no",font=("times new roman",15),bg='white').place(x=50,y=100)
        txt_invoice=Entry(self.root,textvariable=self.variable_invoice,font=("times new roman",15),bg="lightyellow").place(x=160,y=100,width=180,height=28)


        btn_search=Button(self.root,text="Search",command=self.search,font=("times new roman",15,"bold"),bg="#2196f3",fg="white",cursor="hand2").place(x=360,y=100,width=120,height=28)
        btn_search=Button(self.root,text="Clear",command=self.clear,font=("times new roman",15,"bold"),bg="lightgray",cursor="hand2").place(x=500,y=100,width=120,height=28)


        sales_Frame=Frame(self.root,bd=3,relief=RIDGE)
        sales_Frame.place(x=50,y=140,width=200,height=330)

        scrolly=Scrollbar(sales_Frame,orient=VERTICAL)
        self.Sales_list=Listbox(sales_Frame,font=("goudy old style",15),bg="white",yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT,fill=Y)
        scrolly.config(command=self.Sales_list.yview)
        self.Sales_list.pack(fill=BOTH,expand=1)


         #Bill area
        bill_Frame=Frame(self.root,bd=3,relief=RIDGE)
        bill_Frame.place(x=280,y=140,width=410,height=330)

        label_title2=Label(bill_Frame,text="Customer bill area",font=("goudy old style",20),bg="orange").pack(side=TOP,fill=X)

        scrolly2=Scrollbar(bill_Frame,orient=VERTICAL)
        self.bill_area=Text(bill_Frame,bg="lightyellow",yscrollcommand=scrolly.set)
        scrolly2.pack(side=RIGHT,fill=Y) 
        scrolly2.config(command=self.bill_area.yview)
        self.bill_area.pack(fill=BOTH,expand=1)
        self.Sales_list.bind("<ButtonRelease-1>",self.get_data)
        
        #Image

        self.bill_photo=Image.open("images/bill.jpeg")
        self.bill_photo=self.bill_photo.resize((380,300),Image.LANCZOS)
        self.bill_photo=ImageTk.PhotoImage(self.bill_photo)

        self.labelimage1=Label(self.root,image=self.bill_photo,bd=0)
        self.labelimage1.place(x=700,y=110)
        self.show()
        
#--------------------------------------------------------------------------------------------------------------#
    def show(self):
        self.bill_list[:]
        self.Sales_list.delete(0,END)
        for i in os.listdir('bill'):
            if i.split(".")[-1]=='txt':
                self.Sales_list.insert(END,i)
                self.bill_list.append(i.split('.')[0])
    

    def get_data(self,ev):
        index_=self.Sales_list.curselection()
        file_name=self.Sales_list.get(index_)
        print(file_name)
        self.bill_area.delete('1.0',END)
        fp=open(f'bill/{file_name}','r')
        for i in fp:
            self.bill_area.insert(END,i)
        fp.close()

    def search(self):
        if self.variable_invoice.get()=='':
            messagebox.showerror("Error","Invoice number should be required",parent=self.root)
        else:
            if self.variable_invoice.get() in self.bill_list:
                fp=open(f'bill/{self.variable_invoice.get()}.txt','r')
                self.bill_area.delete(1.0,END)
                for i in fp:
                    self.bill_area.insert(END,i)
                fp.close()
            else:
                messagebox.showerror("Error","Invoice number invalid",parent=self.root)
    
    def clear(self):
        self.show()
        self.bill_area.delete('1.0',END)

    



            


        
if __name__=="__main__":
    root=Tk()
    obj=salesclass(root)
    root.mainloop()