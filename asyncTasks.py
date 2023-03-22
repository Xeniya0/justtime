import asyncio
from datetime import datetime
import time



async def once():
    a = 0
    while True:
        await asyncio.sleep(1)
        a += 1
        print(a)

async def twice():
    while True:
        await asyncio.sleep(3)
        print('бдыщщщ')

async def seven():
    while True:
        await asyncio.sleep(7)
        print('бууммммсссссс')

async def test():
    flag = True
    while True:
        await asyncio.sleep(60)
        now = datetime.now()
        current_time = now.strftime('%H:%M')
        if current_time == '23:35':
            print('lol')




async def main():
    task1 = asyncio.create_task(once())
    # task2 = asyncio.create_task(twice())
    # task3 = asyncio.create_task(seven())
    task4 = asyncio.create_task(test())

    await task1
    # await task2
    # await task3
    await task4



if __name__ == '__main__':
    asyncio.run(main())