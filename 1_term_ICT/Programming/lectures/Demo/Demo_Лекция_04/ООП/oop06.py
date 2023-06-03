# Наследование
class Person:
   
    # конструктор
    def __init__(self, name):
        self.__name = name  # устанавливаем имя
        self.__age = 1      # устанавливаем возраст
 
    @property
    def age(self):
        return self.__age
 
    @age.setter
    def age(self, age):
        if age in range(1, 100):
            self.__age = age
        else:
            print("Недопустимый возраст")
     
    @property
    def name(self):
        return self.__name

    # деструктор
    def __del__(self):
    #    print(self.name,"удален из памяти")
        print(self.__name,"удален из памяти")
       
    def display_info(self):
    #    print("Имя: ", self.name, "\tВозраст: ", self.age)
         print("Имя: ", self.__name, "\tВозраст: ", self.__age)


# класс Employee наследуется от класса Person
class Employee(Person):
     def details(self, company):
        # print(self.__name, "работает в компании", company) # так нельзя, self.__name - приватный атрибут
        print(self.name, "работает в компании", company)

# создание объектов класса 
person3 = Person("Петр")
person3.age = 77   # обращение к свойству-геттер
person3.display_info()         

employee1 = Employee("Иван")
employee1.age = 33
employee1.display_info()
employee1.details("Google")


 
del person3     # удаление объекта из памяти
# person3.display_info()  # Этот метод работать не будет, так как person3 уже удален из памяти
# NameError: name 'person3' is not defined
