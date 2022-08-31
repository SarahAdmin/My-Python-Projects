from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
myRoot = Tk()

myLabel = ttk.Label(myRoot, text="This is my Application", background="orange",
                    foreground="deeppink")
myLabel.pack()

def messageOne():
    showinfo( title="Message from Admin",
              message="Hello Tkinter")


ttk.Button(myRoot, text="Click Here", command=messageOne).pack()



myRoot.mainloop()
