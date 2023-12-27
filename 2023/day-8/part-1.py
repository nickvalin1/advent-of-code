instructions = """LRLRLLRRLLRRLRRLRRRLLRLRLRLRLRRLRRRLRLRRLRLLRRLLRLRRLRLRRLLRRRLRLRLRRRLRLLRRRLLLLLLRRRLRRLLLRRLRLRRLRRLRLRRLRRLLRRLRRRLRRRLLRLRLLLRRLLLRRLLRRLRLLRRRLRRRLRRRLRLRRLRRLLLRRRLRRLLRRLRRRLRLRLRRLRRLRRRLRRRLRLLLLRRRLRLRRRLRRRLLRLRRLRRLLRLLLRRLRLRRLRRRLRRRLRRRLLRRRLRLLRRRLRRRLRRRLRRRLRRLRRRLLRRLLRLRLRRRLRRRLRLRRRR"""

with open("nodes.txt") as file:
    rows = list(file)

nodes = {}
for row in rows:
    node, directions = row.split("|")
    left, right = directions.split()
    nodes[node] = {"L": left, "R": right}

node = "AAA"
steps = 0
while node != "ZZZ":
    index = steps % len(instructions)
    node = nodes[node][instructions[index]]
    steps += 1
print(steps)
