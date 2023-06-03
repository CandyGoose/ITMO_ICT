import sys 
"""
определяется суперкласс с именем General и два подкласса с именами Specific1 и Specific2. 
General – это имя категории, а два подкласса – это определенные типы исключений внутри категории
"""


class General(Exception):
    pass

class Specific1(General):
    pass 

class Specific2(General):
    pass 


def raiser0():
    X = General() # Возбуждает экземпляр суперкласса исключения
    raise X

def raiser1():
    X = Specific1() # Возбуждает экземпляр подкласса исключения 
    raise X 

def raiser2():
    X = Specific2() # Возбуждает экземпляр другого подкласса исключения 
    raise X 

for func in (raiser0, raiser1, raiser2): 
    try: 
        func() 
    except General: # Перехватывает исключения General и любые его подклассы 
         print("Экземпляр исключения:", sys.exc_info()[0])  # эквивалент обращения к атрибуту __class__ экземпляра

"""
Экземпляр исключения: <class '__main__.General'>
Экземпляр исключения: <class '__main__.Specific1'>
Экземпляр исключения: <class '__main__.Specific2'>
"""
