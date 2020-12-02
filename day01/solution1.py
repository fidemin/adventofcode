

with open('input.txt') as f:
    entry_list = sorted([int(row) for row in f])
    left_pos = 0
    right_pos = len(entry_list) - 1
    result = None
    while True:
        left_value = entry_list[left_pos]
        right_value = entry_list[right_pos]
        sum_value = left_value + right_value
        if sum_value > 2020:
            right_pos -= 1
        elif sum_value < 2020:
            left_pos += 1
        else:
            result = left_value * right_value
            break

    print(result)
