# Передача аргументов в декорируемую функцию

# всё, что необходимо — передать аргументы дальше

def a_decorator_passing_arguments(function_to_decorate):
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


#декорирование методов

def method_friendly_decorator(method_to_decorate):
    def wrapper(self, lie):
        lie = lie * 0.13
        return method_to_decorate(self, lie)
    return wrapper
 
 
class Lucy():
    def __init__(self):
         self.cost = 30
 
    @method_friendly_decorator
    def sayYourCost(self, lie):
        print("Сейчас %s" % (self.cost + lie))
 
lu = Lucy()
lu.sayYourCost(15)


