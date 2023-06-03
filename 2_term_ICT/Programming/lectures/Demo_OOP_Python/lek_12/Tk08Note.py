from tkinter import *
from tkinter import ttk
 
window = Tk()  
window.title("Добро пожаловать")  
window.geometry('400x250')

""" элемент управления вкладкой - класс Notebook """
tab_control = ttk.Notebook(window)

tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)

tab_control.add(tab1, text='Общие')
tab_control.add(tab2, text='Дополнительно')

"""
После создания вкладок чтобы поместить виджеты внутри этих вкладок,
надо назначить родительское свойство нужной вкладке """

lbl1 = Label(tab1, text='Параметры', padx=5, pady=5)  
lbl1.grid(column=0, row=0)

lbl2 = Label(tab2, text='Сервисы')  
lbl2.grid(column=0, row=0)  

tab_control.pack(expand=1, fill='both')


window.mainloop()
