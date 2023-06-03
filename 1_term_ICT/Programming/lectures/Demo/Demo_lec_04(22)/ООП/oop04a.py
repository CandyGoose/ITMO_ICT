# проблемный класс
class B1:
    count = 0
    
    def __init__(self):
        B1.count += 1
        
    def __del__(self):
        B1.count -= 1
 
a = B1()
b = B1()

print(B1.count) #  2

del a
print(B1.count) #  1

B1.count -= 1
print("B1.count", B1.count) # будет  0, хотя остался объект b


class B11:
    """
    Атрибут, который должен быть не общедоступным (Non-Public) обозначается
    при помощи ведущего подчеркивания _ :
      -	используется для внутренней реализации класса и не предназначен для использования извне;
      -	должен быть использован/изменен только если разработчик-пользователь класса абсолютно уверен в этом.
    """
    _count = 0
    
    def __init__(self, count):
        B11._count += 1
        self._counto = count
        
    def __del__(self):
        B11._count -= 1
 
a = B11(0)
b = B11(0)

"""
Атрибут  _count доступен извне, как и обычный public-атрибут класса
"""
print(B11._count) #  2

print("a._counto", a._counto) # не предусмотрено, но можно

del a
print(B11._count) #  1

B11._count -= 1
print("B11.count", B11._count) # будет  0, хотя остался объект b


# в этом классе скрывается поле самого класса (по соглашению)
class B2:
    """
    Атрибут, который должен быть закрытым (Private), обозначается при помощи ведущего двойного подчеркивания __:
      -	используется для внутренней реализации класса и не предназначен для использования извне;
      - не должен быть использован/изменен разработчиком-пользователем класса
    """
 
    __count = 0
    
    def __init__(self, count):
        B2.__count += 1
        self.__counto = count

    def __del__(self):
        B2.__count -= 1

    def get_count():
        return B2.__count

    def set_count(count):
        B2.__count = count


"""
атрибут __count за пределами класса становится невидимым,
хотя внутри класса он видимый
"""
a = B2(5)
#print("aa",a.__counto)  # AttributeError: 'B2' object has no attribute '__counto'
#print(B2.__count)      # AttributeError: type object 'B2' has no attribute '__count'
B2.set_count(9)
print(B2.get_count())

"""
сокрытие в Python не настоящее и доступ к счетчику получить все же можно
"""
print("dir(B2):\n", dir(B2))
B2._B2__count = 10
print(B2._B2__count)


"""
В Python атрибуты объекту можно назначать за пределами класса, но
если такое поведение нежелательно, его можно запретить с помощью атрибута __setattr__():
"""
# Применение метода __setattr__()
class A:
    def __init__(self, v):
        self.field1 = v
    """
    Можно запретить назначать атрибуты объекту за пределами класса
    с помощью метода __setattr__():
    """
    def __setattr__(self, attr, value):
        """
        Метод __setattr__(), если он присутствует в классе, вызывается всегда,
        когда какому-либо атрибуту выполняется присваивание
        """
        if attr == 'field1':
            self.__dict__[attr] = value
        else:
            raise AttributeError
        """
        Если параметр attr не соответствует допустимым полям,
        то возбуждается исключение AttributeError
        """

a = A(1)        # Факт попытки присвоения значения атрибуту отправляет интерпретатор в метод __setattr__(), где проверяется соответствует ли имя атрибута строке 'field1'. 
a.field2 = 2    # возбуждается исключение AttributeError
print(a.field1, a.field2)


