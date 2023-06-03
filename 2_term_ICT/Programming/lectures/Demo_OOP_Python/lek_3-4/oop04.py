# По умолчанию атрибуты в классах являются общедоступными
class Person:
   
    # конструктор
    def __init__(self, name):
        # self.name = name  # устанавливаем имя
        self.__name = name # приватный атрибут
        # self.age = 10        # устанавливаем возраст
        self.__age = 10

    # геттер
    def get_age(self):
        return self.__age

    # сеттер
    def set_age(self, value):
        if value in range(1, 100):
            self.__age = value
        else:
            print("Недопустимый возраст")


    # деструктор
    def __del__(self):
    #    print(self.name,"удален из памяти")
        print(self.__name,"удален из памяти")
       
    def display_info(self):
    #    print("Имя: ", self.name, "\tВозраст: ", self.age)
         print("Имя: ", self.__name, "\tВозраст: ", self.__age)


# создание объектов класса 
person3 = Person("Петр")
person3.name = "Pet"
person3.__name = "Pet"
print("p3", person3.__name)

person3.set_age(77)
#person3.age = 101
person3.__age = 101
#person3.set_age(77)
person3.display_info()         
 
del person3     # удаление объекта из памяти
# person3.display_info()  # Этот метод работать не будет, так как person3 уже удален из памяти
# NameError: name 'person3' is not defined
