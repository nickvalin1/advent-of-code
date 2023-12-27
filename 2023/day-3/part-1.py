def is_symbol(char):
    if char.isdigit():
        return False
    if char == ".":
        return False
    if char == "\n":
        return False
    return True


def has_symbol(line_number, char_index, number):
    global lines
    start_index = max(0, char_index - 1)
    end_index = min(len(lines[0]) - 1, char_index + len(number))
    # Fists check the current line
    if is_symbol(lines[line_number][start_index]):
        return True
    if is_symbol(lines[line_number][end_index]):
        return True
    # Then check the previous line (if it's not the first line)
    if line_number > 0:
        for i in range(start_index, end_index + 1):
            char = lines[line_number - 1][i]
            if is_symbol(char):
                return True
    # Finally check the next line (if it's not the last line)
    if line_number < len(lines) - 1:
        for i in range(start_index, end_index + 1):
            char = lines[line_number + 1][i]
            if is_symbol(char):
                return True
    return False


sum = 0
with open("schematic.txt", newline="") as file:
    lines = list(file)

for i in range(len(lines)):
    num = ""
    for j, char in enumerate(lines[i]):
        if char.isdigit():
            num = f"{num}{char}"
        elif num:
            num_start = j - len(num)
            if has_symbol(i, num_start, num):
                sum += int(num)
            num = ""

print(sum)
