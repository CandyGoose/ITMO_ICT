from PyQt5 import QtWidgets, uic # pip install pyqt5 
import sys
import random
import string
 
app = QtWidgets.QApplication([])

""" функция условно генерирует ключи """
def generate_pins(size=4, chars=string.digits):
    return ''.join(random.choice(chars) for x in range(size))

def btnClicked():
    print("test: ", generate_pins())

win = uic.loadUi("p1.ui")       # расположение файла .ui

"""
pushButton – это имя объекта (кнопки),
clicked – событие (сигнал),
buttonClicked – функция, которая исполнится при этом событии (слот). """
win.pushButton.clicked.connect(btnClicked)

win.show()
sys.exit(app.exec())
