class Command:
    def execute(self):
        raise NotImplemented('Must be implemented by child class')


class NoopCommand(Command):
    def execute(self):
        pass


class CallCommand(Command):
    def __init__(self, func):
        self.func = func

    def execute(self):
        self.func()


do_nothing = NoopCommand()
