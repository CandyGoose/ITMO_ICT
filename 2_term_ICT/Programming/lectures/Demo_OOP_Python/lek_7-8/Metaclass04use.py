"""
Требуется: в процессе отладки нужно, чтобы всякий раз, когда метод класса выполнялся,
он выводил полное имя перед выполнением своего тела
"""

""" Решение 1. Использование декораторов """
from functools import wraps 
  
def debug(func): 
    '''decorator for debugging passed function'''
      
    @wraps(func) 
    def wrapper(*args, **kwargs): 
        print("Full name of this method:", func.__qualname__) 
        return func(*args, **kwargs) 
    return wrapper 
  
def debugmethods(cls): 
    '''class decorator make use of debug decorator 
       to debug class methods '''
      
    # check in class dictionary for any callable(method) 
    # if exist, replace it with debugged version 
    for key, val in vars(cls).items(): 
        if callable(val): 
            setattr(cls, key, debug(val)) 
    return cls
  

 
@debugmethods
class Calc: 
    def add(self, x, y): 
        return x+y 
    def mul(self, x, y): 
        return x*y 
    def div(self, x, y): 
        return x/y 
      
mycal = Calc() 
print(mycal.add(2, 3))  # Full name of this method: Calc.add   5
print(mycal.mul(5, 2))  # Full name of this method: Calc.mul   10


""" Решение 2. На основе метаклассов:
    классы будут создаваться, а затем сразу же оборачиваться
    декоратором метода отладки """

from functools import wraps 
  
def debug(func): 
    '''decorator for debugging passed function'''
      
    @wraps(func) 
    def wrapper(*args, **kwargs): 
        print("Full name of this method:", func.__qualname__) 
        return func(*args, **kwargs) 
    return wrapper 
  
def debugmethods(cls): 
    '''class decorator make use of debug decorator 
       to debug class methods '''
      
    for key, val in vars(cls).items(): 
        if callable(val): 
            setattr(cls, key, debug(val)) 
    return cls


  
class debugMeta(type): 
    '''meta class передает созданный класс для получения требуемой
       функциональности при отладке (debugmethod)'''
      
    def __new__(cls, clsname, bases, clsdict): 
        obj = super().__new__(cls, clsname, bases, clsdict) 
        obj = debugmethods(obj) 
        return obj 
      
""" Базовый класс с метаклассом 'debugMeta' 
   для всех подклассов будет применена требуемая функциональность """ 
class Base(metaclass=debugMeta):
    pass
  

class Calc(Base): 
    def add(self, x, y): 
        return x+y 
      

class Calc_adv(Calc): 
    def mul(self, x, y): 
        return x*y 
  
""" объект-класс Calc_adv реализует поведение при отладке """ 
mycal = Calc_adv() 
print(mycal.mul(2, 3))  # Full name of this method: Calc_adv.mul  6



