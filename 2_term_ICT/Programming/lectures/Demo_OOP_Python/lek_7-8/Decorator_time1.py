# Используем аргументы и возвращаем значения
# аргументы декорируемой функции передаются функции-обёртке
def mark(func):
    import time
    def wrapper(n1, n2):
        print("Получено:", n1,n2)
        start = time.time()
        return_value = func(n1, n2)
        end = time.time()
        print('[*] Время выполнения: {} секунд.'.format(end-start))
        return return_value
    return wrapper

@mark
def Fb(a,b):
    while (a!=b) :
        if a > b:
            a = a - b
        else:
            b = b - a
    return a 

a, b = 123456789, 987654321
print(Fb(a,b))
