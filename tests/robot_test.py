from toy_robot.robot import Robot
import pytest


class TestRobotPlacement:

    def test_robot_coordinates_are_none_if_not_placed_anywhere(self):
        robot = Robot()
        assert (None, None) == robot.location
        assert robot.direction is None

    def test_robot_is_inactive_if_not_placed_anywhere(self):
        robot = Robot()
        assert not robot.is_activated

    def test_robot_set_coordinates_and_direction_when_place_command_is_given(self):
        robot = Robot()
        coord, position = [0, 0], 'north'
        robot.place(coord, position)

        assert (0, 0) == robot.location
        assert 'NORTH' == robot.direction

    def test_robot_is_set_to_active_when_placement_command_is_giver(self):
        robot = Robot()
        robot.place([0, 0], 'north')

        assert robot.is_activated


class TestRobotRotation:

    def test_robot_should_face_the_next_right_direction_if_right_command_is_given(self):
        robot = Robot()
        robot.place([0, 0], 'north')
        robot.right()

        assert 'EAST' == robot.direction

    def test_robot_should_face_the_next_left_direction_if_left_command_is_given(self):
        robot = Robot()
        robot.place([0, 0], 'east')
        robot.left()

        assert 'NORTH' == robot.direction

    def test_robot_should_face_the_opposite_direction_if_2_consecutive_turns_are_given(self):
        robot = Robot()
        robot.place([0, 0], 'north')
        robot.right()
        robot.right()

        assert 'SOUTH' == robot.direction

    @pytest.mark.parametrize('rotation_direction', [
        'right',
        'left'
    ])
    def test_robot_should_face_same_direction_if_4_consecutive_turns_are_performed(self, rotation_direction):
        robot = Robot()
        robot.place([0, 0], 'north')

        method_to_call = getattr(robot, rotation_direction)
        method_to_call()
        method_to_call()
        method_to_call()
        method_to_call()

        assert 'NORTH' == robot.direction
