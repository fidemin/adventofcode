import pytest

from day04.solution2 import get_number_of_winning_numbers_matched, parse_row


@pytest.mark.parametrize(
    "winning_numbers,numbers,expected",
    [
        ([], [1, 2, 3], 0),
        ([41, 48, 83, 86, 17], [83, 86, 6, 31, 17, 9, 48, 53], 4),
        ([87, 83, 26, 28, 32], [88, 30, 70, 12, 93, 22, 82, 36], 0)
    ]
)
def test_get_number_of_winning_numbers_matched(winning_numbers, numbers, expected):
    actual = get_number_of_winning_numbers_matched(winning_numbers, numbers)
    assert actual == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ('Card  5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36',
         (5, [87, 83, 26, 28, 32], [88, 30, 70, 12, 93, 22, 82, 36])),
        ('Card 12: 87 | 88', (12, [87], [88])),
        # two spaces
        ('Card 12: 87 86 | 9  88', (12, [87, 86], [9, 88])),
    ]
)
def test_parse_row(test_input, expected):
    actual_card_id, actual_winning_numbers, actual_numbers = parse_row(test_input)
    expected_card_id, expected_winning_numbers, expected_numbers = expected

    assert actual_card_id == expected_card_id
    assert_list(actual_winning_numbers, expected_winning_numbers)
    assert_list(actual_numbers, expected_numbers)


def assert_list(l1: list, l2: list):
    assert len(l1) == len(l2)
    assert [e1 == e2 for e1, e2 in zip(l1, l2)]
