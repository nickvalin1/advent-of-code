import csv

sum = 0
with open("games.csv") as file:
    reader = csv.reader(file)
    for game in reader:
        minimums = {"red": 0, "green": 0, "blue": 0}
        for round in game:
            picks = round.split("|")
            for pick in picks:
                count, color = pick.split(" ")
                minimums[color] = max(minimums[color], int(count))
        power = 1
        for color in minimums.values():
            power *= color
        sum += power

print(sum)
