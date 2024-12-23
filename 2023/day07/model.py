from __future__ import annotations

from collections import Counter, defaultdict
from enum import Enum

card_to_number = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14
}

card_to_number_with_joker = {
    'J': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'Q': 12,
    'K': 13,
    'A': 14
}


class HandType(Enum):
    FIVE_OF_A_KIND = 7
    FOUR_OF_A_KIND = 6
    FULL_HOUSE = 5
    THREE_OF_KIND = 4
    TWO_PAIR = 3
    ONE_PAIR = 2
    HIGH_CARD = 1

    @staticmethod
    def from_cards(cards: str) -> HandType:
        counter = Counter(cards)

        kind_counter = defaultdict(int)
        for count in counter.values():
            kind_counter[count] += 1

        return HandType._from_cards_with_kind_counter(kind_counter)

    @staticmethod
    def from_cards_with_joker(cards: str) -> HandType:
        counter = Counter(cards)

        kind_counter = defaultdict(int)
        joker_count = 0
        for card, count in counter.items():
            if card == 'J':
                joker_count = count
                continue
            kind_counter[count] += 1

        kind_counter = HandType._adjust_kind_counter_with_joker(kind_counter, joker_count)
        return HandType._from_cards_with_kind_counter(kind_counter)

    @staticmethod
    def _adjust_kind_counter_with_joker(kind_counter: dict, joker_count) -> dict:
        if joker_count == 0:
            return kind_counter

        if joker_count == 5:
            kind_counter[5] = 1
            return kind_counter

        max_key = 0
        for key in kind_counter.keys():
            max_key = max(max_key, key)

        kind_counter[max_key] -= 1
        if kind_counter[max_key] == 0:
            del kind_counter[max_key]
        kind_counter[max_key + joker_count] += 1

        return kind_counter

    @staticmethod
    def _from_cards_with_kind_counter(kind_counter: dict) -> HandType:
        if 5 in kind_counter:
            return HandType.FIVE_OF_A_KIND

        if 4 in kind_counter:
            return HandType.FOUR_OF_A_KIND

        if 3 in kind_counter:
            if 2 in kind_counter:
                return HandType.FULL_HOUSE
            return HandType.THREE_OF_KIND

        if 2 in kind_counter:
            if kind_counter[2] == 2:
                return HandType.TWO_PAIR
            return HandType.ONE_PAIR
        return HandType.HIGH_CARD


class Hand:
    def __init__(self, cards: str):
        self.cards = cards
        self.card_nums = [card_to_number[card] for card in list(cards)]
        self.hand_type = HandType.from_cards(cards)


class HandWithJoker(Hand):
    def __init__(self, cards: str):
        self.cards = cards
        self.card_nums = [card_to_number_with_joker[card] for card in list(cards)]
        self.hand_type = HandType.from_cards_with_joker(cards)


class Bid:
    def __init__(self, hand: Hand, amount: int):
        self.hand = hand
        self.amount = amount
