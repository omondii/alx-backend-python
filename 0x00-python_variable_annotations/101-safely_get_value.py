#!/usr/bin/env python3
from typing import TypeVar, Dict, Union
""" Given the parameters and the return values, add type annotations to the function """
T = TypeVar('T')


def safely_get_value(dct: Dict[str, T], key: str, default: T = None) -> T:
    """ Use TypeVar to build a generic type.
    Returns an object of type T
    """
    if key in dct:
        return dct[key]
    else:
        return default
