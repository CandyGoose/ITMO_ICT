"""
Используем аргументы и возвращаем значения
аргументы декорируемой функции передаются функции-обёртке
декоратор выполняет декорируемую функцию iters раз,
а затем выводил среднее время выполнения
"""

def mark(iters):
    def actual_decorator(func):
        import time
        def wrapper(n1, n2):
            total = 0
            for i in range(iters):
                start = time.time()
                return_value = func(n1, n2)
                end = time.time()
                total = total + (end-start)
            print('[*] Среднее время выполнения: {} секунд.'.format(total/iters))
            return return_value
        return wrapper
    return actual_decorator

@mark(iters=5)
def Fb(a,b):
    while (a!=b) :
        if a > b:
            a = a - b
        else:
            b = b - a
    return a 

a, b = 123456789, 987654321
print(Fb(a,b))
