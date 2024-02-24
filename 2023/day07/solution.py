from model import Bid, Hand, HandWithJoker


def preprocess(f):
    return [line.strip() for line in f]


def parse_row(row: str, with_joker=False) -> Bid:
    cards, bidStr = row.split(' ')
    if with_joker:
        hand = HandWithJoker(cards)
    else:
        hand = Hand(cards)
    return Bid(hand, int(bidStr))


def solve(filepath: str, with_joker=False):
    with open(filepath, 'r') as f:
        rows = preprocess(f)

    bids = [parse_row(row, with_joker) for row in rows]
    bids.sort(key=lambda bid: (bid.hand.hand_type.value, bid.hand.card_nums))

    ret = 0
    for i in range(1, len(bids) + 1):
        ret += i * bids[i - 1].amount

    return ret
