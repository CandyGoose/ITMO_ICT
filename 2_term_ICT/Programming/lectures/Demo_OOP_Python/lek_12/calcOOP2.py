from tkinter import *
from tkinter import ttk
from tkinter import messagebox
 
class Calc:
    def __init__(self, master):
        self.num_1 = ttk.Entry(master, width=10, font="15", justify=RIGHT)
        self.num_2 = ttk.Entry(master, width=10, font="15", justify=RIGHT)
 
        name_sx = ['minus', 'plus', 'multiply', 'divide','clear']
        operator = ['-','+','*','/','clear']
        for s,o,n in zip(name_sx,operator,range(1,100)):
            exec('self.{0} = ttk.Button(master, text="{1}", command=self.{0})'.format(s,o))
            exec('self.{0}.grid(row={1}, column=2, padx=2, pady=4)'.format(s,n))
 
        self.label = ttk.Label(master, anchor='c', text=0, width=20, font="Arial 14")
 
        self.num_1.grid(row=1, column=1)
        self.num_2.grid(row=2, column=1)
        self.label.grid(row=3, column=1, padx=50, pady=4)
 
    funcs = ['minus', 'plus', 'multiply', 'divide']
    oper = ['-','+','*','/']
    for f, o in zip(funcs, oper):
        def bindedfunc(self, op=o):
            try:
                self.label["text"] = eval('float(self.num_1.get()) {} float(self.num_2.get())'.format(op))
            except ValueError:
                messagebox.showerror("Ошибка заполнения", "Ведите в поле коректные данные")
        exec('{} = bindedfunc'.format(f))
 
    def clear(self):
        self.num_1.delete(0, END)
        self.num_2.delete(0, END)
        self.label["text"] = 0
 
root = Tk()
root.geometry("450x200")
root.title("Калькулятор")
app = Calc(root)
 
root.mainloop()
