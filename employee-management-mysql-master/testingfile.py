import tkinter as tk
from tkinter import ttk, messagebox


def deleteScreen():
    frame = Frame(window)
    frame.pack()
    valueLable = Label(frame, text="Enter the ID of the employee you want to delete: ")
    valueLable.grid(row=1, column=0)
    valueEntry = Entry(frame, text="Enter SSN:")
    valueEntry.grid(row=2, column=0)
    valueEntry = Entry(frame, width=100)
    valueEntry.grid(row=2, column=0, padx=10, pady=10)

    def findAndDeleteEmployee():
        frame = Frame(window)
        frame.pack()

        ssn = valueEntry.get()

        if ssn:
            employees = sqlClient.findEmployee(method="SSn", value=ssn)

            if len(employees) == 0:
                messagebox.showwarning(title="Error", message="No employee found with that SSN.")
            else:
                # Display employee details
                tree = ttk.Treeview(frame, columns=("SSn", "Name", "Location", "Date of Birth", "Joining Date", "Salary", "Department"))
                tree.heading("#0", text="", anchor="center")
                tree.heading("SSn", text="SSn", anchor="center")
                tree.heading("Name", text="name", anchor="center")
                tree.heading("Date of Birth", text="Date of Birth", anchor="center")
                tree.heading("Location", text="Location", anchor="center")
                tree.heading("Joining Date", text="Joining Date", anchor="center")
                tree.heading("Salary",text="Salary", anchor="center")
                tree.heading("Department", text="Department", anchor="center")
                    # ... (set other headings)
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

                    # Delete the employee
            try:
                sqlClient.deleteEmployee(method="SSn",value=ssn)
                messagebox.showinfo(title="Success", message="Employee deleted successfully.")
                deleteScreen()  # Refresh the screen
            except Exception as e:
                messagebox.showerror(title="Error", message=f"Error deleting employee: {str(e)}")
        else:
            messagebox.showerror(title="Error", message="Please enter the ID of the employee to delete.")
    for widget in window.winfo_children():
        widget.destroy()

    
    button = Button(frame, text="Find and Delete", command=findAndDeleteEmployee)
    button.grid(row=3, column=0, sticky="news", padx=10, pady=10)
    button = Button(frame, text="Cancel", command=addEmployee)
    button.grid(row=4, column=0, sticky="news", padx=10, pady=10)
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)






    

            

