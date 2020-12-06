from __future__ import annotations


def parse_input_row(row: str):
    """
    :param row: e.g. 7-11 g: nnffggdmggr
    :return:
    """
    rule_str, password = row.split(': ')
    return rule_str, password


class PasswordRule:
    def __init__(self, first_pos: int, second_pos: int, char: str):
        self._first_pos = first_pos
        self._second_pos = second_pos
        self._char = char

    @staticmethod
    def from_string(rule_str: str) -> PasswordRule:
        """
        :param rule_str: e.g. 2-3 v
        :return:
        """

        positions_str, char = rule_str.split(' ')
        first_pos, second_pos = positions_str.split('-')
        return PasswordRule(int(first_pos) - 1, int(second_pos) - 1, char)

    def validate(self, password):
        """
        :param password:
        :return:
        """
        if len(password) < self._first_pos + 1:
            return False

        if password[self._first_pos] == self._char:
            return True

        if len(password) < self._second_pos + 1:
            return False

        if password[self._second_pos] == self._char:
            return True

        return False


if __name__ == '__main__':
    count = 0
    with open('input.txt') as f:
        for row in f:
            rule_str, password = parse_input_row(row)
            rule = PasswordRule.from_string(rule_str)
            if rule.validate(password):
                count += 1
    print(count)

