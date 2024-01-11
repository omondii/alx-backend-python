#!/usr/bin/env python3
from typing import List, Union
""" type-annotated func that adds ints and floats """


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Returns a float out of a mix of ints and floats """
    return float(sum(mxd_lst))
