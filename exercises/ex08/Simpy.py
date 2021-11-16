"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730384041"


class Simpy:
    """Implement a utility class that is helpful for working with sequences of numerical data."""
    values: list[float]
    
    def __init__(self, values: list[float]):
        """Initialize Simpy with a list of floats."""
        self.values = values

    def __str__(self) -> str:
        """Produce a str representation of Simpy."""
        return f"Simpy({self.values})"

    def fill(self, value: float, num: int) -> None:
        """Fill a Simpy's values with a specific number of repeating values."""
        self.values = []
        i: int = 0
        while i < num:
            self.values.append(value)
            i += 1

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fill in the values attribute with range of values, like the range built-in function, but in terms of floats."""
        assert step != 0.0
        self.values = []
        self.values.append(start)
        i: int = 0
        while self.values[i] != (stop - step):
            self.values.append(self.values[i] + step)
            i += 1

    def sum(self) -> float:
        """Compute and return the sum of all items in the values attribute."""
        result = sum(self.values)
        return result

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Return a new Simpy by overloading the add operator."""
        result: list[float] = []
        if type(rhs) is Simpy:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                result.append(self.values[i] + rhs.values[i])
                i += 1
        elif type(rhs) is float:
            i: int = 0
            while i < len(self.values):
                result.append(self.values[i] + rhs)
                i += 1
        return Simpy(result)

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Return a new Simpy by overloading the power operator."""
        result: list[float] = []
        if type(rhs) is Simpy:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                result.append(self.values[i] ** rhs.values[i])
                i += 1
        elif type(rhs) is float:
            i: int = 0
            while i < len(self.values):
                result.append(self.values[i] ** rhs)
                i += 1
        return Simpy(result)

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Produce a mask based on the equality of each item in the values attribute with some other Simpy object or a float value."""
        result: list[bool] = []
        if type(rhs) is Simpy:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                if self.values[i] == rhs.values[i]:
                    result.append(True)
                else:
                    result.append(False)
                i += 1
        elif type(rhs) is float:
            i: int = 0
            while i < len(self.values):
                if self.values[i] == rhs:
                    result.append(True)
                else:
                    result.append(False)
                i += 1
        return result

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Produce a mask based on the greater than relationship between each item in the values attribute with some other Simpy object or a float value."""
        result: list[bool] = []
        if type(rhs) is Simpy:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                if self.values[i] > rhs.values[i]:
                    result.append(True)
                else:
                    result.append(False)
                i += 1
        elif type(rhs) is float:
            i: int = 0
            while i < len(self.values):
                if self.values[i] > rhs:
                    result.append(True)
                else:
                    result.append(False)
                i += 1
        return result

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Return a new Simpy object containing only the masked/filtered values."""
        result: list[float] = []
        if type(rhs) is int:
            return self.values[rhs]
        else:
            i: int = 0
            assert type(rhs) is list
            assert len(rhs) == len(self.values)
            while i < len(rhs):
                if rhs[i] is True:
                    result.append(self.values[i])
                i += 1
            return Simpy(result)