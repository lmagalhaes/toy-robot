from toy_robot.robot import Robot, Point
import pytest


class TestRobotPlacement:

    def test_robot_location_is_none_if_not_placed_anywhere(self):
        robot = Robot()
        assert Point(None, None) == robot.location
        assert robot.direction is None

    def test_robot_is_inactive_if_not_placed_anywhere(self):
        robot = Robot()
        assert not robot.is_activated

    def test_robot_set_location_and_direction_when_place_command_is_given(self):
        robot = Robot()
        location, position = Point(0, 0), 'north'
        robot.place(location, position)

        assert Point(0, 0) == robot.location
        assert 'NORTH' == robot.direction

    def test_robot_is_set_to_active_when_placement_command_is_given(self):
        robot = Robot()
        robot.place(Point(0, 0), 'north')

        assert robot.is_activated

    def test_ignores_place_command_if_trying_to_place_outside_boundary(self):
        robot = Robot()
        robot.place(Point(5, 5), 'north')

        assert not robot.is_activated


class TestRobotRotation:

    def test_robot_should_face_the_next_right_direction_if_right_command_is_given(self):
        robot = Robot()
        robot.place(Point(0, 0), 'north')
        robot.right()

        assert 'EAST' == robot.direction

    def test_robot_should_face_the_next_left_direction_if_left_command_is_given(self):
        robot = Robot()
        robot.place(Point(0, 0), 'east')
        robot.left()

        assert 'NORTH' == robot.direction

    def test_robot_should_face_the_opposite_direction_if_2_consecutive_turns_are_given(self):
        robot = Robot()
        robot.place(Point(0, 0), 'north')
        robot.right()
        robot.right()

        assert 'SOUTH' == robot.direction

    @pytest.mark.parametrize('rotation_direction', [
        'right',
        'left'
    ])
    def test_robot_should_face_same_direction_if_4_consecutive_turns_are_performed(self, rotation_direction):
        robot = Robot()
        robot.place(Point(0, 0), 'north')

        method_to_call = getattr(robot, rotation_direction)
        method_to_call()
        method_to_call()
        method_to_call()
        method_to_call()

        assert 'NORTH' == robot.direction


class TestRobotMove:

    def test_robot_should_ignore_command_if_location_is_not_set(self):
        robot = Robot()
        robot.move()
        assert not robot.location

    @pytest.mark.parametrize('facing_direction,expected_location', [
        ['north', (2, 3)],
        ['n', (2, 3)],
        ['east', (3, 2)],
        ['e', (3, 2)],
        ['south', (2, 1)],
        ['s', (2, 1)],
        ['west', (1, 2)],
        ['w', (1, 2)]
    ])
    def test_robot_should_move_one_position_towards_the_direction_it_is_facing(self, facing_direction, expected_location):
        robot = Robot()
        robot.place(Point(2, 2), facing_direction)
        robot.move()

        assert expected_location == tuple(robot.location)

    def test_robot_should_ignore_move_if_next_position_is_out_of_boundaries(self):
        initial_location = Point(0, 0)
        robot = Robot()
        robot.place(initial_location, 'south')
        robot.move()
        assert initial_location == robot.location

    def test_robot_should_not_move_south_or_west_when_in_extreme_south_west_location(self):
        initial_location = Point(0, 0)
        robot = Robot()
        robot.place(initial_location, 'south')
        robot.move()
        assert initial_location == robot.location

        robot.right()
        robot.move()

        assert initial_location == robot.location

    def test_robot_should_not_move_north_or_west_when_in_extreme_north_west_location(self):
        initial_location = Point(0, 4)
        robot = Robot()
        robot.place(initial_location, 'north')
        robot.move()
        assert initial_location == robot.location

        robot.left()
        robot.move()

        assert initial_location == robot.location

    def test_robot_should_not_move_north_nor_east_when_in_extreme_north_east_location(self):
        initial_location = Point(4, 4)
        robot = Robot()
        robot.place(initial_location, 'north')
        robot.move()
        assert initial_location == robot.location

        robot.right()
        robot.move()

        assert initial_location == robot.location

    def test_robot_should_not_move_south_nor_east_when_in_extreme_south_east_location(self):
        initial_location = Point(4, 0)
        robot = Robot()
        robot.place(initial_location, 'south')
        robot.move()
        assert initial_location == robot.location

        robot.left()
        robot.move()

        assert initial_location == robot.location


class TestRobotReport:

    def test_should_return_empty_string_if_location_not_set(self):
        robot = Robot()
        assert '' == robot.report()

    def test_should_return_x_y_and_direction_separated_by_comma(self):
        robot = Robot()
        robot.place(Point(2, 4), 'east')
        assert '2,4,EAST' == robot.report()
