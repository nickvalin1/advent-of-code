time = 53897698
record = 313109012141201

permutations = 0
for mps in range(time):
    remaining_time = time - mps
    distance = remaining_time * mps
    if distance > record:
        permutations += 1

print(permutations)
