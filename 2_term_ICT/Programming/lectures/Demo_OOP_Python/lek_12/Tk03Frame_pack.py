from tkinter import *
 
root = Tk()
l1 = Label(width=7, height=4, bg='yellow', text="1")
l2 = Label(width=7, height=4, bg='orange', text="2")
l3 = Label(width=7, height=4, bg='lightgreen', text="3")
l4 = Label(width=7, height=4, bg='lightblue', text="4")

"""
l1.pack()
l2.pack()
l3.pack()
l4.pack()

l1.pack(side = BOTTOM)
l2.pack(side = BOTTOM)
l3.pack(side = BOTTOM)
l4.pack(side = BOTTOM)

l1.pack(side = LEFT)
l2.pack(side = LEFT)
l3.pack(side = LEFT)
l4.pack(side = LEFT)

l1.pack(side = RIGHT)
l2.pack(side = RIGHT)
l3.pack(side = RIGHT)
l4.pack(side = RIGHT)

l1.pack(side = TOP)
l2.pack(side = BOTTOM)
l3.pack(side = RIGHT)
l4.pack(side = LEFT)

l1.pack(side = LEFT)
l2.pack(side = LEFT)
l3.pack(side = BOTTOM)
l4.pack(side = LEFT)

"""

# Фреймы размещают на главном окне, а уже в фреймах – виджеты:
f_top = Frame(root) 
f_bot = Frame(root)
l1 = Label(f_top, width=7, height=4, bg='yellow', text="1")
l2 = Label(f_top, width=7, height=4, bg='orange', text="2")
l3 = Label(f_bot, width=7, height=4, bg='lightgreen', text="3")
l4 = Label(f_bot, width=7, height=4, bg='lightblue', text="4")
 
f_top.pack()
f_bot.pack()
l1.pack(side=LEFT)
l2.pack(side=LEFT)
l3.pack(side=LEFT)
l4.pack(side=LEFT)

# LabelFrame – фрейм с подписью
f_top = LabelFrame(text="Первый") 
f_bot = LabelFrame(text="Второй")
l1 = Label(f_top, width=7, height=4, bg='yellow', text="1")
l2 = Label(f_top, width=7, height=4, bg='orange', text="2")
l3 = Label(f_bot, width=7, height=4, bg='lightgreen', text="3")
l4 = Label(f_bot, width=7, height=4, bg='lightblue', text="4")
 
f_top.pack()
f_bot.pack()
l1.pack(side=LEFT)
l2.pack(side=LEFT)
l3.pack(side=LEFT)
l4.pack(side=LEFT)

root.mainloop()
