''' Ожидаемые объекты
1) корутины являются ожидаемыми и поэтому могут ожидаться из других корутин
2) Задача — это ожидаемый объект, который оборачивается вокруг подпрограммы (coroutine).
Когда корутина обвёрнута в Задачу с такими функциями, как asyncio.create_task(),
то автоматически планируется запуск корутины в ближайшее время

'''
import asyncio
async def async_hello():
    print("hello, world!")
    
async def main():
    # async_hello()  # RuntimeWarning: coroutine 'async_hello' was never awaited
# 1)
    await async_hello()
# 2)
    task = asyncio.create_task(async_hello())
    await task

asyncio.run(main())
