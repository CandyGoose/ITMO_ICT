"""
Основной целью метакласса является автоматическое изменение класса во время его создания. 
Например, это делается для API, когда нужно создать классы, соответствующие текущему контексту.

    Пример. Требуется, чтобы все классы в модуле должны иметь свои атрибуты, и они должны быть записаны в верхнем регистре.

metaclass может быть любым вызываемым объектом, он не обязательно должен быть формальным классом

"""
""" 1. Использование функции """
# метаклассу автоматически передается тот же аргумент, который обычно передается в `type`
def upper_attr(future_class_name, future_class_parents, future_class_attr):
    """
    Возврат объекта класса со списком его атрибутов в верхнем регистре.
    """

    # Логика: выберите любой атрибут, который не начинается с '__' и введите его в верхний регистр
    uppercase_attr = {}
    for name, val in future_class_attr.items():
        if not name.startswith('__'):
            uppercase_attr[name.upper()] = val
        else:
            uppercase_attr[name] = val

    # `type` применяется для создания класса
    return type(future_class_name, future_class_parents, uppercase_attr)


class Foo(metaclass=upper_attr):
    bar = 'bip'


print(hasattr(Foo, 'bar'))     # False
print(hasattr(Foo, 'BAR'))     # True

f = Foo()
print(f.BAR)                   # 'bip'



""" 2. Использование метакласса 
 `type` является классом вроде` str` и `int`и можно наследовать от него
"""

class UpperAttrMetaclass(type):
    """
     метод __new__ вызывается до __init__ - создает объект и возвращает его
      __init__ просто инициализирует объект, переданный как параметр
     метод __new__ редко использукется, за исключением случаев, когда требуется контроль создания объекта
     В этом случае - созданный объект - это класс, и мы хотим его настроить, поэтому переопределяем __new__
    """
     
    def __new__(upperattr_metaclass, future_class_name, future_class_parents, future_class_attr):
        uppercase_attr = {}
        for name, val in future_class_attr.items():
            if not name.startswith('__'):
                uppercase_attr[name.upper()] = val
            else:
                uppercase_attr[name] = val
    # type не переопределяется, а вызывается напрямую.
        return type(future_class_name, future_class_parents, uppercase_attr)

# переопределение type:
class UpperAttrMetaclass(type):

    def __new__(upperattr_metaclass, future_class_name,
                future_class_parents, future_class_attr):

        uppercase_attr = {}
        for name, val in future_class_attr.items():
            if not name.startswith('__'):
                uppercase_attr[name.upper()] = val
            else:
                uppercase_attr[name] = val

        # посвторно используем метод type.__new__ 
        return type.__new__(upperattr_metaclass, future_class_name,
                            future_class_parents, uppercase_attr)

"""
Дополнительный аргумент upperattr_metaclass. В нём нет ничего особенного: этот метод первым аргументом
получает текущий экземпляр.
Точно так же, как и self для обычных методов.
Имена аргументов такие длинные для наглядности, но для self все имена имеют названия обычной длины.
"""
# реальный метакласс будет выглядеть так:
class UpperAttrMetaclass(type):

    def __new__(cls, clsname, bases, dct):

        uppercase_attr = {}
        for name, val in dct.items():
            if not name.startswith('__'):
                uppercase_attr[name.upper()] = val
            else:
                uppercase_attr[name] = val

        return type.__new__(cls, clsname, bases, uppercase_attr)

# Используя метод super, можно сделать код более “чистым”:
class UpperAttrMetaclass(type):

    def __new__(cls, clsname, bases, dct):

        uppercase_attr = {}
        for name, val in dct.items():
            if not name.startswith('__'):
                uppercase_attr[name.upper()] = val
            else:
                uppercase_attr[name] = val

        return super(UpperAttrMetaclass, cls).__new__(cls, clsname, bases, uppercase_attr)


class Fooo(metaclass=UpperAttrMetaclass): 
    bar2 = 'bipp'


print(hasattr(Fooo, 'bar2'))     # False
print(hasattr(Fooo, 'BAR2'))     # True

f2 = Fooo()
print(f2.BAR2)                   # 'bipp'




