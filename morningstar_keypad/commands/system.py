import os

from commands.core import Command


class ShellCommand(Command):
    def __init__(self, command: str):
        self.command = command

    def execute(self):
        os.system(self.command)


def execute(command: str):
    return ShellCommand(command)
