#!/usr/bin/env python3
from typing import Sequence, Any, Union, Optional
""" Duct-type annotations.
Imported sequence module
"""


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    if lst:
        return lst[0]
    else:
        return None
