from collections import Counter


def convert_hand(hand):
    replacements = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
    hex_hand = []
    for card in hand:
        if card in replacements:
            hex_hand.append(replacements[card])
        else:
            hex_hand.append(int(card))
    return hex_hand


def score_hand(hand):
    counter = Counter(hand).most_common()
    if len(counter) == 1:
        # Yahtzee
        first_bit = 7
    elif len(counter) == 2:
        # Four of a kind or full house
        first_bit = 6 if counter[0][1] == 4 else 5
    elif len(counter) == 3:
        # Three of a kind or two pair
        first_bit = counter[0][1] + 1
    elif len(counter) == 4:
        # Pair
        first_bit = 2
    else:
        # High card
        first_bit = 1
    end_bits = [f"{c:x}" for c in hand]
    hex = f"{first_bit}{''.join(end_bits).ljust(5, '0')}"
    return int(hex, 16)


with open("hands.txt") as file:
    rows = list(file)

ranks = {}
hands = {}
for row in rows:
    hand, bid = row.split()
    og_hand = hand
    hand = convert_hand(hand)
    # hand = sorted(hand, reverse=True)
    score = score_hand(hand)
    ranks[score] = int(bid)
sum = 0
max_rank = len(ranks)
for i, score in enumerate(sorted(ranks)):
    sum += (i + 1) * ranks[score]
print(sum)
