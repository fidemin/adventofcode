from common import tree_exists_at_position

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        # Right 1, down 1
        pos_1 = 0
        count_1 = 0

        # Right 3, down 1
        pos_2 = 0
        count_2 = 0

        # Right 5, down 1
        pos_3 = 0
        count_3 = 0

        # Right 7, down 1
        pos_4 = 0
        count_4 = 0

        # Right 1, down 2
        pos_5 = 0
        count_5 = 0

        for i, row_pattern in enumerate(f):
            row_pattern = row_pattern.strip()  # remove \n
            count_1 = count_1 + 1 if tree_exists_at_position(row_pattern, pos_1) else count_1
            pos_1 = (pos_1 + 1) % len(row_pattern)

            count_2 = count_2 + 1 if tree_exists_at_position(row_pattern, pos_2) else count_2
            pos_2 = (pos_2 + 3) % len(row_pattern)

            count_3 = count_3 + 1 if tree_exists_at_position(row_pattern, pos_3) else count_3
            pos_3 = (pos_3 + 5) % len(row_pattern)

            count_4 = count_4 + 1 if tree_exists_at_position(row_pattern, pos_4) else count_4
            pos_4 = (pos_4 + 7) % len(row_pattern)

            if not (i % 2):
                count_5 = count_5 + 1 if tree_exists_at_position(row_pattern, pos_5) else count_5
                pos_5 = (pos_5 + 1) % len(row_pattern)

        print(count_1 * count_2 * count_3 * count_4 * count_5)

