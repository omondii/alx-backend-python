#!/usr/bin/env python3
from typing import Iterable, Sequence, List, Tuple
""" Import iterable object from typing """


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Returns a tuple from a sequence """
    return [(i, len(i)) for i in lst]
