from tkinter import *
from tkinter import ttk
from Variables import core_variables
from Functions import mathematical_functions

# import details
choice = []
for name in dir(mathematical_functions):
    if callable(getattr(mathematical_functions, name)) and not name.startswith("_"):
        choice.append(name)



# Create the main Window
root = Tk()
root.title(core_variables.program_name)
root.minsize(width=500, height=300)

# Main window widgets
Sidebar = ttk.Frame(root, padding=10,)
Sidebar.pack(side=LEFT, anchor=N)
ttk.Label(Sidebar,text='Welcome, please select a formula').pack()

# plan, open secoundary message box for test type and data import
options = ttk.Combobox(Sidebar,values=choice)
options.pack()
a = options.get()
ttk.Button(Sidebar,text='T-Test',command='mathematical_functions.'+a).pack()
    
# Required to post the window
mainloop()