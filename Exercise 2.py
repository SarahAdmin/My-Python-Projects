from tkinter import * 
from tkinter import ttk 

appOne = Tk()
myButton = ttk.Button(appOne, text= "Click Me")
myButton.pack()

print(myButton['text'])
myButton['text'] = "Press Me"
myButton.config(text="Press Me")
print(myButton.config())

print(str(myButton))
print(str(appOne))

ttk.Label(appOne, text="Hello Tkinter Application").pack()


appOne.mainloop()