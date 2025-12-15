
def solve_part1(inputs):
    result = 0
    position = 50

    for input_ in inputs:
        direction = input_[0]
        value = int(input_[1:])

        if direction == 'L':
            position -= value
        else:
            position += value

        position %= 100
        if position == 0:
            result += 1
    return result


def solve(part, sample=False):
    if sample:
        file_path = 'aoc2025/day01/sample.txt'
    else:
        file_path = 'aoc2025/day01/input.txt'

    inputs = []
    with open(file_path) as f:
        for row in f:
            if row.strip():
                inputs.append(row.strip())

    if part == 'part1':
        result = solve_part1(inputs)
    else:
        raise ValueError(f'Unknown part: {part}')
    return result

if __name__ == '__main__':
    print(solve('part1', sample=False))
