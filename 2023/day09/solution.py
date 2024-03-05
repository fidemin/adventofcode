from model import History


def preprocess(f):
    return [line.strip() for line in f]


def solve1(filename):
    with open(filename) as f:
        rows = preprocess(f)

    ret = 0
    for row in rows:
        lst = [int(s) for s in row.split(' ')]
        history = History(lst)
        history.analyze()
        ret += history.predict()

    return ret
