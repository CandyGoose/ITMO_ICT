import asyncio
import datetime

async def add_one(number):
    await asyncio.sleep(0) # измените на 1,2,3
    return number + 1

async def display_date():
    loop = asyncio.get_running_loop()
    end_time = loop.time() + 5.0
    while True:
        print(datetime.datetime.now())
        if (loop.time() + 1.0) >= end_time:
            break
        await asyncio.sleep(1)


async def main():
    task_add = asyncio.create_task(add_one(1))
    task_display = asyncio.create_task(display_date())

    one_plus = await task_add
    print(one_plus)

    await task_display
    

asyncio.run(main())
