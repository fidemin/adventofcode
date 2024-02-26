from __future__ import annotations


class Node:
    network = {}

    @staticmethod
    def from_string(string: str) -> Node:
        """
        :param string: e.g. AAA = (BBB, CCC)
        :return:
        """
        value, pair_str = string.split(' = ')
        left, right = pair_str.lstrip('(').rstrip(')').split(', ')
        return Node(value, None, left, right)

    def __init__(self, value: str, parent=None, left=None, right=None):
        self.value: str = value
        self.parent = parent
        self.left = None
        self.right = None
        if left is not None:
            self.left: Node = Node(left, self)

        if right is not None:
            self.right: Node = Node(right, self)


class Network:
    def __init__(self):
        self._nodes: dict[str, Node] = {}

    def add_node(self, node: Node):
        if node.value in self._nodes:
            old_node = self._nodes[node.value]
            parent = old_node.parent

            if parent is not None:
                if parent.left is old_node:
                    parent.left = node
                else:
                    parent.right = node

        self._nodes[node.value] = node

        if node.left.value in self._nodes:
            node.left = self._nodes[node.left.value]
            node.left.parent = node
        else:
            self._nodes[node.left.value] = node.left

        if node.right.value in self._nodes:
            node.right = self._nodes[node.right.value]
            node.right.parent = node
        else:
            self._nodes[node.right.value] = node.right

    def next_element(self, value: str, direction: str) -> Node:
        if direction == 'L':
            return self._nodes[value].left
        elif direction == 'R':
            return self._nodes[value].right
        raise RuntimeError(f'{direction} is not an available direction')

    @property
    def nodes(self):
        return self._nodes
