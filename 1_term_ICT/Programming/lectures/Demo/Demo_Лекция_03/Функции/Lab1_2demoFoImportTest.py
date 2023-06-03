"""
Псевдоним можно назначить для всего модуля.
Назначение короткого имени для модуля позволит быстрее вызывать функции модуля
"""
import Lab1_5demoFoImport2 as Lb15

Lb15.function1(1,9)

"""
Импортировать любое количество функций из модуля, разделив их имена запятыми
и назначить псевдоним для функции при импортировании

"""
from Lab1_5demoFoImport2 import function2, function4 as f_mul

output = function2(10,12)
print("The value of 'output' is: ",output)

output = f_mul()
print("The value of 'output' is: ",output)

# импортировать все функции в модуле
from Lab1_5demoFoImport2 import *

output = function5(second=10,first=12)
print("The value of 'output' is: ",output)
print(function5.__doc__)
