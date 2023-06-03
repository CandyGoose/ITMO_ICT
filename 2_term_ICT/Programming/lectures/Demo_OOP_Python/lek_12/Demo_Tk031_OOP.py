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
from tkinter import *
 
colors = ['#ff0000', '#ff7d00', '#ffff00', '#00ff00', '#007dff', '#0000ff', '#7d00ff']
colors_2={'#ff0000':"красный", '#ff7d00':"оранжевый", '#ffff00':"желтый", '#00ff00':"зелёный", '#007dff':"голубой", '#0000ff':"синий", '#7d00ff':"фиолетовый"}

root = Tk()
 
class But:
	def __init__(self, master, color):
		self.color = color
		self.b = Button(master, width=20, bg=self.color, command=self.what_color)
		self.b.pack()

	def what_color(self):
		e.delete(0, END)
		e.insert(0, self.color)
		l['text']=colors_2[self.color]
		return self.color
 
l=Label(text="")
l.pack()
e = Entry(width=25, justify='center')
e.pack()
 
for c in colors:
	But(root, c)
 
root.mainloop()
