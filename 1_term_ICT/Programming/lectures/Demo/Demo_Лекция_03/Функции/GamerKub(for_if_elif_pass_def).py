from random import randint
import time

def InputGamer(lstG):
    lstG.append(input('Введите имя 1-го играющего '))
    lstG.append(input('Введите имя 2-го играющего '))
    


def whoChampion(k1, k2, lst):
    k11 = sorted(k1, reverse = True)
    k22 = sorted(k2, reverse = True)
    if k11 > k22:
        return ('Выиграл {0}, число побед: {1}'.format(lst[0], k1))
    elif k11 < k22:
        return ('Выиграл {0}, число побед: {1}'.format(lst[1], k2))
    else:
        return 'Ничья'

def whoChampion2(k1, k2, lst):
    k1.sort(reverse = True)
    k2.sort(reverse = True)
    if k1 > k2:
        return ('Выиграл {0}, число побед: {1}'.format(lst[0], k1))
    elif k1 < k2:
        return ('Выиграл {0}, число побед: {1}'.format(lst[1], k2))
    else:
        return 'Ничья'



lstIgrok = []
InputGamer(lstIgrok)


k1 = [6,5,4,3,5,6,4]
k2 = [6,6,3,3,2,3,6]

fin = whoChampion(k1,k2, lstIgrok)
print(fin)
print(k1, '\n', k2)

fin = whoChampion2(k1,k2, lstIgrok)
print(fin)
print(k1, '\n', k2) 

