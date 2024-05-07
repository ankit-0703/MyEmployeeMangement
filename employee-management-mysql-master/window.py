import tkinter as tk
from tkinter import ttk

def on_closing():
    if tk.messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

root = tk.Tk()
root.title("Beautiful Window")
root.protocol("WM_DELETE_WINDOW", on_closing)

# Create a style
style = ttk.Style()
style.configure("TFrame", background="white")
style.configure("TLabel", background="white", font=("Helvetica", 12))
style.configure("TButton", background="white", font=("Helvetica", 12))

# Create a frame
frame = ttk.Frame(root, style="TFrame")
frame.pack(padx=20, pady=20)

# Create a label
label = ttk.Label(frame, text="Welcome to the beautiful window!")
label.pack(pady=10)

# Create a button
button = ttk.Button(frame, text="Click me!", command=lambda: tk.messagebox.showinfo("Info", "Hello, World!"))
button.pack(pady=10)

root.mainloop()