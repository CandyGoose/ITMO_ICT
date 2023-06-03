"""
Демонстрация реализации объектно-ориентированного подхода
"""
""" Задание.
Текст, введенный пользователем в поле, при нажатии на кнопку разбивается на список слов,
слова сортируются по алфавиту и выводятся в метке.
В окне приложения:
- текстовое поле (entry)
- метка (label)
- кнопка (button)
"""
""" Дополнительно
Требуется несколько похожих объектов-блоков, состоящих из метки, кнопки, поля.
У кнопки каждой группы должна быть своя функция-обработчик клика """

""" Tkinter импортируется стандартно для модуля Python """
from tkinter import *

"""
комплект из метки, кнопки и поля представляет собой один объект,
порождаемый от класса Block """

class Block:
    def __init__(self, master):
        """ виджеты являются значениями полей объекта типа Block """
        self.e = Entry(master, width=30)
        self.b = Button(master, text="Выполнить разбор")
        self.l = Label(master, bg='black', fg='white', width=30)
        self.e.pack()
        self.b.pack()
        self.l.pack()
    def setFunc(self, func):
        """ функция-обработчик события нажатия на кнопку устанавливается не с помощью метода bind(),
            а с помощью свойства кнопки 'command'.
            В этом случае в вызываемом методе не требуется параметр event.
            В метод мы передаем только сам объект. """
        self.b['command'] = eval('self.' + func)
        """ Функция eval() преобразует строку в исполняемый код.
            В результате получается self.b['command'] = self.strToSortlist
            или self.b['command'] = self.strReverse  """
    def strToSortlist(self):
        s = self.e.get()
        s = s.split()
        s.sort()
        self.l['text'] = ' '.join(s)
    def strReverse(self):
        s = self.e.get()
        s = s.split()
        s.reverse()
        self.l['text'] = ' '.join(s)

""" 1.
Объект окна верхнего уровня создается от класса Tk модуля tkinter. 
Переменную, связываемую с объектом, часто называют root (корень)
"""
root = Tk()
root.title("Слово")

""" 2.
первый блок """ 
first_block = Block(root)
first_block.setFunc('strToSortlist')

""" второй блок """ 
second_block = Block(root)
second_block.setFunc('strReverse')

""" 6.
Метод mainloop() объекта Tk запускает главный цикл обработки событий,
что в том числе приводит к отображению главного окна со всеми его объектами """
root.mainloop()

