"""
Демонстрация реализации объектно-ориентированного подхода
"""
""" Задание.
Напишите программу, состоящую из семи кнопок, цвета которых соответствуют цветам радуги.
При нажатии на ту или иную кнопку в текстовое поле должен вставляться код цвета.
Коды цветов в шестнадцатеричной кодировке: #ff0000 – красный, #ff7d00 – оранжевый, #ffff00 – желтый,
#00ff00 – зеленый, #007dff – голубой, #0000ff – синий, #7d00ff – фиолетовый.
 """

""" Tkinter импортируется стандартно для модуля Python """
from tkinter import*
root = Tk()
root.title('#16')
f_1 = Frame(root)
f_2 = Frame(root)
f_3 = Frame(root)
f_4 = Frame(root)
f_1.pack(side=TOP)
f_2.pack(side=BOTTOM)
f_3.pack(side=BOTTOM)
f_4.pack(side=BOTTOM)
e_1 = Entry(f_1)
Label(f_1, text='Цвет в #16 кодировке', font=('Arial', 12)).pack(side=LEFT)
e_1.pack(side=LEFT)
colors = ['#ff0000',
          '#ff7d00',
          '#ffff00',
          '#00ff00',
          '#007dff',
          '#0000ff',
          '#7d00ff'
          ]
buttons = []
class _Button:
    def __init__(self, bg):
        self.bg = bg
        self.create_button()
 
    def create_button(self):
        if len(buttons) < 3:
            b = Button(f_4,
                       bg=self.bg,
                       width=10,
                       height=4,
                       command=self.response)
            b.pack(side=LEFT)
            buttons.append(b)
        elif len(buttons) > 3:
            b = Button(f_3,
                       bg=self.bg,
                       width=10,
                       height=4,
                       command=self.response)
            b.pack(side=LEFT)
            buttons.append(b)
        else:
            b = Button(f_2,
                       bg=self.bg,
                       width=10,
                       height=4,
                       command=self.response)
            b.pack(side=LEFT)
            buttons.append(b)
 
 
 
    def response(self):
        e_1.delete(0, END)
        e_1.insert(0, str(self.bg))
 
 
 
 
for color in colors:
    b = _Button(bg=color)
    #buttons.append([b, color])
mainloop()
