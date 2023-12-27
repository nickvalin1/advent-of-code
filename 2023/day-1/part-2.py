import csv
import re

lookup = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}
sum = 0
with open("codes.txt") as file:
    reader = csv.reader(file)
    for row in reader:
        code = row[0]
        pattern = "one|two|three|four|five|six|seven|eight|nine|1|2|3|4|5|6|7|8|9"
        matches = re.findall(pattern, code)
        first = lookup.get(matches[0], matches[0])
        last = lookup.get(matches[-1], matches[-1])
        code_sum = int(f"{first}{last}")
        sum += code_sum
print(sum)
