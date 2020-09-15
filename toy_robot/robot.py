from toy_robot.utils import Boundary, CardinalCoordinates, Point


default_boundary = Boundary(Point(0, 0), Point(4, 4))


class Robot:

    def __init__(self, location: Point = None, direction: str = None, boundary: Boundary = None):
        self.location = location
        self.direction = direction
        self.boundaries = boundary if boundary else default_boundary

    @property
    def is_activated(self) -> bool:
        return self.location and self._direction

    @property
    def location(self) -> Point:
        return self._location

    @location.setter
    def location(self, location: Point) -> None:
        if not location:
            location = Point(None, None)
        self._location = location

    @property
    def direction(self):
        return None if not self._direction else CardinalCoordinates(self._direction).name

    @direction.setter
    def direction(self, direction: str) -> None:
        if direction:
            direction = CardinalCoordinates[direction.upper()].value
        self._direction = direction

    def place(self, location: Point, direction: str) -> None:
        if self.is_within_boundaries(location):
            self.location = location
        self.direction = direction

    def right(self) -> None:
        self._rotate(1)

    def left(self) -> None:
        self._rotate(-1)

    def _rotate(self, direction: int) -> None:
        new_direction = self._direction + direction
        if not 0 < self._direction + direction < 5:  # full rotation
            new_direction = 1 if new_direction else 4
        self._direction = new_direction

    def move(self) -> None:
        if not self.location:
            return

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
        return location and self.boundaries.is_within_boundaries(location)

    def report(self) -> str:
        if not self.location:
            return ''
        return f'{self.location},{self.direction}'
