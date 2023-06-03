""" классы в Python это объекты """
class Person:
    pass

p = Person()
print(p)                                    # <__main__.Person object at 0x02EBA0D0>
print("Тип объекта p:", type(p))            # Тип объекта p: <class '__main__.Person'>
print("Тип класса Person:", type(Person))   # Тип класса Person: <class 'type'>


""" Поскольку классы являются объектами, они могут быть изменены таким же образом """
# Defining method variables 
Person.x = 45
  
# Defining class methods 
Person.foo = lambda self: print('Hello')

print(hasattr(Person, 'foo'))               # True
print(Person.__dict__)

# creating object 
myobj = Person() 
  
print(myobj.x)  # 45
myobj.foo()     # Hello


Human = Person
print(hasattr(Human, 'foo'))               # True
print(Human.__dict__)

Human.y = 54
print(Person.__dict__)
