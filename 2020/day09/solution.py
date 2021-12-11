from collections import defaultdict, deque


if __name__ == '__main__':
    target_file = 'input.txt'
    preamble_size = 25
    sum_list_by_number = defaultdict(list)
    sum_dict = defaultdict(int)
    count = 0
    result = None
    with open(target_file) as f:
        initial_preamble = []
        for row in f:
            count += 1
            initial_preamble.append(int(row))
            if count == preamble_size:
                break

        preamble_deque = deque(initial_preamble)

        for i, num1 in enumerate(initial_preamble[:preamble_size-1]):
            for num2 in initial_preamble[i+1:]:
                sum_value = num1+num2
                sum_dict[sum_value] += 1
                sum_list_by_number[num1].append(sum_value)

        for row in f:
            this_num = int(row)
            if this_num not in sum_dict:
                result = this_num
                break

            left_most = preamble_deque.popleft()
            removed_sum_list = sum_list_by_number.pop(left_most)
            for removed_sum in removed_sum_list:
                sum_dict[removed_sum] -= 1
                if not sum_dict[removed_sum]:
                    sum_dict.pop(removed_sum)

            for num in preamble_deque:
                sum_value = num + this_num
                sum_dict[sum_value] += 1
                sum_list_by_number[num].append(sum_value)
            preamble_deque.append(this_num)

    target_number = result
    print(target_number)

    with open(target_file) as f:
        number_list = [int(row) for row in f]

    left_cursor = 0
    right_cursor = 0
    is_right = True
    sum_value = number_list[0]

    min_number = None
    max_number = None

    while True:
        if left_cursor == right_cursor:
            right_cursor += 1
            sum_value += number_list[right_cursor]
        elif sum_value == target_number:
            partial_number_list = number_list[left_cursor: right_cursor+1]
            min_number = min(number_list[left_cursor: right_cursor+1])
            max_number = max(number_list[left_cursor: right_cursor+1])
            break
        elif sum_value > target_number:
            sum_value -= number_list[left_cursor]
            left_cursor += 1
        elif sum_value < target_number:
            right_cursor += 1
            sum_value += number_list[right_cursor]
        else:
            assert False

    print(min_number, max_number)
    print(min_number + max_number)










