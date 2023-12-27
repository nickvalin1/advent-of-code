import os
from typing import List, Tuple


def get_bins(start, end, map_index) -> List[Tuple[int, int]]:
    global maps
    map = maps[map_index]
    next_bin = None
    for conversion_table in map:
        destination, source, length = conversion_table
        bin_end = source + length
        if start in range(source, bin_end):
            displacement = start - source
            next_map_start = destination + displacement
            if end in range(source, bin_end):
                displacement = end - source
                next_map_end = destination + displacement
                return [(next_map_start, next_map_end)]
            else:
                if next_bin in range(start, end):
                    displacement = next_bin - source
                    next_map_end = destination + displacement
                    ranges = [(next_map_start, next_map_end)]
                    ranges.extend(get_bins(next_bin, end, map_index))
                    return ranges
                else:
                    return [(next_map_start, destination + length), (bin_end + 1, end)]
        next_bin = source
    return [(start, end)]


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
        conversion_table = sorted(conversion_table, key=lambda x: x[1], reverse=True)
        maps.append(conversion_table)

minimum = None
for i in range(0, len(seeds), 2):
    # print(f"Starting seed range {(i + 2) // 2}/{len(seeds) // 2}")
    start = seeds[i]
    length = seeds[i + 1]
    end = start + length
    bins = [(start, end)]
    for i in range(len(maps)):
        next_bins = []
        for start, end in bins:
            next_bins.extend(get_bins(start, end, i))
        bins = next_bins
    # print(bins)
    for start, _ in bins:
        if minimum is None or start < minimum:
            minimum = start

print(minimum)
