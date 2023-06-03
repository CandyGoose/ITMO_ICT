"""Применение enum
"""
from enum import Enum

class Season(Enum):
    Summer, Fall, Winter, Spring = range(4)
        
class Status(Enum):
    Start = "start"
    Fin = "fin"

class Switch(Enum):
    On = True
    Off = False


winter = Season.Winter.value

available = Status.Fin.value

op = Switch.On.value

print(winter, available, op)

basewin = Season(1)
# получение значения (имени) 
basewinName = basewin.name

print(basewinName)

# получение списка значений
values = list(Season)
print(values)

class Temperature(Enum):
    minT = 0
    levelT = 55
    maxT = 100



tp = Temperature.levelT.value
t1 = 34
if t1 < tp:
    print("work")
else:
    print("not work!")

# в функциональном стиле
Season = Enum('Season', 'Summer, Fall, Winter, Spring')
winter = Season.Winter.value
print(winter)
# получение списка значений
values = list(Season)     #значения с 1
print(values)

#Temperature = Enum('Temperature', dict(minT=0, levelT=55, maxT=100))
Temperature = Enum('Temperature', {'minT':0, 'levelT':55, 'maxT':100})
tp = Temperature.levelT.value
t1 = 34
if t1 < tp:
    print("work")
else:
    print("not work!")
