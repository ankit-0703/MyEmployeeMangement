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
