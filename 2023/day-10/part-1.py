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
length = 0
pipe = start
while (value := pipes[pipe[0] + move[0]][pipe[1] + move[1]]) != "S":
    pipe = pipe[0] + move[0], pipe[1] + move[1]
    length += 1
    rev_move = move[0] * -1, move[1] * -1
    # print(f"value: {value}, move: {move}, rev_move: {rev_move}")
    (move,) = map[value] - {rev_move}

print(math.ceil(length / 2))
