import os
import tkinter as tk
from tkinter import messagebox
username = "h"
password = "h"
adminUser = "Lance"
adminPassword = "b"
def login():
    enteredUser = entUsername.get()
    enteredPassword = entPassword.get()
    if(enteredPassword == adminPassword and enteredUser == adminUser):
        messagebox.showinfo("Admin Login Success",f"      Welcome {adminUser}     ")
        loginwindow.destroy()
        mainMenuWindow()
    elif(enteredPassword == password and enteredUser == username):
        messagebox.showinfo("User Login Success","      Welcome      ")
        loginwindow.destroy()
        mainMenuWindow()
    else:
        messagebox.showinfo("User Login Fail","Please Enter a Correct Username and Password")

def exit():
    messagebox.showinfo("Exit","Thank you for using the application")
    quit()
#Main Menu
def mainMenuWindow():
    mmWindow = tk.Tk()
    mmWindow.title("Main Menu")
    mmWindow.geometry("300x200")
    mmWindow.config(bg="#2f4233") 
    mmWindow.mainloop()

#LOGIN WINDOW
loginwindow = tk.Tk()
loginwindow.title("Login")
loginwindow.geometry("750x375")
loginwindow.resizable(width=False,height=False)

Body = tk.Frame(loginwindow,bg='#536878',height=375,width=750)
Body.grid(row=0,column=0)

lblUsername = tk.Label(Body,text="Username")
lblUsername.config(font=("Times New Roman",24))
lblUsername.place(x=50,y=100)

entUsername = tk.Entry(Body)
entUsername.config(font=("Times New Roman", 20))
entUsername.place(x=50,y=150,width=200,height=60)

lblPassword = tk.Label(Body,text="Password")
lblPassword.config(font=("Times New Roman",24))
lblPassword.place(x=50,y=230)

entPassword = tk.Entry(Body)
entPassword.config(font=("Times New Roman", 20))
entPassword.place(x=50,y=280,width=200,height=60)

loginTitle = tk.Label(Body, text = "Login")
loginTitle.config(font=("Times New Roman",50))
loginTitle.place(x=290,y=30)

btnLogin = tk.Button(Body,text="Login",command=lambda:[login()],width=10)
btnLogin.place(x=500,y=125)
btnLogin.config(font=("Times New Roman", 30))

btnExit = tk.Button(Body,text="Exit",command=exit,width=10)
btnExit.place(x=500,y=250)
btnExit.config(font=("Times New Roman", 30))

loginwindow.mainloop()