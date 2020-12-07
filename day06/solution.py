

def num_of_answer_yes_iter(f):
    yes_set = set()
    for row in f:
        if row == '\n':
            yield len(yes_set)
            yes_set = set()
        else:
            yes_set.update(set(row.strip()))
    if yes_set:
        yield len(yes_set)


if __name__ == '__main__':
    with open('input.txt') as f:
        count = 0
        for num in num_of_answer_yes_iter(f):
            count += num

    print(count)
