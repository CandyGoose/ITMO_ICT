x = 12 #  глобальная переменная (закоментируйте операцию присваивания локальной x)
L = [1,2,3]

# объявление функции - глобальное имя
def get_int(msg): # msg - локальная
    while True:
        try:
           # x = int(input(msg)) # локальная переменная
            return x
        except ValueError as err:
                print(err)

def min_of_cubes(x, y):

    # Идентификаторы 'x' и 'y' являются:
    # - локальными для min_of_cubes()
    # - нелокальными для cube()

    def cube(a):
        return a**3  # 'a' - локальный идентификатор функции cube()

    return min(cube(x), cube(y), cube(c))  # Функция min() находится
                                           # во встроенной области
                                           # видимости и видна везде

# Идентификаторы 'a', 'b' и 'c' имеют глобальную область видимости
a, b, c = 2, 3, 4
print("min_of_cubes = ", min_of_cubes(a, b))  # 8

x = 8
# вызов функции
age = get_int("enter your age: ")
print(age)

#x = 16

# Пробуем изменить глобальную переменную 'c'
a, b, c = 3, 4, 5
def sum_of_2(a, b):
    с = 10
    return a + b + с

print(sum_of_2(a, b))  # 17
print(a, b, c)         # 3 4 5
# По умолчанию, идентификаторы из другой области видимости доступны только для чтения,
# при попытке присвоения, функция создает локальный идентификатор.

# Как изменить глобальную переменную?

# Использование инструкции global

def workL(x):
    #L.append(x)    # изменяется глобальный объект
    #L = x           # L классифицируется как локальный объект и глобальный объет(переменная) не измнится!
    global L
    L = 777         # Глобальная переменная
    print(L, " локальное значение")

workL(23)
print(L, "глобальное значение")

y, z = 1, 2 # Глобальные переменные в модуле 
def all_global():
    global xx    # Объявляется глобальной для присваивания
    xx = y + z   # Объявлять y, z не требуется 

all_global()
print('xx = ', xx)


# Использование инструкции nonlocal
# для изменения переменных

def tester(start):
    state = start       # Обращение к нелокальным переменным
    def nested(label):  
        nonlocal state    # Нелокальные переменные должны существовать
        print(label, state) # Извлекает значение state из области
        state += 1          # UnboundLocalError: local variable 'state' referenced before assignment или
                            # Изменит значение переменной, объявленной как nonlocal
    return nested       # видимости объемлющей функции

F = tester(0)
F("start1")
F("start2")

G = tester(50)
G("book1")
G("book2")
      
