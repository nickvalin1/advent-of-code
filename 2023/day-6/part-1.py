races = [(53, 313), (89, 1090), (76, 1214), (98, 1201)]

product = 1
for time, record in races:
    permutations = 0
    for mps in range(time):
        remaining_time = time - mps
        distance = remaining_time * mps
        if distance > record:
            permutations += 1
    product *= permutations

print(product)
