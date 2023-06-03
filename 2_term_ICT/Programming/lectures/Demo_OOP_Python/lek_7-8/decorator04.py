"""
создаём максимально общий декоратор
хотим, чтобы его можно было применить к любой функции или методу - 
стоит воспользоваться тем, что *args распаковывает список args,
a **kwargs распаковывает словарь kwargs:
    """
def a_decorator_passing_arbitrary_arguments(function_to_decorate):
    # Данная "обёртка" принимает любые аргументы
    def a_wrapper_accepting_arbitrary_arguments(*args, **kwargs):
        print("Передали что-нибудь?")
        print(args)
        print(kwargs)
        # Теперь мы распакуем *args и **kwargs
        function_to_decorate(*args, **kwargs)
    return a_wrapper_accepting_arbitrary_arguments
 
@a_decorator_passing_arbitrary_arguments
def function_with_no_argument():
    print("Python is cool, no argument here.")
 
function_with_no_argument()
# выведет:
# Передали что-нибудь
# ()
# {}
# Python is cool, no argument here.
 
@a_decorator_passing_arbitrary_arguments
def function_with_arguments(a, b, c):
    print( a, b, c)
 
function_with_arguments(1,2,3)
# выведет:
# Передали
# (1, 2, 3)
# {}
# 1 2 3
 
@a_decorator_passing_arbitrary_arguments
def function_with_named_arguments(a, b, c, platypus="Почему нет?"):
    print("Передаем {0}, {1} и {2} парметры '{3}'".format(a, b, c, platypus))
 
function_with_named_arguments("Билл", "Линус", "Стив", platypus="передано")
# выведет:
# Передали ли мне что-нибудь?:
# ('Билл', 'Линус', 'Стив')
# {'platypus': 'передано'}
# Передаем Билл, Линус и Стив парметры 'передано'
 
class Mary():
 
    def __init__(self):
        self.age = 31
 
    @a_decorator_passing_arbitrary_arguments
    def sayYourAge(self, lie=-3): # Теперь мы можем указать значение по умолчанию
        print("Сейчас {0}" .format(self.age + lie))
 
m = Mary()
m.sayYourAge()
# выведет:
# Передали ли мне что-нибудь?:
# (<__main__ .Mary object at 0xb7d303ac>,)
# {}
# Сейчас 28

