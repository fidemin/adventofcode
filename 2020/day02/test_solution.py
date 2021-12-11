from .solution import PasswordRule


class TestPasswordRule:
    def test_from_string(self):
        rule = PasswordRule.from_string('7-11 g')
        assert 7 == rule._min
        assert 11 == rule._max
        assert 'g' == rule._char

    def test_validate(self):
        rule = PasswordRule.from_string('7-11 g')
        assert not rule.is_valid('abgggcgzgg')
        assert rule.is_valid('kdggggdkggg')
        assert rule.is_valid('kdggggdgkggg')
        assert rule.is_valid('kdggggdgkggggzgg')
        assert not rule.is_valid('kggdggggdgkggggzgg')

