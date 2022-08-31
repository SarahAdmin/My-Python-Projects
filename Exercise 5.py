from tkinter import * 
from tkinter import ttk 

appOne = Tk()

myButton = ttk.Button(appOne, text = "Click Me")
myButton.pack()

def message(): 
    print("Clicked!")


myButton.config(command=message)

myButton.invoke()

myButton.state(['!disabled'])







appOne.mainloop()