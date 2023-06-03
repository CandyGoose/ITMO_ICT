"""
Требуется: объявить класс (использующий метакласс), который может следить за временем выаолнения кода
"""
import types, time	 	 
	 	 
class Timer:
    def __init__(self, func=time.perf_counter):
        self.elapsed = 0.0	 	 
        self._func = func	 	 
        self._start = None	 	 

    def start(self):	 	 
        if self._start is not None:	 	 
            raise RuntimeError('Already started')	 	 
        self._start = self._func()	 	 

    def stop(self):	 	 
        if self._start is None:	 	 
            raise RuntimeError('Not started')	 	 
        end = self._func()	 	 
        self.elapsed += end - self._start	 	 
        self._start = None	 	 

    def reset(self):	 	 
        self.elapsed = 0.0	 	 

    @property	 	 
    def running(self):	 	 
        return self._start is not None	 	 

    def __enter__(self):	 	 
        self.start()	 	 
        return self	 	 

    def __exit__(self, *args):	 	 
        self.stop()	 	 

# Далее создаём метакласс Timed, который считает время работы своих методов	 	 
# вместе с функциями установки, которые переписывают методы классa	 	 
# времена создания классов	 	 
# Функция, засекающая время исполнения встроенной функции, возвращает новую,	 	 
# инкапсулируя поведение исходной функции	 	 
def timefunc(fn, *args, **kwargs):	 	 
    def fncomposite(*args, **kwargs):	 	 
        timer = Timer()	 	 
        timer.start()	 	 
        rt = fn(*args, **kwargs)	 	 
        timer.stop()	 	 
        print("Executing %s took %s seconds." % (fn.__name__, timer.elapsed))	 	 
        return rt	 	 
 # возвращает сложную функцию	 	 
    return fncomposite

# Метакласс 'Timed', который заменяет методы своих классов	
# с новым методами 'timed' на поведение сложной функции-преобразователя

class Timed(type):	 	 
    def __new__(cls, name, bases, attr):	 	 
 # меняет каждую функцию на новую, время которой замеряется	 	 
 # запускает вычисление с заданными args и возвращает результат	 	 
       for name, value in attr.items():	 	 
           if type(value) is types.FunctionType or type(value) is types.MethodType:	 	 
               attr[name] = timefunc(value)	 	 
       return super(Timed, cls).__new__(cls, name, bases, attr)	 	 

# Следующий пример кода проверяет метакласс	 	 
# Классы, применяющие метакласс Timed, следует замерить за нас автоматически	 	 
	 	 
class Math(metaclass=Timed):
    def multiply(a, b):	 	 
        product = a * b	 	 
        print(product)	 	 
        return product	 	 

Math.multiply(5, 6)

class Shouter(metaclass=Timed):	 	 
    def intro(self):	 	 
        print("I shout!")	 	 

s = Shouter() 	 	 
s.intro()	 	 

def divide(a, b): 	 	 
    result = a / b	 	 
    print(result)	 	 
    return result	 	 

div = timefunc(divide) 	 	 
div(9, 3)

