'''
Модуль asyncio доступен для предоставления базовой реализации цикла событий
Сравниваются синхронная и асинхронная версии sleep
'''
import asyncio  
import time  
from datetime import datetime

async def custom_sleep():  
    print('SLEEP', datetime.now())
    time.sleep(1)               # синхронный sleep внутри async кода
    #await asyncio.sleep(1)      # асинхронный метод sleep

async def factorial(name, number):  
    f = 1
    for i in range(2, number+1):
        print('Task {}: Compute factorial({})'.format(name, i))
        await custom_sleep()
        f *= i
    print('Task {}: factorial({}) is {}\n'.format(name, number, f))

async def main():
    await asyncio.gather(
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4),
    )
    
start = time.time()

loop = asyncio.get_event_loop()
tasks = [  
    asyncio.ensure_future(factorial("A", 3)),
    asyncio.ensure_future(factorial("B", 4)),
]
loop.run_until_complete(asyncio.wait(tasks))  
loop.close()

asyncio.run(main()) # Python 7+

end = time.time()

print("Total time: {}".format(end - start))

"""
1. Асинхронная версия на 2 секунды быстрее. 
2. Когда используется асинхронный sleep (каждый раз, когда вызываем await asyncio.sleep (1)),
управление передается обратно в event loop, который запускает другую задачу из очереди
(задачу A или задачу B): A -> B -> A -> B -> A -> B
3. В случае стандартного sleep поток простаивает: A -> A -> A -> B -> B -> B -> B. 
"""
