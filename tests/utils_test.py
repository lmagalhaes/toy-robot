from toy_robot import Point


class TestPointDunderComparisonMethods:

    def test_points_are_equals_or_not_equals(self):
        p1,  p2, p3 = Point(1, 1), Point(2, 2), Point(2, 2)

        assert p1 == p1
        assert not p1 != p1
        assert not p1 == p2
        assert p1 != p2
        assert p2 == p3

    def test_lesser_than(self):
        p1, p2 = Point(1, 1), Point(2, 2)
        assert p1 < p2
        assert not p1 < p1
        assert not p2 < p1

    def test_points_are_lesser_or_equals(self):
        p1, p2, p3 = Point(1, 1), Point(2, 2), Point(2, 2)

        assert p1 <= p1
        assert p1 <= p2
        assert p2 <= p3
        assert p3 <= p2
        assert p1 <= p2 <= p3

    def test_points_are_greater(self):
        p1, p2 = Point(1, 1), Point(2, 2)

        assert not p1 > p1
        assert not p1 > p2
        assert not p2 > p2
        assert p2 > p1

    def test_poists_are_greater_or_equals(self):
        p1, p2, p3 = Point(1, 1), Point(2, 2), Point(2, 2)

        assert not p1 >= p2
        assert p2 >= p3
        assert p2 >= p1
        assert p3 >= p1
        assert p3 >= p2 >= p1


class TestPointSum:

    def test_should_return_a_new_pointer_with_the_sum_of_xs_and_yx(self):
        p1, p2 = Point(1, 1), Point(2, 2)
        assert Point(3, 3) == p1.sum(p2)

    def test_should_subtract_if_x_or_y_is_negative(self):
        p1, p2 = Point(1, 1), Point(-1, 2)
        assert Point(0, 3) == p1.sum(p2)


class TestPointStrMethod:

    def test_should_return_x_and_x_coma_separated(self):
        assert '1,2' == str(Point(1, 2))
