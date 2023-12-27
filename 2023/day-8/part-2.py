import math


def prime_factorization(n):
    factors = set()
    while n % 2 == 0:
        n = n // 2
        factors.add(2)

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            n = n // i
            factors.add(i)

    if n > 2:
        factors.add(n)

    return factors


instructions = """LRLRLLRRLLRRLRRLRRRLLRLRLRLRLRRLRRRLRLRRLRLLRRLLRLRRLRLRRLLRRRLRLRLRRRLRLLRRRLLLLLLRRRLRRLLLRRLRLRRLRRLRLRRLRRLLRRLRRRLRRRLLRLRLLLRRLLLRRLLRRLRLLRRRLRRRLRRRLRLRRLRRLLLRRRLRRLLRRLRRRLRLRLRRLRRLRRRLRRRLRLLLLRRRLRLRRRLRRRLLRLRRLRRLLRLLLRRLRLRRLRRRLRRRLRRRLLRRRLRLLRRRLRRRLRRRLRRRLRRLRRRLLRRLLRLRLRRRLRRRLRLRRRR"""

with open("nodes.txt") as file:
    rows = list(file)

nodes = {}
for row in rows:
    node, directions = row.split("|")
    left, right = directions.split()
    nodes[node] = {"L": left, "R": right}

current_nodes = [node for node in nodes if node[2] == "A"]
steps = 0
hash = []
while len(hash) < len(current_nodes):
    index = steps % len(instructions)
    next_nodes = []
    for node in current_nodes:
        if node[2] == "Z":
            hash.append(steps)
        next_nodes.append(nodes[node][instructions[index]])
    current_nodes = next_nodes
    steps += 1
factors = set()
for m in hash:
    factors = prime_factorization(m) | factors
lcm = 1
for factor in factors:
    lcm *= factor
print(lcm)
