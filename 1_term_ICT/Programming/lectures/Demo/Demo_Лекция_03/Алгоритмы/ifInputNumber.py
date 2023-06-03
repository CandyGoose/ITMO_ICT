#p = int(input("Введите число "))
#p=23
#p='23'
'''
if type(p) == int or type(p) == float:
    print("number")
else:
    print("str")

import numbers
if isinstance(p, numbers.Number):
    print("number")
else:
    print("str")


p = input("Введите число ")
if p.isnumeric():
    p1 = int(p)
    print("number", p1)
else:
    print("str", p)
'''
try:
    p2 = int(input("Введите число "))
    print("number")
except:
    print("not number" )
    

