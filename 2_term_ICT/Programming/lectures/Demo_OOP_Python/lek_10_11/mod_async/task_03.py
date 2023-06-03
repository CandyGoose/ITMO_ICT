"""
Две блокирующие задачи: gr1 и gr2, они обращаются к неким сторонним сервисам,
и, пока они ждут ответа, третья функция может работать асинхронно.
"""
import asyncio

async def my_coro(n): 
    print(f"The answer is {n}.")

async def main(): 
    """ Создав задачу, вы запланировали ее запуск
        по усмотрению цикла событий """
    mytask = asyncio.create_task(my_coro(42))
    """программа останавливается
       пока задача не будет завершена"""
    await mytask

loop = asyncio.get_event_loop()
loop.run_until_complete(main())


asyncio.run(main())

