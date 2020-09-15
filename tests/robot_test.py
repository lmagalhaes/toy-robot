from toy_robot.robot import Robot


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
