import math
import random


class Gamer:

    def __init__(self, name, n = 0):
        self.__name = name
        
    def brosok(self):
        self.n = random.randint(1, 6)
        return self.n

    def __str__(self):
        return "У игрока {0.__name!r} выпало {0.n!r} очков".format(self)



g1 = Gamer('Vds')
g1.brosok()
print(g1)    # "У игрока 'Vds' выпало ... очков"

"""
Задание.
Добавьте класс Dice, реализующий сущность игрального кубика и разместите в нем метод,
имитирующий его бросок.
Измените функцианальность класса Игрока,так чтобы его метод броска выполнялся с помощью кубика
(отношение - зависимость)
"""
