#!/usr/bin/env python3
from typing import Callable
""" creates a callable func """


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ takes a float multiplier and returns multiplier_func """
    def multiplier_func(n: float) -> float:
        """ multiplier_func takes a float n and returns
        the result of n*multiplier """
        return n * multiplier
    return multiplier_func
