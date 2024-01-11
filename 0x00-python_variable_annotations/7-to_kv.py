#!/usr/bin/env python3
from typing import Union, Tuple
""" func to print a string and int/float """


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Returns a tuple with the string and square of the passed float/int """
    return (k, v*v)
