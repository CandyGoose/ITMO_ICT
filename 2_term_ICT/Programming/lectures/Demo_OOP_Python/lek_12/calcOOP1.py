from tkinter import *

class Calcul(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.create_widgets()
 
    def create_widgets(self):
        Label(self, text="Число 1").grid(row=1,column=0, sticky=W)
        Label(self, text="Число 2").grid(row=2,column=0, sticky=W)
        self.num_1=Entry(self, width=10)
        self.num_2=Entry(self, width=10)
        self.num_1.grid(row=1, column=0)
        self.num_2.grid(row=2, column=0)
        Button(self, text="+", command=self.addition, width=3).grid(row=3, column=0, sticky=W)
        Button(self, text="-", command=self.substraction, width=3).grid(row=3, column=0)
        Button(self, text="*", command=self.multiplication, width=3).grid(row=4, column=0, sticky=W)
        Button(self, text="/", command=self.division, width=3).grid(row=4, column=0)
        self.answer=Text(self, width=30, height=2, wrap=WORD)
        self.answer.grid(row=5, column=0, sticky=W)
 
    def addition(self):
        try: 
            self.answ=float(self.num_1.get())+float(self.num_2.get())
            self.answ=str(self.num_1.get())+" + "+str(self.num_2.get())+" = "+str(self.answ)
        except ValueError:
            self.answ="Оба числа должны быть заполнены цифрами"
        self.calculate()
 
    def substraction(self):
        try:
            self.answ=float(self.num_1.get())-float(self.num_2.get())
            self.answ=str(self.num_1.get())+" - "+str(self.num_2.get())+" = "+str(self.answ)
        except ValueError:
            self.answ="Оба числа должны быть заполнены цифрами"
        self.calculate()
 
    def multiplication(self):
        try:
            self.answ=float(self.num_1.get())*float(self.num_2.get())
            self.answ=str(self.num_1.get())+" * "+str(self.num_2.get())+" = "+str(self.answ)
        except ValueError:
            self.answ="Оба числа должны быть заполнены цифрами"
        self.calculate()
 
    def division(self):
        try:
            self.answ=float(self.num_1.get())/float(self.num_2.get())
            self.answ=str(self.num_1.get())+" / "+str(self.num_2.get())+" = "+str(self.answ)
        except ZeroDivisionError:
            self.answ="Деление на ноль невозможно"
        except ValueError:
            self.answ="Оба числа должны быть заполнены цифрами"
        self.calculate()
 
    def calculate(self):
        self.answer.delete(0.0,END)
        self.answer.insert(0.0,self.answ)
        self.num_1.delete(0, END)
        self.num_2.delete(0, END)
 
root=Tk()
root.title("Калькулятор")
calc=Calcul(root)
root.mainloop()

