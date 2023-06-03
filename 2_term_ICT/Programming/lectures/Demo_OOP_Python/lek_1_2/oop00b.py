
# class может появляться везде, где могут появляться инструкции,
# даже внутри других инструкций

x = 3
y = -3

if x > 0:
    if y > 0:               # x > 0, y > 0
       class Person:
           name = "1 четверть"   # атрибут класса
           def display_info():
               print("Имя: ", Person.name)
           def display_str():
               return "Приветвенное имя: Уважаемый {}".format(Person.name)
    else:                   # x > 0, y < 0
       class Person:
           name = "4 четверть"   # атрибут класса
           def display_info():
               print("Имя: ", Person.name)
           def display_str():
               return "Приветвенное имя: Уважаемый {}".format(Person.name)
else:
    if y > 0:               # x < 0, y > 0
       class Person:
           name = "2 четверть"   # атрибут класса
           def display_info():
               print("Имя: ", Person.name)
           def display_str():
               return "Приветвенное имя: Уважаемый {}".format(Person.name)
    else:                   # x < 0, y < 0
       class Person:
           name = "3 четверть"   # атрибут класса
           def display_info():
               print("Имя: ", Person.name)
           def display_str():
               return "Приветвенное имя: Уважаемый {}".format(Person.name)






       
# Использование метода класса

Person.display_info()
stPerson = Person.display_str()

print(stPerson)

p = Person()
print(p.name)

