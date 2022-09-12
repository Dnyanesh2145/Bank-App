#imports
from tkinter import *
import tkinter as tk

from tkinter import messagebox
import smtplib
from pymysql import *
from PIL import ImageTk, Image
import math,random

#main screen
root=Tk()
root.title("Banking App")
root.geometry("1199x688+100+58")
root.resizable(False,False)

#Background Image
bg =Image.open("C:\\Users\\Admin\\Downloads\\Telegram Dekstop\\background.jpg")
bg= bg.resize((1199,688))
bg=ImageTk.PhotoImage(bg)

Label(root ,image=bg).place(x=0,y=0,relwidth=1,relheight=1)
#icon
ico = Image.open("C:\\Users\\Admin\\Downloads\\Telegram Dekstop\\imageicon2.png")
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False,photo)


#Frame
frame_1=Frame(root,bg="White")
frame_1.place(x=338 , y=150,width=500,height=400)

#image Import
img = Image.open("C:\\Users\\Admin\\Downloads\\Telegram Dekstop\\bankingapp.png")
img = img.resize((200,200))
img = ImageTk.PhotoImage(img)



                               #Register page



#Functions

def register():

    register_screen= Toplevel(root)
    register_screen.title("Registration")
    register_screen.geometry("400x400+338+150")
    register_screen.resizable(False,False)

    
    

   

    #icon
    ico_1 = Image.open("C:\\Users\\Admin\\Downloads\\Telegram Dekstop\\imageicon2.png")
    photo = ImageTk.PhotoImage(ico_1)
    register_screen.wm_iconphoto(False,photo)
    #Labels
    Label(register_screen,text ="Register Here" ,font =("Impact",15),fg="green").place(x= 150,y=1)
    Label(register_screen,text="Name",font=("calibri",12,"bold"),fg="grey").place(x=100,y=25)
    Label(register_screen,text="D.O.B",font=("calibri",12,"bold"),fg="grey").place(x=100,y=75)
    Label(register_screen,text="Bank A/c No.",font=("calibri",12,"bold"),fg="grey").place(x=100,y=125)
    Label(register_screen,text="Email Id",font=("calibri",12,"bold"),fg="grey").place(x=100,y=175)
    Label(register_screen,text="New Password",font=("calibri",12,"bold"),fg="grey").place(x=100,y=225)
    Label(register_screen,text="Confirm password",font=("calibri",12,"bold"),fg="grey").place(x=100,y=275)

    #variable
    global Name
    global Date
    global Emailid
    global AccountNo
    global Password1
    global Password2
    global data
    global OTP
    

   
        

    #Entries
    Name= Entry(register_screen,bg="#E7E6E6")
    Name.place(x=100,y=50,width=200)
    Date= Entry(register_screen,bg="#E7E6E6",width=200)
    Date.place(x=100,y=100,width=200)
    AccountNo= Entry(register_screen,bg="#E7E6E6")
    AccountNo.place(x=100,y=150,width=200)
    Emailid= Entry(register_screen,bg="#E7E6E6")
    Emailid.place(x=100,y=200,width=200)
    Password1= Entry(register_screen,bg="#E7E6E6",show="*")
    Password1.place(x=100,y=250,width=200)
    Password2= Entry(register_screen,bg="#E7E6E6",show="*")
    Password2.place(x=100,y=300,width=200)


    

    

    def submit():
        if Name.get()==""or Date.get()==""or AccountNo.get()=="" or Emailid.get()==""or Password1.get()==""or Password2.get()=="":
            messagebox.showerror("Error","All fields are mandatory.")
            
            return
        elif len(AccountNo.get())!= 14 :
           messagebox.showerror("Error","Please Enter valid 14 digit bank account number.")
        elif len(Password1.get())<8:
            messagebox.showerror("Error","Passord should be between 8 to 10 character.")
        elif len(Password1.get())>16:
            messagebox.showerror("Error","Password should be between 8 to character.")

        elif Password1.get()!=Password2.get():
            messagebox.showerror("Error","Password not matched.")

        else:
            #SQL DATABASE
            conn = connect(host="localhost",
                           user='root',
                           password='123456789',
                           db='Bankdb')
            cr = conn.cursor()
            query=("Select * from customer_info where EmailId=%s")
            value=(Emailid.get(),)
            cr.execute(query,value)
            row=cr.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist,Please try another email.")
            else:
                cr.execute(''' insert into customer_info values ("{}" ,"{}","{}", '{}','{}',0);'''.format(Name.get(),Date.get(),AccountNo.get(),Emailid.get(),Password1.get()))
                dt=cr.execute('select * from customer_info;')
                for data in cr:
                     print(data)
                conn.commit()
                conn.close()

                
                messagebox.showinfo("info","Registered Succesfully.Email has been sent to your registered mail Id.")
                # creates SMTP session
                s = smtplib.SMTP('smtp.gmail.com', 587)
                  
                # start TLS for security
                s.starttls()
                  
                # Authentication Your Email Address That You Used IN Solution 1
                s.login("dnyaneshrode07@gmail.com ", "wzftltytrsonnvlp")

                subject = "Rgistered Sucesfully"
                text='''Dear {},

    Thank your for registration to our Customer Banking App.We wish to have a great experience with us.
    Now,you can login to your account with the registered email Id. '''.format(Name.get())
                  
                # message to be sent
                message = "subject : {}\n\n{}".format(subject,text)


                  
                # sending the mail
                s.sendmail("dnyaneshrode07@gmail.com ", Emailid.get(), message)
                print("Email has been sent")
                  
                # terminating the session
                s.quit()

                #Screen destroy

                register_screen.destroy()

                


    #Button
    Button(register_screen,text ='Submit',font=('Calibri',12),width=8,bg="#6162FF",fg="white",command=submit).place(x=155,y=350)

         #OTP verification page

def OTP():
    verify_screen= Toplevel(root)
    verify_screen.title("Verification")
    verify_screen.geometry("400x400+338+150")
    verify_screen.resizable(False,False)

    #icon
    ico_2 = Image.open("C:\\Users\\Admin\\Downloads\\Telegram Dekstop\\imageicon2.png")
    photo = ImageTk.PhotoImage(ico_2)
    verify_screen.wm_iconphoto(False,photo)

    #Label
    Label(verify_screen,text ="OTP" ,font =("calibri",12),fg="black").place(x=50,y=160)
    Label(verify_screen,text ="Email Id",font =("calibri",12),fg="black").place(x=50,y=80)

    #Entries
    
    verify1= Entry(verify_screen,bg="#E7E6E6")
    verify1.place(x=50,y=200,width=80)
    Emailid2= Entry(verify_screen,bg="#E7E6E6")
    Emailid2.place(x=50,y=120,width=200)

    def send():
        if Emailid2.get()=="":
            messagebox.showerror("Error","Please enter registered Email Id.")
        else:
            conn = connect(host="localhost",
                                   user='root',
                                   password='123456789',
                                   db='Bankdb')
            cr = conn.cursor()
            cr.execute("select * from customer_info where EmailId=%s ;",(Emailid2.get()))
            check=cr.fetchone()
            if check==None:
                messagebox.showerror("Error","Username does not exist.")
            else:
                global generateOTP
                global E
                E=Emailid2.get()
                #OTP generator
                digits='0123456789'
                OTP=""
                for i in range(4):
                    OTP+=digits[math.floor(random.random()*10)]
                    generateOTP=OTP
                print(generateOTP)
                # creates SMTP session
                s = smtplib.SMTP('smtp.gmail.com', 587)
                  
                # start TLS for security
                s.starttls()
                  
                # Authentication Your Email Address That You Used IN Solution 1
                s.login("dnyaneshrode07@gmail.com ", "wzftltytrsonnvlp")

                subject = "OTP"
                text='''Dear customer ,

Please use OTP {} for password change request. '''.format(generateOTP)
                  
                # message to be sent
                message = "subject : {}\n\n{}".format(subject,text)


                  
                # sending the mail
                s.sendmail("dnyaneshrode07@gmail.com ", E , message)
                print("Email has been sent")
                  
                # terminating the session
                s.quit()
                Label(verify_screen,text ="OTP has been sent to your registered email id." ,font =('calibri',12),fg="green").place(x=1,y=1)

    def verify():
        v_1=verify1.get()
        if verify1.get()=="":
            messagebox.showerror("Error","Please enter OTP ")
        elif v_1 != generateOTP:
            messagebox.showerror("Error","Invalid OTP")
        else:
            messagebox.showinfo("Info","OTP verified")
            verify_screen.destroy()
            #password change screen
            password_screen=Toplevel(root)
            password_screen.title("Password Change")
            password_screen.geometry("400x400+338+150")
            password_screen.resizable(False,False)

            #icon
            ico_2 = Image.open("C:\\Users\\Admin\\Downloads\\Telegram Dekstop\\imageicon2.png")
            photo = ImageTk.PhotoImage(ico_2)
            password_screen.wm_iconphoto(False,photo)

            #Label
            Label(password_screen,text ="Password Change" ,font =("Impact",15),fg="green").place(x=120,y=2)
            Label(password_screen,text="New Password",font=("calibri",12,"bold"),fg="black").place(x=100,y=80)
            Label(password_screen,text="Confirm password",font=("calibri",12,"bold"),fg="black").place(x=100,y=150)

            #Entries
            Password1= Entry(password_screen,bg="#E7E6E6",show="*")
            Password1.place(x=80,y=120,width=200)
            Password2= Entry(password_screen,bg="#E7E6E6",show="*")
            Password2.place(x=80,y=190,width=200)

            def update():
                if Password1.get()=="" or Password2.get()=="":
                    messagebox.showerror("Error","All fields are mandatory.")
                elif len(Password1.get())<8:
                    messagebox.showerror("Error","Passord should be between 8 to 10 character.")
                elif len(Password1.get())>16:
                    messagebox.showerror("Error","Passord should be between 8 to 10 character.")
                elif Password1.get()!=Password2.get():
                    messagebox.showerror("Error","Password not matched.")
                else:
                    p=Password1.get()
                    
                    conn = connect(host="localhost",
                                           user='root',
                                           password='123456789',
                                           db='Bankdb')
                    c= conn.cursor()

                    dt=c.execute('update customer_info set Password1="{}" where EmailId="{}";'.format(p,E))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Info","Password updated succesfully")
                    password_screen.destroy()
                            
            #Button
            Button(password_screen,text ='update',font=('Calibri',12),width=8,bg="#6162FF",fg="white",command=update).place(x=135,y=300)
    

                

            

            

            
            



    Button(verify_screen,text ='send OTP',font=('Calibri',12),width=8,bg="#6162FF",fg="white",command=send).place(x=155,y=250)
    Button(verify_screen,text ='verify',font=('Calibri',12),width=8,bg="#6162FF",fg="white",command=verify).place(x=80,y=250)

    



                                           #Login page 


def Login_session():
    #register screen
    register_screen2= Toplevel(root)
    register_screen2.title("Login")
    register_screen2.geometry("400x400+338+150")
    register_screen2.resizable(False,False)

    

   
    
    #icon
    ico_2 = Image.open("C:\\Users\\Admin\\Downloads\\Telegram Dekstop\\imageicon2.png")
    photo = ImageTk.PhotoImage(ico_2)
    register_screen2.wm_iconphoto(False,photo)

    #Labels
    Label(register_screen2,text ="LOGIN " ,font =("Impact",15),fg="green").place(x= 160,y=30)
    Label(register_screen2,text="USERNAME",font=("calibri",12,"bold"),fg="grey").place(x=100,y=100)
    Label(register_screen2,text="PASSWORD",font=("calibri",12,"bold"),fg="grey").place(x=100,y=170)


    #Entries
    Emailid= Entry(register_screen2,bg="#E7E6E6")
    Emailid.place(x=100,y=130,width=180)
    Password1= Entry(register_screen2,bg="#E7E6E6",show="*")
    Password1.place(x=100,y=200,width=180)

    
    
    def login():
        
        if Emailid.get()==""or Password1.get()=="":
            messagebox.showerror("Error","All fields are mandatory.")
        else:
            conn = connect(host="localhost",
                                   user='root',
                                   password='123456789',
                                   db='Bankdb')
            cr = conn.cursor()
            cr.execute("select * from customer_info where EmailId=%s and Password1=%s",(Emailid.get(),Password1.get()))
            check=cr.fetchone()
            if check==None:
                messagebox.showerror("Error","Invalid Username & Password.")
                Button(register_screen2,text ="Forgot Password?.",font=('Calibri',12),bd=0,width=45,fg="blue",command=OTP).place(x=2,y=330)

            else:
                global v
                v=Emailid.get()
                messagebox.showinfo("Info","Login Successfully.")
                register_screen2.destroy()

                def account():
            
                    #account new screen
                    account_dashboard=Toplevel(root)
                    account_dashboard.title("Dashboard")
                    account_dashboard.geometry("400x400+338+150")
                    conn = connect(host="localhost",
                                       user='root',
                                       password='123456789',
                                       db='Bankdb')
                    c= conn.cursor()

                    dt=c.execute('select FullName from customer_info where EmailId="{}";'.format(v))
                    
                    for data in c:
                        
                          print(data[0])

                    #icon
                    ico_2 = Image.open("C:\\Users\\Admin\\Downloads\\Telegram Dekstop\\imageicon2.png")
                    photo = ImageTk.PhotoImage(ico_2)
                    account_dashboard.wm_iconphoto(False,photo)


                    #Labels
                    Label(account_dashboard,text ="Account Dashboard" ,font =("Impact",20),fg="green").place(x=80,y=30)
                    Label(account_dashboard,text =("Welcome" , data[0]),font =("Impact",15),fg="black").place(x=100,y=90)

                    #Buttons
                    Button(account_dashboard,text ="Personal details",font=('Calibri',12),width=30,bg="#6162FF",fg="white",command=personal_details).place(x=80,y=200)
                    Button(account_dashboard,text ="Deposit",font=('Calibri',12),width=30,bg="#6162FF",fg="white",command=deposit).place(x=80,y=250)
                    Button(account_dashboard,text ="Withdraw",font=('Calibri',12),width=30,bg="#6162FF",fg="white",command=withdraw).place(x=80,y=300)
                    Button(account_dashboard,text ="Log out",font=('Calibri',12),width=10,bd=0,fg="black",command=Login_session).place(x=300,y=1)

                    
                    conn.commit()
                account()
                    
                
            conn.commit()
            conn.close()

        
                    


    

    #Button
    Button(register_screen2,text ="Login",font=('Calibri',12),width=8,bg="#6162FF",fg="white",command=login).place(x=150,y=250)
    Button(register_screen2,text ="Don't have an account?Register.",font=('Calibri',12),bd=0,width=50,fg="blue",command=register).place(x=1,y=300)



                         #personal screen
    
def personal_details():
    #screen
    personal_screen=Toplevel(root)
    personal_screen.title("Personal details")
    personal_screen.geometry("400x400+338+150")

    #iconimg
    ico_2 = Image.open("C:\\Users\\Admin\\Downloads\\Telegram Dekstop\\imageicon2.png")
    photo = ImageTk.PhotoImage(ico_2)
    personal_screen.wm_iconphoto(False,photo)
    def account():
            
        #account new screen
        account_dashboard=Toplevel(root)
        account_dashboard.title("Dashboard")
        account_dashboard.geometry("400x400+338+150")
        conn = connect(host="localhost",
                           user='root',
                           password='123456789',
                           db='Bankdb')
        c= conn.cursor()

        dt=c.execute('select FullName from customer_info where EmailId="{}";'.format(v))
        
        for data in c:
            
              print(data[0])

        #icon
        ico_2 = Image.open("C:\\Users\\Admin\\Downloads\\Telegram Dekstop\\imageicon2.png")
        photo = ImageTk.PhotoImage(ico_2)
        account_dashboard.wm_iconphoto(False,photo)


        #Labels
        Label(account_dashboard,text ="Account Dashboard" ,font =("Impact",20),fg="green").place(x=80,y=30)
        Label(account_dashboard,text =("Welcome" , data[0]),font =("Impact",15),fg="black").place(x=100,y=90)

        #Buttons
        Button(account_dashboard,text ="Personal details",font=('Calibri',12),width=30,bg="#6162FF",fg="white",command=personal_details).place(x=80,y=200)
        Button(account_dashboard,text ="Deposit",font=('Calibri',12),width=30,bg="#6162FF",fg="white",command=deposit).place(x=80,y=250)
        Button(account_dashboard,text ="Withdraw",font=('Calibri',12),width=30,bg="#6162FF",fg="white",command=withdraw).place(x=80,y=300)
        Button(account_dashboard,text ="Log out",font=('Calibri',12),width=10,bd=0,fg="black",command=Login_session).place(x=300,y=1)

        conn.commit()
    
        

    #Label
    Label(personal_screen,text ="Personal Details " ,font =("Impact",20),fg="green").place(x=80,y=20)


    

    #database connection
    conn = connect(host="localhost",
                                   user='root',
                                   password='123456789',
                                   db='Bankdb')
    c= conn.cursor()

    dt=c.execute('select FullName,DOB,BankNo,EmailId,Balance from customer_info where EmailId="{}";'.format(v))
    for data in c:
        Label(personal_screen,text=('FullName :' , data[0]),font=("calibri",12),fg="grey").place(x=20,y=70)
        Label(personal_screen,text=('DOB :' , data[1]),font=("calibri",12),fg="grey").place(x=20,y=110)
        Label(personal_screen,text=('Bank A/c No :' , data[2]),font=("calibri",12),fg="grey").place(x=20,y=150)
        Label(personal_screen,text=('Email Id:' , data[3]),font=("calibri",12),fg="grey").place(x=20,y=190)
        Label(personal_screen,text=('Balance '':' ,float(data[4])),font=("calibri",12),fg="grey").place(x=20,y=230)
    conn.commit()
    conn.close()
    Button(personal_screen,text ="Confirm",font=('Calibri',12),width=8,bg="#6162FF",fg="white",command=account).place(x=150,y=300)
def deposit():
    #var
    global current_balance
    global amount
    #screen
    deposit_screen=Toplevel(root)
    deposit_screen.title("Deposit")
    deposit_screen.geometry("400x400+338+150")

    #iconimg
    ico_2 = Image.open("C:\\Users\\Admin\\Downloads\\Telegram Dekstop\\imageicon2.png")
    photo = ImageTk.PhotoImage(ico_2)
    deposit_screen.wm_iconphoto(False,photo)

    #balance extraction

    conn = connect(host="localhost",
                                       user='root',
                                       password='123456789',
                                       db='Bankdb')
    c= conn.cursor()

    dt=c.execute('select Balance from customer_info where EmailId="{}";'.format(v))
                    
    for data in c:
        current_balance=Label(deposit_screen,text =('Current balance',':',float(data[0])) ,font =12,fg="green")
        current_balance.place(x=80,y=80)
    conn.commit()
    conn.close()

    #Label
    Label(deposit_screen,text =" Deposit " ,font =("Impact",20),fg="green").place(x=100,y=20)
    Label(deposit_screen,text =" Amount " ,font =("Impact",12),fg="grey").place(x=80,y=120)

    amount=IntVar()

    #Entries
    amount= Entry(deposit_screen,bg="#E7E6E6")
    amount.place(x=80,y=150,width=180)
    

    def summ():
        if  float(amount.get())<=0:
            messagebox.showerror("Error","Invalid amount.")
        else:
            s1=float(amount.get())+ float(data[0])
            print(s1)
            conn = connect(host="localhost",
                                           user='root',
                                           password='123456789',
                                           db='Bankdb')
            c= conn.cursor()

            dt=c.execute('update customer_info set Balance={} where EmailId="{}";'.format(s1,v))
            conn.commit()
            conn.close()
            #Label
            messagebox.showinfo('info',"Transaction Successful")

            #mail
            # creates SMTP session
            s = smtplib.SMTP('smtp.gmail.com', 587)
                  
            # start TLS for security
            s.starttls()
              
            # Authentication Your Email Address That You Used IN Solution 1
            s.login("dnyaneshrode07@gmail.com ", "wzftltytrsonnvlp")

            subject = "Transaction sucessful"
            text='''Dear customer,

We would like to inform you that amount of Rs.{} is credited to your bank account. your net available balance is Rs.{}'''.format(amount.get(),s1)
              
            # message to be sent
            message = "subject : {}\n\n{}".format(subject,text)


              
            # sending the mail
            s.sendmail("dnyaneshrode07@gmail.com ", v , message)
            print("Email has been sent")
              
            # terminating the session
            s.quit()

            deposit_screen.destroy()

            

                    
    
    Button(deposit_screen,text ="Deposit",font=('Calibri',12),width=8,bg="#6162FF",fg="white",command=summ).place(x=150,y=250)
    
def withdraw():
    #screen
    withdraw_screen=Toplevel(root)
    withdraw_screen.title("Withdraw")
    withdraw_screen.geometry("400x400+338+150")

    #iconimg
    ico_2 = Image.open("C:\\Users\\Admin\\Downloads\\Telegram Dekstop\\imageicon2.png")
    photo = ImageTk.PhotoImage(ico_2)
    withdraw_screen.wm_iconphoto(False,photo)

    #balance extraction

    conn = connect(host="localhost",
                                       user='root',
                                       password='123456789',
                                       db='Bankdb')
    c= conn.cursor()

    dt=c.execute('select Balance from customer_info where EmailId="{}";'.format(v))
                    
    for data in c:
        current_balance=Label(withdraw_screen,text =('Current balance',':',float(data[0])) ,font =12,fg="green")
        current_balance.place(x=80,y=80)
    conn.commit()
    conn.close()

    #Label
    Label(withdraw_screen,text =" Deposit " ,font =("Impact",20),fg="green").place(x=100,y=20)
    Label(withdraw_screen,text =" Amount " ,font =("Impact",12),fg="grey").place(x=80,y=120)

    amount=IntVar()

    #Entries
    amount= Entry(withdraw_screen,bg="#E7E6E6")
    amount.place(x=80,y=150,width=180)
    

    def sub():
        if  float(amount.get())<=0:
            messagebox.showerror("Error","Invalid amount.")
        else:
            s2= float(data[0])- float(amount.get())
            print(s2)
            conn = connect(host="localhost",
                                           user='root',
                                           password='123456789',
                                           db='Bankdb')
            c= conn.cursor()

            dt=c.execute('update customer_info set Balance={} where EmailId="{}";'.format(s2,v))
            conn.commit()
            conn.close()
            #Label
            messagebox.showinfo('info',"Transaction Successful")

            #mail
            # creates SMTP session
            s = smtplib.SMTP('smtp.gmail.com', 587)
                  
            # start TLS for security
            s.starttls()
              
            # Authentication Your Email Address That You Used IN Solution 1
            s.login("dnyaneshrode07@gmail.com ", "wzftltytrsonnvlp")

            subject = "Transaction sucessful"
            text='''Dear customer,

We would like to inform you that amount of Rs.{} is debited from your bank account. your net available balance is Rs.{}'''.format(amount.get(),s2)
              
            # message to be sent
            message = "subject : {}\n\n{}".format(subject,text)


              
            # sending the mail
            s.sendmail("dnyaneshrode07@gmail.com ", v , message)
            print("Email has been sent")
              
            # terminating the session
            s.quit()

            withdraw_screen.destroy()

            

                    
    
    Button(withdraw_screen,text ="withdraw",font=('Calibri',12),width=8,bg="#6162FF",fg="white",command=sub).place(x=150,y=250)
    
    

#Labels
Label(frame_1,image=img,bd=0).place(x=150,y=50)
Label(frame_1,text ="CUSTOM BANKING APP " ,font =("Impact",15),bg="white").place(x= 160,y=30)

#Buttons
Button(frame_1,text ='Register',font=('Goudy old style',13),width=8,command = register, bg = "#6162FF",fg="white").place(x=220,y=250)
Button(frame_1,text ='Login',font=('Calibri',12),width=8,bg="#6162FF",fg="white",command=Login_session).place(x=220,y=300)







root.mainloop()
