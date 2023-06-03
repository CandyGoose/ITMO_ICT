# декоратор “вручную”

def my_shiny_new_decorator(function_to_decorate):
    """
  Внутри себя декоратор определяет функцию-"обёртку".
  Она будет обёрнута вокруг декорируемой, 
  получая возможность исполнять произвольный код до и после неё.
    """
    def the_wrapper_around_the_original_function():
        print("код, который отработает до вызова функции")
        function_to_decorate()
        print("код, срабатывающий после")
    return the_wrapper_around_the_original_function

# функция
def stand_alone_function():
    print("простая функция")

stand_alone_function()

# Чтобы заменить поведение, можно декорировать её, то есть просто передать декоратору,
# который обернет исходную функцию в любой код, который потребуется, и вернёт новую,
# готовую к использованию функцию

stand_alone_function_decorated = my_shiny_new_decorator(stand_alone_function)
stand_alone_function_decorated()

@my_shiny_new_decorator
def another_stand_alone_function():
    print("новая функция")
another_stand_alone_function()
