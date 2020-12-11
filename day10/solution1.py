from collections import defaultdict

result = {
    1: 1,
    2: 1,
    3: 2
}


def num_of_cases(consec_count):
    if consec_count in result:
        return result[consec_count]

    this_cases = num_of_cases(consec_count - 3) + num_of_cases(consec_count - 2) + num_of_cases(consec_count - 1)
    result[consec_count] = this_cases
    return this_cases


if __name__ == '__main__':
    joltage_list = [0]
    with open('input.txt') as f:
        for row in f:
            joltage_list.append(int(row))

    joltage_list.sort()
    joltage_list.append(joltage_list[len(joltage_list)-1]+3)

    cursor = 0
    consecutive_count = 1
    consecutive_count_list = []

    while cursor < len(joltage_list) - 1:
        #print('this_value: ',  joltage_list[cursor])
        #print('count:', consecutive_count)
        this_value = joltage_list[cursor]
        next_value = joltage_list[cursor+1]
        if (next_value - this_value) == 1:
            consecutive_count += 1
        elif (next_value - this_value) == 3:
            if consecutive_count not in [1, 2]:
                consecutive_count_list.append(consecutive_count)
            consecutive_count = 1
        else:
            assert False
        cursor += 1

    total_cases = 1
    for consecutive_count in consecutive_count_list:
        total_cases *= num_of_cases(consecutive_count)

    print(total_cases)

