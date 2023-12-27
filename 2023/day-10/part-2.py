import math
from typing import Tuple


def find_start(pipes) -> Tuple[int, int]:
    for i in range(len(pipes)):
        if "S" in pipes[i]:
            return (i, pipes[i].find("S"))
    raise ValueError


UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)
map = {"|": {UP, DOWN}, "-": {LEFT, RIGHT}, "L": {UP, RIGHT}, "J": {UP, LEFT}, "7": {LEFT, DOWN}, "F": {RIGHT, DOWN}}

with open("pipes.txt") as file:
    pipes = file.read().splitlines()
start = find_start(pipes)
if pipes[start[0]][start[1] + 1] in {"7", "-"}:
    move = RIGHT
elif pipes[start[0]][start[1] - 1] in {"F", "-"}:
    move = LEFT
else:
    move = UP
pipe = start
system = {start[0]: [start[1]]}
while (value := pipes[pipe[0] + move[0]][pipe[1] + move[1]]) != "S":
    pipe = pipe[0] + move[0], pipe[1] + move[1]
    if pipe[0] in system:
        system[pipe[0]].append(pipe[1])
    else:
        system[pipe[0]] = [pipe[1]]
    rev_move = move[0] * -1, move[1] * -1
    (move,) = map[value] - {rev_move}

area = 0
inside = set()
rows = sorted(system.keys())
for i in rows[1:-1]:
    row = sorted(system[i])
    vertical_edge = pipes[i][row[0]] in {"|", "J", "L", "S"}
    in_system = vertical_edge
    for j in range(1, len(row)):
        length = row[j] - row[j - 1]
        if in_system:
            area += length - 1
            for k in range(row[j - 1], row[j]):
                inside.add((i, k))
        vertical_edge = pipes[i][row[j]] in {"|", "J", "L", "S"}
        if vertical_edge:
            in_system = not in_system
print(area)

print_map = {"L": "└", "F": "┌", "J": "┘", "7": "┐", "|": "│", "-": "─", "S": "┃"}

for i in range(len(pipes)):
    for j in range(len(pipes[i])):
        if i in system and j in system[i]:
            print(print_map[pipes[i][j]], end="")
        # elif (i, j) in inside:
        #   print(".", end="")
        else:
            print(" ", end="")
    print()
