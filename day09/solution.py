from collections import defaultdict, deque


if __name__ == '__main__':
    preamble_size = 25
    sum_list_by_number = defaultdict(list)
    sum_dict = defaultdict(int)
    count = 0
    result = None
    with open('input.txt') as f:
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

    print(result)










