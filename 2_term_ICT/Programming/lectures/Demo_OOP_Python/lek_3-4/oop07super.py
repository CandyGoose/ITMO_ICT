# иерархия классов - полиморфизм

class Person:
    def __init__(self, name, age):
        self.__name = name  # устанавливаем имя
        self.__age = age  # устанавливаем возраст

    @property
    def name(self):
        return self.__name
 
    @property
    def age(self):
        return self.__age
 
    @age.setter
    def age(self, age):
        if age in range(1, 100):
            self.__age = age
        else:
            print("Недопустимый возраст")
 
    def display_info(self):
        print("Имя:", self.__name, "\tВозраст:", self.__age)
  

 
 
class Employee(Person):
    # определение конструктора
    def __init__(self, name, age, company):
        #Person.__init__(self, name, age)
        super().__init__(name, age)
        self.company = company
 
    # переопределение метода display_info
    def display_info(self):
        #Person.display_info(self)
        super().display_info()
        print("Компания:", self.company)
 
 
class Student(Person):
    # определение конструктора
    def __init__(self, name, age, university):
        #Person.__init__(self, name, age)
        super().__init__(name, age)
        self.university = university
 
    # переопределение метода display_info
    def display_info(self):
        print("Студент", self.name, "учится в университете", self.university)

    @staticmethod
    def inc(x):
        return x + 1
    @staticmethod
    def dec(x):
        return x - 1



people = [Person("Иван", 23), Student("Петр", 19, "ИТМО"), Employee("Сергей", 35, "Google")]
 
for person in people:
    person.display_info()
    print()

for person in people:
    if isinstance(person, Student):
        print(person.university)
    elif isinstance(person, Employee):
        print(person.company)
    else:
        print(person.name)
    print()

st = Student("r",1,"t")
x = st.inc(10)
x = Student.dec(6)
print(x)

