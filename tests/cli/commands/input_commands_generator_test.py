from toy_robot.cli.commands import InputCommandsGenerator
from toy_robot.cli.exceptions import WarmUpFileDoesNotExistError
from typing import Generator
from unittest.mock import patch, MagicMock
import pytest


class TestGetInputsFromStandardInput:

    def test_returns_a_generator(self):
        generator = InputCommandsGenerator.from_standard_input()
        assert isinstance(generator, Generator)

    @patch('toy_robot.cli.commands.input')
    def test_reads_input_until_it_has_exhausted(self, input_mock):
        expected_commands = ['command1', 'command2']
        input_mock.side_effect = expected_commands

        with pytest.raises(RuntimeError):
            input_commands = list(InputCommandsGenerator.from_standard_input())
            assert expected_commands == input_commands

        assert 3 == input_mock.call_count


class TestGetInputsFromFile:

    @patch('toy_robot.cli.commands.os')
    def test_raises_exception_if_input_file_does_not_exist(self, os_mock):
        os_mock.path.isfile.return_value = False
        with pytest.raises(WarmUpFileDoesNotExistError):
            with pytest.raises(RuntimeError):
                list(InputCommandsGenerator.from_file('file_name'))

    @patch('toy_robot.cli.commands.open')
    @patch('toy_robot.cli.commands.os')
    def test_ignore_commented_lines_in_the_file(self, os_mock, open_mock):
        os_mock.path.isfile.return_value = True

        file_mock = MagicMock()
        file_mock.readline = MagicMock(side_effect=['command1', '# command2', 'command3'])
        open_mock.return_value.__enter__.return_value = file_mock

        expected_commands = ['command1', 'command3']
        with pytest.raises(RuntimeError):
            input_commands = list(InputCommandsGenerator.from_file('file_name'))
            assert expected_commands == input_commands

        assert 4 == file_mock.readline.call_count
