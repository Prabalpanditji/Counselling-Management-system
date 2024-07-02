from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import webbrowser




win=Tk()
win.geometry("900x700")
win.title("Councling Management System")



def register():
    def click_register():
        id=entry_id.get()
        name=entry_name.get()
        email=entry_email.get()
        psw=entry_password.get()
        contact=entry_contact.get()

        if (id=="" or psw=="" or name=="" or email=="" or contact==""):
            MessageBox.showinfo("Alert","Enter all Credentials")
        else:
            con=mysql.connect(host="localhost",user="root",password="Prabal@123",database="pro")
            cursor=con.cursor()
            cursor.execute("insert into new_table values('"+id+"','"+name+"','"+email+"','"+contact+"','"+psw+"')")
            cursor.execute("commit")

            MessageBox.showinfo("Alert","Registration completed Successfully")
            con.close()
            login()

    f1=Frame(bg="#0096DC")
    f1.place(x=0,y=0,height=500,width=500)

    l1=Label(f1,text="User Id:",font=("Verdena 15"),fg="white",bg="#0096DC")
    l2=Label(f1,text="Name:",font=("Verdena 15"),fg="white",bg="#0096DC")
    l3=Label(f1,text="Email",font=("Verdena 15"),fg="white",bg="#0096DC")
    l4=Label(f1,text="Contact",font=("Verdena 15"),fg="white",bg="#0096DC")
    l5=Label(f1,text="Password:",font=("Verdena 15"),fg="white",bg="#0096DC")

    l1.place(x=100,y=100)
    l2.place(x=100,y=150)
    l3.place(x=100,y=200)
    l4.place(x=100,y=250)
    l5.place(x=100,y=300)

    entry_id=Entry(f1,font=("Verdena 15"))
    entry_name=Entry(f1,font=("Verdena 15"))
    entry_email=Entry(f1,font=("Verdena 15"))
    entry_contact=Entry(f1,font=("Verdena 15"))
    entry_password=Entry(f1,show="*",font=("Verdena 15"))
    
    entry_id.place(x=200,y=100)
    entry_name.place(x=200,y=150)
    entry_email.place(x=200,y=200)
    entry_password.place(x=200,y=300)
    entry_contact.place(x=200,y=250)

    b1=Button(f1,text="Register",font=("Verdena 15"),fg="white",bg="grey",command=click_register)
    b2=Button(f1,text="LogIn",font=("Verdena 15"),fg="white",bg="grey",command=login)
    b1.place(x=150,y=400)
    b2.place(x=250,y=400)
    
   
def login():
    def click_login(id,email,psw):
        
        con=mysql.connect(host="localhost",user="root",password="Prabal@123",database="pro",auth_plugin='mysql_native_password')
        cursor=con.cursor()
        cursor.execute("SELECT Userid FROM new_table")
        database_id=cursor.fetchall()
        cursor.execute("SELECT Email FROM new_table")
        database_email=cursor.fetchall()
        cursor.execute("SELECT Password FROM new_table")
        database_psw=cursor.fetchall()
        
        var1=0
        var2=0
        var3=0
        
        
        for userid in database_id:
               uid=userid[0]
               u=str(uid)
               if(u==id):
                   var1=1    
        for useremail in database_email:
               uml=useremail[0]
               if(uml==email):
                   var2=1    
        for userpsw in database_psw:
               upw=userpsw[0]
               
               if(upw==psw):
                   var3=1    
       
        if (id=="" or psw=="" or email==""):
            MessageBox.showinfo("Alert","Enter all Credentials")
        elif(var1==1 and var2==1 and var3==1):
            MessageBox.showinfo("Alert","Login completed Successfully")
            
            root=Frame(bg="aqua")
            root.place(x=0,y=0,height=500,width=500)
            
            
            
            
            
            # root.geometry("655x333")
            frame=Frame(root,borderwidth=6,bg="grey",relief=SUNKEN)
            frame.pack(side=LEFT,anchor="nw")
            
            def carrer():
                def open_link(event):
                    # l1=Label(text="B.tech",font=("Verdena 15"),fg="white",bg="#0096DC")
                    # l1.place(x=100,y=100)
                    
                    
                    webbrowser.open(url)
                    #webbrowser.place(x=200,y=100)
                f1=Frame(bg="blue")
                f1.place(x=0,y=0,height=500,width=500)
                
                links=[("http://amazon.com"),("http://google.com"),("http://shiksha.com")]
                
                for url in links:
                    l1=Label(f1,text="Google",cursor="hand2")
                    l1.place(x=250,y=250)
                    l1.bind("<Button-1>",lambda e,url=url: open_link(url))
                    l2=Label(f1,text="Amazon",cursor="hand2")
                    l2.place(x=250,y=300)
                    l2.bind("<Button-1>",lambda e,url=url: open_link(url))
                    l3=Label(f1,text="sHIKSHA",cursor="hand2")
                    l3.place(x=250,y=350)
                    l3.bind("<Button-1>",lambda e,url=url: open_link(url))
                
                l2.bind("<Button-1>",open_link)
            def bio():
                def open_link(event):
                    # l1=Label(text="B.tech",font=("Verdena 15"),fg="white",bg="#0096DC")
                    # l1.place(x=100,y=100)
                    
                    
                    webbrowser.open("http:")
                    #webbrowser.place(x=200,y=100)
                f1=Frame(bg="blue")
                f1.place(x=0,y=0,height=500,width=500)
                
                l1=Label(f1,text="Click Here To open link",cursor="hand2")
                l1.place(x=250,y=250)
                l1.bind("<Button-1>",lambda e,url=url:open_link(url))
            
            def comm():
                def open_link(event):
                    # l1=Label(text="B.tech",font=("Verdena 15"),fg="white",bg="#0096DC")
                    # l1.place(x=100,y=100)
                    
                    
                    webbrowser.open("http:")
                    #webbrowser.place(x=200,y=100)
                f1=Frame(bg="blue")
                f1.place(x=0,y=0,height=500,width=500)
                
                l1=Label(f1,text="Click Here To open link",cursor="hand2")
                l1.place(x=250,y=250)
                l1.bind("<Button-1>",open_link)
            
                
            def art():
                def open_link(event):
                    # l1=Label(text="B.tech",font=("Verdena 15"),fg="white",bg="#0096DC")
                    # l1.place(x=100,y=100)
                    
                    
                    webbrowser.open("")
                    #webbrowser.place(x=200,y=100)
                f1=Frame(bg="aqua")
                f1.place(x=0,y=0,height=500,width=500)
                
                l1=Label(f1,text="Click Here To open link",cursor="hand2")
                l1.place(x=250,y=250)
                l1.bind("<Button-1>",open_link)
            
                
                
                
            b1=Button(frame,fg="red",text="Career in Maths",command=carrer)
            b1.pack(side=LEFT)
            b2=Button(frame,fg="red",text="Career in Biology",command=bio)
            b2.pack(side=LEFT)
            b3=Button(frame,fg="red",text="Career in  Commerce",command=comm)
            b3.pack(side=LEFT)
            b4=Button(frame,fg="red",text="Career in  Arts",command=art)
            b4.pack(side=LEFT)
        
        
            
            
           
           

    
            # #Text for form
            # Name = Label(root,text="Name:",font="comicsansms 15")
            # phone= Label(root,text="Phone:",font="comicsansms 15")
            # mail= Label(root,text="E-mail:",font="comicsansms 15")

            # #Pack text for form
            # Name.place(x=100,y=200)
            # phone.place(x=100,y=250)
            # mail.place(x=100,y=300)

            # #Tkinter variable for  storing entries
            # # namevalue = StringVar()
            # # phonevalue= StringVar()
            # # mailvalue= StringVar()

            # #Entries for form
            # Nameentry = Entry(root,font="comicsansms 15")
            # phoneentry = Entry(root,font="comicsansms 15")
            # mailentry = Entry(root,font="comicsansms 15")

            # #Packing the entries
            # Nameentry.place(x=250,y=200)
            # phoneentry.place(x=250,y=250)
            # mailentry.place(x=250,y=300)



            # #Button&packing it and asssigning it a command
            # b=Button(root,text="Submit",font="comicsansms 15")
            # b.place(x=200,y=400)
                        
                        
                        
         
        else:
            MessageBox.showinfo("Alert","There is error")
        
    f1=Frame(bg="#B1DDC6")
    f1.place(x=0,y=0,height=500,width=500)
    
    label_head=Label(f1,text="Fill credentials To Login",font=("Verdena 25"),fg="white",bg="#B1DDC6")
    label_head.place(x=80,y=10)
    
    
    l1=Label(f1,text="User Id:",font=("Verdena 15"),fg="white",bg="#B1DDC6")
    l2=Label(f1,text="Email",font=("Verdena 15"),fg="white",bg="#B1DDC6")
    l3=Label(f1,text="password",font=("Verdena 15"),fg="white",bg="#B1DDC6")
    
    l1.place(x=100,y=100)
    l2.place(x=100,y=150)
    l3.place(x=100,y=200)
    
    entry_id=Entry(f1,font=("Verdena 15"))
    entry_email=Entry(f1,font=("Verdena 15"))
    entry_password=Entry(f1,font=("Verdena 15"),show="*")

    entry_id.place(x=200,y=100)
    entry_email.place(x=200,y=150)
    entry_password.place(x=200,y=200)
    
    b1=Button(f1,text="LogIn",font=("Verdena 15"),fg="white",bg="grey",command=lambda:click_login(entry_id.get(),entry_email.get(),entry_password.get()))
    b2=Button(f1,text="Register",font=("Verdena 15"),fg="white",bg="grey",command=register)
    b1.place(x=150,y=400)
    b2.place(x=250,y=400)


register()
win.mainloop()