from tkinter import * 
from tkinter import ttk 

appOne = Tk()

myLabel = ttk.Label(appOne, text="This is my first application")
myLabel.pack()
myLabel.config(text="Hola, Tkinter")
myLabel.config(text="Hola, Tkinter It\'s been a really long time we last met. Great to see you again!")
myLabel.config(wraplength = 150)
myLabel.config(justify = CENTER)
myLabel.config(foreground = 'red', background='yellow')
myLabel.config(font =('Comic Sans MS',18,'normal'))
myLabel.config(text= "Hola Tkinter")


appOne.mainloop()