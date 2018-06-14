from collections import namedtuple
from typing import Dict

from commands.core import Command, NoopCommand

Address = namedtuple("Address", ['group', 'code', 'action'])


class Executor:
    def __init__(self, commands: Dict[Address, Command]):
        self.commands = commands

    def execute(self, address: Address):
        '''
        Execute command under provided address
        :param address:
        :return:
        '''
        command = self.commands.get(address, NoopCommand())
        command.execute()


def on_key(group, code, action):
    return Address(group=group, code=code, action=action)


def on_code(code):
    return Address(group=code[0], code=code[1], action=code[2])
