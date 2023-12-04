import pytest

from day03.solution1 import Lexer, TokenType, Token, parse_row


class TestLexer:
    @pytest.mark.parametrize(
        "test_input,expected",
        [
            ('........', []),
            ('..123.....', [Token(TokenType.NUM, '123', [2, 4])]),
            ('..*.....', [Token(TokenType.SYMBOL, '*', [2, 2])]),
            ('123...45', [Token(TokenType.NUM, '123', [0, 2]), Token(TokenType.NUM, '45', [6, 7])]),
            ('*....!', [Token(TokenType.SYMBOL, '*', [0, 0]), Token(TokenType.SYMBOL, '!', [5, 5])]),
            ('..#123*45...', [
                Token(TokenType.SYMBOL, '#', [2, 2]),
                Token(TokenType.NUM, '123', [3, 5]),
                Token(TokenType.SYMBOL, '*', [6, 6]),
                Token(TokenType.NUM, '45', [7, 8]),
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
        ('..*.....', [Token(TokenType.SYMBOL, '*', [2, 2])], []),
        ('123...45', [], [Token(TokenType.NUM, '123', [0, 2]), Token(TokenType.NUM, '45', [6, 7])]),
        ('*....!', [Token(TokenType.SYMBOL, '*', [0, 0]), Token(TokenType.SYMBOL, '!', [5, 5])], []),
        ('..#123*45...', [
            Token(TokenType.SYMBOL, '#', [2, 2]),
            Token(TokenType.SYMBOL, '*', [6, 6]),
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
