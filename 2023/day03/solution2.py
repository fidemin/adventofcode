from dataclasses import dataclass
from enum import Enum


class TokenType(Enum):
    EOF = -1
    NUM = 1
    GEAR = 2


@dataclass
class Token:
    type: TokenType
    text: str
    position: list[int]


class Lexer:
    EOF = -1

    def __init__(self, input_: str):
        self._input = input_
        self._length = len(input_)
        self._cursor = -1
        self._current_char = None

    def next_token(self) -> Token:
        while self._current_char != self.EOF:
            if self._current_char is None:
                self._consume()
            elif self._is_int_char():
                return self._number()
            elif self._is_gear():
                return self._gear()
            else:
                # other character is ignored
                self._consume()

        return Token(TokenType.EOF, '', [])

    def _consume(self):
        self._cursor += 1
        if self._cursor >= self._length:
            self._current_char = self.EOF
            return

        self._current_char = self._input[self._cursor]

    def _number(self):
        number_chars = [self._current_char]
        start_pos = self._cursor
        end_pos = self._cursor

        while True:
            self._cursor += 1
            if self._cursor >= self._length:
                self._current_char = self.EOF
                end_pos = self._cursor - 1
                break

            self._current_char = self._input[self._cursor]
            if self._is_int_char():
                number_chars.append(self._current_char)
                end_pos = self._cursor
            else:
                break

        return Token(TokenType.NUM, ''.join(number_chars), [start_pos, end_pos])

    def _is_int_char(self):
        try:
            int(self._current_char)
        except ValueError:
            return False

        return True

    def _gear(self):
        token = Token(TokenType.GEAR, self._current_char, [self._cursor, self._cursor])
        self._cursor += 1
        if self._cursor >= self._length:
            self._current_char = self.EOF
        else:
            self._current_char = self._input[self._cursor]

        return token

    def _is_gear(self):
        return self._current_char == '*'


def parse_row(input_: str):
    lexer = Lexer(input_)

    number_list = []
    gear_list = []

    while True:
        next_token = lexer.next_token()
        if next_token.type == TokenType.EOF:
            break

        if next_token.type == TokenType.GEAR:
            gear_list.append(next_token)
        elif next_token.type == TokenType.NUM:
            number_list.append(next_token)

    return gear_list, number_list


def preprocess(file):
    for line in file:
        yield line.strip()


def is_adjacent(symbol_token: Token, number_token: Token) -> bool:
    position_list = [(max(0, symbol_token.position[0] - 1), symbol_token.position[0] + 1), tuple(number_token.position)]
    position_list.sort()

    # find there is any overlap with two positions
    if position_list[0][1] < position_list[1][0] or position_list[0][0] > position_list[1][1]:
        return False
    return True


def get_gear_number_token_pair(gear: Token, number_list):
    sub_result = []
    for number_token in number_list:
        if is_adjacent(gear, number_token):
            sub_result.append(number_token)
    if len(sub_result) == 2:
        return sub_result
    return None


def multiply_two_number_tokens(token1: Token, token2: Token):
    return int(token1.text) * int(token2.text)


def solve(filepath):
    total = 0

    with open(filepath, 'r') as f:
        iter_ = preprocess(f)
        prev_number_list = []
        current_gear_list, current_number_list = parse_row(next(iter_))

        for row in preprocess(f):
            next_gear_list, next_number_list = parse_row(row)
            for gear_token in current_gear_list:
                gear_number_pair = get_gear_number_token_pair(
                    gear_token,
                    prev_number_list + current_number_list + next_number_list)
                if gear_number_pair is not None:
                    total += multiply_two_number_tokens(*gear_number_pair)

            prev_number_list = current_number_list
            current_gear_list = next_gear_list
            current_number_list = next_number_list

        # handle last row
        for gear_token in current_gear_list:
            gear_number_pair = get_gear_number_token_pair(
                gear_token,
                prev_number_list + current_number_list)

            if gear_number_pair is not None:
                total += multiply_two_number_tokens(*gear_number_pair)
    return total
