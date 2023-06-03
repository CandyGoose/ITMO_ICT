from tkinter import *

li = ["red","green"]

def color(event):
    fra.configure(bg=li[0])
    li[0],li[1] = li[1],li[0]

def outgo(event):
    root.destroy()

def b1(event):
    root.title("Левая кнопка мыши")
def b3(event):
    root.title("Правая кнопка мыши")
def move(event):
    root.title("Движение мышью")

 
root = Tk()

fra = Frame(root,width=100,height=100)
but = Button(root,text="Выход")

fra.pack()
but.pack()

root.bind("<Return>",color) # нажатие клавиши Enter в пределах главного окна
but.bind("<Button-1>",outgo)

root.bind('<Button-1>',b1)
root.bind('<Button-3>',b3)
root.bind('<Motion>',move)


root.mainloop()
