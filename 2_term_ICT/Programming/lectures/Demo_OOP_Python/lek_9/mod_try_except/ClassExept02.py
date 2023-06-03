"""
определяется суперкласс и подкласс для уточнения типа ошибки
"""
# class выводится из суперкласса Exception
class Error(Exception):
    
    def __init__(self, value): 
        self.value = value 
  
    def __str__(self): 
        return(repr(self.value))  

    
  
class TransitionError(Error): 
  
    # Возникает, когда операция пытается выполнить
    # переход, который не разрешен.
    def __init__(self, prev, nex, msg): 
        self.prev = prev 
        self.next = nex 
        self.msg = msg  # Сгенерированное сообщение об ошибке сохраняется в сообщении



try:
    k1 = int(input("Введите номер перехода 'откуда':"))
    k2 = int(input("Введите номер переходов 'куда':"))

    if k1 == 0:
        raise Error(k1)
    if k2<k1:
        raise(TransitionError(k1,k2,"Переход невозможен"))
    dk = k2 - k1
    print("Успешный переход длиной =", dk)
  
except TransitionError as error: 
    print('Exception occured: ', error.msg) 

except Error as e:
        print('\nОпасная ошибка!', e)

except Exception as e:
        print('\nРедкая ошибка!', e)

