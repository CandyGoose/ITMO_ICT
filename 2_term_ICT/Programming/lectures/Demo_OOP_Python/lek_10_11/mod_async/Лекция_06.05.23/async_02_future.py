'''
Объект Future — это специальный ожидаемый (await) объект низкого уровня,
представляющий конечный результат асинхронной операции.
'''
import asyncio
import concurrent.futures

def blocking_io():
    # Файловые операции (такие как журналирование) могут блокировать
    # событийный цикл: запустив их в пуле потоков.
    with open('test', 'rb') as f:
        return f.read(100)

async def main():
    loop = asyncio.get_running_loop()

    ## Опции:

    # 1. Запуск в исполнителе цикла по умолчанию:
    result = await loop.run_in_executor(
        None, blocking_io)
    print('default thread pool', result)

    # 2. Запуск в пользовательском пуле потоков:
    with concurrent.futures.ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(
            pool, blocking_io)
        print('custom thread pool', result)


asyncio.run(main())
