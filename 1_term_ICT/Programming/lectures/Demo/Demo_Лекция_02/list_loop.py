from random import randint
import statistics

""" 1. Список известен заранее """
data = [11,21,3,14,51,16,72,81,19,101,11,27]
print(*data, sep=',')
k = len(data)
print(k)

newdata = []                # пустой список

for d in data:              # просмотр в списке по элементу
    if d % 2 == 0:
        newdata.append(d)
    
print(newdata)


for it in range(k):         # создаются числа-индексы от 0 до k-1
    if data[it]%3 == 0:     # просмотр в списке по индексу
        newdata.append(data[it])

print(newdata)

""" 2. Список не известен заранее - ввод с клавиатуры
       но известно количество """

n = 6
data2 = []
for nom in range(n):
    a = int(input('Введите очередное число '))
    data2.append(a)

print(data2)

""" 2. Список не известен заранее - ввод с клавиатуры
       и также не известно количество """

data3 = []
while True:     # бесконечный цикл
    a = input('Введите очередное число ')
    if a != 'z':
        data3.append(int(a))
    else:
        break

print(data3)

# или тоже самое, но без else:

data4 = []
while True:
    a = input('Введите очередное число ')
    if a == 'z':
        break
    data4.append(int(a))

print(data4)

""" 3. Список не известен заранее - случайные числа """

n = 15
data5 = []
for nom in range(n):
    a = randint(1,100)
    data5.append(a)

print(data5)
print(sum(data5))
print(statistics.mean(data5))

