
from .solution import tree_exists_at_position


def test_tree_exists_at_position():
    row_pattern = '.#..#.'
    assert not tree_exists_at_position(row_pattern, 0)
    assert tree_exists_at_position(row_pattern, 1)
    assert not tree_exists_at_position(row_pattern, 2)
    assert tree_exists_at_position(row_pattern, 4)
