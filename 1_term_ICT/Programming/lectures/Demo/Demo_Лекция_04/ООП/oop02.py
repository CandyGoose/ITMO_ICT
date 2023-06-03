# Функция определяется вне класса
def f1(self, x, y):
    return min(x, x+y)

class Person:
    """Описание персоны"""
    bonus1 = []     #  использование переменной класса - будет общим для всех персон   
    fp = f1         # присваивание объекта-функции локальной переменной (атрибуту класса)
    
    # конструктор
    def __init__(self, name):
        self.name = name        # устанавливаем имя
        self.bonus2 = []         # создает новый пустой список для каждой персоны
       
    def display_info(self):
        print("Имя: {0}\nБонусы:\n{1}\n{2}".format(self.name, self.bonus1, self.bonus2))



# создание объектов класса 
person3 = Person("Иван")
person3.bonus1.append(2)
person3.bonus2.append(22)

person3.display_info()          # обращение к методу экземпляра

person4 = Person("Петр")
person4.bonus1.append(23)
person4.bonus2.append(44)
person4.display_info()



Person.display_info(person3)    # обращение к объекту-функции класса         
 
print(Person.__doc__)           # возвращает строку документации

v = person3.fp(2,6)
print(v)


