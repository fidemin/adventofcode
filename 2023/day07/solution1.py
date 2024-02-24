from model import Bid, Hand


def preprocess(f):
    return [line.strip() for line in f]


def parse_row(row: str) -> Bid:
    cards, bidStr = row.split(' ')
    hand = Hand(cards)
    return Bid(hand, int(bidStr))


def solve(filepath: str):
    with open(filepath, 'r') as f:
        rows = preprocess(f)

    bids = [parse_row(row) for row in rows]
    bids.sort(key=lambda bid: (bid.hand.hand_type.value, bid.hand.card_nums))

    ret = 0
    for i in range(1, len(bids) + 1):
        ret += i * bids[i - 1].amount

    return ret
