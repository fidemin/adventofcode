
from collections import namedtuple

Command = namedtuple('Command', ('op', 'arg'))


class CommandParser:
    @staticmethod
    def parse(command_str: str):
        """
        :param command_str: e.g. jmp +4
        :return:
        """
        op, arg_str = command_str.strip().split(' ')
        arg = int(arg_str)
        return Command(op, arg)


class Interpreter:
    def __init__(self, commands: [Command]):
        self._commands = commands
        self._offset = 0
        self._executed_offset_set = set()
        self.accumulator = 0

    def execute(self):
        while self._offset not in self._executed_offset_set:
            command = commands[self._offset]
            self._executed_offset_set.add(self._offset)
            if command.op == 'nop':
                self._offset = self._offset + 1
                continue
            elif command.op == 'acc':
                self._offset = self._offset + 1
                self.accumulator += command.arg
            elif command.op == 'jmp':
                self._offset = self._offset + command.arg


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        commands = [CommandParser.parse(row) for row in f]
        interpreter = Interpreter(commands)
        interpreter.execute()
        print(interpreter.accumulator)









