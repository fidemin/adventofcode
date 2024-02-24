import pytest

from day07.model import HandType


@pytest.mark.parametrize('cards,expected', [
    ('AAAAA', HandType.FIVE_OF_A_KIND),
    ('AA8AA', HandType.FOUR_OF_A_KIND),
    ('23332', HandType.FULL_HOUSE),
    ('TTT98', HandType.THREE_OF_KIND),
    ('23432', HandType.TWO_PAIR),
    ('A23A4', HandType.ONE_PAIR),
    ('23456', HandType.HIGH_CARD),
])
def test_from_cards(cards, expected):
    actual = HandType.from_cards(cards)
    assert actual == expected
