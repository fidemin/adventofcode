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
    result = 0

    for bank in inputs:
        stack = []

        for i in range(len(bank) - 1, -1, -1):
            battery = int(bank[i])
            if len(stack) < 12:
                stack.append(battery)
                continue

            temp = battery
            temp_list = []

            while stack and temp >= stack[-1]:
                temp_list.append(temp)
                temp = stack.pop()

            for item in reversed(temp_list):
                stack.append(item)

        this_result = 0
        for battery in reversed(stack):
            this_result = this_result * 10 + battery

        # print(bank, this_result, stack)

        result += this_result
    return result


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
