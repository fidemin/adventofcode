from dataclasses import dataclass
from enum import Enum

UNUSABLE_POSITION = -1


class TokenType(Enum):
    EOF = -1
    NUM = 1
    SYMBOL = 2


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
            elif self._current_char == '.':
                self._consume()
            elif self._is_int_char():
                return self._number()
            elif self._is_symbol():
                return self._symbol()

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

    def _symbol(self):
        token = Token(TokenType.SYMBOL, self._current_char, [self._cursor, self._cursor])
        self._cursor += 1
        if self._cursor >= self._length:
            self._current_char = self.EOF
        else:
            self._current_char = self._input[self._cursor]

        return token

    def _is_symbol(self):
        try:
            int(self._current_char)
        except ValueError:
            return False if self._current_char == '.' else True

        return False


def parse_row(input_: str):
    lexer = Lexer(input_)

    number_list = []
    symbol_list = []

    while True:
        next_token = lexer.next_token()
        if next_token.type == TokenType.EOF:
            break

        if next_token.type == TokenType.SYMBOL:
            symbol_list.append(next_token)
        elif next_token.type == TokenType.NUM:
            number_list.append(next_token)

    return symbol_list, number_list


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


def set_number_token_unusable(number_token: Token):
    number_token.position[0] = UNUSABLE_POSITION
    number_token.position[1] = UNUSABLE_POSITION


def adjacent_number_tokens(symbol_list, number_list):
    result = []
    for symbol_token in symbol_list:
        for number_token in number_list:
            if number_token.position[0] == UNUSABLE_POSITION and number_token.position[1] == UNUSABLE_POSITION:
                continue
            if is_adjacent(symbol_token, number_token):
                result.append(number_token)
                set_number_token_unusable(number_token)

    return result


def sum_of_number_tokens(number_tokens: list[Token]):
    return sum([int(token.text) for token in number_tokens])


def solve(filepath):
    total = 0

    with open(filepath, 'r') as f:
        iter_ = preprocess(f)
        prev_number_list = []
        current_symbol_list, current_number_list = parse_row(next(iter_))

        for row in preprocess(f):
            next_symbol_list, next_number_list = parse_row(row)
            number_tokens = []
            number_tokens.extend(adjacent_number_tokens(current_symbol_list, prev_number_list))
            number_tokens.extend(adjacent_number_tokens(current_symbol_list, current_number_list))
            number_tokens.extend(adjacent_number_tokens(current_symbol_list, next_number_list))
            total += sum_of_number_tokens(number_tokens)

            prev_number_list = current_number_list
            current_symbol_list = next_symbol_list
            current_number_list = next_number_list

        # handle last row
        number_tokens = []
        number_tokens.extend(adjacent_number_tokens(current_symbol_list, prev_number_list))
        number_tokens.extend(adjacent_number_tokens(current_symbol_list, current_number_list))
        total += sum_of_number_tokens(number_tokens)

    return total
