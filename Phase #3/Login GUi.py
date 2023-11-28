import os
import tkinter as tk
from tkinter import messagebox
import csv

def login():
    enteredUser = entUsername.get()
    enteredPassword = entPassword.get()
    csvfile=open("users.csv","r")
    reader = csv.reader(csvfile)
    for row in reader:
        if row[1] == enteredUser and row[2] == enteredPassword:
           success = True
           break
        else:
           success = False
    if(success and row[0]=='1'):
        messagebox.showinfo("Admin Login Success",f"      Welcome {enteredUser}     ")
        loginwindow.destroy()
        adminMenu()
    elif(success and row[0]!='1'):
        messagebox.showinfo("User Login Success",f"      Welcome {enteredUser}     ")
        loginwindow.destroy()
        mainMenuWindow()
    else:
        messagebox.showinfo("User Login Fail","Please Enter a Correct Username and Password")

#Function to Exit the Program With Message
def exit():
    messagebox.showinfo("Exit","Thank you for using the application")
    quit()

#Main Menu Window
def mainMenuWindow():
    #Main Menu Below
    mainWindow = tk.Tk()
    mainWindow.title("Main Menu")
    mainWindow.geometry("1500x750")
    mainWindow.resizable(width=False,height=False)

    mainBody = tk.Frame(mainWindow,bg='#536878',height=750,width=1500)
    mainBody.grid(row=0,column=0)

    lblMainTitle = tk.Label(mainBody,text="Main Menu")
    lblMainTitle.config(font=("Times New Roman",40))
    lblMainTitle.place(x=630,y=50)

    btnExit = tk.Button(mainBody,text="Exit",command=exit,width=10)
    btnExit.place(x=635, y=650)
    btnExit.config(font=("Times New Roman", 28))

    btnAdd = tk.Button(mainBody,text="Add",command=addTaskWin,width=11)
    btnAdd.place(x=175, y=550)
    btnAdd.config(font=("Times New Roman", 28))

    btnRemove = tk.Button(mainBody,text="Remove",command=removeTaskWin,width=11)
    btnRemove.place(x=475, y=550)
    btnRemove.config(font=("Times New Roman", 28))

    btnEdit = tk.Button(mainBody,text="Edit",command=editTaskWin,width=11)
    btnEdit.place(x=775, y=550)
    btnEdit.config(font=("Times New Roman", 28))

    btnSearch = tk.Button(mainBody,text="Search",command=searchTaskWin,width=11)
    btnSearch.place(x=1075, y=550)
    btnSearch.config(font=("Times New Roman", 28))

    lblUserList = tk.Label(mainBody, text="Calendar", width=15)
    lblUserList.place(x = 600, y =150)
    lblUserList.config(font=("Times New Roman", 28))

    txtUserList = tk.Text(mainBody, height=20, width=142)
    txtUserList.place(x=175, y = 200)

    mainWindow.mainloop()

#Admin Window 
def adminMenu():
    adminWindow = tk.Tk()
    adminWindow.title("Admin Window")
    adminWindow.geometry("800x400")
    adminWindow.resizable(width=False,height=False)

    adminBody = tk.Frame(adminWindow,bg='#536878',height=400,width=800)
    adminBody.grid(row=0,column=0)

    btnExit = tk.Button(adminBody,text="Exit",command=exit,width=10)
    btnExit.place(x=550,y=250)
    btnExit.config(font=("Times New Roman", 28))

    btnRemoveUser = tk.Button(adminBody,text="Remove User",command=removeUserWin,width=10)
    btnRemoveUser.place(x=550,y=50)
    btnRemoveUser.config(font=("Times New Roman", 28))

    btnUpdateAdmin = tk.Button(adminBody,text="Update Admin",command=updateAdminWin,width=10)
    btnUpdateAdmin.place(x=300,y=50)
    btnUpdateAdmin.config(font=("Times New Roman", 28))

    btnAddUser = tk.Button(adminBody,text="Add User",command=addUserWin,width=10)
    btnAddUser.place(x=50,y=50)
    btnAddUser.config(font=("Times New Roman", 28))

    btnMainMenu = tk.Button(adminBody,text="Main Menu",command=lambda:[mainMenuWindow()],width=10)
    btnMainMenu.place(x=50,y=250)
    btnMainMenu.config(font=("Times New Roman", 28))

    lblUserList = tk.Label(adminBody, text="User List")
    lblUserList.place(x = 330, y =160)
    lblUserList.config(font=("Times New Roman", 28))

    txtUserList = tk.Text(adminBody, height=10, width=25)
    txtUserList.place(x=300, y = 220)

    adminWindow.mainloop()

#Add User GUI
def addUserWin():

    addUserWindow = tk.Tk()
    addUserWindow.title("Add User")
    addUserWindow.geometry("1000x500")
    addUserWindow.resizable(width=False,height=False)

    addUserBody = tk.Frame(addUserWindow,bg='#536878',height=500,width=1000)
    addUserBody.grid(row=0,column=0)

    btnMainMenu = tk.Button(addUserBody,text="Admin Menu",command=addUserWindow.destroy,width=10, height=2)
    btnMainMenu.place(x=750,y=200)
    btnMainMenu.config(font=("Times New Roman", 28))

    btnExit = tk.Button(addUserBody,text="Exit",command=exit,width=10, height=2)
    btnExit.place(x=750,y=350)
    btnExit.config(font=("Times New Roman", 28))

    btnAddUser = tk.Button(addUserBody,text="Add User",command=exit,width=10, height=2)
    btnAddUser.place(x=750,y=50)
    btnAddUser.config(font=("Times New Roman", 28))

    lblAddTitle = tk.Label(addUserBody,text="What user would you like to add?")
    lblAddTitle.config(font=("Times New Roman",24))
    lblAddTitle.place(x=150,y=50)

    lblUsername = tk.Label(addUserBody,text="Username:")
    lblUsername.config(font=("Times New Roman",24))
    lblUsername.place(x=50,y=150)

    entUsername = tk.Entry(addUserBody)
    entUsername.config(font=("Times New Roman", 20))
    entUsername.place(x=50,y=200,width=400,height=60)

    lblPassword = tk.Label(addUserBody,text="Password:")
    lblPassword.config(font=("Times New Roman",24))
    lblPassword.place(x=50,y=300)

    entPassword = tk.Entry(addUserBody)
    entPassword.config(font=("Times New Roman", 20))
    entPassword.place(x=50,y=350,width=400,height=60)

    addUserWindow.mainloop()

#Remove User Below
def removeUserWin():
    removeUserWindow = tk.Tk()
    removeUserWindow.title("Remove User")
    removeUserWindow.geometry("1000x500")
    removeUserWindow.resizable(width=False,height=False)

    removeUserBody = tk.Frame(removeUserWindow,bg='#536878',height=500,width=1000)
    removeUserBody.grid(row=0,column=0)

    btnMainMenu = tk.Button(removeUserBody,text="Admin Menu",command=removeUserWindow.destroy,width=10, height=2)
    btnMainMenu.place(x=750,y=200)
    btnMainMenu.config(font=("Times New Roman", 28))

    btnExit = tk.Button(removeUserBody,text="Exit",command=exit,width=10, height=2)
    btnExit.place(x=750,y=350)
    btnExit.config(font=("Times New Roman", 28))

    btnRemoveUser = tk.Button(removeUserBody,text="Remove User",command=exit,width=10, height=2)
    btnRemoveUser.place(x=750,y=50)
    btnRemoveUser.config(font=("Times New Roman", 28))

    lblAddTitle = tk.Label(removeUserBody,text="What user would you like to remove?")
    lblAddTitle.config(font=("Times New Roman",24))
    lblAddTitle.place(x=150,y=50)

    lblUsername = tk.Label(removeUserBody,text="Username:")
    lblUsername.config(font=("Times New Roman",24))
    lblUsername.place(x=50,y=150)

    entUsername = tk.Entry(removeUserBody)
    entUsername.config(font=("Times New Roman", 20))
    entUsername.place(x=50,y=200,width=400,height=60)

    lblPassword = tk.Label(removeUserBody,text="Password:")
    lblPassword.config(font=("Times New Roman",24))
    lblPassword.place(x=50,y=300)

    entPassword = tk.Entry(removeUserBody)
    entPassword.config(font=("Times New Roman", 20))
    entPassword.place(x=50,y=350,width=400,height=60)

    removeUserWindow.mainloop()

#Update Admin GUI
def updateAdminWin():
    updateAdminWindow = tk.Tk()
    updateAdminWindow.title("Update Admin")
    updateAdminWindow.geometry("1000x500")
    updateAdminWindow.resizable(width=False,height=False)

    updateAdminBody = tk.Frame(updateAdminWindow,bg='#536878',height=500,width=1000)
    updateAdminBody.grid(row=0,column=0)

    btnMainMenu = tk.Button(updateAdminBody,text="Admin Menu",command=updateAdminWindow.destroy,width=10, height=2)
    btnMainMenu.place(x=750,y=200)
    btnMainMenu.config(font=("Times New Roman", 28))

    btnExit = tk.Button(updateAdminBody,text="Exit",command=exit,width=10, height=2)
    btnExit.place(x=750,y=350)
    btnExit.config(font=("Times New Roman", 28))

    btnAddUser = tk.Button(updateAdminBody,text="Update Admin",command=updateAdmin,width=10, height=2)
    btnAddUser.place(x=750,y=50)
    btnAddUser.config(font=("Times New Roman", 28))

    lblAddTitle = tk.Label(updateAdminBody,text="What would you like to change Admin to?")
    lblAddTitle.config(font=("Times New Roman",24))
    lblAddTitle.place(x=150,y=25)

    lblUsername = tk.Label(updateAdminBody,text="New Username:")
    lblUsername.config(font=("Times New Roman",24))
    lblUsername.place(x=50,y=225)

    global entUsername
    entUsername = tk.Entry(updateAdminBody)
    entUsername.config(font=("Times New Roman", 20))
    entUsername.place(x=50,y=275,width=400,height=60)

    lblPassword = tk.Label(updateAdminBody,text="Password:")
    lblPassword.config(font=("Times New Roman",24))
    lblPassword.place(x=50,y=350)

    global entPassword
    entPassword = tk.Entry(updateAdminBody)
    entPassword.config(font=("Times New Roman", 20))
    entPassword.place(x=50,y=400,width=400,height=60)

    lblOldUser = tk.Label(updateAdminBody,text="Old Username:")
    lblOldUser.config(font=("Times New Roman",24))
    lblOldUser.place(x=50,y=100)

    global entOldUser
    entOldUser = tk.Entry(updateAdminBody)
    entOldUser.config(font=("Times New Roman", 20))
    entOldUser.place(x=50,y=150,width=400,height=60)

    updateAdminWindow.mainloop()

#Update Admin Function
def updateAdmin():
    oldAdminUser = entOldUser.get()
    print(oldAdminUser)
    if oldAdminUser == adminUser:
        adminUser = entUsername.get()
        global adminPassword
        adminPassword = entPassword.get()
        messagebox.showinfo("Admin Successfully Updated")
    else:
        messagebox.showinfo("Entered username does not match old username")

#Add Task GUI
def addTaskWin():
    addWindow = tk.Tk()
    addWindow.title("Add Task")
    addWindow.geometry("1000x500")
    addWindow.resizable(width=False,height=False)

    addBody = tk.Frame(addWindow,bg='#536878',height=500,width=1000)
    addBody.grid(row=0,column=0)

    btnMainMenu = tk.Button(addBody,text="Main Menu",command=addWindow.destroy,width=10, height=2)
    btnMainMenu.place(x=750,y=200)
    btnMainMenu.config(font=("Times New Roman", 28))

    btnExit = tk.Button(addBody,text="Exit",command=exit,width=10, height=2)
    btnExit.place(x=750,y=350)
    btnExit.config(font=("Times New Roman", 28))

    btnAddUser = tk.Button(addBody,text="Add Task",command=exit,width=10, height=2)
    btnAddUser.place(x=750,y=50)
    btnAddUser.config(font=("Times New Roman", 28))

    lblTaskName = tk.Label(addBody,text="Task Name:")
    lblTaskName.config(font=("Times New Roman",24))
    lblTaskName.place(x=50,y=50)

    entTaskName = tk.Entry(addBody)
    entTaskName.config(font=("Times New Roman", 20))
    entTaskName.place(x=50,y=100,width=400,height=60)

    lblDate = tk.Label(addBody,text="Task Date:")
    lblDate.config(font=("Times New Roman",24))
    lblDate.place(x=50,y=200)

    entDate = tk.Entry(addBody)
    entDate.config(font=("Times New Roman", 20))
    entDate.place(x=50,y=250,width=150,height=60)

    lblDuration = tk.Label(addBody,text="Task Duration (mins):")
    lblDuration.config(font=("Times New Roman",24))
    lblDuration.place(x=300,y=200)

    entDuration = tk.Entry(addBody)
    entDuration.config(font=("Times New Roman", 20))
    entDuration.place(x=300,y=250,width=300,height=60)

    lblDesc = tk.Label(addBody,text="Task Description:")
    lblDesc.config(font=("Times New Roman",24))
    lblDesc.place(x=50,y=350)

    entDesc = tk.Entry(addBody)
    entDesc.config(font=("Times New Roman", 20))
    entDesc.place(x=50,y=400,width=600,height=60)

    addWindow.mainloop()

#Remove Task GUI
def removeTaskWin():
    removeWindow = tk.Tk()
    removeWindow.title("Remove Task")
    removeWindow.geometry("1000x500")
    removeWindow.resizable(width=False,height=False)

    removeBody = tk.Frame(removeWindow,bg='#536878',height=500,width=1000)
    removeBody.grid(row=0,column=0)

    lblRemove = tk.Label(removeBody,text="What task would you like to remove?:")
    lblRemove.config(font=("Times New Roman",30))
    lblRemove.place(x=75,y=50)

    btnMainMenu = tk.Button(removeBody,text="Main Menu",command=removeWindow.destroy,width=10, height=2)
    btnMainMenu.place(x=750,y=200)
    btnMainMenu.config(font=("Times New Roman", 28))

    btnExit = tk.Button(removeBody,text="Exit",command=exit,width=10, height=2)
    btnExit.place(x=750,y=350)
    btnExit.config(font=("Times New Roman", 28))

    btnAddUser = tk.Button(removeBody,text="Remove Task",command=exit,width=10, height=2)
    btnAddUser.place(x=750,y=50)
    btnAddUser.config(font=("Times New Roman", 28))


    lblTaskName = tk.Label(removeBody,text="Task Name:")
    lblTaskName.config(font=("Times New Roman",24))
    lblTaskName.place(x=50,y=175)

    entTaskName = tk.Entry(removeBody)
    entTaskName.config(font=("Times New Roman", 20))
    entTaskName.place(x=50,y=225,width=400,height=60)

    lblDate = tk.Label(removeBody,text="Task Date:")
    lblDate.config(font=("Times New Roman",24))
    lblDate.place(x=50,y=325)

    entDate = tk.Entry(removeBody)
    entDate.config(font=("Times New Roman", 20))
    entDate.place(x=50,y=375,width=400,height=60)

    removeWindow.mainloop()

#Edit Task GUI
def editTaskWin():
    editWindow = tk.Tk()
    editWindow.title("Edit Task")
    editWindow.geometry("1000x750")
    editWindow.resizable(width=False,height=False)

    editBody = tk.Frame(editWindow,bg='#536878',height=750,width=1000)
    editBody.grid(row=0,column=0)

    lblEdit = tk.Label(editBody,text="What task would you like to edit?:")
    lblEdit.config(font=("Times New Roman",30))
    lblEdit.place(x=200,y=50)

    btnMainMenu = tk.Button(editBody,text="Main Menu",command=editWindow.destroy,width=10, height=2)
    btnMainMenu.place(x=750,y=375)
    btnMainMenu.config(font=("Times New Roman", 28))

    btnExit = tk.Button(editBody,text="Exit",command=exit,width=10, height=2)
    btnExit.place(x=750,y=550)
    btnExit.config(font=("Times New Roman", 28))

    btnEdit = tk.Button(editBody,text="Edit Task",command=exit,width=10, height=2)
    btnEdit.place(x=750,y=200)
    btnEdit.config(font=("Times New Roman", 28))

    lblTaskName = tk.Label(editBody,text="Task Name:")
    lblTaskName.config(font=("Times New Roman",24))
    lblTaskName.place(x=50,y=175)

    entTaskName = tk.Entry(editBody)
    entTaskName.config(font=("Times New Roman", 20))
    entTaskName.place(x=50,y=225,width=300,height=60)

    lblDate = tk.Label(editBody,text="Task Date:")
    lblDate.config(font=("Times New Roman",24))
    lblDate.place(x=450,y=175)

    entDate = tk.Entry(editBody)
    entDate.config(font=("Times New Roman", 20))
    entDate.place(x=450,y=225,width=200,height=60)

    lblNewName = tk.Label(editBody,text="New Task Name:")
    lblNewName.config(font=("Times New Roman",24))
    lblNewName.place(x=50,y=375)

    entNewName = tk.Entry(editBody)
    entNewName.config(font=("Times New Roman", 20))
    entNewName.place(x=50,y=425,width=300,height=60)

    lblNewDate = tk.Label(editBody,text="New Task Date:")
    lblNewDate.config(font=("Times New Roman",24))
    lblNewDate.place(x=450,y=375)

    entNewDate = tk.Entry(editBody)
    entNewDate.config(font=("Times New Roman", 20))
    entNewDate.place(x=450,y=425,width=200,height=60)

    lblNewDesc = tk.Label(editBody,text="New Task Description:")
    lblNewDesc.config(font=("Times New Roman",24))
    lblNewDesc.place(x=50,y=550)

    entNewDesc = tk.Entry(editBody)
    entNewDesc.config(font=("Times New Roman", 20))
    entNewDesc.place(x=50,y=600,width=300,height=60)

    lblNewDur = tk.Label(editBody,text="New Task Duration:")
    lblNewDur.config(font=("Times New Roman",24))
    lblNewDur.place(x=450,y=550)

    entNewDur = tk.Entry(editBody)
    entNewDur.config(font=("Times New Roman", 20))
    entNewDur.place(x=450,y=600,width=200,height=60)

    editWindow.mainloop()

#Search Task GUI
def searchTaskWin():
    searchWindow = tk.Tk()
    searchWindow.title("Search Task")
    searchWindow.geometry("1000x750")
    searchWindow.resizable(width=False,height=False)

    searchBody = tk.Frame(searchWindow,bg='#536878',height=750,width=1000)
    searchBody.grid(row=0,column=0)

    lblEdit = tk.Label(searchBody,text="Search for tasks using one or more identifiers")
    lblEdit.config(font=("Times New Roman",30))
    lblEdit.place(x=200,y=50)

    btnMainMenu = tk.Button(searchBody,text="Main Menu",command=searchWindow.destroy,width=10, height=2)
    btnMainMenu.place(x=750,y=420)
    btnMainMenu.config(font=("Times New Roman", 28))

    btnExit = tk.Button(searchBody,text="Exit",command=exit,width=10, height=2)
    btnExit.place(x=750,y=620)
    btnExit.config(font=("Times New Roman", 28))

    btnSearch = tk.Button(searchBody,text="Search",command=exit,width=10, height=2)
    btnSearch.place(x=750,y=220)
    btnSearch.config(font=("Times New Roman", 28))


    lblTaskName = tk.Label(searchBody,text="Task Name:")
    lblTaskName.config(font=("Times New Roman",24))
    lblTaskName.place(x=50,y=175)

    entTaskName = tk.Entry(searchBody)
    entTaskName.config(font=("Times New Roman", 20))
    entTaskName.place(x=50,y=225,width=300,height=60)

    lblDate = tk.Label(searchBody,text="Task Date:")
    lblDate.config(font=("Times New Roman",24))
    lblDate.place(x=50,y=325)

    entDate = tk.Entry(searchBody)
    entDate.config(font=("Times New Roman", 20))
    entDate.place(x=50,y=375,width=200,height=60)

    lblNewName = tk.Label(searchBody,text="Task Duration:")
    lblNewName.config(font=("Times New Roman",24))
    lblNewName.place(x=50,y=475)

    entNewName = tk.Entry(searchBody)
    entNewName.config(font=("Times New Roman", 20))
    entNewName.place(x=50,y=525,width=300,height=60)

    lblNewDesc = tk.Label(searchBody,text="Task Description:")
    lblNewDesc.config(font=("Times New Roman",24))
    lblNewDesc.place(x=50,y=625)

    entNewDesc = tk.Entry(searchBody)
    entNewDesc.config(font=("Times New Roman", 20))
    entNewDesc.place(x=50,y=675,width=300,height=60)

    lblTasks = tk.Label(searchBody, text="Tasks")
    lblTasks.place(x = 500, y =150)
    lblTasks.config(font=("Times New Roman", 28))

    txtTasks = tk.Text(searchBody, height=32, width=40)
    txtTasks.place(x=390, y = 220)

    searchWindow.mainloop()

#Login GUI
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

btnLogin = tk.Button(Body,text="Login",command=login,width=10)
btnLogin.place(x=500,y=125)
btnLogin.config(font=("Times New Roman", 30))

btnExit = tk.Button(Body,text="Exit",command=exit,width=10)
btnExit.place(x=500,y=250)
btnExit.config(font=("Times New Roman", 30))

loginwindow.mainloop()