'''
Функция asyncio.create_task() используется для конкурентного запуска корутин 
'''
import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    task1 = asyncio.create_task(
        say_after(1, 'hello'))

    task2 = asyncio.create_task(
        say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")

    # Подождать, пока обе задачи не будут выполнены (должны принять
    # около 2 секунд.)
    await task1
    await task2
    #await asyncio.wait([task1, task2])
    print(f"finished at {time.strftime('%X')}")


asyncio.run(main())
