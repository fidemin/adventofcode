def solve_part1(inputs):
    result = 0

    for range_str in inputs:
        min_str = range_str[0]
        max_str = range_str[1]

        n1 = len(min_str)
        n2 = len(max_str)

        for i in range(n1, n2 + 1):
            if i % 2 == 1:
                continue

            if i == n1:
                start_str = min_str
            else:
                start_str = "1" + "0" * (i - 1)

            if i == n2:
                end_str = max_str
            else:
                end_str = "9" * i

            half_str = start_str[: len(start_str) // 2]

            while True:
                if int(half_str * 2) < int(start_str):
                    half_int = int(half_str)
                    half_int += 1
                    half_str = str(half_int)
                    continue

                if int(half_str * 2) > int(end_str):
                    break

                result += int(half_str * 2)

                if int(half_str * 2) == int(end_str):
                    break

                half_int = int(half_str)
                half_int += 1
                half_str = str(half_int)

    return result


def solve_part2(inputs):
    result = 0
    visited = set()

    for range_str in inputs:
        temp = []
        min_str = range_str[0]
        max_str = range_str[1]

        n1 = len(min_str)
        n2 = len(max_str)

        for i in range(n1, n2 + 1):
            if i == n1:
                start_str = min_str
            else:
                start_str = "1" + "0" * (i - 1)

            if i == n2:
                end_str = max_str
            else:
                end_str = "9" * i

            for j in range(1, i // 2 + 1):
                if i % j != 0:
                    continue

                multiplier = i // j
                base_str = start_str[:j]

                while len(base_str) == j:
                    candidate_str = base_str * multiplier

                    if int(candidate_str) < int(start_str):
                        base_int = int(base_str)
                        base_int += 1
                        base_str = str(base_int)
                        continue

                    if int(candidate_str) > int(end_str):
                        break

                    if candidate_str not in visited:
                        visited.add(candidate_str)
                        result += int(candidate_str)
                        temp.append(int(candidate_str))

                    base_int = int(base_str)
                    base_int += 1
                    base_str = str(base_int)
    return result


def solve(part, sample=False):
    if sample:
        file_path = "aoc2025/day02/sample.txt"
    else:
        file_path = "aoc2025/day02/input.txt"

    inputs = []
    with open(file_path) as f:
        row = f.readline().strip()
        inputs = [range.split("-") for range in row.split(",")]

    if part == "part1":
        result = solve_part1(inputs)
    else:
        result = solve_part2(inputs)

    return result
