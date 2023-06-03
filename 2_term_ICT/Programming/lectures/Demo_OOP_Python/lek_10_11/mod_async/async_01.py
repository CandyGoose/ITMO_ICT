'''
Модуль asyncio доступен для предоставления базовой реализации цикла событий
'''
import asyncio
async def async_hello():
    print("hello, world!")

# async_hello()  # RuntimeWarning: coroutine 'async_hello' was never awaited
"""
Объект сопрограммы (coroutine object) ничего не делает,
пока его выполнение не запланировано в цикле событий
"""
loop = asyncio.get_event_loop()
loop.run_until_complete(async_hello())


