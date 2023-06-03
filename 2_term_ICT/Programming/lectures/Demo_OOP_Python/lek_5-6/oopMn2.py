class A():
    def __init__(self):
        super().__init__()
        print("A")

class B():
    def __init__(self):
        super().__init__()
        print("B")

class C(A, B):
    def __init__(self):
        super().__init__()
        print("C")

x = C()         # B A C
print(C.mro())  # позволяет просматривать список  родительских классов 
"""
[
<class '__main__.C'>,
<class '__main__.A'>,
<class '__main__.B'>,
<class 'object'>
]
"""
class First:
    def __init__(self):
        super().__init__()
        print("first")

class Second(First):
    def __init__(self):
        super().__init__()
        print("second")

class Third(First):
    def __init__(self):
        super().__init__()
        print("third")

class Fourth(Second, Third):
    def __init__(self):
        super().__init__()
        print("that it")

x = Fourth() # first third second that it
print(Fourth.mro())
"""
[
<class '__main__.Fourth'>,
<class '__main__.Second'>,
<class '__main__.Third'>,
<class '__main__.First'>,
<class 'object'>]
"""
class First:
    def __init__(self):
        print("first")
        super().__init__()

class Second(First):
    def __init__(self):
        print("second")
        super().__init__()

class Third(First):
    def __init__(self):
        print("third")
        super().__init__()

class Fourth(Second, Third):
    def __init__(self):
        print("that it")
        super().__init__()

x = Fourth()    # that it  second third first
