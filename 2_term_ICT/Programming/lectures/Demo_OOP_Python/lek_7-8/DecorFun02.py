"""
Демонстрация того, как узнать время выполнения функции с помощью декоратора
"""
import time, math 
  
# декоратор для расчета продолжительности любой функции
def calculate_time(func): 
    """
    добавлены аргументы внутри функции inner1
    """
    def inner1(*args, **kwargs): 
        # сохранение времени до выполнения функции
        begin = time.time() 
      
        func(*args, **kwargs) 
  
        # время хранения после выполнения функции
        end = time.time() 
        print("Total time:", func.__name__, end - begin) 
  
    return inner1 
  
  
# Тестирование - это может быть добавлено к любой функции,
# например, для расчета факториала

@calculate_time
def factorial(num): 
    print(math.factorial(num)) 
  
# вызов функции
factorial(10) 
