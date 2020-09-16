from toy_robot.cli.commands import robot_challenge
from toy_robot import Robot

from unittest.mock import MagicMock


class TestRobotChallenge:

    def test_activate_robot_commands_for_each_command_in_the_list(self):
        commands_list = ['place 0,0,1', 'left', 'right', 'move', 'report']

        robot = Robot()
        robot.place = MagicMock()
        robot.left = MagicMock()
        robot.right = MagicMock()
        robot.move = MagicMock()
        robot.report = MagicMock()

        robot_challenge(robot, commands_list)

        assert 1 == robot.move.call_count
        assert 1 == robot.left.call_count
        assert 1 == robot.right.call_count
        assert 1 == robot.place.call_count
        assert 1 == robot.report.call_count

    def test_robot_ignores_invalid_commands(self):
        commands_list = ['place 0,0,1', 'left', 'jump']

        robot = Robot()
        robot.place = MagicMock()
        robot.left = MagicMock()
        robot.jump = MagicMock()

        robot_challenge(robot, commands_list)

        assert 1 == robot.place.call_count
        assert 1 == robot.left.call_count
        assert 0 == robot.jump.call_count
