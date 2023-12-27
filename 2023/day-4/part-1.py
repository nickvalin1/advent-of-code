with open("cards.txt") as file:
    cards = list(file)

sum = 0
for card in cards:
    winning_numbers, my_numbers = card.split("|")
    winning_number_set = set(winning_numbers.split())
    my_number_set = set(my_numbers.split())
    intersection = winning_number_set & my_number_set
    if intersection:
        value = 2 ** (len(intersection) - 1)
        sum += value

print(sum)
