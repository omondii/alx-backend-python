#!/usr/bin/env python3
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n
""" Imported modules
asyncio, wait_n
"""


async def measure_time(n: int, max_delay: int) -> float:
    """ measure_time function with integers n and max_delay as
    arguments that measures the total execution time for
    wait_n(n, max_delay)"""
    s = time.perf_counter()
    await wait_n(n, max_delay)
    elapsed = time.perf_counter() - s
    avarage_time = elapsed / n

    return avarage_time
