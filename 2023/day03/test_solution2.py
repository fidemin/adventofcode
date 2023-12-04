import pytest

from day03.solution2 import Lexer, TokenType, Token, parse_row, is_adjacent


class TestLexer:
    @pytest.mark.parametrize(
        "test_input,expected",
        [
            ('........', []),
            ('..123.....', [Token(TokenType.NUM, '123', [2, 4])]),
            ('..*.....', [Token(TokenType.GEAR, '*', [2, 2])]),
            ('123...45', [Token(TokenType.NUM, '123', [0, 2]), Token(TokenType.NUM, '45', [6, 7])]),
            ('*.!..*', [Token(TokenType.GEAR, '*', [0, 0]), Token(TokenType.GEAR, '*', [5, 5])]),
            ('..#123*45...', [
                Token(TokenType.NUM, '123', [3, 5]),
                Token(TokenType.GEAR, '*', [6, 6]),
                Token(TokenType.NUM, '45', [7, 8]),
            ]),
            ('..#.123.*.45...', [
                Token(TokenType.NUM, '123', [4, 6]),
                Token(TokenType.GEAR, '*', [8, 8]),
                Token(TokenType.NUM, '45', [10, 11]),
            ]),
        ]
    )
    def test_next_token(self, test_input, expected):
        lexer = Lexer(test_input)

        actual = []
        while True:
            next_token = lexer.next_token()
            if next_token.type == TokenType.EOF:
                break
            actual.append(next_token)

        _assert_equal_token_list(actual, expected)


@pytest.mark.parametrize(
    "test_input,expected_symbol_list,expected_number_list",
    [
        ('........', [], []),
        ('..123.....', [], [Token(TokenType.NUM, '123', [2, 4])]),
        ('..*.....', [Token(TokenType.GEAR, '*', [2, 2])], []),
        ('123...45', [], [Token(TokenType.NUM, '123', [0, 2]), Token(TokenType.NUM, '45', [6, 7])]),
        ('*....!', [Token(TokenType.GEAR, '*', [0, 0])], []),
        ('..#123*45...', [
            Token(TokenType.GEAR, '*', [6, 6])
        ], [
             Token(TokenType.NUM, '123', [3, 5]),
             Token(TokenType.NUM, '45', [7, 8]),
         ]),
    ]
)
def test_parse_row(test_input, expected_symbol_list, expected_number_list):
    actual_symbol_list, actual_number_list = parse_row(test_input)
    _assert_equal_token_list(actual_symbol_list, expected_symbol_list)
    _assert_equal_token_list(actual_number_list, expected_number_list)


def _assert_equal_token_list(actual: list[Token], expected: list[Token]):
    assert len(actual) == len(expected)

    for i in range(len(actual)):
        actual_token = actual[i]
        expected_token = expected[i]

        assert actual_token.type == expected_token.type
        assert actual_token.text == expected_token.text
        assert expected_token.position[0] == expected_token.position[0]
        assert expected_token.position[1] == expected_token.position[1]


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ([Token(TokenType.GEAR, '*', [1, 1]), Token(TokenType.NUM, '123', [2, 4])], True),
        ([Token(TokenType.GEAR, '*', [1, 1]), Token(TokenType.NUM, '1', [0, 0])], True),
        ([Token(TokenType.GEAR, '*', [3, 3]), Token(TokenType.NUM, '12', [0, 1])], False),
        ([Token(TokenType.GEAR, '*', [3, 3]), Token(TokenType.NUM, '12', [5, 6])], False),
        ([Token(TokenType.GEAR, '*', [3, 3]), Token(TokenType.NUM, '1234', [1, 5])], True),
        ([Token(TokenType.GEAR, '*', [3, 3]), Token(TokenType.NUM, '1', [2, 4])], True),
        ([Token(TokenType.GEAR, '*', [3, 3]), Token(TokenType.NUM, '12', [4, 5])], True),
        ([Token(TokenType.GEAR, '*', [3, 3]), Token(TokenType.NUM, '12', [1, 2])], True),
    ]
)
def test_is_adjacent(test_input, expected):
    gear_token, number_token = test_input
    actual = is_adjacent(gear_token, number_token)
    assert actual == expected
