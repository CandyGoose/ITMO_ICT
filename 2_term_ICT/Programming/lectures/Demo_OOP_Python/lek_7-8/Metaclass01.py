""" Поскольку классы являются объектами, как и любой другой объект, их можно создавать на ходу"""
def choose_class(name):
    if name == 'foo':
         class Foo():
             pass
         return Foo    # возвращается класс
    else:
         class Bar():
             pass
         return Bar

MyClass = choose_class('foo')
print(MyClass)          # функция возвратила класс    <class '__main__.choose_class.<locals>.Foo'>
print(MyClass())        # создан объект-экземпляр нового класса    <__main__.choose_class.<locals>.Foo object at 0x000001B499A5C6A0>



""" type принимает на вход описание класса и возвращает класс
Синтаксис:
  type(<имя класса>, 
       <кортеж родительских классов>,      # для наследования, может быть пустым
       <словарь, содержащий атрибуты и их значения>)
"""
# возвращает объект-класс:
Person = type("Person", (), {})
