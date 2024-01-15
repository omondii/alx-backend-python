#!/usr/bin/env python3
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n
""" Imported modules
asyncio, wait_n
"""


async def measure_time(n: int, max_delay: int) -> float:
    """ measure_time function with integers n and max_delay as arguments that measures
    the total execution time for wait_n(n, max_delay)"""
    start = time.time()
    await wait_n(n, max_delay)
    end = time.time()

    totaltime = end - start
    return totaltime / n