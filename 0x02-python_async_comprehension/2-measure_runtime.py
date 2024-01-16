#!/usr/bin/env python3
""" Imported modules
asyncio, async_comprehension
"""
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """ measure_runtime should measure the total runtime and return it. """
    tasks = [async_comprehension() for _ in range(4)]

    start = asyncio.get_event_loop().time()
    await asyncio.gather(*tasks)
    end = asyncio.get_event_loop().time()

    runtime = end - start
    return runtime
