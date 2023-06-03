
"""
Базовые классы
 исключения используются в основном в качестве базовых классов для других исключений

ArithmeticError - базовый класс для тех встроенных исключений,
которые возникают при различных арифметических ошибках:
o	OverflowError
o	ZeroDivisionError
o	FloatingPointError
"""
try:   
    a = 10/0  
    print(a)   
#except ZeroDivisionError:   
#        print("This statement is raising an ZeroDivisionError exception.")
except ArithmeticError:   
        print("This statement is raising an arithmetic exception.")

else:   
    print("Success")

"""
LookupError - базовый класс для тех исключений, которые возникают, когда ключ или индекс,
используемый в отображении или последовательности, недопустим или не найден.
Возникают исключения:
o	KeyError
o	IndexError
"""
try:  
    a = [1, 2, 3]  
    print(a[3])
#except IndexError:  
#    print("Index out of bound error.")
except LookupError:  
    print("LookupError - Index out of bound error.")
else:  
    print("Success")




