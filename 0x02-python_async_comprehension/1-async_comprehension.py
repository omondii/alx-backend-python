#!/usr/bin/env python3
""" Imported modules
asyncio, random, async_generator
"""
import asyncio
import random
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """ The coroutine will collect 10 random numbers using an async
    comprehensing over async_generator, then return the 10 random numbers.
    """
    result = [num async for num in async_generator()]
    return result
