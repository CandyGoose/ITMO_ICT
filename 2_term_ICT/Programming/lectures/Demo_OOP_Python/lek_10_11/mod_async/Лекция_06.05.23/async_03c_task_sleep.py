import asyncio

async def delay(delay_seconds: int) -> int:
    print(f'засыпаю на {delay_seconds} с')
    await asyncio.sleep(delay_seconds)
    print(f'сон в течение {delay_seconds} с закончился')
    return delay_seconds

async def add_one(number: int) -> int:
    await delay(0)
    return number + 1 

async def hello_world_message() -> str:
    await delay(1)
    return 'Hello World!'

async def main() -> None:
    sleep_for_three = asyncio.create_task(delay(3))
    print(type(sleep_for_three))

    task_add = asyncio.create_task(add_one(1))
    task_hw = asyncio.create_task(hello_world_message())
    
    result = await sleep_for_three
    print("sleep", result)

    one_plus = await task_add
    print("add", one_plus)

    hw = await task_hw
    print(hw)

asyncio.run(main())
 
