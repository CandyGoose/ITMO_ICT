# применение итераторов
lst = [1, 3, 5, 7, 9]
lst2 = lst[:]

sum1 = 0
for i in lst:
   sum1 += i

print(sum1)

sum2 = 0
iter_obj = iter(lst2)

while True:
    try:
        i = next(iter_obj)
        sum2 += i
    except StopIteration:
       break

print(sum2)

# 1. Последовательности

fruits = ["апельсины", "яблоки", "мандарины", "лимоны"]
#  enumerate(iterable, start=0) - Возвращает итератор, где каждый элемент является парой «номер» - «значение».
# Номер отсчитывается от start
# получить последовательность кортежей (номер, элемент):
print(tuple(enumerate(fruits, start=1)))
print(list(enumerate(fruits, start=1)))

# Используя enumerate(), можно "дать" порядковый номер элементу коллекции в цикле
for i, item in enumerate(fruits, start=1):
    print(i, item)

# Используя sorted(), можно вывести элементы коллекции в порядке возрастания
for item in sorted(fruits):
    print(item)    


# 2. Словари

employee = {"ФИО": "Петов Сергей Викторович",
             "Отдел": "Продаж",
             "Дата рождения": "16.12.1998"}

# По умолчанию цикл for перемещается по ключам
# enumerate() и sorted() аналогично работают только с ключами
for attr in sorted(employee):
    print(attr)  # Получить значение по ключу - employee[attr]

# Используя items() можно сразу получать пару ключ-значение
for attr, value in employee.items():
    print(attr, ":\t", value)
