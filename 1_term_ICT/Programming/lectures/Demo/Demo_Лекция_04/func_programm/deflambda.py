
# одно и тоже с помощью функции и лямбда-выражения
def func(x, y, z):
    return x + y + z

# и лямбда-выражения
f = lambda x, y, z: x + y + z
print(f(1,2,3))

# можно использовать аргументы со значениями по умолчанию:
x = (lambda a="aaa", b="bbb", c="ccc": a + b + c)
print(x("www"))     # wwwbbbccc

# помещать внутрь lambda другие выражения
lower = (lambda x, y: x if x < y else y)
print(lower(23,45))         # 23
print(lower("k23","a45"))   # a45

"""
Применение лямбда-выражений
"""

# Реализация сортировки по требуемому полю

elements = [(2, 12, "Mg"), (1, 11, "Na"), (1, 3, "Li"), (2, 4, "Be")] 
elements.sort()
print(elements)

# по порядковому номеру и названию          
elements.sort(key=lambda e: (e[1], e[2])) 
print(elements)

# по названию, без учета регистра символов, и порядковому номеру: 
elements.sort(key=lambda e: (e[2].lower(), e[1])) 
print(elements)

# выполнеение действий по требованию - вмесо создания трех именованных функций
L = [lambda x: x**2,          # Встроенные определения функций 
     lambda x: x**3, 
     lambda x: x**4]          # Список из трех функций 

for f in L:
    print(f(2))    #  4, 8, 16 

print(L[0](3))     #  9 

#вложенные выражения
def action(x):
    return (lambda y: x + y) # Создать и вернуть ф-цию

act = action(99)
print(act)    # <function <lambda> at 0x00A16A88>
print(act(2))


"""
Совместное применение lambda и других функций
"""
# Функции max и min имеют ключевой аргумент key - параметр сортировки
# key - ссылка на функцию, имеющую 1 возвращающую значение, по которому следует
# сравнивать величины
lst = ["Java", "Basic", "C++", "Python"]
print(max(lst, key=lambda x: x.count("a")))  # Элемент lst, в котором
                                             # больше всего "a"

# filter() - фильтрация элементов последовательности
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61] 
final_list = list(filter(lambda x: (x%2 != 0) , li)) 
print(final_list)           # [5, 7, 97, 77, 23, 73, 61]

# получение общих данных
arr1 = [1, 3, 4, 5, 7] 
arr2 = [2, 3, 5, 6] 
result = list(filter(lambda x: x in arr1, arr2))  
print ("Intersection : ", result)   # [3, 5]


# Функция map применяет к каждому элементу списка переданную функцию
"""
Изменение элементов списка по вашей анонимной функции
"""
mile_distances = [1.0, 6.5, 17.4, 2.4, 9]
kilometer_distances = list(map(lambda x: x * 1.6, mile_distances))
print (kilometer_distances)     #  [1.6, 10.4, 27.84, 3.84, 14.4]


# Функция reduce() принимает 2 аргумента: функцию и последовательность и 
# последовательно применяет функцию-аргумент к элементам списка, возвращает единичное значение.
# Python 3 функция в модуле functools
"""
Вычисление суммы всех элементов списка при помощи reduce:
"""
from functools import reduce
items = [1,2,3,4,5]
sum_all = reduce(lambda x,y: x + y, items)
 
print (sum_all)     # 15

