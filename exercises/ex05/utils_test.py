"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests

__author__ = "730384041"
from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens_all_odds() -> None:
    x: list[int] = [1, 5, 7, 13]
    assert only_evens(x) == []


def test_only_evens_all_evens() -> None:
    x: list[int] = [2, 4, 8]
    assert only_evens(x) == [2, 4, 8]


def test_only_evens_odds_and_evens() -> None:
    x: list[int] = [1, 4, 3, 6, 7]
    assert only_evens(x) == [4, 6]


def test_sub_negative_start_zero_end() -> None:
    x: list[int] = [1, 2, 3, 4, 5]
    assert sub(x, -2, 0) == []


def test_sub_negative_start_greater_end() -> None:
    x: list[int] = [1, 2, 3, 4, 5]
    assert sub(x, -1, 7) == [1, 5]


def test_sub_normal() -> None:
    x: list[int] = [1, 2, 3, 4, 5]
    assert sub(x, 2, 4) == [3, 4]


def test_concat_both_empty() -> None:
    x: list[int] = []
    y: list[int] = []
    assert concat(x, y) == []


def test_concat_empty_y() -> None:
    x: list[int] = [10, 20, 30, 40]
    y: list[int] = []
    assert concat(x, y) == x


def test_concat_normal_lists() -> None:
    x: list[int] = [10, 20, 30, 40]
    y: list[int] = [50, 60, 70]
    assert concat(x, y) == [10, 20, 30, 40, 50, 60, 70]