"""
1) вложение в потоке управления 
Функция action2 возбуждает исключение (нельзя складывать числа и последовательности),
функция action1 обертывает вызов функции action2 в инструкцию try, которая перехватывает исключение
"""
def action2():
    print(1 + [])            # Возбуждает исключение TypeError 

def action1(): 
    try: 
        action2() 
    except TypeError:       # Самая последняя соответствующая инструкция try 
       print('inner try') 


try: 
    action1() 
except TypeError:       # Этот обработчик будет выполнен, только если 
    print('outer try')  # action1 повторно возбудит исключение 



"""
2) синтаксическое вложение

"""
def raise1():
    raise IndexError

def noraise():
    return

def raise2():
    raise SyntaxError

for func in (raise1, noraise, raise2):
    print('\n', func, sep=' ')
    try:
        try:
            func()
        except IndexError:
            print('Вызов IndexError')
        finally:
            print('Работает finally')
    except SyntaxError:
        print('Вызов SyntaxError')
