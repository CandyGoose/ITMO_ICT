import math
"""
>>> myaddd(3,7.5)
10.5
"""

def myadd(a,b):
    """
    Возвращает сумму
    >>> myadd(11,0)
    11
    """
    return a+b

def mysub(a,b):
    return a-b

def mymul(a, b):
   return a * b

def mydiv(a, b):
    if b == 0:
        return 0
    else:
        return a / b

def myqrt3(a):
    return math.pow(a, 1/3)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
