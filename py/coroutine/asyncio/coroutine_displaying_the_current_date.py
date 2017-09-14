# https://docs.python.org/3/library/asyncio-task.html#example-coroutine-displaying-the-current-date

import asyncio
import datetime


async def display_date(loop):
    end_time = loop.time() + 5.0
    while True:
        print(datetime.datetime.now())
        if (loop.time() + 1.0) >= end_time:
            break
        await asyncio.sleep(1)


loop = asyncio.get_event_loop()

loop.run_until_complete(display_date(loop))
loop.close()

