
TARGET = 2020

with open('input.txt') as f:
    entry_list = sorted([int(row) for row in f])
    for anchor_i in range(len(entry_list)-2):
        anchor_value = entry_list[anchor_i]

        result = None
        left_pos = anchor_i + 1
        right_pos = len(entry_list) - 1
        while True:
            left_value = entry_list[left_pos]
            right_value = entry_list[right_pos]
            sum_value = anchor_value + left_value + right_value
            if sum_value > TARGET:
                right_pos -= 1
            elif sum_value < TARGET:
                left_pos += 1
            else:
                result = anchor_value * left_value * right_value
                print(result)
                break

        if result is not None:
            break


