
class Person:

    # конструктор
    def __init__(self, name):
        self.name = name        # устанавливаем имя

    # деструктор
    """
    функция __del__будет вызываться либо в результате вызова оператора del,
    либо при автоматическом удалении объекта
    """
    def __del__(self):
        print(self.name,"удален из памяти")
       
    def display_info(self):
        print("Имя: {0}, Возраст: {1}".format(self.name, self.age))



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


