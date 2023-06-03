"""
определяется суперкласс 
класс реализует дополнительный метод, использующий информацию о состоянии для регистрации ошибки в файле
"""
# class выводится из суперкласса Exception
class Error(Exception):
    
    def __init__(self, value, file): 
        self.value = value
        self.file = file
  
    def __str__(self): 
        return(repr(self.value))  

    def logerror(self):
        log = open(self.file, 'a')
        print('Error!', 'Не допустимое значение:', self.value, file=log) 

    
"""
определяется для уточнения типа ошибки
класс переопределяет дополнительный метод, использующий информацию о состоянии для регистрации ошибки в файле
"""
class TransitionError(Error): 
  
    # Возникает, когда операция пытается выполнить
    # переход, который не разрешен.
    def __init__(self, prev, nex, msg, file): 
        self.prev = prev 
        self.next = nex 
        self.msg = msg  # Сгенерированное сообщение об ошибке сохраняется в сообщении
        self.file = file

    def logerror(self):
        log = open(self.file, 'a')
        strEr = f"'Error!' Из {self.prev} в {self.next} {self.msg}"
        print(strEr, file=log) 

try:
    k1 = int(input("Введите номер перехода 'откуда':"))
    k2 = int(input("Введите номер переходов 'куда':"))

    if k1 == 0:
        raise Error(k1, 'errorFile.txt')
    if k2<k1:
        raise(TransitionError(k1,k2,"переход невозможен", "TransitionErrorFile.txt"))
    dk = k2 - k1
    print("Успешный переход длиной =", dk)
  
except TransitionError as error: 
    print('Exception occured: ', error.msg)
    error.logerror()

except Error as e:
        print('\nОпасная ошибка!', e)
        e.logerror()

except Exception as e:
        print('\nРедкая ошибка!', e)


