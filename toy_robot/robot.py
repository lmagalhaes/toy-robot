from enum import IntEnum


class CardinalCoordinates(IntEnum):

    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4


class Point:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __iter__(self):
        yield self.x
        yield self.y

    def sum(self, other: 'Point') -> 'Point':
        return Point(self.x + other.x, self.y + other.y)

    def __eq__(self, other: 'Point'):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other: 'Point'):
        return self.x != other.x or self.y != other.y

    def __gt__(self, other: 'Point') -> bool:
        return self.x > other.x and self.y > other.y

    def __lt__(self, other: 'Point') -> bool:
        return self.x < other.x and self.y < other.y

    def __ge__(self, other: 'Point') -> bool:
        return self.x >= other.x and self.y >= other.y

    def __le__(self, other: 'Point') -> bool:
        return self.x <= other.x and self.y <= other.y


class Boundary:

    def __init__(self, inferior_limit, superior_limit):
        self.inferior_limit = inferior_limit
        self.superior_limit = superior_limit

    def is_within_boundaries(self, location: Point):
        return self.inferior_limit <= location <= self.superior_limit


default_boundary = Boundary(Point(0, 0), Point(4, 4))


class Robot:

    def __init__(self, location: Point = None, direction: str = None, boundary: Boundary = None):
        self.location = location if location else Point(None, None)
        self.direction = direction
        self.boundaries = boundary if boundary else default_boundary

    @property
    def is_activated(self) -> bool:
        return self.location.x is not None and self.location.y is not None and self._direction

    @property
    def location(self) -> Point:
        return self._location

    @location.setter
    def location(self, location: Point) -> None:
        self._location = location

    @property
    def direction(self):
        return None if not self._direction else CardinalCoordinates(self._direction).name

    @direction.setter
    def direction(self, direction: str) -> None:
        if direction:
            direction = CardinalCoordinates[direction.upper()].value
        self._direction = direction

    def place(self, location, direction) -> None:
        if self.is_within_boundaries(location):
            self.location = location
        self.direction = direction

    def right(self):
        self._rotate(1)

    def left(self):
        self._rotate(-1)

    def _rotate(self, direction: int) -> None:
        new_direction = self._direction + direction
        if not 0 < self._direction + direction < 5:  # full rotation
            new_direction = 1 if new_direction else 4
        self._direction = new_direction

    def move(self) -> None:

        if self.direction == CardinalCoordinates.NORTH.name:
            new_location = self.location.sum(Point(0, 1))

        if self.direction == CardinalCoordinates.SOUTH.name:
            new_location = self.location.sum(Point(0, -1))

        if self.direction == CardinalCoordinates.EAST.name:
            new_location = self.location.sum(Point(1, 0))

        if self.direction == CardinalCoordinates.WEST.name:
            new_location = self.location.sum(Point(-1, 0))

        if self.is_within_boundaries(new_location):
            self.location = new_location

    def is_within_boundaries(self, location: Point) -> bool:
        return self.boundaries.is_within_boundaries(location)
