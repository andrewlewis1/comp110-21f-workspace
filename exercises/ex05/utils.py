"""List utility functions part 2."""

__author__ = "730384041"


def only_evens(x: list[int]) -> list[int]:
    i: int = 0
    result: list[int] = []
    while i < len(x):
        if x[i] % 2 == 0:
            result.append(x[i])
        i += 1
    return result


def sub(a_list: list[int], start: int, end: int) -> list[int]:
    if start < 0:
        start = 0
    if end > len(a_list):
        end = len(a_list)
    if len(a_list) == 0 or start > len(a_list) or end <= 0:
        return []
    start = a_list[start]
    end = a_list[end - 1]
    a_list.clear()
    a_list.append(start)
    a_list.append(end)
    return a_list


def concat(x: list[int], y: list[int]) -> list[int]:
    List: list[int] = x
    i: int = 0
    while i < len(y):
        List.append(y[i])
        i += 1
    return List