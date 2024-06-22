""" This is a module allows the user to add to rational numbers 
        The functions that must be called as add(a,b).
"""

from typing import Union

def sum(a: Union[float,int], b: Union[float,int]) -> float:
    """Sum of two floats.

    Examples:
        >>> sum(3.0, 4.0)
        7.0

    Args:
        a: First argument
        b: Second argument

    Returns:
        Returns the sum operation of `a` and `b`.

    """
    return float( a + b )
