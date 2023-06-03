"""
метакласс MultiBases будет проверять, наследуются ли создаваемые классы от нескольких базовых классов:
если это так, то это вызовет ошибку
"""
 
class MultiBases(type): 
    # overriding __new__ 
    """
    этот метод вызывается перед __init __ (),
    он создает объект и возвращает его.
    Переопределяем этот метод для управления пройесса создания объектов
    """
    def __new__(cls, clsname, bases, clsdict): 
        # если количество базовых классов будет больше одного, то будет сгенерировано исключение 
        if len(bases)>1: 
            raise TypeError("Inherited multiple base classes!!!") 
          
        # в противном случае вызвать метод __new__ базового класса, т.е.
        # вызывается конструктор __init__ 
        return super().__new__(cls, clsname, bases, clsdict)
"""
# метакласс может быть указан с помощью ключевого аргумента metaclass
# теперь MultiBase класс используется для создания классов
# это будет распространено на все подклассы Base
"""
class Base(metaclass=MultiBases): 
    pass

  
# no error is raised 
class A(Base): 
    pass
  
# no error is raised 
class B(Base): 
    pass
  
# This will raise an error! 
class C(A, B):      # TypeError: Inherited multiple base classes!!!
    pass

