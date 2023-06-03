from random import randint
import time


class Dice:
    def __init__(self):
        self.n = randint(1, 6)

    def bro(self):
        self.n = randint(1, 6)
        
        
class Gamer:

    def __init__(self, name, n = 0):
        self.name = name
        
    def brosok(self, dice):
        dice.bro()
        self.n = dice.n
        return self.n

    def __str__(self):
        return "Игрок {0.name}".format(self)


 

def whoChampion(a, b):
    if a > b:
        return ('Выиграл {0}, число побед: {1}'.format(g1, a))
    elif a < b:
        return ('Выиграл {0}, число побед: {1}'.format(g2, b))
    else:
        return 'Ничья'

def InputGamer():
    ig1 = input('Введите имя 1-го играющего ')
    ig2 = input('Введите имя 2-го играющего ')
    return (ig1, ig2)

#Ввод имен играющих
#igrok1 = input('Введите имя 1-го играющего ')
#igrok2 = input('Введите имя 2-го играющего ')

igrok1, igrok2 = InputGamer()
g1 = Gamer(igrok1)
g2 = Gamer(igrok2)
d1 = Dice();

k1 = k2 = 0    # количество побед каждого игрока

for i in range(5):
    #Моделирование бросания кубика первым играющим
    print('Кубик бросает', g1)
    time.sleep(2)
    #n1 = randint(1, 6)
    n1 = g1.brosok(d1)
    print('Выпало:', n1)

    #Моделирование бросания кубика вторым играющим
    print('Кубик бросает', g2)
    time.sleep(2)
    n2 = g2.brosok(d1)
    print('Выпало:', n2)

    #Определение результата (3 возможных варианта)
    if n1 > n2:
        print('В раунде выиграл', g1)
        k1 += 1
    elif n1 < n2:
        print('В раунде выиграл', g2)
        k2 += 1
    else:
        print('Ничья')

fin = whoChampion(k1,k2)
print("Итог игры: ", fin)




#if k1 > k2:
#        print('Выиграл', igrok1, "число побед: ", k1)
#elif k1 < k2:
#        print('Выиграл', igrok2, ": ", k2)
#else:
#        print('Ничья')
