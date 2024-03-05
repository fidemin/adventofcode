import pytest

from .model import History


def assert_2d_list(l1, l2):
    if len(l1) != len(l2):
        return False

    for r1, r2 in zip(l1, l2):
        if len(r1) != len(r2):
            return False

        for e1, e2 in zip(r1, r2):
            if e1 != e2:
                return False
    return True


class TestHistory:
    def test_analyze(self):
        # given
        test_input = [10, 13, 16, 21, 30, 45]

        # when
        history = History(test_input)
        history.analyze()

        # then
        expected = [[10, 13, 16, 21, 30, 45], [3, 3, 5, 9, 15], [0, 2, 4, 6], [2, 2, 2], [0, 0]]
        assert assert_2d_list(history.analyze_result, expected)
        assert history.analyze_complete

    def test_predict(self):
        # given
        test_input = [10, 13, 16, 21, 30, 45]

        # when
        history = History(test_input)
        history.analyze()
        actual = history.predict()

        # then
        expected = 68
        assert actual == expected

    def test_predict_exception(self):
        # given
        test_input = [10, 13, 16, 21, 30, 45]

        # when
        history = History(test_input)

        with pytest.raises(Exception):
            history.predict()
