#!/usr/bin/env python3
""" Imported modules
asyncio, wait_random
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ wait_n spans wait_random n times with specified max_delay
    wait_n should return the list of all the delays 
    """
    spawn = []
    delayed = []
    for _ in range(n):
        delayed_task = asyncio.create_task(wait_random(max_delay))
        delayed_task.add_done_callback(lambda x: delayed.append(x.result()))
        spawn.append(delayed_task)

    for s in spawn:
        await s

    return delayed
