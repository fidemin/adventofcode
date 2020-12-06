from .common import tree_exists_at_position

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        pos = 0
        count = 0
        for row_pattern in f:
            row_pattern = row_pattern.strip()  # remove \n
            result = tree_exists_at_position(row_pattern, pos)
            if result:
                count += 1
            pos = (pos + 3) % len(row_pattern)

        print(count)
