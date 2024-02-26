import math

from model import Node, Network


def preprocess(f):
    return [line.strip() for line in f]


def solve1(filepath):
    with open(filepath) as f:
        rows = preprocess(f)

    instructions = rows[0]

    network = Network()

    for i in range(2, len(rows)):
        row = rows[i]
        node = Node.from_string(row)
        network.add_node(node)

    pos = 'AAA'
    count = 0
    while pos != 'ZZZ':
        inst_pos = count % len(instructions)
        pos = network.next_element(pos, instructions[inst_pos]).value
        count += 1

    return count


def solve2(filepath: str) -> int:
    with open(filepath) as f:
        rows = preprocess(f)

    instructions = rows[0]

    network = Network()

    for i in range(2, len(rows)):
        row = rows[i]
        node = Node.from_string(row)
        network.add_node(node)

    elements = []
    for element in network.nodes:
        if element[2] == 'A':
            elements.append(element)

    counts = []
    for element in elements:
        pos = element
        count = 0
        while pos[2] != 'Z':
            inst_pos = count % len(instructions)
            pos = network.next_element(pos, instructions[inst_pos]).value
            count += 1

        counts.append(count)
    return math.lcm(*counts)
