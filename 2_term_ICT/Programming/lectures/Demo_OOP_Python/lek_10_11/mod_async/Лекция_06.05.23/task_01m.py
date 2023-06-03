'''
Создаются две задачи
'''
import asyncio

async def foo():
    print('Running in foo')
    await asyncio.sleep(0) # установите 1
    print('Explicit context switch to foo again')


async def bar():
    print('Explicit context to bar')
    await asyncio.sleep(0)  
    print('Implicit context switch back to bar')



async def main():
    tasks = [asyncio.create_task(foo()), asyncio.create_task(bar())]
    #print(type(asyncio.create_task(foo())))  # <class '_asyncio.Task'>
    await asyncio.wait(tasks)
    

asyncio.run(main())

