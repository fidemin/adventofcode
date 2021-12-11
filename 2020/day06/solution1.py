

def num_of_answer_yes_iter(file):
    yes_set = set()
    start = True
    for row in file:
        if row == '\n':
            yield len(yes_set)
            yes_set = set()
            start = True
        else:
            if start:
                yes_set = set(row.strip())
                start = False
            else:
                yes_set = yes_set.intersection(set(row.strip()))
    yield len(yes_set)


if __name__ == '__main__':
    with open('input.txt') as f:
        count = 0
        for num in num_of_answer_yes_iter(f):
            count += num

    print(count)
