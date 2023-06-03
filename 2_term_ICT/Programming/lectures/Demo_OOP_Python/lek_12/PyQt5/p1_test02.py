"""
 1. Перейти в папку с проектом, скопирвать файл mainwindow.ui в папку Scripts,
 которая находится в папке с Python’ом, и ввести команду
pyuic5.exe mainwindow.ui -o gui.py
 2. Полученный gui.py перемести в папку с питоновским проектом и подключить
 соответствующим кодом
"""
# C:\Users\niko\AppData\Local\Programs\Python\Python38\Scripts

import random
import string
import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import p1gui

class Example(QWidget, p1gui.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.buttonClicked)

    def generate_pins(self, size=6, chars=string.digits):
        return ''.join(random.choice(chars) for x in range(size))

    def buttonClicked(self):
        print("test: ", self.generate_pins())
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Example()
    form.show()
    app.exec()

