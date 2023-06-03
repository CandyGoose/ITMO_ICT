class A:
    x = 1
    y = 'hello'
    def mel(self, a):
        print('A', self.x+a)

class B:
    z = 'bye'
    x = 10
    def mel(self,b):
        print('B', self.x+b)

class C(A,B):
    def salutation(self):
        return '%d %s %s' % (self.x, self.y, self.z)

    def mel(self):
        super().mel(5)
        B.mel(self, 1)
        print('C ', 1)


print(issubclass(A,A))           # True
print(issubclass(A,C))           # False
print(issubclass(C,A))           # True - является наследником 
print(issubclass(A,object))      # True - является наследником 
print(issubclass(object,A))      # False

inst = C()
print(inst.salutation())    # 1 hello bye
inst.x = 100
inst.mel()
"""
A 105
B 101
C  1
"""
print(isinstance(inst, A)) # True
print(isinstance(inst, B)) # True
