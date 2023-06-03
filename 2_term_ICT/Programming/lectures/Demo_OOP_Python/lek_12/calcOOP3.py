from tkinter import *

class Block:
    def __init__(self, master):
        self.e1 = Entry(master, width=20)
        self.e2 = Entry(master, width=20)
        self.b1 = Button(master, text='+')
        self.b2 = Button(master, text='-')
        self.b3 = Button(master, text='/')
        self.b4 = Button(master, text='*')
        self.l = Label(master, bg='white', fg='black', width=20)
        self.b1['command'] = self.add
        self.b2['command'] = self.substract
        self.b3['command'] = self.divide
        self.b4['command'] = self.multiply
        self.e1.pack()
        self.e2.pack()
        self.b1.pack()
        self.b2.pack()
        self.b3.pack()
        self.b4.pack()
        self.l.pack()
 
    def add(self):
        a = float(self.e1.get()) + float(self.e2.get())
 
        self.l['text'] = a
 
    def substract(self):
        a = float(self.e1.get()) - float(self.e2.get())
 
        self.l['text'] = a
 
    def divide(self):
        a = float(self.e1.get()) / float(self.e2.get())
 
        self.l['text'] = a
 
    def multiply(self):
        a = float(self.e1.get()) * float(self.e2.get())
 
        self.l['text'] = a
 
 
root = Tk()
first_block = Block(root)
 

 
root.mainloop()
