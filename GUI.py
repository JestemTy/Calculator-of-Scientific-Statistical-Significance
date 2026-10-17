from tkinter import *
from tkinter import ttk
from Variables import core_variables
from Functions import mathematical_functions

# Create the main Window
root = Tk()
root.title(core_variables.program_name)
root.minsize(width=500, height=300)

# Main window widgets
base = ttk.Frame(root, padding=10,).pack()
ttk.Label(base,text='Welcome').pack()

# plan, open secoundary message box for test type and data import
ttk.Button(base,text='T-Test',command=mathematical_functions.t_test).pack()

# Required to post the window
mainloop()