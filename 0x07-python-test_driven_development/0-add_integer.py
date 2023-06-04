#!/usr/bin/python3
""" add_integer module """
def add_integer(a, b=98):
    """
    return the sum a and b

    Args:
        a: (int) 
        b=98: (int) with 98 default

    Raise:
        TypeError: if a is not int or b is not int
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
