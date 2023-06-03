from tkinter import *

def output(event):
     s = ent.get()
     if s == "1":
         tex.delete(1.0,END)
         tex.insert(END,"Обслуживание клиентов на втором этаже")
     elif s == "2":
         tex.delete(1.0,END)
         tex.insert(END,"Пластиковые карты выдают в соседнем здании")
     else:
         tex.delete(1.0,END)
         tex.insert(END,"Введите 1 или 2 в поле слева")

 
root = Tk()

ent = Entry(root,width=1)
but = Button(root,text="Вывести")
tex = Text(root,width=20,height=3,font="12", bg="darkgreen", fg='white',wrap=WORD)
ent.focus()

ent.grid(row=0,column=0,padx=20)
but.grid(row=0,column=1)
tex.grid(row=0,column=2,padx=20,pady=10)
but.bind("<Button-1>",output) # три компонента (виджет, событие и функция) связываются с помощью метода bind.
but.bind("<Return>",output)   # нажатие клавиши Enter в фокусе кнопки
root.bind("<Return>",output)  # нажатие клавиши Enter в главном окне


root.mainloop()
