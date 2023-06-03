from oop03_1 import Person


# создание объектов класса
person3 = Person("Петр")
person3.age = 21

person3.display_info()          # обращение к методу экземпляра
Person.display_info(person3)    # обращение к объекту-функции класса

del person3.age                 # удалит атрибут age

print(person3.name)
# person3.display_info()        # Этот метод работать не будет

del person3                     # удаление объекта из памяти
# person3.display_info()        # Этот метод работать не будет, так как person3 уже удален из памяти
# NameError: name 'person3' is not defined


