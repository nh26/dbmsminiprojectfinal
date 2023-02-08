from tkinter import*
from PIL import ImageTk,Image
from tkinter import messagebox
import sqlite3
import os
import email_pass
import smtplib
import time
class login:
    def __init__(self,root):
        self.root=root
        self.root.title("LOGIN SYSTEM")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        

        self.phoneimg=ImageTk.PhotoImage(file="images/iphone.png")
        self.labelphon=Label(self.root,image=self.phoneimg,bd=0,bg="white")
        self.labelphon.place(x=180,y=50)

        self.employeeid=StringVar()
        self.password=StringVar()

        loginframe=Frame(self.root,bd=2,relief=RIDGE,bg="white")

        loginframe.place(x=650,y=90,width=350,height=460)
        
        title=Label(loginframe,text="LOGIN SYSTEM",font=("Elephant",30,"bold"),bg="white").place(x=0,y=30,relwidth=1)

        labeluser=Label(loginframe,text="Employee Id",font=("Andalus",15),bg="white",fg="#767171").place(x=50,y=100)

        textemployeeid=Entry(loginframe,textvariable=self.employeeid,font=("times new roman",15),bg="#ECECEC").place(x=50,y=140,width=250)
        labelpassword=Label(loginframe,text="Password",font=("Andalus",15),bg="white",fg="#767171").place(x=50,y=200)
        textpassword=Entry(loginframe,textvariable=self.password,font=("times new roman",15),bg="#ECECEC").place(x=50,y=240,width=250) 

        buttonlogin=Button(loginframe,command=self.login_sys,text="log in",font=("Arial Rounded MT Bold",15),bg="#00B0F0",activebackground="white",cursor="hand2").place(x=50,y=300,width=250,height=35)
        
        hr=Label(loginframe,bg="lightgray").place(x=50,y=370,width=250,height=2)
        or_=Label(loginframe,text="OR",fg="black",bg="white",font=("times new roman",15,"bold")).place(x=150,y=355)
        
        buttonforget=Button(loginframe,text="forget password",command=self.forgetwindow,cursor="hand2",font=("times new roman",13),bg="white",fg="#00759E",activebackground="white",activeforeground="white").place(x=110,y=390)
        


        self.h=ImageTk.PhotoImage(file="images/h.jpeg")
        self.img0=ImageTk.PhotoImage(file="images/img0.jpeg")
       # self.img1=ImageTk.PhotoImage(file="images/img1.jpg")

        self.img2=ImageTk.PhotoImage(file="images/img2.jpeg")
           

        self.labelchangeimage=Label(self.root,bg="white")
        self.labelchangeimage.place(x=331,y=150,width=240,height=428)

        self.animate()
       

    def animate(self):
        self.img=self.h
        self.h=self.img0
        self.img0=self.img2
      #  self.img1=self.img2
        self.img2=self.img    
        self.labelchangeimage.config(image=self.img)
        self.labelchangeimage.after(1500,self.animate)



    def login_sys(self):     
        con=sqlite3.connect(database=r'DBMS.db')
        cur=con.cursor()
        try:
            if self.employeeid.get()=="" or self.password.get()=="":
                messagebox.showerror("Error ","All Fields Are Required",parent=self.root)
            else:
                cur.execute("select utype from employee where eid=? AND password=?",(self.employeeid.get(),self.password.get()))
                user=cur.fetchone()
                if user==None:
                    messagebox.showerror("Error","Invalid username or Password",parent=self.root)
                else:
                    if user[0]=="Admin":
                        self.root.destroy()
                        os.system("python dashboard.py")
                    else:
                        self.root.destroy()
                        os.system("python billing.py")



        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)    
    def forgetwindow(self):
        con=sqlite3.connect(database=r'DBMS.db')
        cur=con.cursor()
        try:
            if self.employeeid.get()=="":
                 messagebox.showerror("Error","Employee id must be Required",parent=self.root)
            else:
                cur.execute("select email from employee where eid=?",(self.employeeid.get(),))
                email=cur.fetchone()
                if email==None:
                    messagebox.showerror("Error","Invalid employee id,try again",parent=self.root)
                else:
                   self.otp=StringVar()
                   self.newpassword=StringVar()
                   self.confirmpassword=StringVar()
                   # call sendemailfunction()
                   chk=self.sendemail(email[0])
                   if chk!='s':
                    messagebox.showerror("Error","connection error","Try Again",parent =self.root)
                   else:
                    self.forget_window=Toplevel(self.root)
                    self.forget_window.title("RESET PASSWORD")
                    self.forget_window.geometry("400x350+500+100")
                    self.forget_window.focus_force()

                    title=Label(self.forget_window,text='Reset Password',font=("goudy old style",15,"bold"),bg="#3f51b5",fg="white").pack(side=TOP,fill=X)
                    Labelreset=Label(self.forget_window,text='ENTER OTP SENT ON REGISTERED EMAIL',font=("TIMES NEW ROMAN",15)).place(x=15,y=60)
                    textreset=Entry(self.forget_window,textvariable=self.otp,font=("TIMES NEW ROMAN",15),bg="lightyellow").place(x=20,y=100,width=250,height=30)
                 
                    self.Buttonreset=Button(self.forget_window,text="SUBMIT",command=self.validate_otp,font=("TIMES NEW ROMAN",15),bg="lightblue")
                    self.Buttonreset.place(x=280,y=100,width=100,height=30)

                    Labelnewpass=Label(self.forget_window,text='NEW PASSWORD',font=("TIMES NEW ROMAN",15)).place(x=15,y=160)
                    textnewpass=Entry(self.forget_window,textvariable=self.newpassword,font=("TIMES NEW ROMAN",15),bg="lightyellow").place(x=20,y=190,width=250,height=30)
                 
                    Labelconfpass=Label(self.forget_window,text='CONFIRM PASSWORD',font=("TIMES NEW ROMAN",15)).place(x=15,y=225)
                    textconfpass=Entry(self.forget_window,textvariable=self.confirmpassword,font=("TIMES NEW ROMAN",15),bg="lightyellow").place(x=20,y=255,width=250,height=30) 

                    self.Buttonupdate=Button(self.forget_window,text="UPDATE",command=self.update_password,state=DISABLED,font=("TIMES NEW ROMAN",15),bg="lightblue")
                    self.Buttonupdate.place(x=150,y=300,width=100,height=30)
                     
                 

                

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)   

    def update_password(self):
        if self.newpassword.get()=="" or self.confirmpassword.get()=="":
            messagebox.showerror('Error','Password is required',parent=self.forget)
        elif self.newpassword.get()!=self.confirmpassword.get():   
            messagebox.showerror('Error','Password must be same',parent=self.forget_window)     
        else:
             con=sqlite3.connect(database=r'DBMS.db')
             cur=con.cursor()
             try:
                cur.execute("update employee SET password=? where eid=?",(self.newpassword.get(),self.employeeid.get()))
                con.commit()
                messagebox.showinfo("Success","Password updated Successfully",parent=self.forget_window)
                self.forget_window.destroy()
             except Exception as ex:
                messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)                 


    
    def validate_otp(self):
        if int(self._otp)==int(self.otp.get()):
            self.Buttonupdate.config(state=NORMAL)
            self.Buttonreset.config(state=DISABLED)
        else:
            messagebox.showerror('Error',"Invalid otp,try again",parent=self.forget_window)    


    def sendemail(self,to_):
        s=smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        email_=email_pass.email_
        pass_=email_pass.pass_

        s.login(email_,pass_)

        self._otp=int(time.strftime("%H%M%S"))+int(time.strftime("%S"))

        subj="IMS-Reset Password OTP"
        msg=f"Your Reset Otp is {str(self._otp)}.\n\n with regards,\n IMS Team"
        msg="Subject:{}\n\n{}".format(subj,msg)
        s.sendmail(email_,to_,msg)
        chk=s.ehlo()
        if chk[0]==250:
            return 's'
        else:
            return 'f'    

root=Tk()
ob=login(root)
root.mainloop()