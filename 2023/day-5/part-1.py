import os


def convert(value, map):
    for conversion_table in map:
        destination, source, length = conversion_table
        if value in range(source, source + length):
            displacement = value - source
            return destination + displacement
    return value


seeds = [
    2637529854,
    223394899,
    3007537707,
    503983167,
    307349251,
    197383535,
    3543757609,
    276648400,
    2296792159,
    141010855,
    116452725,
    5160533,
    2246652813,
    49767336,
    762696372,
    160455077,
    3960442213,
    105867001,
    1197133308,
    38546766,
]

maps = []
for filename in os.listdir("maps"):
    with open(f"maps/{filename}") as file:
        conversion_table = []
        for row in file:
            conversion_table.append(list(map(int, row.split())))
        maps.append(conversion_table)

min = None
for seed in seeds:
    value = seed
    for map in maps:
        value = convert(value, map)
    if min is None or value < min:
        min = value
print(min)
