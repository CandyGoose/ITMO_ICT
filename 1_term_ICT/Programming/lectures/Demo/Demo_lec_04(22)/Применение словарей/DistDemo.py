# Словари

#несколько способов создания словарей - все они создают один и тот же словарь:
d1 = dict({"id": 1948, "name": "Washer", "size": 3})
d2 = dict(id=1948, name="Washer", size=3)
print(id(d1))  # id() работает как раньше
d3 = dict([("id", 1948), ("name", "Washer"), ("size", 3)])
d4 = dict(zip(("id", "name", "size"), (1948, "Washer", 3)))
d5 = {"id": 1948, "name": "Washer", "size": 3}


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


'''
Данные могут содержать вложенные структуры, поэтому для доступа к более низкому уровню
будем использовать двойные индексы

Пример 1. Сущность "Сотрудник"
'''

employee = {'name': {'first': 'Ivan', 'last': 'Ivanov'},
        'age': 25,
        'job': ['software', 'writing', 'other....'],
        'pay': (1000, 2000, 5000)}


print(employee['name'])           #  имя и фамилия 
print(*employee['name'].values())

print(employee['name']['last'])   # фамилия 

print(employee['pay'][0])         # нижний предел оплаты

for job in employee['job']:
    print(job)                  # все должности
print(*employee['job'])

print(employee['job'][-1])        # последняя должность

print(employee['job'].append('janitor')) #  получает новую должность
print(employee)

''' update - обновление / вставка данных '''
age = {'age': 35}
status = {'status' : 'leader'}
employee.update(age)
print(employee['age'])
employee.update(status)
print(employee)          


'''
Пример 2. Сущность "Крестики-нолики"
словарь можно применить как структуру данных,
которая представляет состояние поля для игры в “крестики-нолики” 
'''
board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ' ,
         'mid-L': ' ', 'mid-M' : ' ', 'mid-R':	' ' ,
         'low-L': ' ', 'low-M' : ' ', 'low-R':	' '}
print(board)
'''
Если игрок X своим первым ходом выберет центральную клетку
'''
step_x = 'X'
step_o  ='0'
board['mid-M'] = step_x
print(board)
