from tkinter import *
from tkinter import ttk
from Variables import core_variables

# Create the main Window
root = Tk()
root.title(core_variables.program_name)
root.minsize(width=500, height=300)

# Main window widgets
base = ttk.Frame(root, padding=10,).pack()
ttk.Label(base,text='Welcome').pack()




# Required to post the window
mainloop()