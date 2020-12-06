from .solution2 import PasswordRule


class TestPasswordRule:
    def test_from_string(self):
        rule = PasswordRule.from_string('7-11 g')
        assert 6 == rule._first_pos
        assert 10 == rule._second_pos
        assert 'g' == rule._char

    def test_validate(self):
        rule = PasswordRule.from_string('7-11 g')
        assert rule.validate('abcdefgzzz')
        assert rule.validate('abcdefahijgab')
        assert rule.validate('abcdefghijgab')
        assert not rule.validate('abcdbbbggbadgk')
        assert not rule.validate('abcdef')
