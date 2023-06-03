'''
Новые задачи можно добавить в цикл,
предоставив другой объект для ожидания использования функции asyncio.wait()

Функция asyncio.wait () принимает список объектов сопрограмм
и немедленно возвращается
'''
import asyncio

async def print_number(number):
       print(number)
"""
асинхронно напечатать последовательность чисел
"""
loop = asyncio.get_event_loop()

loop.run_until_complete(
    asyncio.wait([
        print_number(number)
        for number in range(10)
    ])
)
loop.close()

print("--")
async def main():
       await asyncio.wait([
              print_number(number)
        for number in range(10)
              ])

asyncio.run(main())         # Python 7+
