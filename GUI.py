from tkinter import *
from tkinter import ttk
from Variables import core_variables
from Functions import mathematical_functions

test = [1,2,2]

# Create the main Window
root = Tk()
root.title(core_variables.program_name)
root.minsize(width=500, height=300)

# Main window widgets
base = ttk.Frame(root, padding=10,)
base.pack(side=LEFT, anchor=N)
ttk.Label(base,text='Welcome, please select a formula').pack()

# plan, open secoundary message box for test type and data import
b = ttk.Combobox(base,values=test).pack()
ttk.Button(base,text='T-Test',command=mathematical_functions.t_test).pack()


def printer():
    index = b.current()
    if index:
        a = test[index[0]]  # Combobox.current() returns [index] in a list
    else:
        a = None  # Handle case where nothing is selected
    
    print(a)

ttk.Button(base,text='Run',command=printer).pack()

# Required to post the window
mainloop()