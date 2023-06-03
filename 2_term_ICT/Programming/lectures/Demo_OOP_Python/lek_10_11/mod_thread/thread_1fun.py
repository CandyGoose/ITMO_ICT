# Метод «Функциональный»
# два потока параллельно выводят каждый в свой файл заданное число строк

# из модуля threading импортируем класс Thread
from threading import Thread

def prescript(thefile, num):
    """
    Аргументы целевой функции: имя текстового файла для записи и число строк
    """
    with open(thefile, 'w') as f:
        for i in range(num):
            if num > 500:
                f.write('Большой Демо текст\n')
            else:
                f.write('Маленький Демо текст\n')

thread1 = Thread(target=prescript, args=('f1.txt', 200,))
thread2 = Thread(target=prescript, args=('f2.txt', 1000,))

"""
start() запускает ранее созданный поток
"""
thread1.start()
thread2.start()
"""
Метод join() останавливает поток, когда тот выполнит свои задачи
"""
thread1.join()
thread2.join()
