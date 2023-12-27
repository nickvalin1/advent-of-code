import csv

sum = 0
with open("codes.txt") as file:
    reader = csv.reader(file)
    for row in reader:
        code = row[0]
        first = None
        last = None
        for n in code:
            if n.isdigit():
                first = n
                break
        for i in range(len(code) - 1, -1, -1):
            if code[i].isdigit():
                last = code[i]
                break
        code_sum = int(f"{first}{last}")
        sum += code_sum
print(sum)
