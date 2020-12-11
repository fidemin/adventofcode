from collections import defaultdict


if __name__ == '__main__':
    joltage_list = [0]
    with open('input.txt') as f:
        for row in f:
            joltage_list.append(int(row))

    joltage_list.sort()
    joltage_list.append(joltage_list[len(joltage_list)-1]+3)

    counter = defaultdict(int)
    for i, joltage in enumerate(joltage_list[1:], 1):
        diff = joltage - joltage_list[i-1]
        counter[diff] += 1

    print(counter[1] * counter[3])






