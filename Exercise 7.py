from tkinter import * 
from tkinter import ttk 

appOne = Tk()

myentry = ttk.Entry(appOne, width=30)
myentry.pack()

myentry.get()

appOne.mainloop()