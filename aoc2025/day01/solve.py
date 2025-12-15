
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

def solve_part2(inputs):
    result = 0
    position = 50

    for input_ in inputs:
        direction = input_[0]
        value = int(input_[1:])

        if direction == 'L':
            # if start point is 0, action does not pass 0.
            initial = 1 if position > 0 else 0
            position -= value

            if position <= 0:
                result += initial + abs(position) // 100
        else:
            position += value

            if position >= 100:
                result += position // 100

        position %= 100
        # print(result, input_, position)
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
        result = solve_part2(inputs)
    return result
