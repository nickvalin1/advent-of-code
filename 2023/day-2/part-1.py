import csv


def is_game_possible(game):
    for round in game:
        picks = round.split("|")
        for pick in picks:
            count, color = pick.split(" ")
            if limits[color] < int(count):
                return False
    return True


sum = 0
limits = {"red": 12, "green": 13, "blue": 14}
with open("games.csv") as file:
    reader = csv.reader(file)
    for i, game in enumerate(reader):
        game_id = i + 1
        if is_game_possible(game):
            sum += game_id

print(sum)
