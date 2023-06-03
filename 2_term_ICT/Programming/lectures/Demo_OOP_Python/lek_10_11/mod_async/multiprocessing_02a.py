'''
Модуль Multiprocessing
нужно вычислить сумму всех простых чисел меньше 1 000 000
Решение: распределить числа между своими копиями
и проверять несколько одновременно.
В итоге сложить числа, которые он и его копии

'''

from multiprocessing import Pool

def if_prime(x):
    if x <= 1:
        return 0
    elif x <= 3:
        return x
    elif x % 2 == 0 or x % 3 == 0:
        return 0
    i = 5
    while i**2 <= x:
        if x % i == 0 or x % (i + 2) == 0:
            return 0
        i += 6
    return x

answer = 0

for i in range(1000000):
    answer += if_prime(i)

print(answer)

'''
Породить процессы с помощью multiprocessing.Pool.
Число, которое будет передано в Pool(), будет равно числу порожденных процессов.
Встраивание оператора with гарантирует, что все процессы будут убиты после завершения их работы.

Объединить выходные данные из процесса Pool с помощью функции map.
Входными данными для map будет функция, применяемая к каждому элементу, и сам список элементов
'''
with Pool(2) as p:
    answer = sum(p.map(if_prime, list(range(1000000))))

print(answer)
