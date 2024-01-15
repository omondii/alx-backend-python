#!/usr/bin/env python3
""" Imported modules
asyncio, random
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ Takes in an integer argument, waits for a random delay between 0
    and max_delay and eventually returns it.
    """
    i = random.uniform(0, max_delay)
    await asyncio.sleep(i)
    return i
