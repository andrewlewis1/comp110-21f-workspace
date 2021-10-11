"""List utility functions part 2."""

__author__ = "730384041"


def only_evens(x: list[int]) -> list[int]:
    """Given a list of ints, only_evens should return a list containing only the elements of the input list that were even."""
    i: int = 0
    result: list[int] = []
    while i < len(x):
        if x[i] % 2 == 0:
            result.append(x[i])
        i += 1
    return result


def sub(a_list: list[int], start: int, end: int) -> list[int]:
    """Given a list of ints, a start index, and an end index (not inclusive), sub should generate a List which is a subset of the given list, between the specified start index and the end index - 1."""
    if start < 0:
        start = 0
    if end > len(a_list):
        end = len(a_list)
    if len(a_list) == 0 or start >= len(a_list) or end <= 0:
        return []
    start = a_list[start]
    end = a_list[end - 1]
    a_list.clear()
    a_list.append(start)
    a_list.append(end)
    return a_list


def concat(x: list[int], y: list[int]) -> list[int]:
    """Given two Lists of ints, concat should generate a new List which contains all of the elements of the first list followed by all of the elements of the second list."""
    List: list[int] = x
    i: int = 0
    while i < len(y):
        List.append(y[i])
        i += 1
    return List