"""
Встроенные функции высшего порядка
без импорта библиотек - map и filter
"""

"""
Функция map принимает функцию и итератор, возвращает итератор, элементами которого являются
результаты применения функции к элементам входного итератора.
"""
"""
Не функциональный код принимает список имён и заменяет их случайным статусом"""
import random
names = ['Петр', 'Иван', 'Василий']
code_names = ['Мастер', 'Специалист', 'Ученик']

for i in range(len(names)):
    names[i] = random.choice(code_names)

print(names)

# Как это сделать с помощью map?

a = [1, 2, 3, 4, 5]

list(map(lambda x: x**2, a))        # [1, 4, 9, 16, 25]

# Вариант с функцией map можно заменить на (списковое включение (list comprehensions)):
list(x**2 for x in a)               # [1, 4, 9, 16, 25]

def fun(x):
    if x % 2 == 0:
        return 0
    else:
        return x*2

print(list(map(fun, a)))             # [2, 0, 6, 0, 10]


a = [1, 20, 3, 10, 15]
def fun(x):
    if x < 10:
        return x*1.13
    elif x > 10:
        return x*0.18
    else:
        return x

print(list(map(fun, a)))             # [2, 0, 6, 0, 10]
#решение для задачи с именами:
secret_names = list(map(lambda x: random.choice(code_names), names))
print(secret_names)

"""
Функция filter принимает функцию предикат и итератор, возвращает итератор, элементами которого
являются данные из исходного итератора, для которых предикат возвращает True.
"""

list(filter(lambda x: x > 0, [-11, 11, -21, 21, 0]))            # [11, 21]
# или можно так:
list((v for v in [-1, 1, -2, 2, 0] if v > 0))

list(filter(lambda x: len(x) == 2, ["a", "aa", "b", "bb"]))     # ['aa', 'bb']

"""
Функция reduce сворачивает переданную последовательность с помощью заданной функции.
"""

from functools import reduce

def add(x1,x2):
    return x1+x2
    
a = [1,2,3,4,5]

sum_all = reduce(add, a)

mul_all = reduce(lambda x, y: x*y, a)

print (sum_all, mul_all)     # 15 120


# Пример. Подсчитать как часто слово «капитан» встречается в списке строк

sentences = ['капитан джек воробей',
             'капитан дальнего плавания',
             'ваша лодка готова, капитан']

# не функциональное решение:
cap_count = 0
for sentence in sentences:
    cap_count += sentence.count('капитан')

print(cap_count)

# решение с использованием reduce:
sentences = ['капитан джек воробей',
             'капитан дальнего плавания',
             'ваша лодка готова, капитан']

cap_count = reduce(lambda a, x: a + x.count('капитан'), sentences, 0)

print(cap_count)



''' Пример 1.
    Умножение каждого элемента масива на 0.13
    и округление его до двух знаков'''
print('Сколько чисел будет в списке?')
n = int(input())                                # читаем количество чисел в списке
print(f"Введите {n} чисел")
lis = [float(input())*0.13 for _ in range(n)]     # создание списка
l_sorted = sorted(lis)                            # сортировка массива

l_rounded = list(map(lambda x: round(x, 2), l_sorted))  # округление каждого элемента массива

print(l_rounded)

#with open('newfile.txt', 'w', encoding='utf-8') as f:  # открытие файла с помощью менеджера контекста with ... as ...:
#    f.write(str(l_rounded))  # запись в файл


''' Пример 2.
    Дан список сотрудников,
    требуется вывести список имег отсортированный по алфавиту '''
employees = [
    {'Name': 'Alan Turing', 'age': 25, 'salary': 10000},
    {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000},
    {'Name': 'John Hopkins', 'age': 18, 'salary': 1000},
    {'Name': 'Mikhail Tal', 'age': 405, 'salary': 15000},
]


employees.sort(key=lambda x: x.get('Name'))             # сортировка списка сотрудников по имени
names = list(map(lambda x: x.get('Name'), employees))   # создание списка имен
print(names)





