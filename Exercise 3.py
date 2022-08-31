from tkinter import * 
from tkinter import ttk 

class HelloApp: 

    def __init__(self, master): 
        self.label=ttk.Label(master,text="Hello, Tkinter") 
        self.label.grid(row=0, column=0, columnspan=2)

        ttk.Button(master, text="France", 
        command = self.france_hello).grid(row = 1, column= 0)

        ttk.Button(master, text="Spain", 
        command = self.spain_hello).grid(row = 1, column= 1)

def france_hello(self): 
    self.label.config(text = "Bonjour, Tkinter")

def spain_hello(self): 
    self.label.config(text= "Hola, Tkinter")


def main(): 

      appOne = Tk()
      messageapp = HelloApp(appOne)
      appOne.mainloop()

if __name__ == "__main__": main()
