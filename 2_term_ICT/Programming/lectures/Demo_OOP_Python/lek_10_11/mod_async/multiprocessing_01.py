'''
Модуль asyncio доступен для предоставления базовой реализации цикла событий
'''
import multiprocessing

def worker(x):
    name_proc = multiprocessing.current_process().name
    res = x*x
    print(name_proc, res)
    return res

def f(x):
    return x*x

data = range(3, 7)

if __name__ == '__main__':

    with multiprocessing.Pool(5) as p:
        print(p.map(f, [1, 2, 3]))

    with multiprocessing.Pool(5) as pool:
        print('Результаты:')
        print(pool.map(worker, data))








