class RobotError(Exception):
    """Robot CLI exception"""


class CommandInvalidError(RobotError):
    """ Raises when input command is invalid """


class WarmUpFileDoesNotExistError(RobotError):
    """ Raises when warm-up file does not exist """
