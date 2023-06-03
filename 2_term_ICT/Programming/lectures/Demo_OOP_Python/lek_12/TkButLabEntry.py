"""
В Tkinter существует три способа конфигурирования свойств виджетов: 
− в момент создания объекта, 
− с помощью метода config(), он же configure(), 
− путем обращения к свойству как к элементу словаря
"""

from tkinter import *
 
root = Tk()
b1 = Button(text="Изменить", width=15, height=3) # момент создания объекта
 
def change():
    b1['text'] = "Изменено"     # путем обращения к свойству как к элементу словаря
    b1['bg'] = '#000000'
    b1['activebackground'] = '#555555'
    b1['fg'] = '#ffffff'
    b1['activeforeground'] = '#ffffff'
 
b1.config(command=change)       # с помощью метода config()
 
b1.pack()

l1 = Label(text="Первая", font="Arial 32")
l2 = Label(text="Вторая", font=("Comic Sans MS", 24, "bold"))
l1.config(bd=20, bg='#ffaaaa')
l2.config(bd=20, bg='#aaffff')
l1.pack()
l2.pack()

e1 = Entry(width=50)
e2 = Entry(width=50)

def insert():
    e = e1.get()        # взять текст
    e1.delete(0,END)    # удалить текст 
    e2.insert(0,e)      # вставить текст 

b = Button(text="Вставить", command=insert)
e1.pack()
e2.pack()
b.pack()

root.mainloop()

