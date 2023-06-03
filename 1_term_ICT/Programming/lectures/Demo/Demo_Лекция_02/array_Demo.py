from array import *

my_array = array('i',[1,2,3,4])

print(my_array, list(my_array))

print(my_array[1]) # Доступ к отдельным элементам через индекс

for i in my_array:
    print(i)

'''Добавить значение в массив с помощью метода append'''
my_array.append(6) 
print(list(my_array)) # [1, 2, 3, 4, 6]

''' вставить значение по индексу - первый аргумент является индексом, а второй значением'''
my_array.insert(0,10) 
print(*my_array) # 10 1 2 3 4 6

''' Расширение с помощью метода extend'''
my_extnd_array = array('i', [7,8,9,10])
my_array.extend(my_extnd_array) # my_array-массив расширен значениями из my_extnd_array 
print(*my_array) # 10 1 2 3 4 6 7 8 9 10

'''Добавить элементы из списка в массив, используя метод fromlist '''
c = [11,12,13]
my_array.fromlist(c)
print(*my_array) # 10 1 2 3 4 6 7 8 9 10 11 12 13

'''Удалите любой элемент массива, используя метод remove'''
my_array.remove(3) # элемент 3 был удален из массива
print(*my_array) # 10 1 2 4 6 7 8 9 10 11 12 13

''' Удалить последний элемент массива методом pop '''
my_array.pop()
print(*my_array) # 10 1 2 4 6 7 8 9 10 11 12

''' Получить индекс элемента с помощью метода index '''
print(my_array.index(6)) # index() возвращает первый индекс значения соответствия = 4

'''Получить информацию о буфере массива с помощью метода buffer_info ()
метод предоставляет начальный адрес буфера массива в памяти
и количество элементов в массиве'''
print(my_array.buffer_info()) # (2698076161712, 11)

'''количество вхождений элемента с помощью метода count ''' 
print(my_array.count(10)) # 2

'''Преобразовать массив в список, используя метод tolist '''
print(my_array.tolist())








