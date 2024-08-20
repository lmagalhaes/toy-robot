from enum import IntEnum


class CardinalCoordinates(IntEnum):

    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4
    N = 1
    E = 2
    S = 3
    W = 4


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

    def __bool__(self):
        return self.x is not None and self.y is not None

    def __str__(self):
        return f'{self.x},{self.y}'


class Boundary:

    def __init__(self, inferior_limit, superior_limit):
        self.inferior_limit = inferior_limit
        self.superior_limit = superior_limit

    def is_within_boundaries(self, location: Point):
        return self.inferior_limit <= location <= self.superior_limit
