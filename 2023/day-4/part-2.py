def calculate_card(i):
    global cards
    global hash
    sum = 1
    if i in hash:
        return hash[i]
    card = cards[i]
    winning_numbers, my_numbers = card.split("|")
    winning_number_set = set(winning_numbers.split())
    my_number_set = set(my_numbers.split())
    intersection = winning_number_set & my_number_set
    for j in range(len(intersection)):
        sum += calculate_card(i + j + 1)
    hash[i] = sum
    return sum


with open("cards.txt") as file:
    cards = list(file)

sum = 0
hash = {}
for i in range(len(cards)):
    sum += calculate_card(i)

print(sum)
