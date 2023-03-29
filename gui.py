import tkinter as tk
from tkinter import *
from tkinter import ttk
win=tk.Tk()
win.title("Library Management System")
#create labels
#WIDGETS--> label, buttons, radiobuttons - tk, ttk
#pack,grid
enter_name=ttk.Label(win, text="Enter your name: ")
enter_name.grid(row=0, column=0,sticky=tk.W)
enter_age=ttk.Label(win, text="Enter Age" )
enter_age.grid(row=1, column=0,sticky=tk.W)

win.mainloop()
