"""
Можно создавать свои метаклассы: помощью любого вызываемого объекта,
который способен принять три параметра и вернуть объект класса. 
Метакласс можно указать при объявлении класса.
"""

def my_metaclass(name, parents, attributes):  # объект - метакласс
     return 'Hello'

""" C оказывается переменной, которая указывает на строку 'Hello' """
class C(metaclass=my_metaclass):
     pass

print(C)        # 'Hello'
print(type(C))  # <class 'str'>


# Пример простого метакласса
""" Этот метакласс добавляет метод 'hello' к классам, использующим его значение.
     Так классы получают метод 'hello' без лишних усилий - метакласс
     заботится о генерации кода """
 
class HelloMeta(type):  
    # Метод hello
    def hello(cls):
        print("greetings from %s, a HelloMeta type class" % (type(cls())))

    # Вызываем метакласс
    def __call__(self, *args, **kwargs):
        # создаём новый класс как обычно
        cls = type.__call__(self, *args)

        # определяем новый метод hello для каждого из этих классов
        setattr(cls, "hello", self.hello)

        # возвращаем класс
        return cls

# Проверяем метакласс
class TryHello(metaclass=HelloMeta):  
    def greet(self):
        self.hello()

# Создаём экземпляр метакласса. Он должен автоматически содержать метод hello
# хотя он не объявлен в классе вручную - иными словами, он объявлен за нас метаклассом
greeter = TryHello()  
greeter.greet()
