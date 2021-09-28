"""List utility functions."""

__author__ = "730384041"


# TODO: Implement your functions here.
def all(x: list[int], y: int) -> bool:
    """This function returns a bool indicating whether or not all the ints in a list of ints are the same as a given int."""
    i: int = 0
    count: int = 0
    if len(x) == 0:
        return False
    while i < len(x):
        if y == x[i]:
            count += 1
        i += 1
    if count == len(x):
        return True
    return False


def is_equal(x: list[int], y: list[int]) -> bool:
    """This function returns True if every element at every index is equal two lists of int values."""
    i: int = 0
    count: int = 0
    if len(x) != len(y):
        return False
    while i < len(x):
        if y[i] == x[i]:
            count += 1
        i += 1
    if count == len(x) and count == len(y):
        return True
    return False


def max(x: list[int]) -> int:
    """This function, when given a list of int values, returns the largest in the list."""
    i: int = 1
    max: int = x[0]
    while i < len(x):
        if x[i] > max:
            max = x[i]
        i += 1
    return max