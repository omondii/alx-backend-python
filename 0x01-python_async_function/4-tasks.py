#!/usr/bin/env python3
""" Imported modules
asyncio
"""
import asyncio
import time
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """ measure_time function with integers n and max_delay as
    arguments that measures the total execution time for
    wait_n(n, max_delay)"""
    spawn = []
    delayed = []
    for _ in range(n):
        delayed_task = task_wait_random(max_delay)
        delayed_task.add_done_callback(lambda x: delayed.append(x.result()))
        spawn.append(delayed_task)

    for s in spawn:
        await s

    return delayed
