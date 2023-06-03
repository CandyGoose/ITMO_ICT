'''
Модуль asyncio доступен для предоставления базовой реализации цикла событий
пример двух сопрограмм, одна из которых вызывает другую,
производящую какие-то затратные вычисления

Применяется устаревший механизм сопрограмм,
основанных на генераторах - должен быть применён декоратор @asyncio.coroutine 
'''
import asyncio
"""
будет предупреждение:
DeprecationWarning: "@coroutine" decorator is deprecated since Python 3.8,
use "async def" instead
"""
@asyncio.coroutine
def time_consuming_computation(x):
    print('Computing {0} ** 2...'.format(x))
    yield from asyncio.sleep(1)
    return x ** 2

@asyncio.coroutine
def process_data(x):
    result = yield from time_consuming_computation(x)
    print('{0} ** 2 = {1}'.format(x, result))


if __name__ == '__main__':
    """Функция get_event_loop модуля asyncio возвращает объект цикла событий"""
    loop = asyncio.get_event_loop()
    """метод run_until_complete используется для запуска сопрограммы"""
    loop.run_until_complete(process_data(238))
    loop.close()
