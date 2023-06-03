#  Индексация и срезы
s = "Python"
print(s[-1])    # Последний символ - 'n'
print(s[0:2])   # Срез включает первые 2 символа - 'Py'
print(s[2:-1])  # С 3 по предпоследний символ - 'tho'
print(s[0:-1:2])  # С 1 по предпоследний символ через 2 - 'Pto'

# Параметры [start] и [end] могут быть опущены
# В таком случае срез берется с начала и до конца строки 
print(s[:3])    # Первые 3 символа - 'Pyt'
print(s[3:])    # С 3-го символа до конца - 'hon'

# Срезы можно использовать для получения строки в обратном порядке:
print(s[::-1])  # nohtyP

# Кортежи

t1 = 1,2,3
t2 = (4,5,6)
print(t1, "\n", t2)
print((101, 102, 103)) # передать кортеж значений в функцию

t1 += 11,22,33 # новый кортеж с результатом операции, присваемый ссылке на ноыый объект
print(t1)

# извлечение элементов
print(t1[2], ";", t1[-4] ) # один и тот же элемент
print(t1[2:])   # получение элементов с помощью среза
print(t1[2:4])
 
# вложение кортежей, допускают возможность вложения с любой глубиной вложенности

t3 = t1[3:], 101, t2[1:]
print(t3)
print(t3[0][2])

things = (1, -7.5, ("abc", (5, "ABC"), "queue"))
print(things[2][1][1][2])

# присвоение индексам имена

MANUFACTURER, MODEL, SEATING = (0, 1, 2) # последовательность справа распаковывается
MINIMUM, MAXIMUM = (0, 1)
aircraft = ("Airbus", "A320-200", (100, 220))
print(aircraft [SEATING] [MAXIMUM])

# Именованные кортежи
# можно ссылаться по имени, что позволяет создавать сложные агрегаты из элементов данных

import collections
Sale = collections.namedtuple("Sale", "productid customerid date quantity price")

# создаются объекты типа sale

sales = []
sales.append(Sale(432, 921, "2008-09-14", 3, 7.99))
sales.append(Sale(419, 874, "2008-09-15", 1, 18.49))

total = 0
for sale in sales:
    total += sale.quantity * sale.price
print("Total ${0:.2f}".format(total))


Aircraft = collections.namedtuple("Aircraft", "manufacturer model seating")
Seating = collections.namedtuple("Seating", "minimum maximum")
aircraft = Aircraft("Airbus", "A320-200", Seating(100, 220))
#print(aircraft.seating.maximum)

# Списки
# Список (list) - это упорядоченная изменяемая последовательность элементов
L = [-17.5, "kilo", 49, "V", ["ram", 5, "echo"], 7] 
#print(L[1][0])
#print(L[4][2])
#print(L[4][2][1])

# одновременное извлечение двух или более частей списка
# распаковка с помощью оператора распаковывания (*)
first, *rest = [9, 2, -4, 8, 7]
#print((first, rest)) # (9, [2, -4, 8, 7])
first, *mid, last = "Charles Philip Arthur George Windsor".split()
#print(first, mid, last) # ('Charles', ['Philip', 'Arthur', 'George'], 'Windsor')
*directories, executable = "/usr/local/bin/gvim".split("/")
print(directories, executable)

def product(a, b, с):
    return a * b * с #  * -  оператор умножения

print(product(2, 3, 5)) # обычный вызов с тремя аргументами
L = [2, 3, 5]           # передыча одного распакуемого элемента
print(product(*L))
print(product(2, *L[1:]))   # первый - обычным, второй распаковывется срез


# Словари

#несколько способов создания словарей - все они создают один и тот же словарь:
d1 = dict({"id": 1948, "name": "Washer", "size": 3})
d2 = dict(id=1948, name="Washer", size=3)
d3 = dict([("id", 1948), ("name", "Washer"), ("size", 3)])
d4 = dict(zip(("id", "name", "size"), (1948, "Washer", 3)))
d5 = {"id": 1948, "name": "Washer", "size": 3}
#print(d1)

mydict = {"Key 1": "Value 1", 2: 3, "pi": 3.14} #Создаем словарь с числовыми и целочисленными индексами
print(mydict)

mydict["pi"] = 3.15 #Изменяем элемент словаря под индексом «pi».
#print(mylist)

dp = {} # пустой словарь
# заполнение словаря
dp['color'] = 'red'
dp['index'] = 101
print(dp)

dp['name'] = input("Enter name:  ")
dp['age'] = int(input("Enter age: "))
print(dp)




