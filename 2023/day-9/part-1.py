def derivative(readings, sum=0):
    if all(reading == 0 for reading in readings):
        return sum
    sum += readings[-1]
    next_derivative = []
    for i in range(1, len(readings)):
        next_derivative.append(readings[i] - readings[i - 1])
    return derivative(next_derivative, sum)


with open("history.txt") as file:
    history = list(file)

sum = 0
for row in history:
    readings = row.split()
    sum += derivative(list(map(int, readings)))

print(sum)
