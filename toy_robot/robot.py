from enum import IntEnum
from typing import Iterable


class CardinalCoordinates(IntEnum):
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4


class Robot:

    def __init__(self):
        self._x = None
        self._y = None
        self._direction = None

    @property
    def is_activated(self) -> bool:
        return self._x is not None and self._y is not None and self._direction

    @property
    def location(self) -> Iterable[int]:
        return self._x, self._y

    @location.setter
    def location(self, location: Iterable[int]) -> None:
        self._x, self._y = location

    @property
    def direction(self):
        return None if not self._direction else CardinalCoordinates(self._direction).name

    @direction.setter
    def direction(self, direction: str) -> None:
        direction = CardinalCoordinates[direction.upper()].value
        self._direction = direction

    def place(self, location, direction) -> None:
        self.location = location
        self.direction = direction




