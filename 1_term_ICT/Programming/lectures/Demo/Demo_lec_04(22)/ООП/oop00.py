
class Person:
    name = "Иван"   # атрибут класса

    """        
    метод класса работает с атрибутом класса
    """

    def display_info():
        print("Имя: ", Person.name)

    def display_str():
        return "Приветвенное имя: Уважаемый {}".format(Person.name)

        
# Использование метода класса

Person.display_info()
stPerson = Person.display_str()

print(Person)
print(stPerson)

p = Person()
#p.display_info()    # TypeError: display_info() takes 0 positional arguments but 1 was given
print(p.name)

#p.name = "Polo"
#print(p.name)
