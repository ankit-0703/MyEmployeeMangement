
from tkinter import *
from tkinter import messagebox 
import tkcalendar
from tkinter import ttk
from sqlClient import mySqlClient
import json

import datetime
from PIL import Image,ImageTk

import tkinter.messagebox as messagebox
import mysql.connector
file = open('employee-management-mysql-master\config.json', 'r')
configData = json.load(file)

sqlClient = mySqlClient(username=configData['user'], password=configData['pass'], host=configData['host'], database=configData['database'])

window = Tk()

screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()

windowWidth = int(screenWidth * 0.8)
windowHeight = int(screenHeight * 0.8)

window.geometry(f"{windowWidth}x{windowHeight}")

window_width = int(screenWidth)  # Adjust width as needed
window_height = int(screenHeight)  # Adjust height as needed

image_path=r"C:\Users\ankit\OneDrive\Desktop\3rd year project\employee-management-mysql-master\employee-management-mysql-master\background\R.png"
image=Image.open(image_path)

width,height=image.size
if width <window_width or height > window_height:
    aspect_ratio = width / height
    if aspect_ratio > 1:
        # Resize based on width
        new_width = window_width
        new_height = int(window_width / aspect_ratio)
    else:
        # Resize based on height
        new_height = window_height
        new_width = int(window_height * aspect_ratio)
    image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)


image = ImageTk.PhotoImage(image)


label = Label(window, image=image)
label.place(relx=0, rely=0, x=0, y=0, width=window_width, height=window_height)



def homeScreen():
    frame=Frame(window)
    frame.pack()
    opetionsFrame =LabelFrame(frame, text="Main Menu")
    opetionsFrame.grid(row= 0, column=0, padx=80, pady=80)
    addButton = Button(opetionsFrame, text='Employee Details',height=2, width=15, padx=20, pady=20, font='lucida 10 normal', command=addEmployee)
    addButton.grid(padx=10, pady=10)
    
    addButton = Button(opetionsFrame, text='Department details',height=2, width=15, padx=20, pady=20, font='lucida 10 normal', command=departmentdetail)
    addButton.grid(padx=10, pady=10)
    addButton = Button(opetionsFrame, text='Project details',height=2, width=15, padx=20, pady=20, font='lucida 10 normal', command=projectdetails)
    addButton.grid(padx=10, pady=10)
    
    addButton = Button(opetionsFrame, text='Dependent details',height=2, width=15, padx=20, pady=20, font='lucida 10 normal', command=dependentdetails)
    addButton.grid(padx=10, pady=10)
    
    addButton = Button(opetionsFrame, text='Find details',height=2, width=15, padx=20, pady=20, font='lucida 10 normal', command=finddetails)
    addButton.grid(padx=10, pady=10)

    addButton = Button(opetionsFrame, text='Employee Feedback',height=2, width=15, padx=20, pady=20, font='lucida 10 normal', command=feedbackvalue)
    addButton.grid(padx=10, pady=10)

    
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)
    

def dependentdetails():
    window1=Tk()
    
    screenWidth = window1.winfo_screenwidth()
    screenHeight = window1.winfo_screenheight()

    window.destroy()
    windowWidth = int(screenWidth * 0.7)
    windowHeight = int(screenHeight * 0.7)
    window1.geometry(f"{windowWidth}x{windowHeight}")
    for widget in window1.winfo_children():
        widget.destroy()
        
    frame = Frame(window1)

    opetionsFrame =LabelFrame(frame, text="Dependent Options")
    opetionsFrame.grid(row= 0, column=0, padx=50, pady=50)
    addButton = Button(opetionsFrame, text='Add dependent details',height=2, width=15, padx=20, pady=20, font='lucida 10 normal', command=addDependent)
    addButton.pack(padx=10, pady=10)
    addButton = Button(opetionsFrame, text='Dependent details',height=2, width=15, padx=20, pady=20, font='lucida 10 normal', command=alldepenedentScreen)
    addButton.pack(padx=10, pady=10)
    addButton = Button(opetionsFrame, text='Dependent delete',height=2, width=15, padx=20, pady=20, font='lucida 10 normal', command=delete_depentdent)
    addButton.pack(padx=10, pady=10)
    addButton = Button(opetionsFrame, text='Dependent update',height=2, width=15, padx=20, pady=20, font='lucida 10 normal', command=updateDependentScreen)
    addButton.pack(padx=10, pady=10)

    addButton = Button(frame, text="close", command=window1.destroy)
    addButton.grid(row= 5, column=0, padx=20, pady=10)

    frame.pack()
    
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)

def projectdetails():
    window1=Tk()
    screenWidth = window1.winfo_screenwidth()
    screenHeight = window1.winfo_screenheight()
    window.update()
    windowWidth = int(screenWidth * 0.7)
    windowHeight = int(screenHeight * 0.7)
    window1.geometry(f"{windowWidth}x{windowHeight}")
    for widget in window1.winfo_children():
        widget.destroy()
    frame = Frame(window1)
    opetionsFrame =LabelFrame(frame, text="Project Related Options")
    opetionsFrame.grid(row= 0, column=0, padx=50, pady=50)
    addButton1 = Button(opetionsFrame, text='Add New project',height=2, width=15, padx=20, pady=20, font='lucida 10 normal', command=addproject)
    addButton1.grid(row=0,column=0, sticky='nsew',padx=10,pady=10)
    addButton2 = Button(opetionsFrame,text='View all the project',height=2, width=15, padx=20, pady=20, font='lucida 10 normal', command=allprojectScreen)
    addButton2.grid(row=0,column=1, sticky='nsew',padx=10,pady=10)
    addButton3 = Button(opetionsFrame,text='Project assignment',height=2, width=15, padx=20, pady=20, font='lucida 10 normal', command=addworking)
    addButton3.grid(row=0,column=2, sticky='nsew',padx=10,pady=10)
    addButton4 = Button(opetionsFrame,text='View Project assignment',height=2, width=15, padx=20, pady=20, font='lucida 10 normal', command=working_details)
    addButton4.grid(row=1,column=0, sticky='nsew',padx=10,pady=10)
    
    addButton5 = Button(opetionsFrame,text='Update Project details',height=2, width=15, padx=20, pady=20, font='lucida 10 normal', command=updateProjectScreen)
    addButton5.grid(row=1,column=1, sticky='nsew',padx=10,pady=10)
    
    addButton6 = Button(opetionsFrame,text='Update working details',height=2, width=15, padx=20, pady=20, font='lucida 10 normal', command=updateworking)
    addButton6.grid(row=1,column=2, sticky='nsew',padx=10,pady=10)
    
    button = Button(frame, text="Cancel", command=window1.destroy)
    button.grid(row=4, column=0, sticky="news", padx=20, pady=10)
    frame.pack()
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)
def departmentdetail():
    window1=Tk()
    screenWidth = window1.winfo_screenwidth()
    screenHeight = window1.winfo_screenheight()
    window1Width = int(screenWidth * 0.9)
    window1Height = int(screenHeight * 0.9)
    window1.geometry(f"{window1Width}x{window1Height}")
    
    for widget in window1.winfo_children():
        widget.pack_forget()
    frame = Frame(window1)
    

    opetionsFrame =LabelFrame(frame, text="Department related Options" )
    opetionsFrame.grid(row= 0, column=0, padx=50, pady=50)
    #addButton = Button(frame, text="Back", command=homeScreen)
    addButton0 = Button(opetionsFrame, text='Add New Department Manager',height=2, width=15, padx=20, pady=20, font='lucida 10 normal', command=addDepScreen)
    addButton0.grid(row=0,column=0,padx=20,pady=20)
    
    addButton1 = Button(opetionsFrame,text='View the department details',height=2, width=15, padx=20, pady=20, font='lucida 10 normal', command=allDepartmentScreen)
    addButton1.grid(row=0,column=2,padx=20,pady=20)
    #addButton.pack(padx=10, pady=10)
    addButton2 = Button(opetionsFrame,text='Add department location',height=2, width=15, padx=20, pady=20, font='lucida 10 normal', command=addDlocation)
    addButton2.grid(row=0,column=4,padx=20,pady=20)
    #addButton.pack(padx=10, pady=10)
    addButton3 = Button(opetionsFrame,text='View department location',height=2, width=15, padx=20, pady=20, font='lucida 10 normal', command= allDepartmentScreenloc)
    addButton3.grid(row=2,column=0,padx=20,pady=20)
    #addButton.pack(padx=10, pady=10)
    addButton4 = Button(opetionsFrame,text='update department manager',height=2, width=15, padx=20, pady=20, font='lucida 10 normal', command= update_department)
    addButton4.grid(row=2,column=2,padx=20,pady=20)
    #addButton1.pack(padx=10, pady=10)
    addButton5 = Button(opetionsFrame,text='Update department location',height=2, width=15, padx=20, pady=20, font='lucida 10 normal', command= update_department_location)
    addButton5.grid(row=2,column=4,padx=20,pady=20)
    #addButton.pack(padx=10, pady=10)
    button = Button(frame, text="Cancel", command=window1.destroy)
    button.grid(row=4, column=0, sticky="news", padx=20, pady=10)
    
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)
    
    
    frame.pack()
def  addEmployee():
    for widget in window.winfo_children():
        widget.pack_forget()
    frame = Frame(window)
    
    opetionsFrame =LabelFrame(frame, text="Employee related Options")
    opetionsFrame.grid(row= 0, column=0, padx=50, pady=50)
    addButton = Button(opetionsFrame, text='Add New Employee',height=2, width=15, padx=20, pady=20, font='lucida 10 normal', command=addScreen)
    addButton.pack(padx=10, pady=10)
    addButton = Button(opetionsFrame,text='Delete An Employee',height=2, width=15, padx=20, pady=20, font='lucida 10 normal', command=deleteScreen)
    addButton.pack(padx=10, pady=10)
    addButton = Button(opetionsFrame, text='Update An Employee',height=2, width=15, padx=20, pady=20, font='lucida 10 normal', command=updateScreen)
    addButton.pack(padx=10, pady=10)
    addButton = Button(opetionsFrame,text='View All Employees',height=2, width=15, padx=20, pady=20, font='lucida 10 normal', command=allEmployeeScreen)
    addButton.pack(padx=10, pady=10)
    addbutton = Button(opetionsFrame ,text="Back", command=homeScreen)
    addbutton.pack(padx=10, pady=10)
            
    frame.pack()
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)

def addScreen():
    window_addEMP_addEMP = Tk()
    screenWidth = window_addEMP_addEMP.winfo_screenwidth()
    screenHeight = window_addEMP_addEMP.winfo_screenheight()

    window_addEMP_addEMPWidth = int(screenWidth * 0.7)
    window_addEMP_addEMPHeight = int(screenHeight * 0.7)
    for widget in window_addEMP_addEMP.winfo_children():
        widget.pack_forget()

    window_addEMP_addEMP.geometry(f"{window_addEMP_addEMPWidth}x{window_addEMP_addEMPHeight}")
    def enterData():
        location= locationVar.get()
        firstname = firstNameEntry.get()
        lastname = lastNameEntry.get()
        birthDate = birthDateCalendar.get_date().strftime("%Y-%m-%d")
        def check_age(birthDate):
            today = datetime.date.today().year
            try:
                birth_year = int(birthDate[:4])
            except ValueError:
                raise ValueError("Invalid birth date format. Please use YYYY-MM-DD.")
            age = today - birth_year
            if age < 18:
                return False  # Employee is not eligible
            else:
                return True  # Employee is eligible
        '''
        today=datetime.date.today().year
        age=int(today)-int(birthDate[:4])
        if age < 18:
            messagebox.showerror('Error','Employee must be 18 year old to joim the company')
            return
        '''
        if not check_age(birthDate):
            messagebox.showerror(title="Error",message=("Employee must be 18 year old or older to join the company."))
        
        
        joiningDate=joiningDateCalendar.get_date().strftime("%Y-%m-%d")
        joining_age=int(joiningDate[:4])-int(birthDate[:4])
        if joiningDate<birthDate or joining_age<18:
            messagebox.showerror("Error","You cannot join the company due to  invalid date and/or age.")
            return
        salary = salaryEntry.get()
        
        department = departmentVar.get()
        if location and firstname and lastname and birthDate and salary and joiningDate and department:
            sqlClient.insertEmployee(location=location,name=f'{firstname.capitalize()} {lastname.capitalize()}', dateOfBirth=birthDate, joiningDate=joiningDate, salary=salary, department=department)
            messagebox.showwarning(title="Success", message="A new employee details added into the databse.")
            locationVar.set("")
            firstNameEntry.delete(0,END)
            lastNameEntry.delete(0,END)
            salaryEntry.delete(0,END)
            departmentVar.set("")
        else: 
            messagebox.showwarning(title="Error", message="All fields are required.")

    frame = Frame(window_addEMP_addEMP)
    
    
    employeeDetailsFrame =LabelFrame(frame, text="Add An Employee")
    employeeDetailsFrame.grid(row= 0, column=0, padx=20, pady=10)

    firstNameLabel = Label(employeeDetailsFrame, text="First Name")
    firstNameLabel.grid(row=0, column=0)
    lastNameLabel = Label(employeeDetailsFrame, text="Last Name")
    lastNameLabel.grid(row=0, column=1)
    birthDateLabel = Label(employeeDetailsFrame, text="Birth Date (dd-mm-yyyy)")
    locationLabel= Label(employeeDetailsFrame,text='Location : ')
    locationLabel.grid(row=0,column=2)
    birthDateLabel.grid(row=2, column=0)
    joiningDateLabel = Label(employeeDetailsFrame, text="Joining Date (dd-mm-yyyy)")
    joiningDateLabel.grid(row=2, column=1)
    salaryLabel = Label(employeeDetailsFrame, text="Salary")
    salaryLabel.grid(row=2, column=2)
    departmentLabel = Label(employeeDetailsFrame, text="Department")
    departmentLabel.grid(row=2, column=3)

    
    firstNameEntry = Entry(employeeDetailsFrame)
    lastNameEntry = Entry(employeeDetailsFrame)
    birthDateCalendar = tkcalendar.DateEntry(employeeDetailsFrame)
    joiningDateCalendar = tkcalendar.DateEntry(employeeDetailsFrame)
    salaryEntry = Entry(employeeDetailsFrame)
    firstNameEntry.grid(row=1, column=0)
    lastNameEntry.grid(row=1, column=1)
    birthDateCalendar.grid(row=3, column=0)
    joiningDateCalendar.grid(row=3, column=1)
    salaryEntry.grid(row=3, column=2)
    
    departmentVar=StringVar(employeeDetailsFrame)
    departmentVar.set("")
    departmentMenu=OptionMenu(employeeDetailsFrame, departmentVar, *("Account", "Administration", "Logistics", "Developers", "Research"))
    departmentMenu.grid(row=3, column=3)
    
    locationVar=StringVar(employeeDetailsFrame)
    locationVar.set("")
    locationMenu=OptionMenu(employeeDetailsFrame, locationVar, *("Banglore","Chennai","Hyderabad","Delhi","Mumbai"))
    locationMenu.grid(row=1, column=2)


    for widget in employeeDetailsFrame.winfo_children():
        widget.grid_configure(padx=10, pady=5)

    button = Button(frame, text="Save Employee Details", command= enterData)
    button.grid(row=3, column=0, sticky="news", padx=20, pady=10)
    button = Button(frame, text="Cancel", command=window_addEMP_addEMP.destroy)
    button.grid(row=4, column=0, sticky="news", padx=20, pady=10)
    frame.pack()
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)



def deleteScreen():
    window = Tk()
    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()

    windowWidth = int(screenWidth * 0.7)
    windowHeight = int(screenHeight * 0.7)
    window.geometry(f"{windowWidth}x{windowHeight}")
    def findAndDeleteEmployee():
        

        frame = Frame(window)
        frame.pack(fill="both", expand=True)

        ssn = valueEntry.get()
        if not ssn:
            messagebox.showerror('Error', 'Please provide an SSN')
            return
        if ssn:
            employees = sqlClient.findEmployee(method="SSn", value=ssn)
            if len(employees) == 0:
                messagebox.showwarning(title="Error", message="No employee found with that SSN.")
                return
            else:
                # Display employee details
                tree = ttk.Treeview(frame, columns=("SSn", "Name", "Location", "Date of Birth", "Joining Date", "Salary", "Department"))
                tree.heading("SSn", text="SSn", anchor="center")
                tree.heading("Name", text="Name", anchor="center")
                tree.heading("Date of Birth", text="Date of Birth", anchor="center")
                tree.heading("Location", text="Location", anchor="center")
                tree.heading("Joining Date", text="Joining Date", anchor="center")
                tree.heading("Salary", text="Salary", anchor="center")
                tree.heading("Department", text="Department", anchor="center")
        # ... (set other headings)
                for row in employees:
                    tree.insert("", "end", values=row)
            try:
                sqlClient.deleteEmployee(method="SSn",value=ssn)
                messagebox.showinfo(title="Success", message="Employee deleted successfully.")
                allEmployeeScreen()  # Refresh the screen
            except Exception as e:
                    messagebox.showerror(title="Error", message=f"Error deleting employee: {str(e)}")

                
                
    for widget in window.winfo_children():
        widget.pack_forget()

    frame = Frame(window)
    valueLable = Label(frame, text="Enter the ID of the employee you want to delete: ")
    valueLable.grid(row=1, column=0)
    valueEntry = Entry(frame, text="Enter SSN:")
    valueEntry.grid(row=2, column=0)
    valueEntry = Entry(frame, width=100)
    valueEntry.grid(row=2, column=0, padx=10, pady=10)
    
    button = Button(frame, text="Find and Delete", command=findAndDeleteEmployee)
    button.grid(row=3, column=0, sticky="news", padx=10, pady=10)
    button = Button(frame, text="Cancel", command=window.destroy)
    button.grid(row=4, column=0, sticky="news", padx=10, pady=10)
    frame.pack()
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)
    

def updateScreen():
    window=Tk()
    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()

    windowWidth = int(screenWidth * 0.7)
    windowHeight = int(screenHeight * 0.7)
    window.geometry(f"{windowWidth}x{windowHeight}")
    
    for widget in window.winfo_children():
        widget.pack_forget()
    frame = Frame(window)
    frame.pack()

    findEmployeeFrame =LabelFrame(frame, text="Update An Employee")
    findEmployeeFrame.grid(row= 0, column=0, padx=20, pady=10)
    options = [
    "SSn",
    "Name",
    "Birth Date",
    "Joining Date",
    "Salary",
    "Department"
    ]
    usingOpt = StringVar(findEmployeeFrame)
    usingOpt.set("Find Employee Using")

    menu = OptionMenu(findEmployeeFrame, usingOpt, *options)
    menu.grid(row=0, column=0,padx=10, pady=10)

    def nextUpdate():

        def find():
            def update():
                selectedEmployee = tree.selection()
                if len(selectedEmployee) == 0:
                    messagebox.showwarning(title="Error", message="Select an employee first.")
                else:
                    for item in selectedEmployee:
                        itemValue = tree.item(item, 'values')
                        ind = 0
                        if usingOptValue == 'SSn':
                            ind = 0
                        elif usingOptValue== 'Name':
                            ind = 1
                        elif usingOptValue == 'Birth Date':
                            ind = 2
                        elif usingOptValue== 'Location':
                            ind =3
                        elif usingOptValue == 'Joining Date':
                            ind = 4
                        elif  usingOptValue == 'Salary':
                            ind = 5
                        elif  usingOptValue == 'Department':
                            ind = 6
                        else:
                            ind = 7
                    for widget in window.winfo_children():
                        widget.destroy()
                    def enterData():
                        #ssn=ssnEntry.get()
                        firstname = firstNameEntry.get()
                        lastname = lastNameEntry.get()
                        birthDate = birthDateEntry.get()
                        location = locationVar.get()
                        #copyval=copyvalEntry.get()
                        joiningDate = joiningDateEntry.get()
                        salary = salaryEntry.get()
                        department =  departmentVar.get()
                        if firstname and lastname and birthDate and location and joiningDate and salary and department:
                            sqlClient.updateEmployee(method=usingOptValue, value=itemValue, newValue=(f'{firstname.capitalize()} {lastname.capitalize()}', birthDate,location, joiningDate, salary, department))
                            messagebox.showwarning(title="Success", message="Updated Employee Details")
                            allEmployeeScreen()
                        else: 
                            messagebox.showwarning(title="Error", message="All fields are required.")

                    frame = Frame(window)
                    
                    
                    employeeDetailsFrame =LabelFrame(frame, text="Update Employee Details")
                    employeeDetailsFrame.grid(row= 0, column=0, padx=20, pady=10)
                    firstNameLabel = Label(employeeDetailsFrame, text="First Name")
                    firstNameLabel.grid(row=0, column=0)
                    lastNameLabel = Label(employeeDetailsFrame, text="Last Name")
                    lastNameLabel.grid(row=0, column=1)
                    birthDateLabel = Label(employeeDetailsFrame, text="Birth Date (yyyy-mm-dd)")
                    birthDateLabel.grid(row=0, column=2)
                    joiningDateLabel = Label(employeeDetailsFrame, text="Joining Date (yyyy-mm-dd)")
                    joiningDateLabel.grid(row=0, column=3)
                    locationLabel= Label(employeeDetailsFrame,text='Country/Region')
                    locationLabel.grid(row=2,column=0)
                    salaryLabel = Label(employeeDetailsFrame, text="Salary")
                    salaryLabel.grid(row=2, column=1)
                    departmentLabel = Label(employeeDetailsFrame, text="Department")
                    departmentLabel.grid(row=2, column=2)

                    #ssnLabel=Label(employeeDetailsFrame,text="Social Security Number")
                    #ssnLabel.grid(row=2,column=3)
                    #ssnEntry=Entry(employeeDetailsFrame)
                    #ssnEntry.insert(6,itemValue[0])
                    #ssnEntry.grid(row=3,column=3)

                    firstNameEntry = Entry(employeeDetailsFrame)
                    firstNameEntry.insert(0,itemValue[1].split(" ")[0])
                    lastNameEntry = Entry(employeeDetailsFrame)
                    lastNameEntry.insert(1,itemValue[1].split(" ")[1])
                    birthDateEntry =Entry(employeeDetailsFrame)
                    birthDateEntry.insert(1,itemValue[3])
                    def on_select_location(event):
                        selected_value = usingOpt3.get()  # Get the selected value from the menu
                        locationVar.set(selected_value)
                    #locationVar=optMenu3
                    locationVar = StringVar(employeeDetailsFrame)
                    locationVar.set("")

                    locationList=[
                    "Bengaluru",
                    "Chennai",
                    "Delhi",
                    "Kolkata",
                    "Hyderabad"
                    ]
                    #usingOpt3 = StringVar(employeeDetailsFrame)
                    #usingOpt3.set("") 
                    usingOpt3 = OptionMenu(employeeDetailsFrame,locationVar,*locationList)
                    usingOpt3.grid(row=3, column=0)
                    usingOpt3.bind("<<ComboboxSelected>>", on_select_location)  # Bind the selection event
                    def copy_to_entry_location():
                        copyvalEntry.delete(0,END)  # Clear the entry box before copying
                        copyvalEntry.insert(0, locationVar.get())  # Insert the copied value at the beginning

                    # ... (other code for creating employeeDetailsFrame)

                    button = Button(employeeDetailsFrame, text="Click", command=copy_to_entry_location)
                    button.grid(row=4, column=0)

                    copyvalEntry = Entry(employeeDetailsFrame)
                    copyvalEntry.grid(row=5, column=0)
                    # Create your button here
                    #button = Button(employeeDetailsFrame, text="Click", command=lambda: print(locationVar.get()))
                    #copyval1=locationVar.get()
                    #button.grid(row=4, column=0)
                    #copyvalEntry=Entry(employeeDetailsFrame)
                    #copyvalEntry.grid(row=5, column=0)
                    #copyvalEntry.insert(2,itemValue[4])
                    joiningDateEntry = Entry(employeeDetailsFrame)
                    joiningDateEntry.insert(3,itemValue[4])
                    salaryEntry = Entry(employeeDetailsFrame)
                    salaryEntry.insert(4,itemValue[5])
                    firstNameEntry.grid(row=1, column=0)
                    lastNameEntry.grid(row=1, column=1)
                    birthDateEntry.grid(row=1, column=2)
                    joiningDateEntry.grid(row=1, column=3)
                    salaryEntry.grid(row=3, column=1)
                    def on_select_department(event):
                        selected_value=usingOpt1.get()
                        departmentVar.set(selected_value)
                    departmentVar=StringVar(employeeDetailsFrame)
                    departmentVar.set("")
                    departmentList = [
                    "Accounts",
                    "Administration",
                    "I T",
                    "Sales",
                    "Research",
                    ]
                    usingOpt1 = OptionMenu(employeeDetailsFrame,departmentVar,*departmentList)
                    usingOpt1.grid(row=3, column=2)
                    usingOpt1.bind("<<ComboboxSelected>>", on_select_department)  # Bind the selection event
                    def copy_to_entry_department():
                        copyvalEntry1.delete(0,END)  # Clear the entry box before copying
                        copyvalEntry1.insert(0, departmentVar.get())  # Insert the copied value at the beginning
                    
                    # ... (other code for creating employeeDetailsFrame)

                    button = Button(employeeDetailsFrame, text="Click", command=copy_to_entry_department)
                    button.grid(row=4, column=2)

                    copyvalEntry1 = Entry(employeeDetailsFrame)
                    copyvalEntry1.grid(row=5, column=2)  
                    #13usingOpt1 = StringVar(employeeDetailsFrame)
                    #usingOpt1.set("") 
                    #departmentVar.insert(5,itemValue[6])


                    for widget in employeeDetailsFrame.winfo_children():
                        widget.grid_configure(padx=10, pady=5)

                    button = Button(frame, text="Update Employee Details", command= enterData)
                    button.grid(row=3, column=0, sticky="news", padx=20, pady=10)
                    button = Button(frame, text="Cancel", command= window.destroy)
                    button.grid(row=4, column=0, sticky="news", padx=20, pady=10)
                    frame.place(relx=0.5, rely=0.5, anchor=CENTER)
            
            if selection==2:
                employees = sqlClient.findEmployee(method=usingOptValue, value=valueEntry.get_date())
            elif selection==3:
                employees = sqlClient.findEmployee(method=usingOptValue, value=valueEntry.option_get())
            elif selection==4:
                employees = sqlClient.findEmployee(method=usingOptValue, value=valueEntry.get())
            if len(employees) == 0:
                messagebox.showwarning(title="Error", message="No match found.")
            else:
                tree = ttk.Treeview(nextDeleteFrame, columns=("SSn","Name","Location","Date of Birth", "Joining Date", "Salary", "Department"))
                tree.heading("#0", text="", anchor="center") 
                tree.heading("SSn", text="SSn", anchor="center")
                tree.heading("Name", text="Name", anchor="center")
                tree.heading("Date of Birth", text="Date of Birth", anchor="center")
                tree.heading("Location", text="Location", anchor="center")
                tree.heading("Joining Date", text="Joining Date", anchor="center")
                tree.heading("Salary", text="Salary", anchor="center")
                tree.heading("Department", text="Department", anchor="center")

                tree.column("#0", width=0,anchor="center")
                tree.column("SSn", width=50, anchor="center")
                tree.column("Name", width=200, anchor="center")
                tree.column("Date of Birth", width=100, anchor="center")
                tree.column("Location", width=100, anchor="center")
                tree.column("Joining Date", width=100, anchor="center")
                tree.column("Salary", width=100, anchor="center")
                tree.column("Department", width=100, anchor="center")

            for row in employees:
                tree.insert("", "end", values=row)
                tree.grid(row= 4, column=0, padx=20, pady=10)
            deleteButton = Button(nextDeleteFrame, text="SELECT", command=update)
            deleteButton.grid(row= 5, column=0, padx=20, pady=10)
        usingOptValue = usingOpt.get()
        if usingOptValue == '':
            messagebox.showwarning(title="Error", message="Select an option first.")
        else:
            for widget in window.winfo_children():
                widget.destroy()
            frame = Frame(window)
            

            nextDeleteFrame =LabelFrame(frame, text="Update An Employee")
            nextDeleteFrame.grid(row= 0, column=0, padx=20, pady=10)

            valueLable = Label(nextDeleteFrame, text=f"Enter {usingOptValue}")
            valueLable.grid(row=0, column=0)
            if  usingOptValue=='Birth Date' or usingOptValue=='Joining Date':
                valueEntry = tkcalendar.DateEntry(nextDeleteFrame, date_pattern='dd/mm/yyyy')
                valueEntry.grid(row=1, column=0)
                selection=2
            elif usingOptValue=='department':
                valueEntry=["",""]
                usingOpt.set("department.") 
                optMenu2 = OptionMenu(nextDeleteFrame,usingOpt,*["Accounts","Administration","Sales","","Research"])
                optMenu2.grid(row=1, column=0)
                selection=3
            else:
                valueEntry = Entry(nextDeleteFrame, width=100)
                valueEntry.grid(row=1, column=0)
                selection=4
            button = Button(nextDeleteFrame, text="Find", command=find)
            button.grid(row=2, column=0,sticky="news",padx=10, pady=10)
            button = Button(nextDeleteFrame ,text="Back", command=window.destroy)
            button.grid(row=3, column=0,sticky="news",padx=10, pady=10)
            frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    button = Button(findEmployeeFrame, text="Next", command=nextUpdate, width=25)
    button.grid(row=1, column=0,sticky="news",padx=10, pady=10)
    button = Button(findEmployeeFrame ,text="Cancel", command=window.destroy)
    button.grid(row=2, column=0,sticky="news",padx=10, pady=10)
    frame.pack()
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)
def allEmployeeScreen():
    window = Tk()

    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()

    windowWidth = int(screenWidth * 0.7)
    windowHeight = int(screenHeight * 0.7)
    window.geometry(f"{windowWidth}x{windowHeight}")
    employees  = sqlClient.getAllEmployees()
    if len(employees) == 0:
        messagebox.showwarning(title="Error", message="No employees in the detabase.")
    else:
        for widget in window.winfo_children():
           widget.pack_forget()
        frame = Frame(window)
        

        allEmployeeFrame =LabelFrame(frame, text="Employees")
        allEmployeeFrame.grid(row= 0, column=0, padx=20, pady=10)
        tree = ttk.Treeview(allEmployeeFrame, columns=("SSN", "Name","Location", "Date of Birth", "Joining Date", "Salary", "Department"))
        tree.heading("#0", text="", anchor="center") 
        #tree.heading("ID", text="ID", anchor="center")
        tree.heading("SSN", text="SSN", anchor="center")
        tree.heading("Name", text="Name", anchor="center")
        tree.heading("Date of Birth", text="Date of Birth", anchor="center")
        tree.heading("Location", text="Location", anchor="center")
        tree.heading("Joining Date", text="Joining Date", anchor="center")
        tree.heading("Salary", text="Salary", anchor="center")
        tree.heading("Department", text="Department", anchor="center")
        tree.column("#0", width=0,anchor="center")
        tree.column("SSN", width=50, anchor="center")
        tree.column("Name", width=200, anchor="center")
        tree.column("Date of Birth", width=100, anchor="center")
        tree.column("Location", width=100, anchor="center")
        tree.column("Joining Date", width=100, anchor="center")
        tree.column("Salary", width=100, anchor="center")
        tree.column("Department", width=100, anchor="center")

        for row in employees:
            tree.insert("", "end", values=row)
        tree.grid(row= 4, column=0, padx=20, pady=10)
        deleteButton = Button(allEmployeeFrame, text="Back", command=window.destroy)
        deleteButton.grid(row= 5, column=0, padx=20, pady=10)
        frame.pack()
        frame.place(relx=0.5, rely=0.5, anchor=CENTER)


def addDepScreen():
   
    window = Tk()

    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()

    windowWidth = int(screenWidth * 0.7)
    windowHeight = int(screenHeight * 0.7)
    window.geometry(f"{windowWidth}x{windowHeight}")
    for widget in window.winfo_children():
        widget.pack_forget()

    def entersData():
        Dname = DnameVar.get().capitalize()  # Capitalize department name
        Dnumber = DnumberVar.get()
        Mgr_ssn = Mgr_ssnEntry.get()
        phone = phoneEntry.get()
        if Dname and Dnumber and Mgr_ssn and phone:
            try:
                sqlClient.insertDepartment(dname=f'{Dname.capitalize()}',Dnumber=Dnumber, Mgr_ssn=Mgr_ssn,phone=phone)
                messagebox.showwarning(title="Success", message="New details been added to Department table.")
                DnameVar.set("")
                DnumberVar.set("")
                Mgr_ssnEntry.delete(0,END)
                phoneEntry.delete(0,END)
            except mysql.connector.errors.IntegrityError as err:
                if err.errno==1062:
                    window.destroy()
                    messagebox.showerror(title="Error", message="Department Number already exists. Please choose a different one or update the existing entry")
                else:
                # Handle other integrity errors if needed
                    raise err
               
        else:
            messagebox.showwarning(title="Error", message="All fields are required.")
        
    def update_department_number(selected_department):
        department_number_options = {
            "Account": "110099",
            "Administration": "111199",
            "Developers": "112299",
            "Logistics": "113399",
            "Research": "114499"
        }
        DnumberVar.set(department_number_options.get(selected_department, ""))
    def update_department_name(selected_department_number):
        department_name_options = {
            "110099": "Account",
            "111199": "Administration",
            "112299": "Developers",
            "113399": "Logistics",
            "114499": "Research"
        }
        DnameVar.set(department_name_options.get(selected_department_number, ""))

    frame = Frame(window)
    

    DepartmentFrame = LabelFrame(frame, text="Add An Employee")
    DepartmentFrame.grid(row=0, column=0, padx=20, pady=10)

    DnameLabel = Label(DepartmentFrame, text="Department Name")
    DnameLabel.grid(row=0, column=0)
    DnumberLabel = Label(DepartmentFrame, text="Department Number")
    DnumberLabel.grid(row=0, column=1)
    Mgr_ssnLabel = Label(DepartmentFrame, text="Manager SSN")
    Mgr_ssnLabel.grid(row=0, column=2)
    phoneLabel = Label(DepartmentFrame, text="Phone Number")
    phoneLabel.grid(row=2, column=0)

    DnameVar =StringVar(DepartmentFrame)
    DnameVar.set("")
    departmentMenu =OptionMenu(DepartmentFrame, DnameVar, *("Account", "Administration", "Developers", "Logistics", "Research"), command=update_department_number)
    departmentMenu.grid(row=1, column=0)

    DnumberVar = StringVar(DepartmentFrame)
    DnumberVar.set("")
    departmentMenu1 = OptionMenu(DepartmentFrame, DnumberVar,*("110099", "111199", "112299", "113399", "114499"),command=update_department_name)  # Initially empty
    departmentMenu1.grid(row=1, column=1)

    Mgr_ssnEntry = Entry(DepartmentFrame)
    phoneEntry = Entry(DepartmentFrame)
    Mgr_ssnEntry.grid(row=1, column=2)
    phoneEntry.grid(row=3, column=0)

    for widget in DepartmentFrame.winfo_children():
        widget.grid_configure(padx=10, pady=5)

    
    button = Button(frame, text="Save Department Details", command=entersData)
    button.grid(row=3, column=0, sticky="news", padx=20, pady=10)
    button = Button(frame, text="Cancel", command=window.destroy)  # Assuming departmentdetail exists elsewhere
    button.grid(row=4, column=0, sticky="news", padx=20, pady=10)
    frame.pack()
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    # Update department number on initial selection (optional)
# ... rest of your code
    update_department_number(DnameVar.get())  # Get initial department
    update_department_name(DnumberVar.get())

def update_department():
    window = Tk()

    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()

    windowWidth = int(screenWidth * 0.7)
    windowHeight = int(screenHeight * 0.7)
    window.geometry(f"{windowWidth}x{windowHeight}")
    for widget in window.winfo_children():
        widget.pack_forget()
    frame = Frame(window)
    frame.pack()

    finddepartmentFrame =LabelFrame(frame, text="Update An Employee")
    finddepartmentFrame.grid(row= 0, column=0, padx=20, pady=10)
    options = [
    "Mgr_SSN"
    ]
    usingOpt = StringVar(finddepartmentFrame)
    usingOpt.set("Find department Using")

    menu = OptionMenu(finddepartmentFrame, usingOpt, *options)
    menu.grid(row=0, column=0,padx=10, pady=10)
    def nextUpdate():

        def find():
            def update():
                    selecteddepartment = tree.selection()
                    if len(selecteddepartment) == 0:
                        messagebox.showwarning(title="Error", message="Select an employee first.")
                    else:
                        for item in selecteddepartment:
                            itemValue = tree.item(item, 'values')
                            ind = 0
                            if usingOptValue == "Mgr_SSN":
                                ind = 0
                            
                            if usingOptValue == 'Dnumber':
                                ind = 1
                            else:
                                ind = 7
                    for widget in window.winfo_children():
                        widget.destroy()
                    def entersData():
                        Dname = DnameVar.get().capitalize()  # Capitalize department name
                        Dnumber = DnumberVar.get()
                        Mgr_ssn = Mgr_ssnEntry.get()
                        phone = phoneEntry.get()
                        if Dname and Dnumber and Mgr_ssn and phone:
                            sqlClient.updatedepartment(method=usingOpt,value=itemValue,newValue=(f'{Dname.capitalize()}',Dnumber,Mgr_ssn,phone))
                            messagebox.showwarning(title="Success", message="New details been updated to Department table.")
                            allDepartmentScreen()
                        else:
                            messagebox.showwarning(title="Error", message="All fields are required.")
        
                    def update_department_number(selected_department):
                        department_number_options = {
                            "Account": "110099",
                            "Administration": "111199",
                            "Developers": "112299",
                            "Logistics": "113399",
                            "Research": "114499"
                         }
                        DnumberVar.set(department_number_options.get(selected_department, ""))
                    def update_department_name(selected_department_number):
                        department_name_options = {
                            "110099": "Account",
                            "111199": "Administration",
                            "112299": "Developers",
                            "113399": "Logistics",
                            "114499": "Research"
                        }
                        DnameVar.set(department_name_options.get(selected_department_number, ""))

                    frame = Frame(window)
    

                    DepartmentFrame = LabelFrame(frame, text="update department Manager")
                    DepartmentFrame.grid(row=0, column=0, padx=20, pady=10)

                    DnameLabel = Label(DepartmentFrame, text="Department Name")
                    DnameLabel.grid(row=0, column=0)
                    DnumberLabel = Label(DepartmentFrame, text="Department Number")
                    DnumberLabel.grid(row=0, column=1)
                    Mgr_ssnLabel = Label(DepartmentFrame, text="Manager SSN")
                    Mgr_ssnLabel.grid(row=0, column=2)
                    phoneLabel = Label(DepartmentFrame, text="Phone Number")
                    phoneLabel.grid(row=4, column=0)
                    def on_select_location(event):
                        selected_value = departmentMenu.get()  # Get the selected value from the menu
                        departmentMenu.set(selected_value)
                    DnameVar =StringVar(DepartmentFrame)
                    DnameVar.set("")
                    departmentMenu =OptionMenu(DepartmentFrame, DnameVar, *("Account", "Administration", "Developers", "Logistics", "Research"), command=update_department_number)
                    departmentMenu.grid(row=1, column=0)
                    departmentMenu.bind("<<ComboboxSelected>>", on_select_location)  # Bind the selection event
                    def copy_to_entry_location():
                        copyvalEntry.delete(0,END)  # Clear the entry box before copying
                        copyvalEntry.insert(0, DnameVar.get())
                    def on_select_department(event):
                        selected_value=departmentMenu1.get()
                        DnumberVar.set(selected_value)
                    button = Button(DepartmentFrame, text="Click", command=copy_to_entry_location)
                    button.grid(row=2, column=0)

                    copyvalEntry = Entry(DepartmentFrame)
                    copyvalEntry.grid(row=3, column=0)
                    copyvalEntry.insert(0,itemValue[0])
                    DnumberVar = StringVar(DepartmentFrame)
                    DnumberVar.set("")
                    departmentMenu1 = OptionMenu(DepartmentFrame, DnumberVar,*("110099", "111199", "112299", "113399", "114499"),command=update_department_name)  # Initially empty
                    departmentMenu1.grid(row=1, column=1)
                    departmentMenu1.bind("<<ComboboxSelected>>", on_select_department)  # Bind the selection event

                    def copy_to_entry_department():
                        copyvalEntry1.delete(0,END)  # Clear the entry box before copying
                        copyvalEntry1.insert(0, DnumberVar.get())
                        
                    button = Button(DepartmentFrame, text="Click", command=copy_to_entry_department)
                    button.grid(row=2, column=1)
                    copyvalEntry1 = Entry(DepartmentFrame)
                    copyvalEntry1.grid(row=3, column=1)
                    copyvalEntry1.insert(1,itemValue[1])
                    Mgr_ssnEntry = Entry(DepartmentFrame)
                    Mgr_ssnEntry.insert(2,itemValue[2])
                    Mgr_ssnEntry.grid(row=1, column=2)
                    phoneEntry = Entry(DepartmentFrame)
                    phoneEntry.insert(3,itemValue[3])
                    phoneEntry.grid(row=5, column=0)

                    for widget in DepartmentFrame.winfo_children():
                        widget.grid_configure(padx=10, pady=5)

    
                    button = Button(frame, text="Save Department Details", command=entersData)
                    button.grid(row=3, column=0, sticky="news", padx=20, pady=10)
                    button = Button(frame, text="Cancel", command=window.destroy)  # Assuming departmentdetail exists elsewhere
                    button.grid(row=4, column=0, sticky="news", padx=20, pady=10)
                    frame.pack()
                    frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    # Update department number on initial selection (optional)
# ... rest of your code
                    update_department_number(DnameVar.get())  # Get initial department
                    update_department_name(DnumberVar.get())
            dept=sqlClient.findEmployeedep(method=usingOptValue,value=valueEntry.get())
            if len(dept)==0:
                messagebox.showwarning(title="Error", message="No match found.")
            else:
                tree = ttk.Treeview(nextDeleteFrame, columns=("Dname","Dnumber","Mgr_SSN","phone"))
                tree.heading("#0", text="", anchor="center") 
                tree.heading("Dname", text="Dname", anchor="center")
                tree.heading("Dnumber", text="Dnumber", anchor="center")
                tree.heading("Mgr_SSN", text="Mgr_SSN", anchor="center")
                tree.heading("phone", text="phone", anchor="center")
            
                tree.column("#0", width=0,anchor="center")
                tree.column("Dname", width=50, anchor="center")
                tree.column("Dnumber", width=200, anchor="center")
                tree.column("Mgr_SSN", width=100, anchor="center")
                tree.column("phone", width=100, anchor="center")
            
            for row in dept:
                tree.insert("", "end", values=row[:])
                tree.grid(row= 4, column=0, padx=20, pady=10)
            deleteButton = Button(nextDeleteFrame, text="SELECT", command=update)
            deleteButton.grid(row= 5, column=0, padx=20, pady=10)
        usingOptValue=usingOpt.get()
        if usingOptValue=='':
                messagebox.showwarning(title="Error", message="Select an option first.")
        else:
            for widget in window.winfo_children():
                widget.destroy()
            frame = Frame(window)
            

            nextDeleteFrame =LabelFrame(frame, text="Update a department")
            nextDeleteFrame.grid(row= 0, column=0, padx=20, pady=10)
            valueEntry = Entry(nextDeleteFrame, width=100)
            valueEntry.grid(row=1, column=0)
            button = Button(nextDeleteFrame, text="Find", command=find)
            button.grid(row=2, column=0,sticky="news",padx=10, pady=10)
            button = Button(nextDeleteFrame ,text="Back", command=window.destroy)
            button.grid(row=3, column=0,sticky="news",padx=10, pady=10)
            frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    button = Button(finddepartmentFrame, text="Next", command=nextUpdate, width=25)
    button.grid(row=1, column=0,sticky="news",padx=10, pady=10)
    button = Button(finddepartmentFrame ,text="Cancel", command=window.destroy)
    button.grid(row=2, column=0,sticky="news",padx=10, pady=10)
    frame.pack()
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)
                

def allDepartmentScreen():
    window = Tk()

    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()

    windowWidth = int(screenWidth * 0.7)
    windowHeight = int(screenHeight * 0.7)
    window.geometry(f"{windowWidth}x{windowHeight}")
    department  = sqlClient.getAlldepartment()
    if len(department) == 0:
        messagebox.showwarning(title="Error", message="No Department in the database.")
    else:
        for widget in window.winfo_children():
            widget.pack_forget()
        frame = Frame(window)
        

        alldepartmentFrame =LabelFrame(frame, text="Department")
        alldepartmentFrame.grid(row= 0, column=0, padx=20, pady=10)
        tree = ttk.Treeview(alldepartmentFrame, columns=("Department Name", "Department code","Department Manager SSN","Manager Phone"))
        
        tree.heading("Department Name", text="Department Name", anchor="center")
        tree.heading("Department code", text="Department code", anchor="center")
        tree.heading("Department Manager SSN", text="Department Manager SSN", anchor="center")
        tree.heading("Manager Phone", text="Manager Phone", anchor="center")
        tree.column("#0", width=0,anchor="center")
        tree.column("Department Name", width=100, anchor="center")
        tree.column("Department code", width=100, anchor="center")
        tree.column("Department Manager SSN", width=100, anchor="center")
        tree.column("Manager Phone", width=100, anchor="center")
        
        for row in department:
            tree.insert("", "end", values=row)
        tree.grid(row= 4, column=0, padx=20, pady=10)
        deleteButton = Button(alldepartmentFrame, text="Back", command=window.destroy)
        deleteButton.grid(row= 5, column=0, padx=20, pady=10)
        frame.pack()    
        frame.place(relx=0.5, rely=0.5, anchor=CENTER)

def addDlocation():

    window = Tk()

    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()

    windowWidth = int(screenWidth * 0.7)
    windowHeight = int(screenHeight * 0.7)
    window.geometry(f"{windowWidth}x{windowHeight}")
    for widget in window.winfo_children():
        widget.pack_forget()
    def entersData():
        Dnumber = DnumberVar.get()
        Dlocation = locationVar.get()
        try:
            if Dnumber and  Dlocation:
                sqlClient.insertDepartmentlocation(Dnumber=Dnumber,Dlocation=f'{Dlocation.capitalize()}')
                messagebox.showwarning(title="Success", message="New details been added to Department table.")
                DnumberVar.delete(0,END)
                locationVar.delete(0,END)
            else: 
                messagebox.showwarning(title="Error", message="All fields are required.")
        except mysql.connector.errors.IntegrityError as err:
            messagebox.showerror(title="Error",message="The department locaiton you want to add is seems to be already exsits, please try to update the value")
    frame = Frame(window)
    

    DepartmentFrame =LabelFrame(frame, text="Add Department location")
    DepartmentFrame.grid(row= 0, column=0, padx=20, pady=10)

    DnumberLabel= Label(DepartmentFrame, text="Department Number")
    DnumberLabel.grid(row=0, column=0)

    DlocationLabel= Label(DepartmentFrame, text="Department location")
    DlocationLabel.grid(row=0, column=1)
    
    DnumberVar = StringVar(DepartmentFrame)
    DnumberVar.set("")
    departmentMenu1 = OptionMenu(DepartmentFrame, DnumberVar,*("110099", "111199", "112299", "113399", "114499"))  # Initially empty
    departmentMenu1.grid(row=1, column=0)
    locationVar=StringVar(DepartmentFrame)
    locationVar.set("")
    locationMenu=OptionMenu(DepartmentFrame, locationVar, *("Banglore","Chennai","Hyderabad","Delhi","Mumbai"))
    locationMenu.grid(row=1, column=1)



    for widget in DepartmentFrame.winfo_children():
        widget.grid_configure(padx=10, pady=5)

    button = Button(frame, text="Save Department Details", command= entersData)
    button.grid(row=3, column=0, sticky="news", padx=20, pady=10)
    button = Button(frame, text="Cancel", command= window.destroy)
    button.grid(row=4, column=0, sticky="news", padx=20, pady=10)
    frame.pack()
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)

def update_department_location():
    window = Tk()

    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()

    windowWidth = int(screenWidth * 0.7)
    windowHeight = int(screenHeight * 0.7)
    window.geometry(f"{windowWidth}x{windowHeight}")
    for widget in window.winfo_children():
        widget.pack_forget()
    frame = Frame(window)
    frame.pack()

    finddepartmentlocFrame =LabelFrame(frame, text="Update department location")
    finddepartmentlocFrame.grid(row= 0, column=0, padx=20, pady=10)
    options = [
    "Dnumber"
    ]
    usingOpt = StringVar(finddepartmentlocFrame)
    usingOpt.set("Find department Location Using")

    menu = OptionMenu(finddepartmentlocFrame, usingOpt, *options)
    menu.grid(row=0, column=0,padx=10, pady=10)
    def nextUpdate():

        def find():
            def update():
                    selecteddepartmentloc = tree.selection()
                    if len(selecteddepartmentloc) == 0:
                        messagebox.showwarning(title="Error", message="Select an option first.")
                    else:
                        for item in selecteddepartmentloc:
                            itemValue = tree.item(item, 'values')
                            ind = 0
                            if usingOptValue == "Dnumber":
                                ind = 0
                            else:
                                ind = 7
                    for widget in window.winfo_children():
                        widget.destroy()
                    def entersData():
                            
                        Dlocation = DlocationVar.get()
                       
                        if Dlocation :
                            window.destroy()
                            sqlClient.updatedepartmentlocation(method=usingOpt,value=itemValue,newValue=copyvalEntry)
                            messagebox.showwarning(title="Success", message="New details been updated to Department location table.")
                            allDepartmentScreenloc()
                        else:
                            messagebox.showwarning(title="Error", message="All fields are required.")
        
                        
                    frame = Frame(window)
    

                    DepartmentlocFrame = LabelFrame(frame, text="update department Manager")
                    DepartmentlocFrame.grid(row=0, column=0, padx=20, pady=10)

                    DlocationLabel = Label(DepartmentlocFrame, text="Department Location")
                    DlocationLabel.grid(row=0, column=0)
                        
                        
                    def on_select_location(event):
                        selected_value = departmentMenu.get()  # Get the selected value from the menu
                        departmentMenu.set(selected_value)
                    DlocationVar =StringVar(DepartmentlocFrame)
                    DlocationVar.set("Enter Department Location")
                    departmentMenu =OptionMenu(DepartmentlocFrame, DlocationVar, *("Bengaluru", "Chennai", "Delhi", "Kolkata", "Hyderabad"))
                    departmentMenu.grid(row=1, column=0)
                    departmentMenu.bind("<<ComboboxSelected>>", on_select_location)  # Bind the selection event
                        
                    copyvalEntry = Entry(DepartmentlocFrame)
                    def copy_to_entry_location():
                        copyvalEntry.delete(0,END)  # Clear the entry box before copying
                        copyvalEntry.insert(0, DlocationVar.get())
                    button=Button(DepartmentlocFrame,text='Copy',command=copy_to_entry_location)
                    button.grid(row=1,column=1)
                    copyvalEntry.grid(row=3, column=0)
                    copyvalEntry.insert(1,itemValue[1])

                        
                    for widget in DepartmentlocFrame.winfo_children():
                        widget.grid_configure(padx=10, pady=5)

    
                    button = Button(frame, text="Save Department Details", command=entersData)
                    button.grid(row=4, column=0, sticky="news", padx=20, pady=10)
                    button = Button(frame, text="Cancel", command=window.destroy)  # Assuming departmentdetail exists elsewhere
                    button.grid(row=5, column=0, sticky="news", padx=20, pady=10)
                    frame.pack()
                    frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    # Update department number on initial selection (optional)
# ... rest of your code
                        
            deptloc=sqlClient.findDepartmentLOC(method=usingOptValue,value=valueEntry.get(),)
            if len(deptloc)==0:
                messagebox.showwarning(title="Error", message="No match found.")
            else:
                tree = ttk.Treeview(nextDeleteFrame, columns=("Department number","Location"))
                tree.heading("#0", text="", anchor="center") 
                tree.heading("Department number", text="Department number", anchor="center")
                tree.heading("Location", text="Location", anchor="center")
                
            
                tree.column("#0", width=0,anchor="center")
                tree.column("Department number", width=200, anchor="center")
                tree.column("Location", width=100, anchor="center")
            
            for row in deptloc:
                tree.insert("", "end", values=row[:])
                tree.grid(row= 4, column=0, padx=20, pady=10)
            deleteButton = Button(nextDeleteFrame, text="SELECT", command=update)
            deleteButton.grid(row= 5, column=0, padx=20, pady=10)
            
        usingOptValue=usingOpt.get()
        if usingOptValue=='':
                messagebox.showwarning(title="Error", message="Select an option first.")

        else:
            for widget in window.winfo_children():
                widget.destroy()
            frame = Frame(window)
            

            nextDeleteFrame =LabelFrame(frame, text="Update a department location")
            def on_select_location1(event):
                    selected_value = departmentMenu.get()  # Get the selected value from the menu
                    departmentMenu.set(selected_value)
            DlocationVar =StringVar(nextDeleteFrame)
            DlocationVar.set("Enter Department Location")
            departmentMenu =OptionMenu(nextDeleteFrame, DlocationVar, *("110099", "111199", "112299", "113399", "114499"))
            departmentMenu.grid(row=1, column=0)
            departmentMenu.bind("<<ComboboxSelected>>", on_select_location1)  # Bind the selection event
                        
            valueEntry = Entry(nextDeleteFrame)
            def copy_to_entry_location1():
                    valueEntry.delete(0,END)  # Clear the entry box before copying
                    valueEntry.insert(0, DlocationVar.get())
            button=Button(nextDeleteFrame,text='Copy',command=copy_to_entry_location1)
            button.grid(row=1,column=1)
                #copyvalEntry.grid(row=3, column=0)
                #copyvalEntry.insert(1,itemValue[1])
            nextDeleteFrame.grid(row= 0, column=0, padx=20, pady=10)
            valueEntry = Entry(nextDeleteFrame, width=100)
            valueEntry.grid(row=2, column=0)
            button = Button(nextDeleteFrame, text="Find", command=find)
            button.grid(row=3, column=0,sticky="news",padx=10, pady=10)
            button = Button(nextDeleteFrame ,text="Back", command=window.destroy)
            button.grid(row=4, column=0,sticky="news",padx=10, pady=10)
            frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    button = Button(finddepartmentlocFrame, text="Next", command=nextUpdate, width=25)
    button.grid(row=1, column=0,sticky="news",padx=10, pady=10)
    button = Button(finddepartmentlocFrame ,text="Cancel", command=window.destroy)
    button.grid(row=2, column=0,sticky="news",padx=10, pady=10)
    frame.pack()
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)

def allDepartmentScreen():

    window = Tk()

    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()

    windowWidth = int(screenWidth * 0.7)
    windowHeight = int(screenHeight * 0.7)
    window.geometry(f"{windowWidth}x{windowHeight}")
    department  = sqlClient.getAlldepartment()
    if len(department) == 0:
        messagebox.showwarning(title="Error", message="No Department in the database.")
    else:
        for widget in window.winfo_children():
            widget.pack_forget()
        frame = Frame(window)
        

        alldepartmentFrame =LabelFrame(frame, text="Department")
        alldepartmentFrame.grid(row= 0, column=0, padx=50, pady=10)
        tree = ttk.Treeview(alldepartmentFrame, columns=("Department Name", "Department code","Dept Mgr SSN","Manager Phone"))
        
        tree.heading("Department Name", text="Department Name", anchor="center")
        tree.heading("Department code", text="Department code", anchor="center")
        tree.heading("Dept Mgr SSN", text="Dept Mgr SSN", anchor="center")
        tree.heading("Manager Phone", text="Manager Phone", anchor="center")
        tree.column("#0", width=0,anchor="center")
        tree.column("Department Name", width=100, anchor="center")
        tree.column("Department code", width=100, anchor="center")
        tree.column("Dept Mgr SSN", width=100, anchor="center")
        tree.column("Manager Phone", width=100, anchor="center")
        
        for row in department:
            tree.insert("", "end", values=row)
        tree.grid(row= 4, column=0, padx=20, pady=10)
        deleteButton = Button(alldepartmentFrame, text="Back", command=window.destroy)
        deleteButton.grid(row= 5, column=0, padx=20, pady=10)
        frame.pack()
        frame.place(relx=0.5, rely=0.5, anchor=CENTER)
def allDepartmentScreenloc():
    window = Tk()

    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()

    windowWidth = int(screenWidth * 0.7)
    windowHeight = int(screenHeight * 0.7)
    window.geometry(f"{windowWidth}x{windowHeight}")

    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()

    departmentloc  = sqlClient.getalldepartmentloc()
    if len(departmentloc) == 0:
        messagebox.showwarning(title="Error", message="No Department location in the database.")
    else:
        for widget in window.winfo_children():
            widget.pack_forget()
        frame = Frame(window)
     

        alldepartmentlocFrame =LabelFrame(frame, text="Department Location")
        alldepartmentlocFrame.grid(row= 0, column=0, padx=20, pady=10)
        tree = ttk.Treeview(alldepartmentlocFrame, columns=("Department Number", "Department Location"))
        
        tree.heading("Department Number", text="Department Number", anchor="center")
        tree.heading("Department Location", text="Department Location", anchor="center")
        
        tree.column("#0", width=0,anchor="center")
        tree.column("Department Number", width=150, anchor="center")
        tree.column("Department Location", width=150, anchor="center")
        
        for row in departmentloc:
            tree.insert("", "end", values=row)
        tree.grid(row= 4, column=0, padx=20, pady=10)
        deleteButton = Button(alldepartmentlocFrame, text="Back", command=window.destroy)
        deleteButton.grid(row= 5, column=0, padx=20, pady=10)
        frame.pack()
        frame.place(relx=0.5, rely=0.5, anchor=CENTER)
def addproject():

    window = Tk()

    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()

    windowWidth = int(screenWidth * 0.7)
    windowHeight = int(screenHeight * 0.7)
    window.geometry(f"{windowWidth}x{windowHeight}")
    for widget in window.winfo_children():
        widget.pack_forget()
    def entersData():
        Pname = PnameEntry.get()
        Pnumber = PnumberEntry.get()
        Plocation = locationVar.get()
        Dnumber = DnumberVar.get()
        try:
            if Pname and Pnumber and Plocation and Dnumber:
                sqlClient.insertproject(Pname=f'{Pname.capitalize()}',Pnumber=Pnumber, Plocation=f'{Plocation.capitalize()}',Dnumber=Dnumber)
                messagebox.showwarning(title="Success", message="New details been added to Department table.")
                PnameEntry.delete(0,END)
                PnumberEntry.delete(0,END)
                locationVar.set("")
                DnumberVar.set("")
                window.destroy()
            else: 
                messagebox.showwarning(title="Error", message="All fields are required.")
        except mysql.connector.errors.IntegrityError as err:
            messagebox.showerror(title="Error", message=("The Entered Project id already exsisted please update it or enter another project id inacse it's new"))
    frame = Frame(window)
    

    projectFrame =LabelFrame(frame, text="Add a project")
    projectFrame.grid(row= 0, column=0, padx=20, pady=10)

    PnameLabel= Label(projectFrame, text="Project Name")
    PnameLabel.grid(row=0, column=0)
    PnumberLabel= Label(projectFrame, text="Project Number")
    PnumberLabel.grid(row=0, column=1)
    locationVar= Label(projectFrame, text="Project location")
    locationVar.grid(row=0, column=2)
    phoneLabel= Label(projectFrame, text="Departmen Number")
    phoneLabel.grid(row=2, column=0)

    PnameEntry = Entry(projectFrame)
    PnumberEntry = Entry(projectFrame)
    #PlocationEntry = Entry(projectFrame)
    #DnumberEntry = Entry(projectFrame)
    PnameEntry.grid(row=1, column=0)
    PnumberEntry.grid(row=1, column=1)
    #PlocationEntry.grid(row=1, column=2)
    #DnumberEntry.grid(row=3, column=0)
    locationVar=StringVar(projectFrame)
    locationVar.set("")
    locationMenu=OptionMenu(projectFrame, locationVar, *("Banglore","Chennai","Hyderabad","Delhi","Mumbai"))
    locationMenu.grid(row=1, column=2)

    DnumberVar=StringVar(projectFrame)
    DnumberVar.set("Department Number")
    departmentMenu1=OptionMenu(projectFrame,DnumberVar, *("110099", "111199", "112299", "113399", "114499"))
    departmentMenu1.grid(row=3, column=0)

    for widget in projectFrame.winfo_children():
        widget.grid_configure(padx=10, pady=5)

    button = Button(frame, text="Save Department Details", command= entersData)
    button.grid(row=3, column=0, sticky="news", padx=20, pady=10)
    button = Button(frame, text="Cancel", command= window.destroy)
    button.grid(row=4, column=0, sticky="news", padx=20, pady=10)
    frame.pack()
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)
def updateProjectScreen():
    window=Tk()
    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()

    windowWidth = int(screenWidth * 0.7)
    windowHeight = int(screenHeight * 0.7)
    window.geometry(f"{windowWidth}x{windowHeight}")
    
    for widget in window.winfo_children():
        widget.destroy()
    frame = Frame(window)
    frame.pack()

    findprojectFrame =LabelFrame(frame, text="Find prject")
    findprojectFrame.grid(row= 0, column=0, padx=20, pady=10)
    options = [
    'Project ID',
    'Project Name',
    'Project location',
    'Department Number'
    ]
    usingOpt = StringVar(findprojectFrame)
    usingOpt.set("Find Project Using")

    menu = OptionMenu(findprojectFrame, usingOpt, *options)
    menu.grid(row=0, column=0,padx=10, pady=10)

    def nextUpdate():

        def find():
            def update():
                selectedproject = tree.selection()
                if len(selectedproject) == 0:
                    messagebox.showwarning(title="Error", message="Select an employee first.")
                else:
                    for item in selectedproject:
                        itemValue = tree.item(item, 'values')
                        ind = 0
                        if usingOptValue == 'Project ID':
                            ind = 0
                        elif usingOptValue== 'Project Name':
                            ind = 1
                        elif usingOptValue == 'Project Location':
                            ind = 2
                        elif usingOptValue== 'Department Number':
                            ind =3
                        
                        else:
                            ind = 7
                    for widget in window.winfo_children():
                        widget.destroy()
                    def entersData():
                        Pname = PnameEntry.get().capitalize()
                        #Pnumber = PnumberEntry.get()
                        Plocation = locationVar.get()
                        Dnumber = departmentVar.get()
                        try:
                            if Pname and Plocation and Dnumber:
                                sqlClient.updateproject(method=usingOptValue,value=itemValue,newValue=(f'{Pname.capitalize()}',f'{Plocation.capitalize()}',Dnumber))
                                window.destroy()
                                messagebox.showwarning(title="Success", message="New details been added to Department table.")
                            else: 
                                messagebox.showwarning(title="Error", message="All fields are required.")
                        except mysql.connector.errors.IntegrityError as err:
                            window.destroy()
                            messagebox.showerror(title="Error",message="As this Project is in progress you cannot Change the project ID. In order to change it please delete it from Prject assignment")
                    frame = Frame(window)
    

                    projectFrame =LabelFrame(frame, text="Add a project")
                    projectFrame.grid(row= 0, column=0, padx=20, pady=10)

                    PnameLabel= Label(projectFrame, text="Project Name")
                    PnameLabel.grid(row=0, column=0)
                    #PnumberLabel= Label(projectFrame, text="Project Number")
                    #PnumberLabel.grid(row=0, column=1)
                    locationVar= Label(projectFrame, text="Project location")
                    locationVar.grid(row=0, column=2)
                    DnumberLabel= Label(projectFrame, text="Department Number")
                    DnumberLabel.grid(row=2, column=0)

                    PnameEntry = Entry(projectFrame)
                    PnameEntry.insert(0,itemValue[0])
                    PnameEntry.grid(row=1, column=0)
                    #PnumberEntry = Entry(projectFrame)
                    #PnumberEntry.insert(1,itemValue[1])
                    #PnumberEntry.grid(row=1, column=1)
    
                    def on_select_location(event):
                        selected_value=usingOpt1.get()
                        locationVar.set(selected_value)
                            
                    locationVar = StringVar(projectFrame)
                    locationVar.set("")

                    locationList=[
                            "Bengaluru",
                            "Chennai",
                            "Delhi",
                            "Kolkata",
                            "Hyderabad",
                            ]
                    usingOpt3 = OptionMenu(projectFrame,locationVar,*locationList)
                    usingOpt3.grid(row=1, column=2)
                    usingOpt3.bind("<<ComboboxSelected>>", on_select_location)  # Bind the selection event
                    def copy_to_entry_location():
                            copyvalEntry.delete(0,END)  # Clear the entry box before copying
                            copyvalEntry.insert(0, locationVar.get())  # Insert the copied value at the beginning

            
                    button = Button(projectFrame, text="Click", command=copy_to_entry_location)
                    button.grid(row=2, column=2)

                    copyvalEntry = Entry(projectFrame)
                    copyvalEntry.grid(row=3, column=2)
                    def on_select_department(event):
                            selected_value=usingOpt1.get()
                            departmentVar.set(selected_value)
                    departmentVar=StringVar(projectFrame)
                    departmentVar.set("")
                    departmentList = [
                            "110099",
                            "111199",
                            "112299",
                            "113399",
                            "114499",
                        ]
                    usingOpt1 = OptionMenu(projectFrame,departmentVar,*departmentList)
                    usingOpt1.grid(row=3, column=0)
                    usingOpt1.bind("<<ComboboxSelected>>", on_select_department)  # Bind the selection event
                    def copy_to_entry_department():
                            copyvalEntry1.delete(0,END)  # Clear the entry box before copying
                            copyvalEntry1.insert(0, departmentVar.get())  # Insert the copied value at the beginning
                    
                    

                    button = Button(projectFrame, text="Click", command=copy_to_entry_department)
                    button.grid(row=4, column=0)

                    copyvalEntry1 = Entry(projectFrame)
                    copyvalEntry1.grid(row=5, column=0)
                    for widget in projectFrame.winfo_children():
                        widget.grid_configure(padx=10, pady=5)


                    
                    
                    button = Button(frame, text="Update project Details", command= entersData)
                    button.grid(row=6, column=0, sticky="news", padx=20, pady=10)
                    button = Button(frame, text="Cancel", command= window.destroy)
                    button.grid(row=7, column=0, sticky="news", padx=20, pady=10)
                    frame.place(relx=0.5, rely=0.5, anchor=CENTER)
            
            project = sqlClient.findproject(method=usingOptValue, value=valueEntry.get())
            if len(project) == 0:
                messagebox.showwarning(title="Error", message="No match found.")
            else:
                tree = ttk.Treeview(nextDeleteFrame, columns=("P-Name","P-ID","P-Location","P-Department"))
                tree.heading("#0", text="", anchor="center") 
                tree.heading("P-Name", text="P-Name", anchor="center")
                tree.heading("P-ID", text="P-ID", anchor="center")
                tree.heading("P-Location", text="P-Location", anchor="center")
                tree.heading("P-Department", text="P-Department", anchor="center")

                tree.column("#0", width=0,anchor="center")
                tree.column("P-Name", width=200, anchor="center")
                tree.column("P-ID", width=50, anchor="center")
                tree.column("P-Location", width=200, anchor="center")
                tree.column("P-Department", width=100, anchor="center")

            for row in project:
                tree.insert("", "end", values=row)
                tree.grid(row= 4, column=0, padx=20, pady=10)
            deleteButton = Button(nextDeleteFrame, text="SELECT", command=update)
            deleteButton.grid(row= 5, column=0, padx=20, pady=10)
        usingOptValue = usingOpt.get()
        if usingOptValue == '':
            messagebox.showwarning(title="Error", message="Select an option first.")
        else:
            for widget in window.winfo_children():
                widget.destroy()
            frame = Frame(window)
            

            nextDeleteFrame =LabelFrame(frame, text="Find Project")
            nextDeleteFrame.grid(row= 0, column=0, padx=20, pady=10)

            valueLable = Label(nextDeleteFrame, text=f"Enter {usingOptValue}")
            valueLable.grid(row=0, column=0)
            valueEntry = Entry(nextDeleteFrame, width=100)
            valueEntry.grid(row=1, column=0)
            
            button = Button(nextDeleteFrame, text="Find", command=find)
            button.grid(row=2, column=0,sticky="news",padx=10, pady=10)
            button = Button(nextDeleteFrame ,text="Back", command=window.destroy)
            button.grid(row=3, column=0,sticky="news",padx=10, pady=10)
            frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    button = Button(findprojectFrame, text="Next", command=nextUpdate, width=25)
    button.grid(row=1, column=0,sticky="news",padx=10, pady=10)
    button = Button(findprojectFrame ,text="Cancel", command=window.destroy)
    button.grid(row=2, column=0,sticky="news",padx=10, pady=10)
    frame.pack()
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)


def allprojectScreen():
    window = Tk()

    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()

    windowWidth = int(screenWidth * 0.7)
    windowHeight = int(screenHeight * 0.7)
    window.geometry(f"{windowWidth}x{windowHeight}")
    project  = sqlClient.getallproject()
    if len(project) == 0:
        messagebox.showwarning(title="Error", message="No Department in the database.")
    else:
        for widget in window.winfo_children():
            widget.pack_forget()
        frame = Frame(window)
        

        alldepartmentFrame =LabelFrame(frame, text="Project")
        alldepartmentFrame.grid(row= 0, column=0, padx=20, pady=10)
        tree = ttk.Treeview(alldepartmentFrame, columns=("Project Name", "Project Number","Project location","Department Number"))
        
        tree.heading("Project Name", text="Project Name", anchor="center")
        tree.heading("Project Number", text="Project Number", anchor="center")
        tree.heading("Project location", text="Project location", anchor="center")
        tree.heading("Department Number", text="Department Number", anchor="center")
        tree.column("#0", width=0,anchor="center")
        tree.column("Project Name", width=100, anchor="center")
        tree.column("Project Number", width=100, anchor="center")
        tree.column("Project location", width=100, anchor="center")
        tree.column("Department Number", width=100, anchor="center")
        
        for row in project:
            tree.insert("", "end", values=row)
        tree.grid(row= 4, column=0, padx=20, pady=10)
        deleteButton = Button(alldepartmentFrame, text="Back", command=window.destroy)
        deleteButton.grid(row= 5, column=0, padx=20, pady=10)
        frame.pack()
        frame.place(relx=0.5, rely=0.5, anchor=CENTER)
def working_details():
    window = Tk()

    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()

    windowWidth = int(screenWidth * 0.7)
    windowHeight = int(screenHeight * 0.7)
    window.geometry(f"{windowWidth}x{windowHeight}")
    working  = sqlClient.workingScreen()
    if len(working) == 0:
        messagebox.showwarning(title="Error", message="No  Working Hours data in the database.")
    else:
        for widget in window.winfo_children():
            widget.pack_forget()
        frame = Frame(window)
        

        workingFrame =LabelFrame(frame, text="Employee and project working details")
        workingFrame.grid(row= 0, column=0)
        tree = ttk.Treeview(workingFrame, columns=("ESSN","Project Number", "Working Hours"))

        tree.heading("ESSN", text="ESSN", anchor="center")
        tree.heading("Project Number", text="Project  Number", anchor="center")
        tree.heading("Working Hours", text="Working Hours", anchor="center")
        tree.column("#0", width=0,anchor="center")
        tree.column("ESSN", width=100, anchor="center")
        tree.column("Project Number", width=100, anchor="center")
        tree.column("Working Hours", width=100, anchor="center")
        
        for row in working:
            tree.insert("", "end", values=row)
        tree.grid(row= 0, column=0)
        deleteButton = Button(workingFrame, text="Back", command=window.destroy)
        deleteButton.grid(row= 5, column=0)
        frame.pack()
        frame.place(relx=0.5, rely=0.5, anchor=CENTER)
def addworking():
    window = Tk()

    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()

    windowWidth = int(screenWidth * 0.7)
    windowHeight = int(screenHeight * 0.7)
    window.geometry(f"{windowWidth}x{windowHeight}")
    for widget in window.winfo_children():
        widget.pack_forget()
    def entersData():
        Essn = EssnEntry.get()
        Pnumber = PnumberEntry.get()
        workinghour = workinghourEntry.get()
        if Essn and  Pnumber and workinghour:
            sqlClient.insertworking(Essn=Essn, Pnumber=Pnumber, Hours=workinghour)
            messagebox.showwarning(title="Success", message="New details been added to working hours table.")
            EssnEntry.delete(0,END)
            PnumberEntry.delete(0,END)
            workinghourEntry.delete(0,END)
        else: 
            messagebox.showwarning(title="Error", message="All fields are required.")

    frame = Frame(window)
    #frame.pack()

    workingFrame =LabelFrame(frame, text="Working Hour details")
    workingFrame.grid(row= 0, column=0, padx=20, pady=10)

    EssnLabel= Label(workingFrame, text="Essn")
    EssnLabel.grid(row=0, column=0)
    PnumberLabel= Label(workingFrame, text="Project number")
    PnumberLabel.grid(row=0, column=1)
    workinghourLabel= Label(workingFrame, text="Working Hours")
    workinghourLabel.grid(row=0, column=2)
    
    EssnEntry = Entry(workingFrame)
    EssnEntry.grid(row=1, column=0)
    PnumberEntry = Entry(workingFrame)
    PnumberEntry.grid(row=1, column=1)
    workinghourEntry = Entry(workingFrame)
    workinghourEntry.grid(row=1, column=2)

    for widget in workingFrame.winfo_children():
        widget.grid_configure(padx=10, pady=5)

    button = Button(frame, text="Save Department Details", command= entersData)
    button.grid(row=3, column=0, sticky="news", padx=20, pady=10)
    button = Button(frame, text="Cancel", command= window.destroy)
    button.grid(row=4, column=0, sticky="news", padx=20, pady=10)
    frame.pack()
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)

def updateworking():
    window6=Tk()
    screen6Width = window6.winfo_screenwidth()
    screen6Height = window6.winfo_screenheight()

    window6Width = int(screenWidth * 0.7)
    window6Height = int(screenHeight * 0.7)
    window6.geometry(f"{window6Width}x{window6Height}")
    
    for widget in window6.winfo_children():
        widget.pack_forget()
    frame = Frame(window6)
    frame.pack()

    findworkingFrame =LabelFrame(frame, text="Update working details")
    findworkingFrame.grid(row= 0, column=0, padx=20, pady=10)
    options = [
    'Employee SSN',
    'Project Number',
    'Working hour',
    ]
    usingOpt = StringVar(findworkingFrame)
    usingOpt.set("Find Details Using")

    menu = OptionMenu(findworkingFrame, usingOpt, *options)
    menu.grid(row=0, column=0,padx=10, pady=10)

    def nextUpdate():

        def find():
            def update():
                selectedwork = tree.selection()
                if len(selectedwork) == 0:
                    messagebox.showwarning(title="Error", message="Select an employee first.")
                else:
                    for item in selectedwork:
                        itemValue = tree.item(item, 'values')
                        ind = 0
                        if usingOptValue == 'Project ID':
                            ind = 0
                        elif usingOptValue== 'Project Name':
                            ind = 1
                        elif usingOptValue == 'Project Location':
                            ind = 2
                        elif usingOptValue== 'Department Number':
                            ind =3
                        
                        else:
                            ind = 7
                    for widget in window6.winfo_children():
                        widget.destroy()
                    def entersData():
                        Essn = EssnEntry.get()
                        Pnumber = PnumberEntry.get()
                        workinghour = workinghourEntry.get()
                        try:
                            if Essn and  Pnumber and workinghour:
                                sqlClient.updateworking(method=usingOpt,value=itemValue,newValue=(Essn,Pnumber,workinghour))
                                #window.destroy()
                                messagebox.showwarning(title="Success", message="New details been added to working hours table.")

                            else: 
                                messagebox.showwarning(title="Error", message="All fields are required.")
                        except mysql.connector.IntegrityError as err:
                            window6.destroy()
                            messagebox.showerror("Error","Failed to add data.")
                    frame = Frame(window6)


                    workingFrame =LabelFrame(frame, text="Working Hour details")
                    workingFrame.grid(row= 0, column=0, padx=20, pady=10)

                    EssnLabel= Label(workingFrame, text="Essn")
                    EssnLabel.grid(row=0, column=0)
                    PnumberLabel= Label(workingFrame, text="Project number")
                    PnumberLabel.grid(row=0, column=1)
                    workinghourLabel= Label(workingFrame, text="Working Hours")
                    workinghourLabel.grid(row=0, column=2)
    
                    EssnEntry = Entry(workingFrame)
                    EssnEntry.insert(0,itemValue[0])
                    EssnEntry.grid(row=1, column=0)
                    PnumberEntry = Entry(workingFrame)
                    PnumberEntry.insert(1, itemValue[1])
                    PnumberEntry.grid(row=1, column=1)
                    workinghourEntry = Entry(workingFrame)
                    workinghourEntry.insert(2,itemValue[2])
                    workinghourEntry.grid(row=1, column=2)

                    for widget in workingFrame.winfo_children():
                        widget.grid_configure(padx=10, pady=5)

                    button = Button(frame, text="Update project Details", command= entersData)
                    button.grid(row=6, column=0, sticky="news", padx=20, pady=10)
                    button = Button(frame, text="Cancel", command= window6.destroy)
                    button.grid(row=7, column=0, sticky="news", padx=20, pady=10)
                    frame.place(relx=0.5, rely=0.5, anchor=CENTER)
            working = sqlClient.findworking(method=usingOptValue, value=valueEntry.get())
            if len(working) == 0:
                messagebox.showwarning(title="Error", message="No match found.")
            else:
                tree = ttk.Treeview(nextDeleteFrame, columns=("ESSN","PNumber","Hours-spent"))
                tree.heading("#0", text="", anchor="center") 
                tree.heading("ESSN", text="ESSN", anchor="center")
                tree.heading("PNumber", text="PNumber", anchor="center")
                tree.heading("Hours-spent", text="Hours spent", anchor="center")

                tree.column("#0", width=0,anchor="center")
                tree.column("ESSN", width=50, anchor="center")
                tree.column("PNumber", width=200, anchor="center")
                tree.column("Hours-spent", width=100, anchor="center")

            for row in working:
                tree.insert("", "end", values=row)
                tree.grid(row= 4, column=0, padx=20, pady=10)
            deleteButton = Button(nextDeleteFrame, text="SELECT", command=update)
            deleteButton.grid(row= 5, column=0, padx=20, pady=10)
        usingOptValue = usingOpt.get()
        if usingOptValue == '':
            messagebox.showwarning(title="Error", message="Select an option first.")
        else:
            for widget in window6.winfo_children():
                widget.pack_forget()
            frame = Frame(window6)
            

            nextDeleteFrame =LabelFrame(frame, text="Update working")
            nextDeleteFrame.grid(row= 0, column=0, padx=20, pady=10)

            valueLable = Label(nextDeleteFrame, text=f"Enter {usingOptValue}")
            valueLable.grid(row=0, column=0)
            valueEntry = Entry(nextDeleteFrame, width=100)
            valueEntry.grid(row=1, column=0)
            
            button = Button(nextDeleteFrame, text="Find", command=find)
            button.grid(row=2, column=0,sticky="news",padx=10, pady=10)
            button = Button(nextDeleteFrame ,text="Back", command=window6.destroy)
            button.grid(row=3, column=0,sticky="news",padx=10, pady=10)
            frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    button = Button(findworkingFrame, text="Next", command=nextUpdate, width=25)
    button.grid(row=1, column=0,sticky="news",padx=10, pady=10)
    button = Button(findworkingFrame,text="Cancel", command=window6.destroy)
    button.grid(row=2, column=0,sticky="news",padx=10, pady=10)
    frame.pack()
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)

def addDependent():
    window = Tk()

    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()

    windowWidth = int(screenWidth * 0.7)
    windowHeight = int(screenHeight * 0.7)
    window.geometry(f"{windowWidth}x{windowHeight}")
    for widget in window.winfo_children():
        widget.pack_forget()
    def enterData():
        Essn=EssnEntry.get()
        Dependentfirstname = DependentfirstNameEntry.get()
        Dependentlastname = DependentlastNameEntry.get()
        DependentbirthDate = DependentbirthDateCalendar.get_date().strftime(" %Y-%m-%d ")
        DependentGender = DependentGenderVar.get()
        Relationship = RelationshipVar.get()
        try:
            if Essn and Dependentfirstname and Dependentlastname and DependentbirthDate and DependentGender and Relationship:
                sqlClient.insertDependent(Essn=Essn,name=f'{Dependentfirstname.capitalize()} {Dependentlastname.capitalize()}', dateOfBirth=DependentbirthDate,gender=DependentGender,relationship=Relationship)
                messagebox.showwarning(title="Success", message="A new employee details added into the databse.")
                EssnEntry.delete(0,END)
                DependentfirstNameEntry.delete(0,END)
                DependentlastNameEntry.delete(0,END)
                DependentGenderVar.set("")
                RelationshipVar.set("")
            else: 
                messagebox.showwarning(title="Error", message="All fields are required.")
        except mysql.connector.errors.IntegrityError as err:
            messagebox.showerror(title="Failed to Add Dependents",message="Please check the Essn as it already exsists, please update it.")
    frame = Frame(window)

    frame.pack_forget()
    DependentDetailsFrame =LabelFrame(frame, text="Add An Dependent")
    DependentDetailsFrame.grid(row= 0, column=0, padx=20, pady=10)
    EssnLabel= Label(DependentDetailsFrame,text="Employee Social Security Number :")
    EssnLabel.grid(row=0,column=0)
    DependentfirstNameLabel = Label(DependentDetailsFrame, text="First Name")
    DependentfirstNameLabel.grid(row=0, column=1)
    DependentlastNameLabel = Label(DependentDetailsFrame, text="Last Name")
    DependentlastNameLabel.grid(row=0, column=2)
    DependentbirthDateLabel = Label(DependentDetailsFrame, text="Birth Date (dd-mm-yyyy)")
    DependentbirthDateLabel.grid(row=0, column=3)
    DependentGenderLabel = Label(DependentDetailsFrame, text="Select Relationship")
    DependentGenderLabel.grid(row=2, column=0)
    DependentRelationLabel = Label(DependentDetailsFrame, text="Select Gender")
    DependentRelationLabel.grid(row=2, column=2)
    
    
    EssnEntry = Entry(DependentDetailsFrame)
    DependentfirstNameEntry = Entry(DependentDetailsFrame)
    DependentlastNameEntry = Entry(DependentDetailsFrame)
    DependentbirthDateCalendar = tkcalendar.DateEntry(DependentDetailsFrame)
    EssnEntry.grid(row=1, column=0)
    DependentfirstNameEntry.grid(row=1, column=1)
    DependentlastNameEntry.grid(row=1, column=2)
    DependentbirthDateCalendar.grid(row=1, column=3)
    
    RelationshipVar=StringVar(DependentDetailsFrame)
    RelationshipVar.set("")
    RelationshipMenu=OptionMenu(DependentDetailsFrame, RelationshipVar, *("Father", "Mother","Spouse","Son","Daughter"))
    RelationshipMenu.grid(row=3, column=0)
    
    DependentGenderVar=StringVar(DependentDetailsFrame)
    DependentGenderVar.set("")
    DependentGenderMenu=OptionMenu(DependentDetailsFrame, DependentGenderVar, *("M", "F"))
    DependentGenderMenu.grid(row=3, column=2)



    for widget in DependentDetailsFrame.winfo_children():
        widget.grid_configure(padx=10, pady=5)

    button = Button(frame, text="Save Employee Details", command= enterData)
    button.grid(row=3, column=0, sticky="news", padx=20, pady=10)
    button = Button(frame, text="Cancel", command= window.destroy)
    button.grid(row=4, column=0, sticky="news", padx=20, pady=10)
    frame.pack()
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)
    
def alldepenedentScreen():
    window = Tk()

    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()

    windowWidth = int(screenWidth * 0.7)
    windowHeight = int(screenHeight * 0.7)
    window.geometry(f"{windowWidth}x{windowHeight}")
    dependent  = sqlClient.dependentScreen()
    if len(dependent) == 0:
        messagebox.showwarning(title="Error", message="No employees in the detabase.")
    else:
        for widget in window.winfo_children():
            widget.pack_forget()
        frame = Frame(window)
        #frame.pack()

        allDependentFrame =LabelFrame(frame, text="Dependents")
        allDependentFrame.grid(row= 0, column=0, padx=20, pady=10)
        tree = ttk.Treeview(allDependentFrame, columns=("SSN", "Name","Gender","Date of Birth","Relationship"))
        tree.heading("SSN", text="SSN", anchor="center")
        tree.heading("Name", text="Name", anchor="center")
        tree.heading("Gender", text="Gender", anchor="center")
        tree.heading("Date of Birth", text="Date of Birth", anchor="center")
        tree.heading("Relationship", text="Relationship", anchor="center")
        tree.column("#0", width=0,anchor="center")
        tree.column("SSN", width=50, anchor="center")
        tree.column("Name", width=200, anchor="center")
        tree.column("Gender", width=100, anchor="center")
        tree.column("Date of Birth", width=100, anchor="center")
        tree.column("Relationship", width=100, anchor="center")
        
        for row in dependent:
            tree.insert("", "end", values=row)
        tree.grid(row= 4, column=0, padx=20, pady=10)
        deleteButton = Button(allDependentFrame, text="Back", command=window.destroy)
        deleteButton.grid(row= 5, column=0, padx=20, pady=10)
        frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        frame.pack()

def delete_depentdent():

    window = Tk()
    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()

    windowWidth = int(screenWidth * 0.7)
    windowHeight = int(screenHeight * 0.7)
    window.geometry(f"{windowWidth}x{windowHeight}")
    def findAndDeletedependent():
        

        frame = Frame(window)
        frame.pack(fill="both", expand=True)

        ssn = valueEntry.get()
        if not ssn:
            messagebox.showerror('Error', 'Please provide an SSN')
            return
        if ssn:
            dependent = sqlClient.finddependent(method="SSn", value=ssn)
            if len(dependent) == 0:
                messagebox.showwarning(title="Error", message="No employee found with that SSN.")
                return
            else:
                # Display employee details
                tree = ttk.Treeview(frame, columns=("SSn", "Name", "Gender", "Date of Birth", "Relationship"))
                tree.heading("SSn", text="SSn", anchor="center")
                tree.heading("Name", text="Name", anchor="center")
                tree.heading("Gender", text="Gender", anchor="center")
                tree.heading("Date of Birth", text="Date of Birth", anchor="center")
                tree.heading("Relationship", text="Department", anchor="center")
        # ... (set other headings)
                for row in dependent:
                    tree.insert("", "end", values=row)
                try:
                    sqlClient.deletedependent(method="SSn",value=ssn)
                    messagebox.showinfo(title="Success", message="Employee deleted successfully.")
                    allEmployeeScreen()  # Refresh the screen
                except Exception as e:
                    messagebox.showerror(title="Error", message=f"Error deleting employee: {str(e)}")
                    
    for widget in window.winfo_children():
        widget.pack_forget()

    frame = Frame(window)
    valueLable = Label(frame, text="Enter the ID of the employee you want to delete: ")
    valueLable.grid(row=1, column=0)
    valueEntry = Entry(frame, text="Enter SSN:")
    valueEntry.grid(row=2, column=0)
    valueEntry = Entry(frame, width=100)
    valueEntry.grid(row=2, column=0, padx=10, pady=10)
    
    button = Button(frame, text="Find and Delete", command=findAndDeletedependent)
    button.grid(row=3, column=0, sticky="news", padx=10, pady=10)
    button = Button(frame, text="Cancel", command=window.destroy)
    button.grid(row=4, column=0, sticky="news", padx=10, pady=10)
    frame.pack()
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)

def updateDependentScreen():
    window=Tk()
    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()

    windowWidth = int(screenWidth * 0.7)
    windowHeight = int(screenHeight * 0.7)
    window.geometry(f"{windowWidth}x{windowHeight}")
    
    for widget in window.winfo_children():
        widget.pack_forget()
    frame = Frame(window)
    frame.pack()

    finddependentFrame =LabelFrame(frame, text="Update An dependent")
    finddependentFrame.grid(row= 0, column=0, padx=20, pady=10)
    options = [
    "SSn"
    ]
    usingOpt = StringVar(finddependentFrame)
    usingOpt.set("Find Dependent Using")

    menu = OptionMenu(finddependentFrame, usingOpt, *options)
    menu.grid(row=0, column=0,padx=10, pady=10)

    def nextUpdate():

        def find():
            def update():
                selecteddependent = tree.selection()
                if len(selecteddependent) == 0:
                    messagebox.showwarning(title="Error", message="Select an employee first.")
                else:
                    for item in selecteddependent:
                        itemValue = tree.item(item, 'values')
                        ind = 0
                        if usingOptValue == 'SSn':
                            ind = 0
                        else:
                            ind = 7
                    for widget in window.winfo_children():
                        widget.destroy()
                    def enterData():
                        Essn=EssnEntry.get()
                        Dependentfirstname = DependentfirstNameEntry.get()
                        Dependentlastname = DependentlastNameEntry.get()
                        DependentbirthDate = DependentbirthDateCalendar.get()
                        DependentGender = DependentGenderVar.get()
                        Relationship = RelationshipVar.get()
                        if Essn and Dependentfirstname and Dependentlastname and DependentbirthDate and Relationship and DependentGender:
                            sqlClient.updateDependent(method=usingOptValue, value=itemValue, newValue=(Essn,f'{Dependentfirstname.capitalize()} {Dependentlastname.capitalize()}',DependentGender,DependentbirthDate, Relationship))
                            messagebox.showwarning(title="Success", message="Dependent Details has been successfully updated")
                            alldepenedentScreen()
                        else: 
                            messagebox.showwarning(title="Error", message="All fields are required.")

                    frame = Frame(window)
                    
                    
                    DependentDetailsFrame =LabelFrame(frame, text="Add An Dependent")
                    DependentDetailsFrame.grid(row= 0, column=0, padx=20, pady=10)
                    EssnLabel= Label(DependentDetailsFrame,text="Employee Social Security Number :")
                    EssnLabel.grid(row=0,column=0)
                    DependentfirstNameLabel = Label(DependentDetailsFrame, text="First Name")
                    DependentfirstNameLabel.grid(row=0, column=1)
                    DependentlastNameLabel = Label(DependentDetailsFrame, text="Last Name")
                    DependentlastNameLabel.grid(row=0, column=2)
                    DependentbirthDateLabel = Label(DependentDetailsFrame, text="Birth Date (dd-mm-yyyy)")
                    DependentbirthDateLabel.grid(row=0, column=3)
                    DependentGenderLabel = Label(DependentDetailsFrame, text="Select Relationship")
                    DependentGenderLabel.grid(row=2, column=0)
                    DependentRelationLabel = Label(DependentDetailsFrame, text="Select Gender")
                    DependentRelationLabel.grid(row=2, column=2)
    

                    EssnEntry = Entry(DependentDetailsFrame)
                    EssnEntry.grid(row=1, column=0)
                    EssnEntry.insert(0,itemValue[0])
                    DependentfirstNameEntry = Entry(DependentDetailsFrame)
                    DependentfirstNameEntry.insert(0,itemValue[1])
                    DependentfirstNameEntry.grid(row=1, column=1)
                    DependentlastNameEntry = Entry(DependentDetailsFrame)
                    DependentlastNameEntry.grid(row=1, column=2)
                    DependentlastNameEntry.insert(3,itemValue[1])
    

                    def on_select_relation(event):
                        selected_value = RelationshipMenu.get()  # Get the selected value from the menu
                        RelationshipMenu.set(selected_value)
                    
                    RelationshipVar=StringVar(DependentDetailsFrame)
                    RelationshipVar.set("")
                    RelationshipMenu=OptionMenu(DependentDetailsFrame, RelationshipVar, *("Father", "Mother","Spouse","Son","Daughter"))
                    RelationshipMenu.grid(row=3, column=0)
                    def copy_to_entry_relation():
                        copyvalEntry1.delete(0,END)  # Clear the entry box before copying
                        copyvalEntry1.insert(0, RelationshipVar.get())  # Insert the copied value at the beginning

                    
                    button = Button(DependentDetailsFrame, text="Click", command=copy_to_entry_relation)
                    button.grid(row=4, column=0)

                    copyvalEntry1 = Entry(DependentDetailsFrame)
                    copyvalEntry1.bind("<Button-1>", on_select_relation)     # Bind the function to the mouse click event
                    copyvalEntry1.grid(row=5, column=0)

                    DependentGenderVar=StringVar(DependentDetailsFrame)
                    DependentGenderVar.set("")
                    DependentGenderMenu=OptionMenu(DependentDetailsFrame, DependentGenderVar, *("M", "F"))
                    DependentGenderMenu.grid(row=3, column=2)
                    def on_select_location(event):
                        selected_value = DependentGenderMenu.get()  # Get the selected value from the menu
                        DependentGenderVar.set(selected_value)

                    DependentGenderMenu.bind("<<ComboboxSelected>>", on_select_location)  # Bind the selection event
                    def copy_to_entry_location():
                        copyvalEntry.delete(0,END)  # Clear the entry box before copying
                        copyvalEntry.insert(0, DependentGenderVar.get())  # Insert the copied value at the beginning

                    # ... (other code for creating employeeDetailsFrame)

                    button = Button(DependentDetailsFrame, text="Click", command=copy_to_entry_location)
                    button.grid(row=4, column=2)



                    copyvalEntry = Entry(DependentDetailsFrame)
                    copyvalEntry.grid(row=5, column=2)

                    
    
                    DependentbirthDateCalendar = Entry(DependentDetailsFrame)
                    DependentbirthDateCalendar.insert(0,itemValue[3])
                    DependentbirthDateCalendar.grid(row=1,column=3)
                    

                    for widget in DependentDetailsFrame.winfo_children():
                        widget.grid_configure(padx=10, pady=5)

                    button = Button(frame, text="Update Dependent Details", command= enterData)
                    button.grid(row=3, column=0, sticky="news", padx=20, pady=10)
                    button = Button(frame, text="Cancel", command= window.destroy)
                    button.grid(row=4, column=0, sticky="news", padx=20, pady=10)
                    frame.place(relx=0.5, rely=0.5, anchor=CENTER)
            
            dependent = sqlClient.finddependent(method=usingOptValue, value=valueEntry.get())
            if len(dependent) == 0:
                messagebox.showwarning(title="Error", message="No match found.")
            else:
                tree = ttk.Treeview(nextDeleteFrame, columns=("SSN", "Name","Gender","Date of Birth","Relationship"))
                tree.heading("SSN", text="SSN", anchor="center")
                tree.heading("Name", text="Name", anchor="center")
                tree.heading("Gender", text="Gender", anchor="center")
                tree.heading("Date of Birth", text="Date of Birth", anchor="center")
                tree.heading("Relationship", text="Relationship", anchor="center")
                tree.column("#0", width=0,anchor="center")
                tree.column("SSN", width=50, anchor="center")
                tree.column("Name", width=200, anchor="center")
                tree.column("Gender", width=100, anchor="center")
                tree.column("Date of Birth", width=100, anchor="center")
                tree.column("Relationship", width=100, anchor="center")
        
            for row in dependent:
                tree.insert("", "end", values=row)
                tree.grid(row= 4, column=0, padx=20, pady=10)
            deleteButton = Button(nextDeleteFrame, text="SELECT", command=update)
            deleteButton.grid(row= 5, column=0, padx=20, pady=10)
            deleteButton = Button(nextDeleteFrame, text="Back", command=window.destroy)
            deleteButton.grid(row= 6, column=0, padx=20, pady=10)

        usingOptValue = usingOpt.get()
        if usingOptValue == '':
            messagebox.showwarning(title="Error", message="Select an option first.")
        else:
            for widget in window.winfo_children():
                widget.destroy()
            frame = Frame(window)
            

            nextDeleteFrame =LabelFrame(frame, text="Update the dependent")
            nextDeleteFrame.grid(row= 0, column=0, padx=20, pady=10)

            valueLable = Label(nextDeleteFrame, text=f"Enter {usingOptValue}")
            valueLable.grid(row=0, column=0)
            valueEntry = Entry(nextDeleteFrame, width=100)
            valueEntry.grid(row=1, column=0)
                
            button = Button(nextDeleteFrame, text="Find", command=find)
            button.grid(row=2, column=0,sticky="news",padx=10, pady=10)
            button = Button(nextDeleteFrame ,text="Back", command=window.destroy)
            button.grid(row=3, column=0,sticky="news",padx=10, pady=10)
            frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    button = Button(finddependentFrame, text="Next", command=nextUpdate, width=25)
    button.grid(row=1, column=0,sticky="news",padx=10, pady=10)
    button = Button(finddependentFrame ,text="Cancel", command=window.destroy)
    button.grid(row=2, column=0,sticky="news",padx=10, pady=10)
    frame.pack()
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)

def finddetails():
    frame=Frame(window)
    frame.pack()
    opetionsFrame =LabelFrame(frame, text="Find details of")
    opetionsFrame.grid(row= 0, column=0, padx=80, pady=80)
    addButton = Button(opetionsFrame, text='Employee Details',height=2, width=15, padx=20, pady=20, font='lucida 10 normal', command=findemployee)
    addButton.grid(padx=10, pady=10)
    
    addButton = Button(opetionsFrame, text='Department details',height=2, width=15, padx=20, pady=20, font='lucida 10 normal', command=findEmployeedep)
    addButton.grid(padx=10, pady=10)
    addButton = Button(opetionsFrame, text='Project details',height=2, width=15, padx=20, pady=20, font='lucida 10 normal', command=findprojectdetail)
    addButton.grid(padx=10, pady=10)
    
    addButton = Button(opetionsFrame, text='Dependent details',height=2, width=15, padx=20, pady=20, font='lucida 10 normal', command=finddependent)
    addButton.grid(padx=10, pady=10)
    
    
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)
def findemployee():
    window=Tk()
    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()

    windowWidth = int(screenWidth * 0.7)
    windowHeight = int(screenHeight * 0.7)
    window.geometry(f"{windowWidth}x{windowHeight}")
    
    for widget in window.winfo_children():
        widget.pack_forget()
    frame = Frame(window)
    frame.pack()

    findEmployeeFrame =LabelFrame(frame, text="Update An Employee")
    findEmployeeFrame.grid(row= 0, column=0, padx=20, pady=10)
    options = [
    "SSn",
    "Name",
    "Birth Date",
    "Joining Date",
    "Salary",
    "Department"
    ]
    usingOpt = StringVar(findEmployeeFrame)
    usingOpt.set("Find Employee Using")

    menu = OptionMenu(findEmployeeFrame, usingOpt, *options)
    menu.grid(row=0, column=0,padx=10, pady=10)

    def nextUpdate():

        def find():
            
            if selection==2:
                employees = sqlClient.findEmployee(method=usingOptValue, value=valueEntry.get_date())
            elif selection==3:
                employees = sqlClient.findEmployee(method=usingOptValue, value=valueEntry.option_get())
            elif selection==4:
                employees = sqlClient.findEmployee(method=usingOptValue, value=valueEntry.get())
            if len(employees) == 0:
                messagebox.showwarning(title="Error", message="No match found.")
            else:
                tree = ttk.Treeview(nextDeleteFrame, columns=("SSn","Name","Location","Date of Birth", "Joining Date", "Salary", "Department"))
                tree.heading("#0", text="", anchor="center") 
                tree.heading("SSn", text="SSn", anchor="center")
                tree.heading("Name", text="Name", anchor="center")
                tree.heading("Date of Birth", text="Date of Birth", anchor="center")
                tree.heading("Location", text="Location", anchor="center")
                tree.heading("Joining Date", text="Joining Date", anchor="center")
                tree.heading("Salary", text="Salary", anchor="center")
                tree.heading("Department", text="Department", anchor="center")

                tree.column("#0", width=0,anchor="center")
                tree.column("SSn", width=50, anchor="center")
                tree.column("Name", width=200, anchor="center")
                tree.column("Date of Birth", width=100, anchor="center")
                tree.column("Location", width=100, anchor="center")
                tree.column("Joining Date", width=100, anchor="center")
                tree.column("Salary", width=100, anchor="center")
                tree.column("Department", width=100, anchor="center")

            for row in employees:
                tree.insert("", "end", values=row)
                tree.grid(row= 4, column=0, padx=20, pady=10)
        usingOptValue = usingOpt.get()
        if usingOptValue == '':
            messagebox.showwarning(title="Error", message="Select an option first.")
        else:
            for widget in window.winfo_children():
                widget.destroy()
            frame = Frame(window)
            

            nextDeleteFrame =LabelFrame(frame, text="Update An Employee")
            nextDeleteFrame.grid(row= 0, column=0, padx=20, pady=10)

            valueLable = Label(nextDeleteFrame, text=f"Enter {usingOptValue}")
            valueLable.grid(row=0, column=0)
            if  usingOptValue=='Birth Date' or usingOptValue=='Joining Date':
                valueEntry = tkcalendar.DateEntry(nextDeleteFrame, date_pattern='dd/mm/yyyy')
                valueEntry.grid(row=1, column=0)
                selection=2
            elif usingOptValue=='department':
                valueEntry=["",""]
                usingOpt.set("department.") 
                optMenu2 = OptionMenu(nextDeleteFrame,usingOpt,*["Accounts","Administration","Sales","","Research"])
                optMenu2.grid(row=1, column=0)
                selection=3
            else:
                valueEntry = Entry(nextDeleteFrame, width=100)
                valueEntry.grid(row=1, column=0)
                selection=4
            button = Button(nextDeleteFrame, text="Find", command=find)
            button.grid(row=2, column=0,sticky="news",padx=10, pady=10)
            button = Button(nextDeleteFrame ,text="Back", command=window.destroy)
            button.grid(row=3, column=0,sticky="news",padx=10, pady=10)
            frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    button = Button(findEmployeeFrame, text="Next", command=nextUpdate, width=25)
    button.grid(row=1, column=0,sticky="news",padx=10, pady=10)
    button = Button(findEmployeeFrame ,text="Cancel", command=window.destroy)
    button.grid(row=2, column=0,sticky="news",padx=10, pady=10)
    frame.pack()
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)
    
def findEmployeedep():
    window=Tk()
    frame=Frame(window)
    frame.pack()
    opetionsFrame =LabelFrame(frame, text="Main Menu")
    opetionsFrame.grid(row= 0, column=0, padx=80, pady=80)
    addButton = Button(opetionsFrame, text='Full Department details',height=2, width=15, padx=20, pady=20, font='lucida 10 normal', command=findempdep)
    addButton.grid(padx=10, pady=10)
    
    addButton = Button(opetionsFrame, text='Full Department details',height=2, width=15, padx=20, pady=20, font='lucida 10 normal', command=find_dep_loc)
    addButton.grid(padx=10, pady=10)
    
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)

def findempdep():
    window = Tk()

    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()

    windowWidth = int(screenWidth * 0.7)
    windowHeight = int(screenHeight * 0.7)
    window.geometry(f"{windowWidth}x{windowHeight}")
    for widget in window.winfo_children():
        widget.pack_forget()
    frame = Frame(window)
    frame.pack()

    finddepartmentFrame =LabelFrame(frame, text="Update An Employee")
    finddepartmentFrame.grid(row= 0, column=0, padx=20, pady=10)
    options = [
    "Mgr_SSN",
    "Department Number"
    ]
    usingOpt = StringVar(finddepartmentFrame)
    usingOpt.set("Find department Using")

    menu = OptionMenu(finddepartmentFrame, usingOpt, *options)
    menu.grid(row=0, column=0,padx=10, pady=10)
    def nextUpdate():

        def find():
            dept=sqlClient.findEmployeedep(method=usingOptValue,value=valueEntry.get())
            if len(dept)==0:
                messagebox.showwarning(title="Error", message="No match found.")
            else:
                tree = ttk.Treeview(nextDeleteFrame, columns=("Dname","Dnumber","Mgr_SSN","phone"))
                tree.heading("#0", text="", anchor="center") 
                tree.heading("Dname", text="Dname", anchor="center")
                tree.heading("Dnumber", text="Dnumber", anchor="center")
                tree.heading("Mgr_SSN", text="Mgr_SSN", anchor="center")
                tree.heading("phone", text="phone", anchor="center")
            
                tree.column("#0", width=0,anchor="center")
                tree.column("Dname", width=50, anchor="center")
                tree.column("Dnumber", width=200, anchor="center")
                tree.column("Mgr_SSN", width=100, anchor="center")
                tree.column("phone", width=100, anchor="center")
            
            for row in dept:
                tree.insert("", "end", values=row[:])
                tree.grid(row= 4, column=0, padx=20, pady=10)

        usingOptValue=usingOpt.get()
        if usingOptValue=='':
                messagebox.showwarning(title="Error", message="Select an option first.")
        else:
            for widget in window.winfo_children():
                widget.destroy()
            frame = Frame(window)
            

            nextDeleteFrame =LabelFrame(frame, text="Update a department")
            nextDeleteFrame.grid(row= 0, column=0, padx=20, pady=10)
            valueEntry = Entry(nextDeleteFrame, width=100)
            valueEntry.grid(row=1, column=0)
            button = Button(nextDeleteFrame, text="Find", command=find)
            button.grid(row=2, column=0,sticky="news",padx=10, pady=10)
            button = Button(nextDeleteFrame ,text="Back", command=window.destroy)
            button.grid(row=3, column=0,sticky="news",padx=10, pady=10)
            frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    button = Button(finddepartmentFrame, text="Next", command=nextUpdate, width=25)
    button.grid(row=1, column=0,sticky="news",padx=10, pady=10)
    button = Button(finddepartmentFrame ,text="Cancel", command=window.destroy)
    button.grid(row=2, column=0,sticky="news",padx=10, pady=10)
    frame.pack()
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)

def find_dep_loc():
    window = Tk()

    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()

    windowWidth = int(screenWidth * 0.7)
    windowHeight = int(screenHeight * 0.7)
    window.geometry(f"{windowWidth}x{windowHeight}")
    for widget in window.winfo_children():
        widget.pack_forget()
    frame = Frame(window)
    frame.pack()

    finddepartmentlocFrame =LabelFrame(frame, text="Update department location")
    finddepartmentlocFrame.grid(row= 0, column=0, padx=20, pady=10)
    options = [
    "Dnumber"
    ]
    usingOpt = StringVar(finddepartmentlocFrame)
    usingOpt.set("Find department Location Using")

    menu = OptionMenu(finddepartmentlocFrame, usingOpt, *options)
    menu.grid(row=0, column=0,padx=10, pady=10)
    def nextUpdate():

        def find():
                        
            deptloc=sqlClient.findDepartmentLOC(method=usingOptValue,value=valueEntry.get(),)
            if len(deptloc)==0:
                messagebox.showwarning(title="Error", message="No match found.")
            else:
                tree = ttk.Treeview(nextDeleteFrame, columns=("Department number","Location"))
                tree.heading("#0", text="", anchor="center") 
                tree.heading("Department number", text="Department number", anchor="center")
                tree.heading("Location", text="Location", anchor="center")
                
            
                tree.column("#0", width=0,anchor="center")
                tree.column("Department number", width=200, anchor="center")
                tree.column("Location", width=100, anchor="center")
            
            for row in deptloc:
                tree.insert("", "end", values=row[:])
                tree.grid(row= 4, column=0, padx=20, pady=10)
            
        usingOptValue=usingOpt.get()
        if usingOptValue=='':
                messagebox.showwarning(title="Error", message="Select an option first.")

        else:
            for widget in window.winfo_children():
                widget.destroy()
            frame = Frame(window)
            

            nextDeleteFrame =LabelFrame(frame, text="Update a department location")
            def on_select_location1(event):
                    selected_value = departmentMenu.get()  # Get the selected value from the menu
                    departmentMenu.set(selected_value)
            DlocationVar =StringVar(nextDeleteFrame)
            DlocationVar.set("Enter Department Location")
            departmentMenu =OptionMenu(nextDeleteFrame, DlocationVar, *("110099", "111199", "112299", "113399", "114499"))
            departmentMenu.grid(row=1, column=0)
            departmentMenu.bind("<<ComboboxSelected>>", on_select_location1)  # Bind the selection event
                        
            valueEntry = Entry(nextDeleteFrame)
            def copy_to_entry_location1():
                    valueEntry.delete(0,END)  # Clear the entry box before copying
                    valueEntry.insert(0, DlocationVar.get())
            button=Button(nextDeleteFrame,text='Copy',command=copy_to_entry_location1)
            button.grid(row=1,column=1)
                #copyvalEntry.grid(row=3, column=0)
                #copyvalEntry.insert(1,itemValue[1])
            nextDeleteFrame.grid(row= 0, column=0, padx=20, pady=10)
            valueEntry = Entry(nextDeleteFrame, width=100)
            valueEntry.grid(row=2, column=0)
            button = Button(nextDeleteFrame, text="Find", command=find)
            button.grid(row=3, column=0,sticky="news",padx=10, pady=10)
            button = Button(nextDeleteFrame ,text="Back", command=window.destroy)
            button.grid(row=4, column=0,sticky="news",padx=10, pady=10)
            frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    button = Button(finddepartmentlocFrame, text="Next", command=nextUpdate, width=25)
    button.grid(row=1, column=0,sticky="news",padx=10, pady=10)
    button = Button(finddepartmentlocFrame ,text="Cancel", command=window.destroy)
    button.grid(row=2, column=0,sticky="news",padx=10, pady=10)
    frame.pack()
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)

def findprojectdetail():
    window=Tk()
    frame=Frame(window)
    frame.pack()
    opetionsFrame =LabelFrame(frame, text="Main Menu")
    opetionsFrame.grid(row= 0, column=0, padx=80, pady=80)
    addButton = Button(opetionsFrame, text='Full project detials',height=2, width=15, padx=20, pady=20, font='lucida 10 normal', command=findprojectdetail)
    addButton.grid(padx=10, pady=10)
    
    addButton = Button(opetionsFrame, text='Full working details',height=2, width=15, padx=20, pady=20, font='lucida 10 normal', command=findworking)
    addButton.grid(padx=10, pady=10)
    
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)

def findProjectScreen():
    window=Tk()
    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()

    windowWidth = int(screenWidth * 0.7)
    windowHeight = int(screenHeight * 0.7)
    window.geometry(f"{windowWidth}x{windowHeight}")
    
    for widget in window.winfo_children():
        widget.destroy()
    frame = Frame(window)
    frame.pack()

    findprojectFrame =LabelFrame(frame, text="Find prject")
    findprojectFrame.grid(row= 0, column=0, padx=20, pady=10)
    options = [
    'Project ID',
    'Project Name',
    'Project location',
    'Department Number'
    ]
    usingOpt = StringVar(findprojectFrame)
    usingOpt.set("Find Project Using")

    menu = OptionMenu(findprojectFrame, usingOpt, *options)
    menu.grid(row=0, column=0,padx=10, pady=10)

    def nextUpdate():

        def find():
            
            project = sqlClient.findproject(method=usingOptValue, value=valueEntry.get())
            if len(project) == 0:
                messagebox.showwarning(title="Error", message="No match found.")
            else:
                tree = ttk.Treeview(nextDeleteFrame, columns=("P-Name","P-ID","P-Location","P-Department"))
                tree.heading("#0", text="", anchor="center") 
                tree.heading("P-Name", text="P-Name", anchor="center")
                tree.heading("P-ID", text="P-ID", anchor="center")
                tree.heading("P-Location", text="P-Location", anchor="center")
                tree.heading("P-Department", text="P-Department", anchor="center")

                tree.column("#0", width=0,anchor="center")
                tree.column("P-Name", width=200, anchor="center")
                tree.column("P-ID", width=50, anchor="center")
                tree.column("P-Location", width=200, anchor="center")
                tree.column("P-Department", width=100, anchor="center")

            for row in project:
                tree.insert("", "end", values=row)
                tree.grid(row= 4, column=0, padx=20, pady=10)
        usingOptValue = usingOpt.get()
        if usingOptValue == '':
            messagebox.showwarning(title="Error", message="Select an option first.")
        else:
            for widget in window.winfo_children():
                widget.destroy()
            frame = Frame(window)
            

            nextDeleteFrame =LabelFrame(frame, text="Find Project")
            nextDeleteFrame.grid(row= 0, column=0, padx=20, pady=10)

            valueLable = Label(nextDeleteFrame, text=f"Enter {usingOptValue}")
            valueLable.grid(row=0, column=0)
            valueEntry = Entry(nextDeleteFrame, width=100)
            valueEntry.grid(row=1, column=0)
            
            button = Button(nextDeleteFrame, text="Find", command=find)
            button.grid(row=2, column=0,sticky="news",padx=10, pady=10)
            button = Button(nextDeleteFrame ,text="Back", command=window.destroy)
            button.grid(row=3, column=0,sticky="news",padx=10, pady=10)
            frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    button = Button(findprojectFrame, text="Next", command=nextUpdate, width=25)
    button.grid(row=1, column=0,sticky="news",padx=10, pady=10)
    button = Button(findprojectFrame ,text="Cancel", command=window.destroy)
    button.grid(row=2, column=0,sticky="news",padx=10, pady=10)
    frame.pack()
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)

def findworking():
    window6=Tk()
    screen6Width = window6.winfo_screenwidth()
    screen6Height = window6.winfo_screenheight()

    window6Width = int(screenWidth * 0.7)
    window6Height = int(screenHeight * 0.7)
    window6.geometry(f"{window6Width}x{window6Height}")
    
    for widget in window6.winfo_children():
        widget.pack_forget()
    frame = Frame(window6)
    frame.pack()

    findworkingFrame =LabelFrame(frame, text="Update working details")
    findworkingFrame.grid(row= 0, column=0, padx=20, pady=10)
    options = [
    'Employee SSN',
    'Project Number',
    'Working hour',
    ]
    usingOpt = StringVar(findworkingFrame)
    usingOpt.set("Find Details Using")

    menu = OptionMenu(findworkingFrame, usingOpt, *options)
    menu.grid(row=0, column=0,padx=10, pady=10)

    def nextUpdate():

        def find():
            working = sqlClient.findworking(method=usingOptValue, value=valueEntry.get())
            if len(working) == 0:
                messagebox.showwarning(title="Error", message="No match found.")
            else:
                tree = ttk.Treeview(nextDeleteFrame, columns=("ESSN","PNumber","Hours-spent"))
                tree.heading("#0", text="", anchor="center") 
                tree.heading("ESSN", text="ESSN", anchor="center")
                tree.heading("PNumber", text="PNumber", anchor="center")
                tree.heading("Hours-spent", text="Hours spent", anchor="center")

                tree.column("#0", width=0,anchor="center")
                tree.column("ESSN", width=50, anchor="center")
                tree.column("PNumber", width=200, anchor="center")
                tree.column("Hours-spent", width=100, anchor="center")

            for row in working:
                tree.insert("", "end", values=row)
                tree.grid(row= 4, column=0, padx=20, pady=10)
        usingOptValue = usingOpt.get()
        if usingOptValue == '':
            messagebox.showwarning(title="Error", message="Select an option first.")
        else:
            for widget in window6.winfo_children():
                widget.pack_forget()
            frame = Frame(window6)
            

            nextDeleteFrame =LabelFrame(frame, text="Update working")
            nextDeleteFrame.grid(row= 0, column=0, padx=20, pady=10)

            valueLable = Label(nextDeleteFrame, text=f"Enter {usingOptValue}")
            valueLable.grid(row=0, column=0)
            valueEntry = Entry(nextDeleteFrame, width=100)
            valueEntry.grid(row=1, column=0)
            
            button = Button(nextDeleteFrame, text="Find", command=find)
            button.grid(row=2, column=0,sticky="news",padx=10, pady=10)
            button = Button(nextDeleteFrame ,text="Back", command=window6.destroy)
            button.grid(row=3, column=0,sticky="news",padx=10, pady=10)
            frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    button = Button(findworkingFrame, text="Next", command=nextUpdate, width=25)
    button.grid(row=1, column=0,sticky="news",padx=10, pady=10)
    button = Button(findworkingFrame,text="Cancel", command=window6.destroy)
    button.grid(row=2, column=0,sticky="news",padx=10, pady=10)
    frame.pack()
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)


def finddependent():
    window=Tk()
    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()

    windowWidth = int(screenWidth * 0.7)
    windowHeight = int(screenHeight * 0.7)
    window.geometry(f"{windowWidth}x{windowHeight}")
    
    for widget in window.winfo_children():
        widget.destroy()
    frame = Frame(window,border=10,height=400,width=800)
    frame.pack()

    finddependentFrame =LabelFrame(frame, text="Update An dependent")
    finddependentFrame.grid(row= 0, column=0, padx=20, pady=10)
    options = [
    "SSn"
    ]
    usingOpt = StringVar(finddependentFrame)
    usingOpt.set("Find Dependent Using")

    menu = OptionMenu(finddependentFrame, usingOpt, *options)
    menu.grid(row=0, column=0,padx=10, pady=10)

    def nextUpdate():

        def find():            
            dependent = sqlClient.finddependent(method=usingOptValue, value=valueEntry.get())
            if len(dependent) == 0:
                messagebox.showwarning(title="Error", message="No match found.")
            else:
                tree = ttk.Treeview(nextDeleteFrame, columns=("SSN", "Name","Gender","Date of Birth","Relationship"))
                tree.heading("SSN", text="SSN", anchor="center")
                tree.heading("Name", text="Name", anchor="center")
                tree.heading("Gender", text="Gender", anchor="center")
                tree.heading("Date of Birth", text="Date of Birth", anchor="center")
                tree.heading("Relationship", text="Relationship", anchor="center")
                tree.column("#0", width=0,anchor="center")
                tree.column("SSN", width=50, anchor="center")
                tree.column("Name", width=200, anchor="center")
                tree.column("Gender", width=100, anchor="center")
                tree.column("Date of Birth", width=100, anchor="center")
                tree.column("Relationship", width=100, anchor="center")
        
            for row in dependent:
                tree.insert("", "end", values=row)
                tree.grid(row= 4, column=0, padx=20, pady=10)

        usingOptValue = usingOpt.get()
        if usingOptValue == '':
            messagebox.showwarning(title="Error", message="Select an option first.")
        else:
            for widget in window.winfo_children():
                widget.destroy()
            frame = Frame(window)
            

            nextDeleteFrame =LabelFrame(frame, text="Update the dependent")
            nextDeleteFrame.grid(row= 0, column=0, padx=20, pady=10)

            valueLable = Label(nextDeleteFrame, text=f"Enter {usingOptValue}")
            valueLable.grid(row=0, column=0)
            valueEntry = Entry(nextDeleteFrame, width=100)
            valueEntry.grid(row=1, column=0)
                
            button = Button(nextDeleteFrame, text="Find", command=find)
            button.grid(row=2, column=0,sticky="news",padx=10, pady=10)
            button = Button(nextDeleteFrame ,text="Back", command=window.destroy)
            button.grid(row=3, column=0,sticky="news",padx=10, pady=10)
            frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    button = Button(finddependentFrame, text="Next", command=nextUpdate, width=25)
    button.grid(row=1, column=0,sticky="news",padx=10, pady=10)
    button = Button(finddependentFrame ,text="Cancel", command=window.destroy)
    button.grid(row=2, column=0,sticky="news",padx=10, pady=10)
    frame.pack()
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)


def feedbackvalue():
    window_addEMP_addEMP = Tk()
    screenWidth = window_addEMP_addEMP.winfo_screenwidth()
    screenHeight = window_addEMP_addEMP.winfo_screenheight()

    window_addEMP_addEMPWidth = int(screenWidth * 0.7)
    window_addEMP_addEMPHeight = int(screenHeight * 0.7)
    for widget in window_addEMP_addEMP.winfo_children():
        widget.pack_forget()

    window_addEMP_addEMP.geometry(f"{window_addEMP_addEMPWidth}x{window_addEMP_addEMPHeight}")
    def enterData():
        firstname = firstNameEntry.get()
        feedbackname = feedbackEntry.get()
        if firstname:
            sqlClient.insertfeedback(ssn=firstname,feedback=feedbackname)
            messagebox.showwarning(title="Success", message="A new employee feedback added into the databse.")
            firstNameEntry.delete(0,END)
            feedbackEntry.delete(0,END)
        else: 
            messagebox.showwarning(title="Error", message="All fields are required.")

    frame = Frame(window_addEMP_addEMP)
    
    
    employeeDetailsFrame =LabelFrame(frame, text="Add feedback")
    employeeDetailsFrame.grid(row= 0, column=0, padx=20, pady=10)

    firstNameLabel = Label(employeeDetailsFrame, text="SSN")
    firstNameLabel.grid(row=0, column=0)
    feedbackLabel = Label(employeeDetailsFrame, text="Feedback")
    feedbackLabel.grid(row=1, column=0,padx=20,pady=20,)

    
    firstNameEntry = Entry(employeeDetailsFrame)
    feedbackEntry = Entry(employeeDetailsFrame)
    firstNameEntry.grid(row=0, column=1)
    feedbackEntry.grid(row=1, column=1)

    for widget in employeeDetailsFrame.winfo_children():
        widget.grid_configure(padx=10, pady=5)

    button = Button(frame, text="Save Feedback", command= enterData)
    button.grid(row=3, column=0, sticky="news", padx=20, pady=10)
    button = Button(frame, text="Cancel", command=window_addEMP_addEMP.destroy)
    button.grid(row=4, column=0, sticky="news", padx=20, pady=10)
    frame.pack()
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)


homeScreen()

window.mainloop()
