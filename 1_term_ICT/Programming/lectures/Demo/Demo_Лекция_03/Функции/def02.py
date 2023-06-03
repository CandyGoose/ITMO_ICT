def function1(first,second):        # локальные переменные - внутри функции
    c = first + second
    return c

def functionMul(first,second):
    c = first * second
    return c

a = 10
b = 20
resSum = function1(a,function1(a,b))
resMul = function1(a,functionMul(a,b))
print("The value of \"res\" is: ", resSum, resMul)     # 40 210

def num(v):
    v.append('ten')

my_list = ['one','seven']
num(my_list)
print(my_list)

"""
Функции являются полиморфными - то есть они могут обрабатывать объекты
произвольных типов, при условии, что они поддерживают ожидаемый интерфейс
"""

newL = function1(my_list, my_list) # если функции передать объекты другого типа
print(newL)

# если функции передать объекты совершенразных типов
#newL = function1(my_list, 2) # если функции передать объекты другого типа
print(newL) # TypeError: can only concatenate list (not "int") to list

# если функции передать объекты совершенразных типов
newL = functionMul(my_list, 2) # если функции передать объекты другого типа
print(newL) # теперь ошибки не будет - строка умеет умножать на целое


def intersect(seq1, seq2):
    """
    то же, что и генератор списков [x for x in s1 if x in s2] 
    """
    res = []    # Изначально пустой результат
    for x in seq1:
        # Обход последовательности seq1
        if x in seq2: # Общий элемент? 
            res.append(x) # Добавить в конец 
    return res 

s1 = "SPAM" 
s2 = "SCAM" 
s12 = intersect(s1, s2)     # Аргументы - строки
print("intersect: ", s12)   # ['S', 'A', 'M']

x = intersect([1, 2, 3], (1, 4)) # Смешивание типов (аргументы список и кортеж) - полиморфность
print(x)        # 1

#x = intersect(123, 143) # Смешивание типов, но TypeError: 'int' object is not iterable
#print(x)


# для передачи позиционных аргументов можно использовать оператор  
# распаковывания последовательностей (*)
def product(*args):
    result = 1
    for arg in args:
        result *= arg
    return result 

print(product(1,2,3))       # 6
print(product(1,2,3,4))     # 24
print(product(1,2,3,4,5))   # 120

# использовать именованные аргументы после позиционных 
def sum_of_powers(*args, power=1):
    result = 0
    for arg in args:
        result += arg ** power 
    return result
print(sum_of_powers(1,2,3,4))               # 10
print(sum_of_powers(1,2,3,4, power = 2))    # 30
print(sum_of_powers(1,2,3,4,5, power = 3))  # 225



def num2(v):
    v+=2; print('внутри функции -', v)      # 5

b = 3
num2(b) # передача параметров неизменяемых типов
print('после "возвращения" из функции -', b) # 3
