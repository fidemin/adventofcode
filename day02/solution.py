from __future__ import annotations


class PasswordRule:
    def __init__(self, min_: int, max_: int, char: str):
        self._min = min_
        self._max = max_
        self._char = char

    @staticmethod
    def from_string(rule_str: str) -> PasswordRule:
        """
        :param rule_str: e.g. 2-3 v
        :return:
        """

        min_max_str, char = rule_str.split(' ')
        min_str, max_str = min_max_str.split('-')
        return PasswordRule(int(min_str), int(max_str), char)

    def validate(self, password):
        """
        :param password:
        :return:
        """

        match_count = 0
        for char in password:
            if self._char == char:
                match_count += 1
            if match_count > self._max:
                return False

        if self._min <= match_count <= self._max:
            return True
