"""Practice with dictionaries."""

__author__ = "730384041"


def invert(x: dict[str, str]) -> dict[str, str]:
    """Given a dictionary of [str, str], invert should return a dict[str, str] that inverts the keys and the values."""
    y: dict[str, str] = {}
    for key, value in x.items():
        if value in y.keys():
            raise KeyError("More than one of the same value cannot be inverted into keys!")
        else:
            y[value] = key
    return y


def favorite_color(x: dict[str, str]) -> str:
    """favorite_color has one parameter, of type dict[str, str] of names and favorite colors and returns a str which is the color that appears most frequently."""
    y: dict[str, int] = {}
    for key, value in x.items():
        if value in y:
            y[value] += 1
        else:
            y[value] = 1
    return max(y, key=y.get)


def count(x: list[str]) -> dict[str, int]:
    """Given a list[str], this function will produce a dict[str, int] where each key is a unique value in the given list and each value associated is the count of the number of times that value appeared in the input list."""
    y: dict[str, int] = {}
    for key in x:
        if key in y:
            y[key] += 1
        else:
            y[key] = 1
    return y