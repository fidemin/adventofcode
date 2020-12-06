from .solution2 import PasswordRule


class TestPasswordRule:
    def test_from_string(self):
        rule = PasswordRule.from_string('7-11 g')
        assert 6 == rule._first_pos
        assert 10 == rule._second_pos
        assert 'g' == rule._char

    def test_validate(self):
        rule = PasswordRule.from_string('7-11 g')
        assert rule.is_valid('abcdefgzzz')
        assert rule.is_valid('abcdefahijgab')
        assert not rule.is_valid('abcdefghijgab')
        assert not rule.is_valid('abcdbbbggbadgk')
        assert not rule.is_valid('abcdef')
