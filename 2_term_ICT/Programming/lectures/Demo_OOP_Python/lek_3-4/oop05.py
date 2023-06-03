# По умолчанию атрибуты в классах являются общедоступными
"""
Свойство определяется при помощи декораторов:
- @property: определяет метод получения значения;
- @r.setter: определяет метод установки значения свойства r.
Имя свойства r определяется в наименовании обоих методов и декораторе @r.setter. Если необходимо реализовать свойство «только для чтения», второй метод может быть опущен
"""

class Person:
   
    # конструктор
    def __init__(self, name):
        self.__name = name  # устанавливаем имя
        self.__age = 1      # устанавливаем возраст
 
    @property               # Для создания свойства-геттера
    def age(self):
        return self.__age
 
    @age.setter             # Для создания свойства-сеттера 
    def age(self, age):
        if age in range(1, 100):
            self.__age = age
        else:
            print("Недопустимый возраст")
     
    @property               # свойство только для чтения
    def name(self):
        return self.__name



    # деструктор
    def __del__(self):
    #    print(self.name,"удален из памяти")
        print(self.__name,"удален из памяти")
       
    def display_info(self):
    #    print("Имя: ", self.name, "\tВозраст: ", self.age)
         print("Имя: ", self.__name, "\tВозраст: ", self.__age)


# создание объектов класса 
person3 = Person("Петр")
person3.age = 77   # обращение к свойству-cеттер
#person3.name = "Вася"  # AttributeError: can't set attribute

person3.display_info()         
 
del person3     # удаление объекта из памяти
# person3.display_info()  # Этот метод работать не будет, так как person3 уже удален из памяти
# NameError: name 'person3' is not defined
