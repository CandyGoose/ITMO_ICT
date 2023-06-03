""" Демонстрация декоратора functool.wraps
"""

from functools import wraps

def a_decorator_passing_arguments(function_to_decorate):
    #@wraps(function_to_decorate)
    def a_wrapper_accepting_arguments(arg1, arg2): # аргументы прибывают отсюда
        print("Получено:", arg1, arg2)
        function_to_decorate(arg1, arg2)
    return a_wrapper_accepting_arguments
 
# Теперь, когда мы вызываем функцию, которую возвращает декоратор,
# мы вызываем её "обёртку", передаём ей аргументы и уже в свою очередь
# она передаёт их декорируемой функции
 
@a_decorator_passing_arguments
def print_full_name(first_name, last_name):
    print("Меня зовут", first_name, last_name)

print_full_name("Иван", "Петров")


# если без применения декоратора @wraps(function_to_decorate)
# запросим функцию о ее имени
print(print_full_name.__name__) # a_wrapper_accepting_arguments
"""
Атрибут __name__, который возвращает имя функции при ее определении,
теперь отражает возвращенную внутреннюю функцию используемую в декораторе
"""

print(help(print_full_name))
"""
получаем строку документации функцию внутренней функции
Help on function a_wrapper_accepting_arguments in module __main__:
a_wrapper_accepting_arguments(arg1, arg2)
    #@wraps(function_to_decorate)
"""

# Повторите печать имени функции с примененем декоратора @wraps(function_to_decorate)
"""
получаем имя и строку документации вызываемой функции

print_full_name
Help on function print_full_name in module __main__:
print_full_name(first_name, last_name)

"""
