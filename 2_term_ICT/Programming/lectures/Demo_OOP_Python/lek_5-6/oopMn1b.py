"""
Если у нескольких родителей будут одинаковые методы? 
Какой метод в таком случае будет использовать наследник? 
"""
class A:
    x = 1
    y = 'hello'
    def mel(self, a):
        print('A', self.x+a)

class B(A):
    z = 'bye'
    x = 10
    def mel(self,b):
        print('B', self.x+b)

class C(A):
    def salutation(self):
        return '%d %s %s' % (self.x, self.y, self.z)

    def mel(self, b):
        super().mel(b)
        B.mel(self, 1)
        print('C ', 1)


class D(B, C):
    pass
    """"
    Если необходимо использовать метод конкретного родителя,
    например класса С, нужно напрямую вызвать его по имени класса,
    передав self в качестве аргумента
    """
    #def mel(self, d):
    #    C.mel(self, d)
    



inst = D()
print(inst.salutation())    # 10 hello bye
inst.mel(2)                 # B 12

print(isinstance(inst, A)) # True
print(isinstance(inst, B)) # True
"""
Для определения порядка используется алгоритм поиска в ширину,
то есть сначала интерпретатор будет искать метод в классе B, если его там нет - в классе С, потом A. 
Посмотреть в каком порядке будут проинспектированы родительские классы при помощи метода класса mro():
"""
print(D.mro())
"""
[<class '__main__.D'>,
 <class '__main__.B'>,
  <class '__main__.C'>,
   <class '__main__.A'>,
    <class 'object'>]
"""
"""
Если убрать из класса B метод mel()?
A 12
A 11
C  1
"""
