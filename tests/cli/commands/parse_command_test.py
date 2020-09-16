from toy_robot import Point
from toy_robot.cli.commands import parse_command
from toy_robot.cli.exceptions import CommandInvalidError
import pytest


class TestParseCommand:

    def test_raises_command_invalid_exception_if_command_is_not_in_the_list_of_valid_command(self):
        with pytest.raises(CommandInvalidError) as exc:
            parse_command('invalid')

    @pytest.mark.parametrize('input_command', [
        'left',
        'right',
        'move',
        'report'
    ])
    def test_returns_list_with_command_and_empty_input_params_if_command_different_from_place(self, input_command):
        expected = [input_command, []]
        assert expected == parse_command(input_command)

    def test_return_list_with_command_and_extra_parameters_if_command_is_place(self):
        input_command = 'place 1,1,north'
        expected = ['place', [Point(1, 1), 'north']]
        assert expected == parse_command(input_command)
