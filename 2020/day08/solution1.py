
from collections import namedtuple
from copy import deepcopy

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
        while True:
            command = self._commands[self._offset]
            if command.op == 'jmp' and self._offset in self._executed_offset_set:
                return False

            self._executed_offset_set.add(self._offset)
            if command.op == 'nop':
                self._offset = self._offset + 1
                continue
            elif command.op == 'acc':
                self._offset = self._offset + 1
                self.accumulator += command.arg
            elif command.op == 'jmp':
                self._offset = self._offset + command.arg

            if self._offset >= len(self._commands):
                return True


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        this_commands = [CommandParser.parse(row) for row in f]
        nop_or_jmp_offset_commands = [
            (offset, command) for offset, command in enumerate(this_commands) if command.op in ['nop', 'jmp']]

        for offset, nop_or_jmp_command in nop_or_jmp_offset_commands:
            alt_commands = deepcopy(this_commands)
            if nop_or_jmp_command.op == 'nop':
                alt_commands[offset] = Command('jmp', nop_or_jmp_command.arg)
            elif nop_or_jmp_command.op == 'jmp':
                alt_commands[offset] = Command('nop', nop_or_jmp_command.arg)

            interpreter = Interpreter(alt_commands)
            result = interpreter.execute()
            if result:
                print(interpreter.accumulator)
