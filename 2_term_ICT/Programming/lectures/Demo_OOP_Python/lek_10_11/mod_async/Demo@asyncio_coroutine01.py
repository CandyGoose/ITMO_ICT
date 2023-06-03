'''
Применяется устаревший механизм сопрограмм,
основанных на генераторах - должен быть применён декоратор @asyncio.coroutine 
'''
import asyncio
import random
import time

@asyncio.coroutine
def consume():
    """Сопрограмма обработки данных"""
    running_sum = 0
    count = 0
    while True:
        data = yield from produce()
        running_sum += data
        count += 1
        print('Got data: {}\nTotal count: {}\nAverage: {}\n'.format(
            data, count, running_sum / count))

@asyncio.coroutine
def produce():
    """Сопрограмма выдачи данных."""
    yield from asyncio.sleep(1)
    data = random.randint(0, 100) # имитация - получение данных с внешнего сервера или базы данных
    return data


def main():
    """
    основной является сопрограмма consumer, а producer выдаёт одну порцию данных
    """
    loop = asyncio.get_event_loop()
    loop.run_until_complete(consume())
    loop.close()


if __name__ == '__main__':
    main()
