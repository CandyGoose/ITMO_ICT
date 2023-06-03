'''
Модуль asyncio доступен для предоставления базовой реализации цикла событий
'''
import asyncio
async def async_hello():
    print("hello, world!")
    
async def main():
    print('Hello ...')
    await asyncio.sleep(1)
    print('... World!')

async_hello()           # RuntimeWarning: coroutine 'async_hello' was never awaited
''' что возвращает корутин? '''
print(async_hello(),        # <coroutine object async_hello at 0x000002D4C2D2A8F0>
      type(async_hello()))  # <class 'coroutine'>   
"""
Объект сопрограммы (coroutine object) ничего не делает,
пока его выполнение не запланировано в цикле событий
"""
loop = asyncio.get_event_loop() # DeprecationWarning: There is no current event loop
loop.run_until_complete(async_hello())


asyncio.run(async_hello())

asyncio.run(main())
'''
Функция asyncio.run()
- управляет переданной корутиной,
заботясь об управлении asyncio событийного цикла;
- всегда создаёт новый событийный цикл и закрывает его в конце.
Еe следует использовать в качестве основной точки входа для asyncio программ
'''
