from .solution import PasswordRule


class TestPasswordRule:
    def test_from_string(self):
        rule = PasswordRule.from_string('7-11 g')
        assert 7 == rule._min
        assert 11 == rule._max
        assert 'g' == rule._char

    def test_validate(self):
        rule = PasswordRule.from_string('7-11 g')
        assert not rule.validate('abgggcgzgg')
        assert rule.validate('kdggggdkggg')
        assert rule.validate('kdggggdgkggg')
        assert rule.validate('kdggggdgkggggzgg')
        assert not rule.validate('kggdggggdgkggggzgg')

