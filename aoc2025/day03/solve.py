def solve_part1(inputs):
    result = 0
    for bank in inputs:
        first = int(bank[0])
        max_joltage = 0

        for i in range(1, len(bank)):
            battery = int(bank[i])
            max_joltage = max(max_joltage, first * 10 + battery)
            if battery > first:
                first = battery
        result += max_joltage

    return result


def solve_part2(inputs):
    pass


def solve(part, sample=False):
    if sample:
        file_path = "aoc2025/day03/sample.txt"
    else:
        file_path = "aoc2025/day03/input.txt"

    inputs = []
    with open(file_path) as f:
        for row in f:
            inputs.append(row.strip())

    if part == "part1":
        result = solve_part1(inputs)
    else:
        result = solve_part2(inputs)

    return result
