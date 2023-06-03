import asyncio
import datetime

async def delay(delay_seconds: int) -> int:
    print(f'засыпаю на {delay_seconds} с')
    await asyncio.sleep(delay_seconds)
    print(f'сон в течение {delay_seconds} с закончился')
    return delay_seconds


async def main() -> None:
    print(datetime.datetime.now())
    sleep_for_three = asyncio.create_task(delay(3))
    sleep_again = asyncio.create_task(delay(3))
    sleep_once_more = asyncio.create_task(delay(3))

    try:
        await asyncio.wait_for(sleep_for_three, timeout=2)
        await asyncio.wait_for(sleep_again, timeout=1)
        await sleep_once_more
    except asyncio.TimeoutError:
        print('timeOut')
        
    print(datetime.datetime.now())

asyncio.run(main())
 
