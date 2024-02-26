import pytest

from day08.model import Node, Network


class TestNode:
    def test_from_string(self):
        test_input = 'AAA = (BBB, CCC)'

        node = Node.from_string(test_input)

        assert node.value == 'AAA'
        assert node.parent is None
        assert node.left.value == 'BBB'
        assert node.left.parent is node
        assert node.right.value == 'CCC'
        assert node.right.parent is node

    @pytest.mark.parametrize('value, left, right', (
            ('AAA', 'BBB', 'CCC'),
            ('AAA', None, 'CCC'),
            ('AAA', None, None),
    ))
    def test_node(self, value, left, right):
        actual = Node(value, None, left, right)

        assert value == actual.value
        if left is not None:
            assert left == actual.left.value
        else:
            assert left is actual.left

        if right is not None:
            assert right == actual.right.value
        else:
            assert right is actual.right


class TestNetwork:
    def test_add_element(self):
        node1 = Node('AAA', None, 'BBB', 'CCC')
        node2 = Node('BBB', None, 'ZZZ', 'CCC')
        node3 = Node('CCC', None, 'AAA', 'BBB')

        network = Network()
        network.add_node(node1)
        network.add_node(node2)
        network.add_node(node3)

        assert node1.left.right.left.value == 'AAA'
        assert node1.left.right.left is node1

    def test_next_element(self):
        node = Node('AAA', None, 'BBB', 'CCC')
        network = Network()
        network.add_node(node)

        actual_left = network.next_element(node.value, 'L')
        actual_right = network.next_element(node.value, 'R')
        assert actual_left.value == 'BBB'
        assert actual_right.value == 'CCC'
