'''
Модуль Multiprocessing 

'''

import os
from multiprocessing import Process
 
 
def doubler(number):
    """
    Функция умножитель на два
    """
    result = number * 2
    proc = os.getpid()
    print('{0} doubled to {1} by process id: {2}'.format(
        number, result, proc))
 
 

numbers = [5, 10, 15, 20, 25]
procs = []
    
for index, number in enumerate(numbers):
    proc = Process(target=doubler, args=(number,))
    procs.append(proc)
    proc.start()
    
for proc in procs:
    proc.join()
