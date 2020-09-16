import os
from typing import Generator

from click import command

from toy_robot import Robot, Point
from toy_robot.cli.exceptions import CommandInvalidError, WarmUpFileDoesNotExistError


ROOT_FOLDER = os.path.join(
    os.path.abspath(os.path.dirname(__file__)),
    '..',
    '..'
)

APP_HOME = os.getenv('APP_HOME') or ROOT_FOLDER


WARMUP_FILE_LOCATION = os.path.join(
    APP_HOME,
    'resources',
    'robot_warmup.txt'
)


class InputCommandsGenerator:

    @staticmethod
    def from_file(file_path: str) -> Generator:
        if not os.path.isfile(file_path):
            raise WarmUpFileDoesNotExistError(f'{file_path} is not a valid file.')

        with open(file_path, 'r') as input_file:
            line = input_file.readline()
            while line:
                line = line.strip()
                print(line)
                if line.startswith('#'):  # ignore commented lines
                    line = input_file.readline()
                    continue

                yield line
                line = input_file.readline()

    @staticmethod
    def from_standard_input() -> Generator:
        count = 0
        while True:
            yield input(f'CMD #{count}: ')
            count += 1


def robot_challenge(robot: Robot, commands: Generator) -> None:
    print('Starting Robot.\nTo exit press CTRL+C at any time...')


    for command in commands:
        try:
            command, params = parse_command(command)
        except CommandInvalidError as exc:
            print(str(exc))
        else:
            robot_command = getattr(robot, command)
            response = robot_command(*params)
            if command == 'report':
                print(response)


def parse_command(command: str) -> list:
    command_name, parameters = _extract_name_and_parameters(command)

    if command_name not in ['place', 'move', 'left', 'right', 'report']:
        raise CommandInvalidError(f'Command "{command}" is unknown and will be ignored.')

    if command_name == 'place':
        parameters = _parse_place_command_parameters(parameters)
    return [command_name, parameters]


def _extract_name_and_parameters(command: str) -> str:
    command_pieces = command.lower().split(' ')
    command_name = command_pieces[0]
    parameters = []
    if len(command_pieces) > 1:
        parameters = command_pieces[1:][0]

    return [command_name, parameters]


def _parse_place_command_parameters(parameters):
    x, y, direction = parameters.split(',')
    return [Point(int(x), int(y)), direction]


@command()
def warm_up(): # pragma: no cover
    """
    Reads the warm-up file and automatically sends commands to the robot.

    This command reads input commands to the robot from the resources/robot-warmup.txt file.

    All commands in that file will be automatically issues to the robot and will stop automatically once
    all commands where issued
    """
    commands = InputCommandsGenerator.from_file(WARMUP_FILE_LOCATION)
    robot_challenge(Robot(), commands)


@command()
def start():  # pragma: no cover
    """
    Starts a new robot and prompt for new commands to be issues.

    To enable the robot to start responding, an initial 'PLACE' commands is required  with proper coordinates and direction,
    and the robot will not respond to any command before the initial 'PLACE' command.

    The robot only works within the boundaries that are defined by an imaginary square of fixed size 5X5. Starting from
    (0,0) up to (4,4).

    Once the robot is placed in a valid position any subsequent command will be issued to the robot,
    but any command that moves the robot outside its limits will be ignored, including another 'PLACE' command.


    Available commands:

    \b
    PLACE X,Y,F: Place on position (X:int,Y:int) facing F.
        Valid F values: NORTH, SOUTH, EAST, WEST.
    MOVE: Robot moves 1 position towards the direction it is facing
    LEFT: Robot rotate to the left, without changing position
    RIGHT: Robot rotate to the right, without changing position
    REPORT: Prints robot's current position and direction it is facing. If not placed correctly prints nothing
    """
    commands = InputCommandsGenerator.from_standard_input()
    robot_challenge(Robot(), commands)
