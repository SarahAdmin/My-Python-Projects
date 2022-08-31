from tkinter import * 
from tkinter import ttk 

appOne = Tk()

mybuttonTwo = ttk.Checkbutton(appOne, text="Cheeseburger?")
mybuttonTwo.pack()


cheeseburger = StringVar()
cheeseburger.set('Cheeseburger?')
cheeseburger.get()
'Cheeseburger?'
mybuttonTwo.config(variable= cheeseburger, onvalue = 'Cheeseburger Please :)', 
offvalue="Boo Cheeseburger :(")

cheeseburger.get()

fastFood = StringVar()
ttk.Radiobutton(appOne, text="Cheeseburger", variable=fastFood, value='Cheeseburger').pack()
ttk.Radiobutton(appOne, text="Fries", variable=fastFood, value="Fries").pack()

fastFood.get()





appOne.mainloop()

