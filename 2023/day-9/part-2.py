def derivative(readings):
    if all(reading == 0 for reading in readings):
        return 0
    next_derivative = []
    for i in range(1, len(readings)):
        next_derivative.append(readings[i] - readings[i - 1])
    extrapolation = derivative(next_derivative)
    return next_derivative[0] - extrapolation


with open("history.txt") as file:
    history = list(file)

sum = 0
for row in history:
    readings = list(map(int, row.split()))
    sum += readings[0] - derivative(readings)

print(sum)
